# Eishkom AI — Universal Item Extraction Tracker & Queue

> **Stage 1 Release Cycle:** `koeberg-stage-1`, `kendal-stage-1`, `kendal-flash-stage-1`, `gariep-stage-1`, `gariep-flash-stage-1`  
> **Master Corpus:** **301 Exam Pairs (602 DBE PDFs)**  
> **Quarantined for EVAL:** **33 Papers (Strictly held out)**  
> **Training Target:** **268 Papers**  
> **Verified Extracted Items:** **13169 atomic items** across **266 papers** (31282 total marks verified)  

---

## 1. Executive Status Board

| Metric | Status | Description |
|---|---|---|
| **Pilot Wave (Page 1)** | **4/4 COMPLETE** | 4/4 Core Subjects verified (Maths P1, Physics P2, English HL, Afrikaans HL) |
| **Wave 2 (Page 2)** | **100% COMPLETE** | 4/4 Core Subjects verified (Maths P2, Physics P1, English FAL P1, Afrikaans FAL P1) |
| **Wave 3 (Page 3)** | **100% COMPLETE** | Maths P1, Physics P1, English HL P1, Afrikaans HL P1 (2022) |
| **Wave 4 (Page 4)** | **100% COMPLETE** | Maths P2, Physics P2, English FAL P1, Afrikaans FAL P1 (2022) |
| **Wave 5 (Page 5)** | **100% COMPLETE** | Maths P1, Physics P1, English HL P1, Afrikaans HL P1 (2021) |
| **Wave 6 (Page 6)** | **100% COMPLETE** | Maths P2, Physics P2, English FAL P1, Afrikaans FAL P1 (2021) |
| **Wave 7 (Page 7)** | **100% COMPLETE** | Maths P1, Physics P1, English HL P1, Afrikaans HL P1 (2020) |
| **Wave 8 (Page 8)** | **100% COMPLETE** | Maths P2, Physics P2, English FAL P1, Afrikaans FAL P1 (2020) |
| **Wave 9 (Page 9)** | **100% COMPLETE** | Maths P1, Physics P1, English HL P1, Afrikaans HL P1 (2019) |
| **Wave 10 (Page 10)** | **100% COMPLETE** | Maths P2, Physics P2, English FAL P1, Afrikaans FAL P1 (2019) |
| **Wave 11 (Page 11)** | **100% COMPLETE** | Maths P1, Physics P1, English HL P1, Afrikaans HL P1 (2018) |
| **Wave 12 (Page 12)** | **100% COMPLETE** | Maths P2, Physics P2, English FAL P1, Afrikaans FAL P1 (2018) |
| **Total Extracted Items** | **13169 Items** | KaTeX formatted, UDVES standardized, atomic multiple choice |
| **Total Marks Accounted** | **31282 Marks** | 100% agreement with DBE official memorandums |
| **Quarantined Benchmark** | **33 Papers** | Locked in `workspace/eval/` — 0% training contamination |

---

## 2. Page 1: Pilot Wave (Completed & Verified)

| Status | Source ID | Subject | Grade | Session | Items | Marks | KaTeX Errors | Flagged Review | Dual Mirror |
|:---:|---|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| [x] | `dbe-mathematics-g12-p1-2023-nov` | mathematics | Gr 12 | 2023 Nov | **51** | **150** | 0 | 0 | Yes |
| [x] | `dbe-physical_sciences-g12-p2-2025-nov` | physical | Gr 12 | 2025 Nov | **68** | **150** | 0 | 0 | Yes |
| [x] | `dbe-english_hl-g12-p1-2023-nov` | english | Gr 12 | 2023 Nov | **35** | **70** | 0 | 0 | Yes |
| [x] | `dbe-afrikaans_hl-g12-p1-2023-nov` | afrikaans | Gr 12 | 2023 Nov | **41** | **70** | 0 | 0 | Yes |

---

## 3. Page 2: Wave 2 (Grade 12 Nov 2023 Wave)

| Status | Source ID | Subject | Grade | Session | Items | Marks | KaTeX Errors | Flagged Review | Dual Mirror |
|:---:|---|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| [x] | `dbe-mathematics-g12-p2-2023-nov` | mathematics | Gr 12 | 2023 Nov | **53** | **150/150** | 0 | 0 | Yes |
| [x] | `dbe-physical_sciences-g12-p1-2023-nov` | physical | Gr 12 | 2023 Nov | **61** | **150/150** | 0 | 0 | Yes |
| [x] | `dbe-english_fal-g12-p1-2023-nov` | english | Gr 12 | 2023 Nov | **47** | **80/80** | 0 | 0 | Yes |
| [x] | `dbe-afrikaans_fal-g12-p1-2023-nov` | afrikaans | Gr 12 | 2023 Nov | **68** | **80/80** | 0 | 0 | Yes |

---

## 4. Page 3: Wave 3 (Grade 12 Nov 2022 Core STEM & Languages)

| Status | Source ID | Subject | Grade | Session | Items | Marks | KaTeX Errors | Flagged Review | Dual Mirror |
|:---:|---|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| [x] | `dbe-mathematics-g12-p1-2022-nov` | mathematics | Gr 12 | 2022 Nov | **49** | **150/150** | 0 | 0 | Yes |
| [x] | `dbe-physical_sciences-g12-p1-2022-nov` | physical | Gr 12 | 2022 Nov | **59** | **150/150** | 0 | 0 | Yes |
| [x] | `dbe-english_hl-g12-p1-2022-nov` | english | Gr 12 | 2022 Nov | **32** | **70/70** | 0 | 0 | Yes |
| [x] | `dbe-afrikaans_hl-g12-p1-2022-nov` | afrikaans | Gr 12 | 2022 Nov | **42** | **70/70** | 0 | 0 | Yes |

---

## 5. Page 4: Wave 4 (Grade 12 Nov 2022 Core STEM & FAL)

| Status | Source ID | Subject | Grade | Session | Items | Marks | KaTeX Errors | Flagged Review | Dual Mirror |
|:---:|---|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| [x] | `dbe-mathematics-g12-p2-2022-nov` | mathematics | Gr 12 | 2022 Nov | **54** | **150/150** | 0 | 0 | Yes |
| [x] | `dbe-physical_sciences-g12-p2-2022-nov` | physical | Gr 12 | 2022 Nov | **68** | **150/150** | 0 | 0 | Yes |
| [x] | `dbe-english_fal-g12-p1-2022-nov` | english | Gr 12 | 2022 Nov | **48** | **80/80** | 0 | 0 | Yes |
| [x] | `dbe-afrikaans_fal-g12-p1-2022-nov` | afrikaans | Gr 12 | 2022 Nov | **66** | **80/80** | 0 | 0 | Yes |

---

## 6. Page 5: Wave 5 (Grade 12 Nov 2021 Core Wave)

| Status | Source ID | Subject | Grade | Session | Items | Marks | KaTeX Errors | Flagged Review | Dual Mirror |
|:---:|---|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| [x] | `dbe-mathematics-g12-p1-2021-nov` | mathematics | Gr 12 | 2021 Nov | **52** | **150/150** | 0 | 0 | Yes |
| [x] | `dbe-physical_sciences-g12-p1-2021-nov` | physical | Gr 12 | 2021 Nov | **56** | **150/150** | 0 | 0 | Yes |
| [x] | `dbe-english_hl-g12-p1-2021-nov` | english | Gr 12 | 2021 Nov | **31** | **70/70** | 0 | 0 | Yes |
| [x] | `dbe-afrikaans_hl-g12-p1-2021-nov` | afrikaans | Gr 12 | 2021 Nov | **47** | **70/70** | 0 | 0 | Yes |

---

## 7. Page 6: Wave 6 (Grade 12 Nov 2021 Core STEM & FAL)

| Status | Source ID | Subject | Grade | Session | Items | Marks | KaTeX Errors | Flagged Review | Dual Mirror |
|:---:|---|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| [x] | `dbe-mathematics-g12-p2-2021-nov` | mathematics | Gr 12 | 2021 Nov | **52** | **150/150** | 0 | 0 | Yes |
| [x] | `dbe-physical_sciences-g12-p2-2021-nov` | physical | Gr 12 | 2021 Nov | **71** | **150/150** | 0 | 0 | Yes |
| [x] | `dbe-english_fal-g12-p1-2021-nov` | english | Gr 12 | 2021 Nov | **49** | **80/80** | 0 | 0 | Yes |
| [x] | `dbe-afrikaans_fal-g12-p1-2021-nov` | afrikaans | Gr 12 | 2021 Nov | **63** | **80/80** | 0 | 0 | Yes |

---

## 8. Page 7: Wave 7 (Grade 12 Nov 2020 Core STEM & HL)

| Status | Source ID | Subject | Grade | Session | Items | Marks | KaTeX Errors | Flagged Review | Dual Mirror |
|:---:|---|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| [x] | `dbe-mathematics-g12-p1-2020-nov` | mathematics | Gr 12 | 2020 Nov | **48** | **150/150** | 0 | 0 | Yes |
| [x] | `dbe-physical_sciences-g12-p1-2020-nov` | physical | Gr 12 | 2020 Nov | **57** | **150/150** | 0 | 0 | Yes |
| [x] | `dbe-english_hl-g12-p1-2020-nov` | english | Gr 12 | 2020 Nov | **29** | **70/70** | 0 | 0 | Yes |
| [x] | `dbe-afrikaans_hl-g12-p1-2020-nov` | afrikaans | Gr 12 | 2020 Nov | **41** | **70/70** | 0 | 0 | Yes |

---

## 9. Page 8: Wave 8 (Grade 12 Nov 2020 Core STEM & FAL)

| Status | Source ID | Subject | Grade | Session | Items | Marks | KaTeX Errors | Flagged Review | Dual Mirror |
|:---:|---|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| [x] | `dbe-mathematics-g12-p2-2020-nov` | mathematics | Gr 12 | 2020 Nov | **51** | **150/150** | 0 | 0 | Yes |
| [x] | `dbe-physical_sciences-g12-p2-2020-nov` | physical | Gr 12 | 2020 Nov | **71** | **150/150** | 0 | 0 | Yes |
| [x] | `dbe-english_fal-g12-p1-2020-nov` | english | Gr 12 | 2020 Nov | **48** | **80/80** | 0 | 0 | Yes |
| [x] | `dbe-afrikaans_fal-g12-p1-2020-nov` | afrikaans | Gr 12 | 2020 Nov | **67** | **80/80** | 0 | 0 | Yes |

---

## 10. Page 9: Wave 9 (Grade 12 Nov 2019 Core STEM & HL)

| Status | Source ID | Subject | Grade | Session | Items | Marks | KaTeX Errors | Flagged Review | Dual Mirror |
|:---:|---|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| [x] | `dbe-mathematics-g12-p1-2019-nov` | mathematics | Gr 12 | 2019 Nov | **48** | **150/150** | 0 | 0 | Yes |
| [x] | `dbe-physical_sciences-g12-p1-2019-nov` | physical | Gr 12 | 2019 Nov | **59** | **150/150** | 0 | 0 | Yes |
| [x] | `dbe-english_hl-g12-p1-2019-nov` | english | Gr 12 | 2019 Nov | **30** | **70/70** | 0 | 0 | Yes |
| [x] | `dbe-afrikaans_hl-g12-p1-2019-nov` | afrikaans | Gr 12 | 2019 Nov | **42** | **70/70** | 0 | 0 | Yes |

---

## 11. Page 10: Wave 10 (Grade 12 Nov 2019 Core STEM & FAL)

| Status | Source ID | Subject | Grade | Session | Items | Marks | KaTeX Errors | Flagged Review | Dual Mirror |
|:---:|---|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| [x] | `dbe-mathematics-g12-p2-2019-nov` | mathematics | Gr 12 | 2019 Nov | **46** | **150/150** | 0 | 0 | Yes |
| [x] | `dbe-physical_sciences-g12-p2-2019-nov` | physical | Gr 12 | 2019 Nov | **68** | **150/150** | 0 | 0 | Yes |
| [x] | `dbe-english_fal-g12-p1-2019-nov` | english | Gr 12 | 2019 Nov | **47** | **80/80** | 0 | 0 | Yes |
| [x] | `dbe-afrikaans_fal-g12-p1-2019-nov` | afrikaans | Gr 12 | 2019 Nov | **67** | **80/80** | 0 | 0 | Yes |

---

## 12. Page 11: Wave 11 (Grade 12 Nov 2018 Core STEM & HL)

| Status | Source ID | Subject | Grade | Session | Items | Marks | KaTeX Errors | Flagged Review | Dual Mirror |
|:---:|---|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| [x] | `dbe-mathematics-g12-p1-2018-nov` | mathematics | Gr 12 | 2018 Nov | **48** | **150/150** | 0 | 0 | Yes |
| [x] | `dbe-physical_sciences-g12-p1-2018-nov` | physical | Gr 12 | 2018 Nov | **60** | **150/150** | 0 | 0 | Yes |
| [x] | `dbe-english_hl-g12-p1-2018-nov` | english | Gr 12 | 2018 Nov | **29** | **70/70** | 0 | 0 | Yes |
| [x] | `dbe-afrikaans_hl-g12-p1-2018-nov` | afrikaans | Gr 12 | 2018 Nov | **44** | **70/70** | 0 | 0 | Yes |

---

## 13. Page 12: Wave 12 (Grade 12 Nov 2018 Core STEM & FAL)

| Status | Source ID | Subject | Grade | Session | Items | Marks | KaTeX Errors | Flagged Review | Dual Mirror |
|:---:|---|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| [x] | `dbe-mathematics-g12-p2-2018-nov` | mathematics | Gr 12 | 2018 Nov | **60** | **150/150** | 0 | 0 | Yes |
| [x] | `dbe-physical_sciences-g12-p2-2018-nov` | physical | Gr 12 | 2018 Nov | **72** | **150/150** | 0 | 0 | Yes |
| [x] | `dbe-english_fal-g12-p1-2018-nov` | english | Gr 12 | 2018 Nov | **47** | **80/80** | 0 | 0 | Yes |
| [x] | `dbe-afrikaans_fal-g12-p1-2018-nov` | afrikaans | Gr 12 | 2018 Nov | **68** | **80/80** | 0 | 0 | Yes |

---

## 13. Page 13: May/June & 2025 Sessions (Recent Completions)

| Status | Source ID | Subject | Grade | Session | Items | Marks | KaTeX Errors | Flagged Review | Dual Mirror |
|:---:|---|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| [x] | `dbe-afrikaans_fal-g12-p1-2018-may` | afrikaans | Gr 12 | 2018 | **67** | **80** | 0 | 0 | Yes |
| [x] | `dbe-afrikaans_fal-g12-p1-2019-may` | afrikaans | Gr 12 | 2019 | **69** | **80** | 0 | 0 | Yes |
| [x] | `dbe-afrikaans_fal-g12-p1-2021-may` | afrikaans | Gr 12 | 2021 | **56** | **70** | 0 | 0 | Yes |
| [x] | `dbe-afrikaans_fal-g12-p1-2022-may` | afrikaans | Gr 12 | 2022 | **60** | **70** | 0 | 0 | Yes |
| [x] | `dbe-afrikaans_fal-g12-p1-2023-may` | afrikaans | Gr 12 | 2023 | **68** | **80** | 0 | 0 | Yes |
| [x] | `dbe-afrikaans_fal-g12-p1-2025-may` | afrikaans | Gr 12 | 2025 | **66** | **80** | 11 | 0 | Yes |
| [x] | `dbe-afrikaans_fal-g12-p1-2025-nov` | afrikaans | Gr 12 | 2025 | **68** | **80** | 0 | 0 | Yes |
| [x] | `dbe-afrikaans_fal-g12-p2-2018-may` | afrikaans | Gr 12 | 2018 | **65** | **80** | 0 | 0 | Yes |
| [x] | `dbe-afrikaans_fal-g12-p2-2018-nov` | afrikaans | Gr 12 | 2018 | **65** | **88** | 0 | 0 | Yes |
| [x] | `dbe-afrikaans_fal-g12-p2-2019-may` | afrikaans | Gr 12 | 2019 | **78** | **101** | 0 | 0 | Yes |
| [x] | `dbe-afrikaans_fal-g12-p2-2019-nov` | afrikaans | Gr 12 | 2019 | **73** | **87** | 0 | 0 | Yes |
| [x] | `dbe-afrikaans_fal-g12-p2-2020-nov` | afrikaans | Gr 12 | 2020 | **71** | **79** | 0 | 0 | Yes |
| [x] | `dbe-afrikaans_fal-g12-p2-2021-may` | afrikaans | Gr 12 | 2021 | **70** | **87** | 0 | 0 | Yes |
| [x] | `dbe-afrikaans_fal-g12-p2-2021-nov` | afrikaans | Gr 12 | 2021 | **79** | **108** | 0 | 0 | Yes |
| [x] | `dbe-afrikaans_fal-g12-p2-2022-may` | afrikaans | Gr 12 | 2022 | **83** | **107** | 0 | 0 | Yes |
| [x] | `dbe-afrikaans_fal-g12-p2-2022-nov` | afrikaans | Gr 12 | 2022 | **56** | **96** | 0 | 0 | Yes |
| [x] | `dbe-afrikaans_fal-g12-p2-2023-may` | afrikaans | Gr 12 | 2023 | **66** | **98** | 0 | 0 | Yes |
| [x] | `dbe-afrikaans_fal-g12-p2-2023-nov` | afrikaans | Gr 12 | 2023 | **66** | **77** | 0 | 0 | Yes |
| [x] | `dbe-afrikaans_fal-g12-p2-2025-may` | afrikaans | Gr 12 | 2025 | **73** | **88** | 0 | 0 | Yes |
| [x] | `dbe-afrikaans_fal-g12-p2-2025-nov` | afrikaans | Gr 12 | 2025 | **270** | **315** | 0 | 0 | Yes |
| [x] | `dbe-afrikaans_hl-g12-p1-2018-may` | afrikaans | Gr 12 | 2018 | **46** | **70** | 0 | 0 | Yes |
| [x] | `dbe-afrikaans_hl-g12-p1-2019-may` | afrikaans | Gr 12 | 2019 | **44** | **70** | 0 | 0 | Yes |
| [x] | `dbe-afrikaans_hl-g12-p1-2021-may` | afrikaans | Gr 12 | 2021 | **44** | **70** | 0 | 0 | Yes |
| [x] | `dbe-afrikaans_hl-g12-p1-2022-may` | afrikaans | Gr 12 | 2022 | **44** | **70** | 0 | 0 | Yes |
| [x] | `dbe-afrikaans_hl-g12-p1-2023-may` | afrikaans | Gr 12 | 2023 | **38** | **70** | 0 | 0 | Yes |
| [x] | `dbe-afrikaans_hl-g12-p1-2025-may` | afrikaans | Gr 12 | 2025 | **41** | **70** | 0 | 0 | Yes |
| [x] | `dbe-afrikaans_hl-g12-p1-2025-nov` | afrikaans | Gr 12 | 2025 | **39** | **70** | 0 | 0 | Yes |
| [x] | `dbe-afrikaans_hl-g12-p2-2018-may` | afrikaans | Gr 12 | 2018 | **53** | **131** | 0 | 0 | Yes |
| [x] | `dbe-afrikaans_hl-g12-p2-2018-nov` | afrikaans | Gr 12 | 2018 | **48** | **142** | 0 | 0 | Yes |
| [x] | `dbe-afrikaans_hl-g12-p2-2019-may` | afrikaans | Gr 12 | 2019 | **51** | **150** | 0 | 0 | Yes |
| [x] | `dbe-afrikaans_hl-g12-p2-2019-nov` | afrikaans | Gr 12 | 2019 | **53** | **176** | 0 | 0 | Yes |
| [x] | `dbe-afrikaans_hl-g12-p2-2020-nov` | afrikaans | Gr 12 | 2020 | **52** | **175** | 0 | 0 | Yes |
| [x] | `dbe-afrikaans_hl-g12-p2-2021-may` | afrikaans | Gr 12 | 2021 | **43** | **118** | 0 | 0 | Yes |
| [x] | `dbe-afrikaans_hl-g12-p2-2021-nov` | afrikaans | Gr 12 | 2021 | **63** | **141** | 0 | 0 | Yes |
| [x] | `dbe-afrikaans_hl-g12-p2-2022-may` | afrikaans | Gr 12 | 2022 | **60** | **179** | 0 | 0 | Yes |
| [x] | `dbe-afrikaans_hl-g12-p2-2022-nov` | afrikaans | Gr 12 | 2022 | **57** | **144** | 0 | 0 | Yes |
| [x] | `dbe-afrikaans_hl-g12-p2-2023-may` | afrikaans | Gr 12 | 2023 | **51** | **148** | 0 | 0 | Yes |
| [x] | `dbe-afrikaans_hl-g12-p2-2023-nov` | afrikaans | Gr 12 | 2023 | **56** | **145** | 0 | 0 | Yes |
| [x] | `dbe-afrikaans_hl-g12-p2-2025-may` | afrikaans | Gr 12 | 2025 | **50** | **147** | 0 | 0 | Yes |
| [x] | `dbe-afrikaans_hl-g12-p2-2025-nov` | afrikaans | Gr 12 | 2025 | **104** | **350** | 0 | 0 | Yes |
| [x] | `dbe-english_fal-g12-p1-2018-may` | english | Gr 12 | 2018 | **51** | **80** | 0 | 0 | Yes |
| [x] | `dbe-english_fal-g12-p1-2019-may` | english | Gr 12 | 2019 | **48** | **80** | 0 | 0 | Yes |
| [x] | `dbe-english_fal-g12-p1-2021-may` | english | Gr 12 | 2021 | **49** | **80** | 0 | 0 | Yes |
| [x] | `dbe-english_fal-g12-p1-2022-may` | english | Gr 12 | 2022 | **48** | **80** | 0 | 0 | Yes |
| [x] | `dbe-english_fal-g12-p1-2023-may` | english | Gr 12 | 2023 | **48** | **80** | 0 | 0 | Yes |
| [x] | `dbe-english_fal-g12-p1-2025-may` | english | Gr 12 | 2025 | **49** | **80** | 0 | 0 | Yes |
| [x] | `dbe-english_fal-g12-p1-2025-nov` | english | Gr 12 | 2025 | **48** | **80** | 0 | 48 | Yes |
| [x] | `dbe-english_fal-g12-p2-2018-may` | english | Gr 12 | 2018 | **99** | **175** | 0 | 0 | Yes |
| [x] | `dbe-english_fal-g12-p2-2018-nov` | english | Gr 12 | 2018 | **202** | **391** | 0 | 0 | Yes |
| [x] | `dbe-english_fal-g12-p2-2019-may` | english | Gr 12 | 2019 | **86** | **175** | 0 | 0 | Yes |
| [x] | `dbe-english_fal-g12-p2-2019-nov` | english | Gr 12 | 2019 | **6** | **169** | 0 | 0 | Yes |
| [x] | `dbe-english_fal-g12-p2-2020-nov` | english | Gr 12 | 2020 | **68** | **140** | 0 | 0 | Yes |
| [x] | `dbe-english_fal-g12-p2-2021-may` | english | Gr 12 | 2021 | **90** | **175** | 0 | 0 | Yes |
| [x] | `dbe-english_fal-g12-p2-2021-nov` | english | Gr 12 | 2021 | **81** | **158** | 0 | 0 | Yes |
| [x] | `dbe-english_fal-g12-p2-2022-may` | english | Gr 12 | 2022 | **78** | **156** | 0 | 0 | Yes |
| [x] | `dbe-english_fal-g12-p2-2022-nov` | english | Gr 12 | 2022 | **84** | **175** | 0 | 0 | Yes |
| [x] | `dbe-english_fal-g12-p2-2023-may` | english | Gr 12 | 2023 | **86** | **175** | 0 | 0 | Yes |
| [x] | `dbe-english_fal-g12-p2-2023-nov` | english | Gr 12 | 2023 | **90** | **175** | 0 | 0 | Yes |
| [x] | `dbe-english_fal-g12-p2-2025-may` | english | Gr 12 | 2025 | **105** | **210** | 0 | 0 | Yes |
| [x] | `dbe-english_fal-g12-p2-2025-nov` | english | Gr 12 | 2025 | **90** | **210** | 0 | 90 | Yes |
| [x] | `dbe-english_hl-g12-p1-2018-may` | english | Gr 12 | 2018 | **29** | **70** | 0 | 0 | Yes |
| [x] | `dbe-english_hl-g12-p1-2019-may` | english | Gr 12 | 2019 | **29** | **70** | 0 | 0 | Yes |
| [x] | `dbe-english_hl-g12-p1-2021-may` | english | Gr 12 | 2021 | **29** | **70** | 0 | 0 | Yes |
| [x] | `dbe-english_hl-g12-p1-2022-may` | english | Gr 12 | 2022 | **33** | **70** | 0 | 0 | Yes |
| [x] | `dbe-english_hl-g12-p1-2023-may` | english | Gr 12 | 2023 | **31** | **70** | 0 | 0 | Yes |
| [x] | `dbe-english_hl-g12-p1-2025-may` | english | Gr 12 | 2025 | **36** | **70** | 0 | 0 | Yes |
| [x] | `dbe-english_hl-g12-p1-2025-nov` | english | Gr 12 | 2025 | **33** | **70** | 0 | 0 | Yes |
| [x] | `dbe-english_hl-g12-p2-2018-may` | english | Gr 12 | 2018 | **50** | **218** | 0 | 0 | Yes |
| [x] | `dbe-english_hl-g12-p2-2018-nov` | english | Gr 12 | 2018 | **48** | **234** | 0 | 0 | Yes |
| [x] | `dbe-english_hl-g12-p2-2019-may` | english | Gr 12 | 2019 | **40** | **187** | 0 | 0 | Yes |
| [x] | `dbe-english_hl-g12-p2-2019-nov` | english | Gr 12 | 2019 | **48** | **234** | 0 | 0 | Yes |
| [x] | `dbe-english_hl-g12-p2-2020-nov` | english | Gr 12 | 2020 | **48** | **234** | 0 | 0 | Yes |
| [x] | `dbe-english_hl-g12-p2-2021-may` | english | Gr 12 | 2021 | **49** | **237** | 0 | 0 | Yes |
| [x] | `dbe-english_hl-g12-p2-2021-nov` | english | Gr 12 | 2021 | **49** | **237** | 0 | 0 | Yes |
| [x] | `dbe-english_hl-g12-p2-2022-may` | english | Gr 12 | 2022 | **49** | **237** | 0 | 0 | Yes |
| [x] | `dbe-english_hl-g12-p2-2022-nov` | english | Gr 12 | 2022 | **49** | **228** | 0 | 0 | Yes |
| [x] | `dbe-english_hl-g12-p2-2023-may` | english | Gr 12 | 2023 | **67** | **300** | 0 | 0 | Yes |
| [x] | `dbe-english_hl-g12-p2-2023-nov` | english | Gr 12 | 2023 | **52** | **225** | 0 | 0 | Yes |
| [x] | `dbe-english_hl-g12-p2-2025-may` | english | Gr 12 | 2025 | **76** | **300** | 0 | 0 | Yes |
| [x] | `dbe-english_hl-g12-p2-2025-nov` | english | Gr 12 | 2025 | **77** | **300** | 0 | 0 | Yes |
| [x] | `dbe-fisiese_wetenskappe-g10-v1-2015-nov` | fisiese | Gr 10 | 2015 | **69** | **163** | 0 | 1 | Yes |
| [x] | `dbe-fisiese_wetenskappe-g10-v1-2016-nov` | fisiese | Gr 10 | 2016 | **76** | **164** | 0 | 0 | Yes |
| [x] | `dbe-fisiese_wetenskappe-g10-v1-2017-nov` | fisiese | Gr 10 | 2017 | **52** | **124** | 0 | 0 | Yes |
| [x] | `dbe-fisiese_wetenskappe-g10-v1-2018-nov` | fisiese | Gr 10 | 2018 | **52** | **131** | 0 | 0 | Yes |
| [x] | `dbe-fisiese_wetenskappe-g10-v2-2015-nov` | fisiese | Gr 10 | 2015 | **60** | **103** | 0 | 0 | Yes |
| [x] | `dbe-fisiese_wetenskappe-g10-v2-2016-nov` | fisiese | Gr 10 | 2016 | **34** | **65** | 0 | 0 | Yes |
| [x] | `dbe-fisiese_wetenskappe-g10-v2-2017-nov` | fisiese | Gr 10 | 2017 | **23** | **64** | 0 | 0 | Yes |
| [x] | `dbe-fisiese_wetenskappe-g10-v2-2018-nov` | fisiese | Gr 10 | 2018 | **55** | **107** | 0 | 1 | Yes |
| [x] | `dbe-fisiese_wetenskappe-g11-v1-2015-nov` | fisiese | Gr 11 | 2015 | **46** | **121** | 0 | 0 | Yes |
| [x] | `dbe-fisiese_wetenskappe-g11-v1-2016-nov` | fisiese | Gr 11 | 2016 | **14** | **35** | 0 | 0 | Yes |
| [x] | `dbe-fisiese_wetenskappe-g11-v1-2017-nov` | fisiese | Gr 11 | 2017 | **35** | **88** | 0 | 0 | Yes |
| [x] | `dbe-fisiese_wetenskappe-g11-v1-2018-nov` | fisiese | Gr 11 | 2018 | **25** | **60** | 0 | 0 | Yes |
| [x] | `dbe-fisiese_wetenskappe-g11-v2-2015-nov` | fisiese | Gr 11 | 2015 | **29** | **48** | 0 | 0 | Yes |
| [x] | `dbe-fisiese_wetenskappe-g11-v2-2016-nov` | fisiese | Gr 11 | 2016 | **33** | **86** | 0 | 0 | Yes |
| [x] | `dbe-fisiese_wetenskappe-g11-v2-2017-nov` | fisiese | Gr 11 | 2017 | **43** | **143** | 0 | 1 | Yes |
| [x] | `dbe-fisiese_wetenskappe-g11-v2-2018-nov` | fisiese | Gr 11 | 2018 | **66** | **150** | 0 | 0 | Yes |
| [x] | `dbe-fisiese_wetenskappe-g12-v1-2018-may` | fisiese | Gr 12 | 2018 | **55** | **149** | 0 | 0 | Yes |
| [x] | `dbe-fisiese_wetenskappe-g12-v1-2018-nov` | fisiese | Gr 12 | 2018 | **12** | **37** | 0 | 0 | Yes |
| [x] | `dbe-fisiese_wetenskappe-g12-v1-2019-may` | fisiese | Gr 12 | 2019 | **19** | **55** | 0 | 0 | Yes |
| [x] | `dbe-fisiese_wetenskappe-g12-v1-2020-nov` | fisiese | Gr 12 | 2020 | **18** | **55** | 0 | 0 | Yes |
| [x] | `dbe-fisiese_wetenskappe-g12-v1-2021-may` | fisiese | Gr 12 | 2021 | **35** | **102** | 0 | 0 | Yes |
| [x] | `dbe-fisiese_wetenskappe-g12-v1-2021-nov` | fisiese | Gr 12 | 2021 | **24** | **69** | 0 | 0 | Yes |
| [x] | `dbe-fisiese_wetenskappe-g12-v1-2022-may` | fisiese | Gr 12 | 2022 | **11** | **39** | 0 | 0 | Yes |
| [x] | `dbe-fisiese_wetenskappe-g12-v1-2022-nov` | fisiese | Gr 12 | 2022 | **28** | **88** | 0 | 0 | Yes |
| [x] | `dbe-fisiese_wetenskappe-g12-v1-2023-may` | fisiese | Gr 12 | 2023 | **34** | **111** | 0 | 0 | Yes |
| [x] | `dbe-fisiese_wetenskappe-g12-v1-2023-nov` | fisiese | Gr 12 | 2023 | **46** | **117** | 0 | 0 | Yes |
| [x] | `dbe-fisiese_wetenskappe-g12-v1-2025-may` | fisiese | Gr 12 | 2025 | **41** | **120** | 0 | 2 | Yes |
| [x] | `dbe-fisiese_wetenskappe-g12-v1-2025-nov` | fisiese | Gr 12 | 2025 | **46** | **132** | 0 | 0 | Yes |
| [x] | `dbe-fisiese_wetenskappe-g12-v2-2018-may` | fisiese | Gr 12 | 2018 | **32** | **78** | 0 | 0 | Yes |
| [x] | `dbe-fisiese_wetenskappe-g12-v2-2018-nov` | fisiese | Gr 12 | 2018 | **17** | **30** | 0 | 0 | Yes |
| [x] | `dbe-fisiese_wetenskappe-g12-v2-2019-may` | fisiese | Gr 12 | 2019 | **73** | **150** | 0 | 1 | Yes |
| [x] | `dbe-fisiese_wetenskappe-g12-v2-2020-nov` | fisiese | Gr 12 | 2020 | **65** | **130** | 0 | 0 | Yes |
| [x] | `dbe-fisiese_wetenskappe-g12-v2-2021-may` | fisiese | Gr 12 | 2021 | **21** | **64** | 0 | 0 | Yes |
| [x] | `dbe-fisiese_wetenskappe-g12-v2-2021-nov` | fisiese | Gr 12 | 2021 | **24** | **57** | 0 | 0 | Yes |
| [x] | `dbe-fisiese_wetenskappe-g12-v2-2022-may` | fisiese | Gr 12 | 2022 | **11** | **34** | 0 | 0 | Yes |
| [x] | `dbe-fisiese_wetenskappe-g12-v2-2022-nov` | fisiese | Gr 12 | 2022 | **13** | **34** | 0 | 0 | Yes |
| [x] | `dbe-fisiese_wetenskappe-g12-v2-2023-may` | fisiese | Gr 12 | 2023 | **55** | **125** | 0 | 0 | Yes |
| [x] | `dbe-fisiese_wetenskappe-g12-v2-2023-nov` | fisiese | Gr 12 | 2023 | **22** | **64** | 0 | 0 | Yes |
| [x] | `dbe-fisiese_wetenskappe-g12-v2-2025-may` | fisiese | Gr 12 | 2025 | **69** | **150** | 0 | 0 | Yes |
| [x] | `dbe-fisiese_wetenskappe-g12-v2-2025-nov` | fisiese | Gr 12 | 2025 | **26** | **72** | 0 | 0 | Yes |
| [x] | `dbe-mathematics-g10-p1-2015-nov` | mathematics | Gr 10 | 2015 | **33** | **89** | 0 | 0 | Yes |
| [x] | `dbe-mathematics-g10-p1-2016-nov` | mathematics | Gr 10 | 2016 | **32** | **76** | 0 | 0 | Yes |
| [x] | `dbe-mathematics-g10-p1-2017-nov` | mathematics | Gr 10 | 2017 | **38** | **86** | 1 | 0 | Yes |
| [x] | `dbe-mathematics-g10-p1-2018-nov` | mathematics | Gr 10 | 2018 | **20** | **41** | 0 | 0 | Yes |
| [x] | `dbe-mathematics-g10-p2-2015-nov` | mathematics | Gr 10 | 2015 | **15** | **31** | 0 | 0 | Yes |
| [x] | `dbe-mathematics-g10-p2-2016-nov` | mathematics | Gr 10 | 2016 | **21** | **58** | 0 | 0 | Yes |
| [x] | `dbe-mathematics-g10-p2-2017-nov` | mathematics | Gr 10 | 2017 | **39** | **100** | 0 | 0 | Yes |
| [x] | `dbe-mathematics-g10-p2-2018-nov` | mathematics | Gr 10 | 2018 | **18** | **42** | 0 | 0 | Yes |
| [x] | `dbe-mathematics-g11-p1-2015-nov` | mathematics | Gr 11 | 2015 | **29** | **89** | 0 | 1 | Yes |
| [x] | `dbe-mathematics-g11-p1-2016-nov` | mathematics | Gr 11 | 2016 | **42** | **124** | 0 | 0 | Yes |
| [x] | `dbe-mathematics-g11-p1-2017-nov` | mathematics | Gr 11 | 2017 | **48** | **150** | 0 | 0 | Yes |
| [x] | `dbe-mathematics-g11-p1-2018-nov` | mathematics | Gr 11 | 2018 | **6** | **21** | 0 | 0 | Yes |
| [x] | `dbe-mathematics-g11-p2-2015-nov` | mathematics | Gr 11 | 2015 | **55** | **152** | 0 | 0 | Yes |
| [x] | `dbe-mathematics-g11-p2-2016-nov` | mathematics | Gr 11 | 2016 | **26** | **64** | 0 | 0 | Yes |
| [x] | `dbe-mathematics-g11-p2-2017-nov` | mathematics | Gr 11 | 2017 | **10** | **27** | 0 | 0 | Yes |
| [x] | `dbe-mathematics-g11-p2-2018-nov` | mathematics | Gr 11 | 2018 | **49** | **138** | 0 | 0 | Yes |
| [x] | `dbe-mathematics-g12-p1-2018-may` | mathematics | Gr 12 | 2018 | **1** | **4** | 0 | 0 | No |
| [x] | `dbe-mathematics-g12-p1-2019-may` | mathematics | Gr 12 | 2019 | **12** | **35** | 0 | 6 | Yes |
| [x] | `dbe-mathematics-g12-p1-2021-may` | mathematics | Gr 12 | 2021 | **11** | **41** | 0 | 0 | Yes |
| [x] | `dbe-mathematics-g12-p1-2022-may` | mathematics | Gr 12 | 2022 | **46** | **150** | 0 | 0 | Yes |
| [x] | `dbe-mathematics-g12-p1-2023-may` | mathematics | Gr 12 | 2023 | **52** | **150** | 0 | 0 | Yes |
| [x] | `dbe-mathematics-g12-p1-2025-may` | mathematics | Gr 12 | 2025 | **47** | **150** | 0 | 0 | Yes |
| [x] | `dbe-mathematics-g12-p1-2025-nov` | mathematics | Gr 12 | 2025 | **49** | **150** | 0 | 0 | Yes |
| [x] | `dbe-mathematics-g12-p2-2019-may` | mathematics | Gr 12 | 2019 | **5** | **10** | 0 | 0 | Yes |
| [x] | `dbe-mathematics-g12-p2-2022-may` | mathematics | Gr 12 | 2022 | **53** | **150** | 0 | 0 | Yes |
| [x] | `dbe-mathematics-g12-p2-2023-may` | mathematics | Gr 12 | 2023 | **55** | **150** | 0 | 2 | Yes |
| [x] | `dbe-mathematics-g12-p2-2025-may` | mathematics | Gr 12 | 2025 | **52** | **150** | 0 | 0 | Yes |
| [x] | `dbe-mathematics-g12-p2-2025-nov` | mathematics | Gr 12 | 2025 | **54** | **150** | 0 | 2 | Yes |
| [x] | `dbe-physical_sciences-g10-p1-2015-nov` | physical | Gr 10 | 2015 | **55** | **132** | 0 | 0 | Yes |
| [x] | `dbe-physical_sciences-g10-p1-2016-nov` | physical | Gr 10 | 2016 | **65** | **140** | 0 | 0 | Yes |
| [x] | `dbe-physical_sciences-g10-p1-2017-nov` | physical | Gr 10 | 2017 | **62** | **150** | 0 | 1 | Yes |
| [x] | `dbe-physical_sciences-g10-p1-2018-nov` | physical | Gr 10 | 2018 | **67** | **144** | 0 | 0 | Yes |
| [x] | `dbe-physical_sciences-g10-p2-2015-nov` | physical | Gr 10 | 2015 | **83** | **150** | 0 | 0 | Yes |
| [x] | `dbe-physical_sciences-g10-p2-2016-nov` | physical | Gr 10 | 2016 | **46** | **90** | 0 | 1 | Yes |
| [x] | `dbe-physical_sciences-g10-p2-2017-nov` | physical | Gr 10 | 2017 | **4** | **6** | 0 | 0 | Yes |
| [x] | `dbe-physical_sciences-g10-p2-2018-nov` | physical | Gr 10 | 2018 | **9** | **12** | 0 | 0 | Yes |
| [x] | `dbe-physical_sciences-g11-p1-2015-nov` | physical | Gr 11 | 2015 | **50** | **142** | 0 | 0 | Yes |
| [x] | `dbe-physical_sciences-g11-p1-2016-nov` | physical | Gr 11 | 2016 | **64** | **150** | 0 | 0 | Yes |
| [x] | `dbe-physical_sciences-g11-p1-2017-nov` | physical | Gr 11 | 2017 | **60** | **150** | 0 | 0 | Yes |
| [x] | `dbe-physical_sciences-g11-p1-2018-nov` | physical | Gr 11 | 2018 | **10** | **20** | 0 | 0 | Yes |
| [x] | `dbe-physical_sciences-g11-p2-2015-nov` | physical | Gr 11 | 2015 | **77** | **150** | 0 | 0 | Yes |
| [x] | `dbe-physical_sciences-g11-p2-2016-nov` | physical | Gr 11 | 2016 | **74** | **182** | 0 | 0 | Yes |
| [x] | `dbe-physical_sciences-g11-p2-2017-nov` | physical | Gr 11 | 2017 | **52** | **127** | 0 | 0 | Yes |
| [x] | `dbe-physical_sciences-g11-p2-2018-nov` | physical | Gr 11 | 2018 | **66** | **150** | 0 | 0 | Yes |
| [x] | `dbe-physical_sciences-g12-p1-2018-may` | physical | Gr 12 | 2018 | **55** | **149** | 0 | 0 | Yes |
| [x] | `dbe-physical_sciences-g12-p1-2019-may` | physical | Gr 12 | 2019 | **56** | **150** | 0 | 0 | Yes |
| [x] | `dbe-physical_sciences-g12-p1-2021-may` | physical | Gr 12 | 2021 | **60** | **167** | 0 | 0 | Yes |
| [x] | `dbe-physical_sciences-g12-p1-2022-may` | physical | Gr 12 | 2022 | **52** | **150** | 0 | 0 | Yes |
| [x] | `dbe-physical_sciences-g12-p1-2023-may` | physical | Gr 12 | 2023 | **53** | **150** | 0 | 0 | Yes |
| [x] | `dbe-physical_sciences-g12-p1-2025-may` | physical | Gr 12 | 2025 | **55** | **150** | 0 | 0 | Yes |
| [x] | `dbe-physical_sciences-g12-p1-2025-nov` | physical | Gr 12 | 2025 | **55** | **150** | 0 | 0 | Yes |
| [x] | `dbe-physical_sciences-g12-p2-2018-may` | physical | Gr 12 | 2018 | **75** | **150** | 0 | 0 | Yes |
| [x] | `dbe-physical_sciences-g12-p2-2019-may` | physical | Gr 12 | 2019 | **73** | **150** | 0 | 0 | Yes |
| [x] | `dbe-physical_sciences-g12-p2-2021-may` | physical | Gr 12 | 2021 | **69** | **150** | 0 | 0 | Yes |
| [x] | `dbe-physical_sciences-g12-p2-2022-may` | physical | Gr 12 | 2022 | **64** | **134** | 0 | 0 | Yes |
| [x] | `dbe-physical_sciences-g12-p2-2023-may` | physical | Gr 12 | 2023 | **64** | **150** | 0 | 0 | Yes |
| [x] | `dbe-physical_sciences-g12-p2-2023-nov` | physical | Gr 12 | 2023 | **68** | **150** | 0 | 0 | Yes |
| [x] | `dbe-physical_sciences-g12-p2-2025-may` | physical | Gr 12 | 2025 | **69** | **150** | 0 | 0 | Yes |
| [x] | `dbe-wiskunde-g10-v1-2015-nov` | wiskunde | Gr 10 | 2015 | **36** | **91** | 0 | 0 | Yes |
| [x] | `dbe-wiskunde-g10-v1-2016-nov` | wiskunde | Gr 10 | 2016 | **37** | **84** | 0 | 0 | Yes |
| [x] | `dbe-wiskunde-g10-v1-2017-nov` | wiskunde | Gr 10 | 2017 | **41** | **90** | 0 | 2 | Yes |
| [x] | `dbe-wiskunde-g10-v1-2018-nov` | wiskunde | Gr 10 | 2018 | **44** | **134** | 0 | 0 | Yes |
| [x] | `dbe-wiskunde-g10-v2-2015-nov` | wiskunde | Gr 10 | 2015 | **2** | **2** | 0 | 0 | Yes |
| [x] | `dbe-wiskunde-g10-v2-2016-nov` | wiskunde | Gr 10 | 2016 | **39** | **100** | 0 | 0 | Yes |
| [x] | `dbe-wiskunde-g10-v2-2017-nov` | wiskunde | Gr 10 | 2017 | **39** | **100** | 0 | 2 | Yes |
| [x] | `dbe-wiskunde-g10-v2-2018-nov` | wiskunde | Gr 10 | 2018 | **39** | **97** | 0 | 0 | Yes |
| [x] | `dbe-wiskunde-g11-v1-2015-nov` | wiskunde | Gr 11 | 2015 | **43** | **134** | 0 | 2 | Yes |
| [x] | `dbe-wiskunde-g11-v1-2016-nov` | wiskunde | Gr 11 | 2016 | **44** | **134** | 0 | 2 | Yes |
| [x] | `dbe-wiskunde-g11-v1-2017-nov` | wiskunde | Gr 11 | 2017 | **31** | **101** | 0 | 1 | Yes |
| [x] | `dbe-wiskunde-g11-v1-2018-nov` | wiskunde | Gr 11 | 2018 | **47** | **150** | 0 | 0 | Yes |
| [x] | `dbe-wiskunde-g11-v2-2015-nov` | wiskunde | Gr 11 | 2015 | **46** | **127** | 0 | 6 | Yes |
| [x] | `dbe-wiskunde-g11-v2-2016-nov` | wiskunde | Gr 11 | 2016 | **2** | **2** | 0 | 0 | Yes |
| [x] | `dbe-wiskunde-g11-v2-2017-nov` | wiskunde | Gr 11 | 2017 | **34** | **118** | 0 | 2 | Yes |
| [x] | `dbe-wiskunde-g11-v2-2018-nov` | wiskunde | Gr 11 | 2018 | **31** | **94** | 0 | 0 | Yes |
| [x] | `dbe-wiskunde-g12-v1-2018-may` | wiskunde | Gr 12 | 2018 | **5** | **18** | 0 | 0 | Yes |
| [x] | `dbe-wiskunde-g12-v1-2018-nov` | wiskunde | Gr 12 | 2018 | **44** | **135** | 0 | 1 | Yes |
| [x] | `dbe-wiskunde-g12-v1-2019-may` | wiskunde | Gr 12 | 2019 | **43** | **124** | 0 | 17 | Yes |
| [x] | `dbe-wiskunde-g12-v1-2020-nov` | wiskunde | Gr 12 | 2020 | **38** | **116** | 0 | 5 | Yes |
| [x] | `dbe-wiskunde-g12-v1-2021-may` | wiskunde | Gr 12 | 2021 | **46** | **150** | 0 | 0 | Yes |
| [x] | `dbe-wiskunde-g12-v1-2021-nov` | wiskunde | Gr 12 | 2021 | **41** | **121** | 0 | 1 | Yes |
| [x] | `dbe-wiskunde-g12-v1-2022-may` | wiskunde | Gr 12 | 2022 | **36** | **120** | 0 | 0 | Yes |
| [x] | `dbe-wiskunde-g12-v1-2022-nov` | wiskunde | Gr 12 | 2022 | **41** | **122** | 0 | 1 | Yes |
| [x] | `dbe-wiskunde-g12-v1-2023-may` | wiskunde | Gr 12 | 2023 | **52** | **150** | 0 | 1 | Yes |
| [x] | `dbe-wiskunde-g12-v1-2023-nov` | wiskunde | Gr 12 | 2023 | **34** | **98** | 0 | 0 | Yes |
| [x] | `dbe-wiskunde-g12-v1-2025-may` | wiskunde | Gr 12 | 2025 | **28** | **93** | 0 | 2 | Yes |
| [x] | `dbe-wiskunde-g12-v1-2025-nov` | wiskunde | Gr 12 | 2025 | **38** | **117** | 0 | 0 | Yes |
| [x] | `dbe-wiskunde-g12-v2-2018-may` | wiskunde | Gr 12 | 2018 | **39** | **120** | 0 | 2 | Yes |
| [x] | `dbe-wiskunde-g12-v2-2018-nov` | wiskunde | Gr 12 | 2018 | **60** | **150** | 0 | 1 | Yes |
| [x] | `dbe-wiskunde-g12-v2-2019-may` | wiskunde | Gr 12 | 2019 | **40** | **128** | 0 | 17 | Yes |
| [x] | `dbe-wiskunde-g12-v2-2020-nov` | wiskunde | Gr 12 | 2020 | **45** | **129** | 0 | 0 | Yes |
| [x] | `dbe-wiskunde-g12-v2-2021-may` | wiskunde | Gr 12 | 2021 | **42** | **130** | 0 | 10 | Yes |
| [x] | `dbe-wiskunde-g12-v2-2021-nov` | wiskunde | Gr 12 | 2021 | **48** | **142** | 0 | 0 | Yes |
| [x] | `dbe-wiskunde-g12-v2-2022-may` | wiskunde | Gr 12 | 2022 | **35** | **101** | 0 | 0 | Yes |
| [x] | `dbe-wiskunde-g12-v2-2022-nov` | wiskunde | Gr 12 | 2022 | **1** | **1** | 0 | 0 | Yes |
| [x] | `dbe-wiskunde-g12-v2-2023-may` | wiskunde | Gr 12 | 2023 | **55** | **150** | 1 | 1 | Yes |
| [x] | `dbe-wiskunde-g12-v2-2023-nov` | wiskunde | Gr 12 | 2023 | **50** | **141** | 0 | 0 | Yes |
| [x] | `dbe-wiskunde-g12-v2-2025-may` | wiskunde | Gr 12 | 2025 | **48** | **131** | 0 | 5 | Yes |
| [x] | `dbe-wiskunde-g12-v2-2025-nov` | wiskunde | Gr 12 | 2025 | **22** | **58** | 0 | 2 | Yes |

---

## 14. Remaining Training Queue Overview

> **Total Training Papers Remaining:** 2

| Subject Track | Pending Papers | Next Up in Pipeline |
|---|:---:|---|
| **mathematics** | 2 | `dbe-mathematics-g12-p2-2021-may`, `dbe-mathematics-g12-p2-2018-may` |

---

## 15. Evaluation Benchmark Quarantine (Held-Out)

> [!IMPORTANT]
> The following 17 papers are strictly locked in `workspace/eval/` and NEVER processed into training datasets:

| Status | Source ID | Subject | Year | Notes |
|:---:|---|---|:---:|---|
| [LOCKED] | `dbe-maths-g12-p1-2024-nov` | mathematics | 2024 | `held out for EVAL (do not train on it)` |
| [LOCKED] | `dbe-afrikaans_fal-g12-p1-2024-nov` | afrikaans | 2024 | `held out for EVAL (do not train on it)` |
| [LOCKED] | `dbe-afrikaans_fal-g12-p2-2024-nov` | afrikaans | 2024 | `held out for EVAL (do not train on it)` |
| [LOCKED] | `dbe-afrikaans_hl-g12-p1-2024-nov` | afrikaans | 2024 | `held out for EVAL (do not train on it)` |
| [LOCKED] | `dbe-afrikaans_hl-g12-p2-2024-nov` | afrikaans | 2024 | `held out for EVAL (do not train on it)` |
| [LOCKED] | `dbe-english_fal-g12-p1-2024-nov` | english | 2024 | `held out for EVAL (do not train on it)` |
| [LOCKED] | `dbe-english_fal-g12-p2-2024-nov` | english | 2024 | `held out for EVAL (do not train on it)` |
| [LOCKED] | `dbe-english_hl-g12-p1-2024-nov` | english | 2024 | `held out for EVAL (do not train on it)` |
| [LOCKED] | `dbe-english_hl-g12-p2-2024-nov` | english | 2024 | `held out for EVAL (do not train on it)` |
| [LOCKED] | `dbe-mathematics-g12-p1-2024-nov` | mathematics | 2024 | `held out for EVAL (do not train on it)` |
| [LOCKED] | `dbe-wiskunde-g12-v1-2024-nov` | wiskunde | 2024 | `held out for EVAL (do not train on it)` |
| [LOCKED] | `dbe-mathematics-g12-p2-2024-nov` | mathematics | 2024 | `held out for EVAL (do not train on it)` |
| [LOCKED] | `dbe-wiskunde-g12-v2-2024-nov` | wiskunde | 2024 | `held out for EVAL (do not train on it)` |
| [LOCKED] | `dbe-physical_sciences-g12-p1-2024-nov` | physical | 2024 | `held out for EVAL (do not train on it)` |
| [LOCKED] | `dbe-fisiese_wetenskappe-g12-v1-2024-nov` | fisiese | 2024 | `held out for EVAL (do not train on it)` |
| [LOCKED] | `dbe-physical_sciences-g12-p2-2024-nov` | physical | 2024 | `held out for EVAL (do not train on it)` |
| [LOCKED] | `dbe-fisiese_wetenskappe-g12-v2-2024-nov` | fisiese | 2024 | `held out for EVAL (do not train on it)` |
| [LOCKED] | `dbe-afrikaans_fal-g12-p1-2024-may` | afrikaans | 2024 | `` |
| [LOCKED] | `dbe-afrikaans_fal-g12-p2-2024-may` | afrikaans | 2024 | `` |
| [LOCKED] | `dbe-afrikaans_hl-g12-p1-2024-may` | afrikaans | 2024 | `` |
| [LOCKED] | `dbe-afrikaans_hl-g12-p2-2024-may` | afrikaans | 2024 | `` |
| [LOCKED] | `dbe-english_fal-g12-p1-2024-may` | english | 2024 | `` |
| [LOCKED] | `dbe-english_fal-g12-p2-2024-may` | english | 2024 | `` |
| [LOCKED] | `dbe-english_hl-g12-p1-2024-may` | english | 2024 | `` |
| [LOCKED] | `dbe-english_hl-g12-p2-2024-may` | english | 2024 | `` |
| [LOCKED] | `dbe-mathematics-g12-p1-2024-may` | mathematics | 2024 | `` |
| [LOCKED] | `dbe-wiskunde-g12-v1-2024-may` | wiskunde | 2024 | `` |
| [LOCKED] | `dbe-mathematics-g12-p2-2024-may` | mathematics | 2024 | `` |
| [LOCKED] | `dbe-wiskunde-g12-v2-2024-may` | wiskunde | 2024 | `` |
| [LOCKED] | `dbe-physical_sciences-g12-p1-2024-may` | physical | 2024 | `` |
| [LOCKED] | `dbe-fisiese_wetenskappe-g12-v1-2024-may` | fisiese | 2024 | `` |
| [LOCKED] | `dbe-physical_sciences-g12-p2-2024-may` | physical | 2024 | `` |
| [LOCKED] | `dbe-fisiese_wetenskappe-g12-v2-2024-may` | fisiese | 2024 | `` |
