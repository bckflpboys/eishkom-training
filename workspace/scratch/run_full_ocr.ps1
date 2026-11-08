Add-Type -AssemblyName System.Runtime.WindowsRuntime
$asTaskGeneric = [System.WindowsRuntimeSystemExtensions].GetMethods() | ? { $_.Name -eq 'AsTask' -and $_.GetParameters().Count -eq 1 -and $_.ContainsGenericParameters } | Select-Object -First 1

function Await-WinRT($winRtAsyncOp, $resultType) {
    $asTask = $asTaskGeneric.MakeGenericMethod($resultType)
    $task = $asTask.Invoke($null, @($winRtAsyncOp))
    $task.Wait()
    return $task.Result
}

[Windows.Storage.StorageFile, Windows.Storage, ContentType = WindowsRuntime] | Out-Null
[Windows.Graphics.Imaging.BitmapDecoder, Windows.Foundation.UniversalApiContract, ContentType = WindowsRuntime] | Out-Null
[Windows.Media.Ocr.OcrEngine, Windows.Foundation.UniversalApiContract, ContentType = WindowsRuntime] | Out-Null

$engine = [Windows.Media.Ocr.OcrEngine]::TryCreateFromUserProfileLanguages()
$allText = @()

for ($p = 1; $p -le 16; $p++) {
    $imgPath = (Resolve-Path "workspace/scratch/page_$p.png").Path
    $fileOp = [Windows.Storage.StorageFile]::GetFileFromPathAsync($imgPath)
    $file = Await-WinRT $fileOp ([Windows.Storage.StorageFile])

    $streamOp = $file.OpenAsync([Windows.Storage.FileAccessMode]::Read)
    $stream = Await-WinRT $streamOp ([Windows.Storage.Streams.IRandomAccessStream])

    $decoderOp = [Windows.Graphics.Imaging.BitmapDecoder]::CreateAsync($stream)
    $decoder = Await-WinRT $decoderOp ([Windows.Graphics.Imaging.BitmapDecoder])

    $bitmapOp = $decoder.GetSoftwareBitmapAsync()
    $bitmap = Await-WinRT $bitmapOp ([Windows.Graphics.Imaging.SoftwareBitmap])

    $ocrOp = $engine.RecognizeAsync($bitmap)
    $ocrResult = Await-WinRT $ocrOp ([Windows.Media.Ocr.OcrResult])

    $allText += "=== page $p ==="
    $allText += $ocrResult.Text
    Write-Host "Page $p OCR complete: $($ocrResult.Text.Length) characters"
}

$fullContent = $allText -join "`r`n`r`n"
[System.IO.File]::WriteAllText("workspace/scratch/dbe-mathematics-g12-p2-2018-nov-qp-ocr.txt", $fullContent, [System.Text.Encoding]::UTF8)
[System.IO.File]::WriteAllText("workspace/text/dbe-mathematics-g12-p2-2018-nov.txt", $fullContent, [System.Text.Encoding]::UTF8)
Write-Host "Done! Saved to workspace/text/dbe-mathematics-g12-p2-2018-nov.txt"
