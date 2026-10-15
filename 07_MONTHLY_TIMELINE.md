# 🗓️ MASTER TIMELINE — Oct 2026 → Oct 2028 (the single source of truth)

> **Rebuilt**: October 15, 2026, after the full review. **If any other file disagrees with this one, this file wins.**
> **Start point (honest):** June–September 2026 produced no study. The real restart was **October 5, 2026** (`18_RESTART_8_WEEKS.md`).
> **Fixed dates this plan is built on:**
> - **Bond ends 1 Oct 2027** (+1 day for every leave day taken). Resign on/after that date → **3-month notice → last working day ≈ 1 Jan 2028.**
> - **Bremerhaven ESD = summer intake only** (April). uni-assist deadline **31 Dec** every year.
> - **Darmstadt** portal opens **December** for the next winter. **Dortmund** Pre-Check from **January**, application **1 Apr – 15 Jun**.
> - CGPA **7.87 → German ≈ 2.28**. Backlogs: **15** (14 credit + 1 non-credit), all cleared.

---

## THE SHAPE OF THE NEXT TWO YEARS

```
OCT 2026 ─┬─ PHASE 0  Restart (C basics + electronics basics)          ~3.5 h/wk
NOV 2026 ─┘
DEC 2026 ─┬─ PHASE 1  Finish C + analog basics                         ~6 h/wk
JAN 2027 ─┘
FEB 2027 ─┬─ PHASE 2  STM32 (ARM Cortex-M, drivers, ADC+DMA)           ~8–10 h/wk
  …       │           + German A1 (commute) + English foundation (daily)
MAY 2027 ─┘
JUN 2027 ─┬─ PHASE 3  ECG prototype (ADC+DMA+DSP) · APS · Goethe A1    ~8–10 h/wk
JUL 2027 ─┘
AUG 2027 ─┬─ IELTS INTENSIVE  (embedded on maintenance)
SEP 2027 ─┤
OCT 2027 ─┘  IELTS exam · BOND ENDS 1 Oct → resign · notice starts
NOV 2027 ─┬─ PHASE 4  FreeRTOS + PCB (OrCAD) · APPLICATIONS WAVE 1
DEC 2027 ─┘           Bremerhaven (31 Dec) · Darmstadt (Dec) · TUHH
JAN 2028 ─┬─ FREE (last working day ≈ 1 Jan) · full-time portfolio
  …       │  Dortmund Pre-Check · Lübeck · applications WAVE 2
MAR 2028 ─┘  ── if Bremerhaven admits you: fly ~March, start April ──
APR 2028 ─┬─ APPLICATIONS WAVE 3 (Dortmund, RWU, FAU, HAW, Chemnitz, Deggendorf)
JUL 2028 ─┘
AUG 2028 ─┬─ Admission → blocked account → visa → flight
SEP 2028 ─┘
OCT 2028 ──  START WINTER SEMESTER 2028
```

---

## WEEKLY HOURS — REALISTIC RAMP (not the old 22 h/week)

| Period | Weekdays | Saturday | Sunday | Commute (audio) | Active total |
|:---|:---|:---|:---|:---|:---|
| Oct–Nov 2026 | 15 min reading | 2 h C | 1 h electronics | English 30 min/day | **~3.5 h** |
| Dec 2026–Jan 2027 | 15–20 min | 3 h | 2 h | English | **~6 h** |
| Feb–Jul 2027 | 20–30 min | 4 h | 3 h | English + German | **~8–10 h** |
| Aug–Sep 2027 | 20 min (IELTS vocab) | 3 h IELTS + 1 h embedded | 3 h IELTS | English | IELTS-first |
| Oct–Dec 2027 (notice period) | 20–30 min | 4 h | 3 h + applications | German | **~8–10 h** |
| Jan–Sep 2028 (free) | — | — | — | — | **~30 h** (full-time) |

**Rule:** only increase hours after the previous level has held for **4 weeks in a row** in `PROGRESS.md`.

---

## MONTH BY MONTH

### 2026

#### October 2026 — Phase 0 (Restart, weeks 1–4)
- [ ] C: K.N. King Ch 1–8 (see `18_RESTART_8_WEEKS.md`)
- [ ] Electronics: Ohm's law, dividers, KVL/KCL, LED + pull-ups — **Neso Academy** + breadboard
- [ ] **Buy the Udemy cart** (8 courses, ₹4,122) before the sale ends
- [ ] **Start The English Master Course** — 30 min/day (commute or lunch). Turn **autocorrect OFF** on phone + laptop
- [ ] Bond date ✅ (1 Oct 2027) → ask HR for it **in writing**
- [ ] Ask a colleague: does Unistring use OrCAD/Allegro? Confirm the Cadence licence may be used for weekend learning
- [ ] Bremerhaven follow-up to Mr Lüders: is **Control Systems (3 credits)** enough for the 5 CP control requirement?
- [ ] **Oct 19:** one follow-up email to Chemnitz + RWU if still silent

#### November 2026 — Phase 0 (weeks 5–8)
- [ ] 🪔 Diwali week (Nov 8) = buffer
- [ ] C: K.N. King Ch 9–12 (functions, multi-file, **pointers**)
- [ ] Electronics: capacitors, RC filter, diode, transistor switch
- [ ] **Nov 29 — Restart review** (pass criteria in `18`). Pass → Phase 1. Fail → run another 8 weeks at the same size

#### December 2026 — Phase 1 (finish C)
- [ ] K.N. King Ch 13–17: strings, preprocessor, **structs/unions/enums**, advanced pointers (linked lists)
- [ ] FastBit *Embedded C* (owned) — the sections matching each chapter, at 1.5×
- [ ] Electronics: **op-amps** — TI Precision Labs (first modules)
- [ ] Hand-written: circular buffer, linked list, bit macros (`SET/CLEAR/TOGGLE/READ_BIT`)

#### January 2027 — Phase 1 (C exit)
- [ ] K.N. King Ch 18–20: declarations, program structure, **bitwise / low-level / `volatile`**
- [ ] Makefiles + GDB (content from `12C_JULY_WEEK3.md`)
- [ ] State machine with function-pointer dispatch (Miro Samek's free YouTube course for concepts)
- [ ] **Start German:** DW *Nicos Weg* A1 on the commute
- [ ] **Jan 31 — Phase 1 exit test** (5 tests from `13D_AUGUST_WEEK4.md`, from memory)

### 2027

#### February 2027 — Phase 2 (ARM Cortex-M)
- [ ] Udemy **ARM Cortex-M3/M4 Programming** (FastBit) — memory map, NVIC, exceptions, startup
- [ ] STM32 setup: CubeIDE, ST-Link, first blink **HAL + register level**
- [ ] *Practical electronics bridge* hands-on (`15_FUNDAMENTALS_BRIDGE.md`) before wiring boards

#### March–April 2027 — Phase 2 (drivers)
- [ ] FastBit **MCU1** (owned): GPIO, interrupts, UART, I²C, SPI — register-level drivers
- [ ] **Portfolio Project 1 → GitHub:** `stm32-baremetal-drivers` (GPIO/UART/I²C/SPI, README + logic-analyzer captures)
- [ ] **April:** free IELTS practice test (British Council) → honest baseline → switch from English Master Course to the **IELTS Band 7+** course

#### May 2027 — Phase 2 (ADC + DMA)
- [ ] Udemy **DMA Programming Demystified** + ADC on STM32
- [ ] Buy for the ECG prototype: AD8232 module + electrodes (~₹1,000)
- [ ] Startup Rung-0: start the **Design History File** (1 page per prototype)

#### June 2027 — Phase 3 (ECG prototype)
- [ ] **Portfolio Project 2:** AD8232 → STM32 ADC + DMA → UART → live plot of your own ECG
- [ ] Udemy **DSP From Ground Up on ARM** — first half (FIR/IIR, CMSIS-DSP)
- [ ] **Apply for APS** (aps-india.de) — needs degree certificate + **corrected** first-year memo + all memos
- [ ] Book the **Goethe A1** exam (Goethe-Zentrum Hyderabad) for July

#### July 2027 — Phase 3 (ECG prototype done)
- [ ] On-chip filtering: 50 Hz notch + baseline high-pass → heart rate from R-R intervals
- [ ] Project 2 README: block diagram, plots before/after filtering, what failed
- [ ] **Goethe-Zertifikat A1** exam
- [ ] Book IELTS for **early October**

#### August–September 2027 — IELTS INTENSIVE
- [ ] **IELTS first:** 1 full mock every weekend, 3–4 hand-written essays/week, daily speaking recording
- [ ] Embedded on maintenance: 1 h/week (tidy GitHub, write READMEs)
- [ ] German: commute audio only
- [ ] APS certificate should arrive — follow up if not
- [ ] Shortlist final universities (see `01_UNIVERSITIES.md` → "Application plan")

#### October 2027 — BOND ENDS · IELTS
- [ ] **1 Oct: bond ends** (+leave days) → **submit resignation** → notice runs to ≈ **1 Jan 2028**
- [ ] Ask HR for an **experience/service certificate** now (needed for applications before you leave)
- [ ] **IELTS exam** (early Oct). Below 7.0 → retake in November
- [ ] uni-assist: create account; the **Bremerhaven Summer 2028** round opens ~mid/late October
- [ ] Draft motivation letter + Europass CV (`05_APPLICATION_DOCS.md`)

#### November 2027 — Phase 4 + Applications Wave 1
- [ ] **Submit Bremerhaven via uni-assist** (aim Nov 30; hard deadline Dec 31)
- [ ] **Email TUHH** again (they asked you to write in November 2027)
- [ ] Udemy **Mastering RTOS (FreeRTOS)** → port Project 2 to FreeRTOS tasks
- [ ] Udemy **OrCAD/Allegro** — start; design the ECG board schematic
- [ ] IELTS retake if needed

#### December 2027 — Applications Wave 1
- [ ] **Darmstadt (IMSEIT)** portal opens → apply (own portal, no uni-assist)
- [ ] **TUHH** application window opens (1 Dec – 1 Mar)
- [ ] Optional: FH Westküste Microelectronic Systems (summer intake, 1 Dec – 15 Jan)
- [ ] **31 Dec — Bremerhaven deadline** (should already be submitted)
- [ ] Loan research (SBI Scholar / HDFC Credila) — only if family funding needs a backup

### 2028

#### January 2028 — FREE (last working day ≈ 1 Jan)
- [ ] Collect **relieving letter + experience certificate** (and an Arbeitszeugnis-style reference if HR will write one)
- [ ] **Dortmund Pre-Check** portal opens mid-January → upload documents (precheck.go-study-europe.de)
- [ ] **TH Lübeck Biomedical Engineering** — non-EU window 1 Jan – 1 May
- [ ] Full-time portfolio: **Project 3 = custom PCB** (OrCAD → order from a PCB fab) running FreeRTOS firmware
- [ ] Udemy **MCU2** (owned): timers, PWM, low power

#### February 2028 — Bremerhaven decision window
- [ ] **If Bremerhaven admits you:** open blocked account (€11,904 in 2026 — check the current amount), health insurance, **VFS visa appointment immediately**
- [ ] Otherwise: continue Project 3; German A2 (Nicos Weg)

#### March 2028
- [ ] **If Bremerhaven + visa:** fly ~mid-March, semester starts April 🎓
- [ ] Otherwise: Project 3 done; start **Project 4** (wearable: IMU + EMG/ECG + BLE via Nordic DevAcademy — the tremor-wearable direction from `Startup/11`)

#### April–July 2028 — Applications Wave 3 (Winter 2028)
| Deadline | University |
|:---|:---|
| 15 Apr | RWU Ravensburg-Weingarten (€1,500/sem) |
| 1 Apr – 15 Jun | **FH Dortmund** (needs Pre-Check code) |
| 1 May | **TH Lübeck BME** (non-EU) |
| 31 May | FAU Erlangen Medical Engineering (Medical Robotics track) |
| 15 Jul | **HAW Hamburg** (Microelectronic Systems / Biomedical Eng.), **TU Chemnitz**, **TH Deggendorf** |
- [ ] Udemy **ISO 14971** (medical device risk management) — useful for interviews and the thesis
- [ ] German A2 → Goethe A2 exam (Deggendorf needs A2 within 2 semesters; helps everywhere)

#### August–September 2028
- [ ] Accept the best offer → blocked account → health insurance → **visa** (allow 6–10 weeks) → flight → housing

#### October 2028
- [ ] 🎓 **START WINTER SEMESTER 2028**

---

## IF THINGS SLIP (decided in advance)

| Slip | What happens |
|:---|:---|
| Restart review fails (Nov 29) | Repeat 8 weeks at the same size. Everything after shifts ~2 months; Bremerhaven April 2028 likely drops, **Winter 2028 is still fine** |
| IELTS < 7.0 in Oct | Retake Nov. Most targets need only 6.0–6.5; 7.0 is the comfort target |
| IELTS not done by Dec 2027 | Skip Bremerhaven 2028 → apply Bremerhaven **April 2029** + Winter 2028 elsewhere |
| Projects behind schedule | Apply with what exists — 1 solid, documented project beats 3 half-done ones |
| No admission for Winter 2028 | Bremerhaven **April 2029** (deadline 31 Dec 2028) + Winter 2029 round, with a stronger portfolio |
| Visa late for Bremerhaven | Defer to Winter 2028 offers already in hand |

---

## WHAT EACH FILE IS FOR NOW

| File | Use |
|:---|:---|
| **`07_MONTHLY_TIMELINE.md`** (this) | **The plan.** Month-by-month |
| `18_RESTART_8_WEEKS.md` | The current 8 weeks, in detail |
| `PROGRESS.md` | Weekly honesty log + checkpoints |
| `00_MASTER_ROADMAP.md` | Profile, risks, money, contingencies |
| `01_UNIVERSITIES.md` | Target list + application plan |
| `03_GERMAN_LANGUAGE.md` · `04_IELTS_PREP.md` · `05_APPLICATION_DOCS.md` | Language + paperwork detail |
| `06_EMBEDDED_LEARNING.md` · `10_RESOURCES.md` | What to learn, from which course/book |
| `16_UNIVERSITY_ENQUIRY_EMAILS.md` · `17_GLOBAL_MASTERS_OPTIONS.md` | University replies + global options |
| `09_ULTIMATE_STUDY_PLAN.md`, `10A–13E` weekly files | **Topic content only** — their dates are from the never-executed June 2026 plan |
| `Startup/` | Long-term medical-device company plan — its Rung-0 prototypes **are** your portfolio projects |
