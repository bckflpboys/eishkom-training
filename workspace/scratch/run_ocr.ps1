[Windows.Media.Ocr.OcrEngine, Windows.Foundation.UniversalApiContract, ContentType = WindowsRuntime] | Out-Null
[Windows.Graphics.Imaging.BitmapDecoder, Windows.Foundation.UniversalApiContract, ContentType = WindowsRuntime] | Out-Null
[Windows.Storage.StorageFile, Windows.Storage, ContentType = WindowsRuntime] | Out-Null

function Get-OcrText($imagePath) {
    $file = [Windows.Storage.StorageFile]::GetFileFromPathAsync($imagePath).GetAwaiter().GetResult()
    $stream = $file.OpenAsync([Windows.Storage.FileAccessMode]::Read).GetAwaiter().GetResult()
    $decoder = [Windows.Graphics.Imaging.BitmapDecoder]::CreateAsync($stream).GetAwaiter().GetResult()
    $bitmap = $decoder.GetSoftwareBitmapAsync().GetAwaiter().GetResult()
    $engine = [Windows.Media.Ocr.OcrEngine]::TryCreateFromUserProfileLanguages()
    $result = $engine.RecognizeAsync($bitmap).GetAwaiter().GetResult()
    return $result.Text
}

$output = @()
for ($i = 1; $i -le 16; $i++) {
    $pngPath = (Resolve-Path "workspace/scratch/page_$i.png").Path
    $text = Get-OcrText -imagePath $pngPath
    $output += "=== PAGE $i ==="
    $output += $text
    Write-Host "Processed page $i"
}

$output | Out-File -FilePath "workspace/scratch/qp_ocr_full.txt" -Encoding utf8
Write-Host "All pages OCRed successfully!"
