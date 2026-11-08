with open('workspace/text/dbe-mathematics-g12-p2-2022-nov-memo.txt', 'r', encoding='utf-8') as f:
    content = f.read()

# find cutoff at line 139
cutoff_marker = '| 7.2 | $\\frac{CD}{\\sin(135^\\circ - x)} = \\frac{3p}{\\sin x}$'
cutoff_idx = content.find(cutoff_marker)
if cutoff_idx != -1:
    base = content[:cutoff_idx]
else:
    base = content

continuation = '''| 7.2 | $\\frac{CD}{\\sin(135^\\circ - x)} = \\frac{3p}{\\sin x}$<br>$CD = \\frac{3p\\sin(135^\\circ - x)}{\\sin x}$<br>$CD = \\frac{3p(\\sin 135^\\circ\\cos x - \\cos 135^\\circ\\sin x)}{\\sin x}$<br>$CD = \\frac{3p(\\sin 45^\\circ\\cos x + \\cos 45^\\circ\\sin x)}{\\sin x}$<br>$CD = \\frac{3p\\left(\\frac{\\sqrt{2}}{2}\\cos x + \\frac{\\sqrt{2}}{2}\\sin x\\right)}{\\sin x}$<br>$CD = \\frac{3p\\cdot\\frac{\\sqrt{2}}{2}(\\sin x + \\cos x)}{\\sin x}$<br>$CD = \\frac{3p(\\sin x + \\cos x)}{\\sqrt{2}\\sin x}$ | $\\checkmark$ correct use of sine rule<br>$\\checkmark 135^\\circ - x$<br>$\\checkmark$ compound angle<br>$\\checkmark$ special values<br>$\\checkmark$ factorisation | (5) |
| 7.3 | $\\text{Area } \\triangle ADC = \\frac{1}{2}(AD)(CD)\\sin A\\hat{D}C$<br>$\\phantom{\\text{Area } \\triangle ADC} = \\frac{1}{2}(3p)\\left(\\frac{3p(\\sin x + \\cos x)}{\\sqrt{2}\\sin x}\\right)\\sin 45^\\circ$<br>$\\phantom{\\text{Area } \\triangle ADC} = \\frac{1}{2}(30)\\left(\\frac{30(\\sin 110^\\circ + \\cos 110^\\circ)}{\\sqrt{2}\\sin 110^\\circ}\\right)\\sin 45^\\circ$<br>$\\phantom{\\text{Area } \\triangle ADC} = 143{,}11\\text{ m}^2$ | $\\checkmark$ correct use of area rule<br>$\\checkmark$ substitution in area rule<br>$\\checkmark$ answer | (3) |
| | | | **[10]** |

---

## QUESTION / VRAAG 8

| 8.1.1 | $\\hat{P} = 180^\\circ - 64^\\circ = 116^\\circ \\quad [\\text{opp } \\angle\\text{s of cyclic quad / teenoorst. } \\angle\\text{e van kvh}]$ | $\\checkmark\\text{S} \\quad \\checkmark\\text{R}$ | (2) |
| :--- | :--- | :--- | :---: |
| 8.1.2 | $\\hat{M}_1 + 64^\\circ = 90^\\circ \\quad [\\angle\\text{ in semi-circle / } \\angle\\text{ in halwe sirkel}]$<br>$\\hat{M}_1 = 26^\\circ$ | $\\checkmark\\text{R}$<br>$\\checkmark\\text{S}$ | (2) |
| 8.1.3 | $\\hat{O}_1 = 2 \\times 26^\\circ = 52^\\circ \\quad [\\angle\\text{ at centre } = 2 \\times \\angle\\text{ at circumference / midpts. } \\angle = 2 \\times \\text{omtreks. } \\angle]$ | $\\checkmark\\text{S} \\quad \\checkmark\\text{R}$ | (2) |
| 8.2.1 | Midpt theorem / Midpt. stelling<br>**OR/OF**<br>Converse prop intercept theorem | $\\checkmark\\text{R}$<br><br>$\\checkmark\\text{R}$ | (1)<br><br>(1) |
| 8.2.2 | $BG = 2DE = 2(3x - 1) = 6x - 2 \\quad [\\text{Midpt theorem / Midpt. stelling}]$<br>$\\frac{BG}{GH} = \\frac{BF}{FC} \\quad [\\text{line } \\parallel \\text{ one side of } \\triangle \\text{ OR prop theorem; } FG \\parallel CH / \\text{lyn } \\parallel \\text{ een sy v. } \\triangle]$<br>$\\frac{6x - 2}{x + 1} = \\frac{4}{1}$<br>$4x + 4 = 6x - 2$<br>$2x = 6$<br>$x = 3$<br><br>**OR/OF**<br>$\\frac{BF}{FC} = \\frac{BG}{GH} \\quad [\\text{line } \\parallel \\text{ one side of } \\triangle \\text{ OR prop theorem; } FG \\parallel CH]$<br>$\\frac{AE}{AG} = \\frac{DE}{BG} \\quad [\\triangle ADE \\parallel\\parallel\\parallel \\triangle ABG]$<br>$BG = 4x + 4$<br>$\\frac{1}{2} = \\frac{3x - 1}{4x + 4}$<br>$4x + 4 = 6x - 2$<br>$x = 3$ | $\\checkmark\\text{S} \\quad \\checkmark\\text{R}$<br><br>$\\checkmark\\text{S} \\quad \\checkmark\\text{R}$<br><br>$\\checkmark$ equation in $x$<br><br>$\\checkmark$ answer<br><br><br>$\\checkmark\\text{S} \\quad \\checkmark\\text{R}$<br><br>$\\checkmark\\text{S} \\quad \\checkmark\\text{R}$<br><br>$\\checkmark$ equation in $x$<br>$\\checkmark$ answer | (6)<br><br><br><br><br><br><br><br>(6) |
| | | | **[13]** |

---

## QUESTION / VRAAG 9

| 9.1 | Construction: Draw $OA$ and $OB$<br>In $\\triangle ADO$ and $\\triangle BDO$:<br>$OA = OB \\quad [\\text{radii / radiusse}]$<br>$OD = OD \\quad [\\text{common side / gemeenskaplike sy}]$<br>$AD = DB \\quad [\\text{given / gegee}]$<br>$\\therefore \\triangle ADO \\equiv \\triangle BDO \\quad [\\text{SSS / S;S;S}]$<br>$\\therefore \\hat{D}_1 = \\hat{D}_2 \\quad [\\triangle ADO \\equiv \\triangle BDO]$<br>But $\\hat{D}_1 + \\hat{D}_2 = 180^\\circ \\quad [\\angle\\text{s on a str line / } \\angle\\text{e op \\'n reguitlyn}]$<br>$\\therefore \\hat{D}_1 = \\hat{D}_2 = 90^\\circ$<br>$\\therefore OD \\perp AB$<br><br>**OR/OF**<br>Construction: Draw $OA$ and $OB$<br>In $\\triangle ADO$ and $\\triangle BDO$:<br>$AD = DB \\quad [\\text{given / gegee}]$<br>$\\hat{A} = \\hat{B} \\quad [\\angle\\text{s opp equal sides / } \\angle\\text{e teenoor gelyke sye}]$<br>$OA = OB \\quad [\\text{radii / radiusse}]$<br>$\\therefore \\triangle ADO \\equiv \\triangle BDO \\quad [\\text{SAS / S;}\\angle\\text{;S}]$<br>$\\therefore \\hat{D}_1 = \\hat{D}_2$<br>$\\therefore OD \\perp AB \\quad [\\angle\\text{s on a str line / } \\angle\\text{e op \\'n reguitlyn}]$ | $\\checkmark$ construction<br><br>$\\checkmark$ first pair of sides<br>$\\checkmark$ other 2 pairs<br>$\\checkmark\\text{R [SSS]}$<br><br>$\\checkmark\\text{R [}\\angle\\text{s on a str line]}$<br><br><br><br>$\\checkmark$ construction<br><br>$\\checkmark$ first pair of sides<br>$\\checkmark$ other 2 pairs<br>$\\checkmark\\text{R [SAS]}$<br><br>$\\checkmark\\text{R [}\\angle\\text{s on a str line]}$ | (5)<br><br><br><br><br><br><br><br><br><br>(5) |
| 9.2.1 | $O\\hat{T}G = 90^\\circ \\quad [\\text{line from centre to midpt of chord / lyn van midpt. sirkel na midpt. koord}]$<br>$O\\hat{B}G = 90^\\circ \\quad [\\text{tan } \\perp \\text{ radius / raaklyn } \\perp \\text{ radius}]$<br>$\\therefore O\\hat{T}G = O\\hat{B}G = 90^\\circ$<br>$\\therefore OTBG \\text{ is a cyclic quadrilateral} \\quad [\\text{line subtends equal } \\angle\\text{s OR converse } \\angle\\text{s in same segment / lyn onderspan gelyke } \\angle\\text{e}]$ | $\\checkmark\\text{S} \\quad \\checkmark\\text{R}$<br><br>$\\checkmark\\text{S} \\quad \\checkmark\\text{R}$<br><br>$\\checkmark\\text{R}$ | (5) |
| 9.2.2 | $\\hat{S} = G\\hat{T}B \\quad [\\text{corresp } \\angle\\text{s; } GF \\parallel PS / \\text{ooreenk. } \\angle\\text{e; } GF \\parallel PS]$<br>$\\text{But } G\\hat{T}B = G\\hat{O}B \\quad [\\angle\\text{s in the same segment / } \\angle\\text{e in dies. sirkelsegment}]$<br>$\\therefore G\\hat{O}B = \\hat{S}$ | $\\checkmark\\text{S} \\quad \\checkmark\\text{R}$<br><br>$\\checkmark\\text{S} \\quad \\checkmark\\text{R}$ | (4) |
| | | | **[14]** |

---

## QUESTION / VRAAG 10

| 10.1 | $\\hat{P}_1 = \\hat{Q}_1 \\quad [\\text{tan-chord theorem / } \\angle \\text{ tussen raaklyn en koord}]$<br>$\\hat{S}_1 = \\hat{Q}_1 + \\hat{Q}_2 \\quad [\\text{ext } \\angle \\text{ of cyclic quad / buite } \\angle \\text{ v. kvh}]$<br>$\\therefore \\hat{S}_1 = \\hat{P}_1 + \\hat{Q}_2$<br>$\\hat{T}_2 = \\hat{R}_2 + \\hat{Q}_2 \\quad [\\text{ext } \\angle \\text{ of } \\triangle / \\text{buite } \\angle \\text{ v. } \\triangle]$<br>$\\text{but } \\hat{R}_2 = \\hat{P}_1 \\quad [\\text{given / gegee}]$<br>$\\therefore \\hat{T}_2 = \\hat{P}_1 + \\hat{Q}_2$<br>$\\therefore \\hat{S}_1 = \\hat{T}_2 = \\hat{P}_1 + \\hat{Q}_2$ | $\\checkmark\\text{S}$<br>$\\checkmark\\text{S/R}$<br><br>$\\checkmark\\text{S}$<br><br>$\\checkmark\\text{S}$ | (4) |
| 10.2 | In $\\triangle ASD \\text{ and } \\triangle ACR$:<br>$\\hat{A} = \\hat{A} \\quad [\\text{common } \\angle / \\text{gemeenskaplike } \\angle]$<br>$\\hat{S}_1 = \\hat{T}_2 \\quad [\\text{proven / reeds bewys}]$<br>$\\hat{T}_2 = \\hat{C}_2 \\quad [\\text{alt } \\angle\\text{s; } QS \\parallel CA / \\text{verw. } \\angle\\text{e; } QS \\parallel CA]$<br>$\\therefore \\hat{S}_1 = \\hat{C}_2$<br>$\\hat{D}_1 = \\hat{R}_1 \\quad [\\text{sum of } \\angle\\text{s in } \\triangle / \\angle\\text{e v. } \\triangle]$<br>$\\therefore \\triangle ASD \\parallel\\parallel\\parallel \\triangle ACR \\quad [\\angle;\\angle;\\angle]$<br>$\\therefore \\frac{AD}{AR} = \\frac{AS}{AC} \\quad [\\text{corresponding sides in proportion / ooreenstemmende sye in dies. verhouding}]$ | $\\checkmark \\text{identifying } \\triangle\\text{'s}$<br>$\\checkmark\\text{S}$<br><br>$\\checkmark\\text{S/R}$<br>$\\checkmark\\text{S}$<br>$\\checkmark\\text{S (or R)}$ | (5) |
| 10.3 | $\\frac{SD}{CR} = \\frac{AS}{AC} \\quad [\\triangle ASD \\parallel\\parallel\\parallel \\triangle ACR]$<br>$\\therefore AS = \\frac{AC \\times SD}{CR}$<br>$\\frac{AS}{AR} = \\frac{CT}{CR} \\quad [\\text{line } \\parallel \\text{ one side of } \\triangle \\text{ OR prop theorem; } TS \\parallel CA / \\text{lyn } \\parallel \\text{ een sy v. } \\triangle]$<br>$\\therefore AS = \\frac{AR \\times CT}{CR}$<br>$\\therefore \\frac{AC \\times SD}{CR} = \\frac{AR \\times CT}{CR}$<br>$\\therefore AC \\times SD = AR \\times TC$ | $\\checkmark\\text{S}$<br><br><br>$\\checkmark\\text{S} \\quad \\checkmark\\text{R}$<br><br><br>$\\checkmark \\text{equating}$ | (4) |
| | | | **[13]** |

**TOTAL / TOTAAL: 150**
'''

full_content = base + continuation
with open('workspace/text/dbe-mathematics-g12-p2-2022-nov-memo.txt', 'w', encoding='utf-8') as f:
    f.write(full_content)
print('Restored full memo text. Total length:', len(full_content))
