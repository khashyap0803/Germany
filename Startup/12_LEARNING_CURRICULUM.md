# 📚 LEARNING CURRICULUM (v3 — zero → biomedical-device engineer)

> How you (and your sister) go from "embedded engineer" to "person who can design a certified neuro wearable."
> **Four tracks run in parallel.** Track 1 is the spine; Tracks 2–4 wrap around it. Depth: **you + sister = ultra; father = technical advisor only (can't go deep into biology/clinical); mother = not on this curriculum.**
> ⏱️ All of this happens **outside your job hours** until the bond ends (~mid/late 2027). Your Unistring RF/embedded work is *paid, aligned training* — treat it as Track 1 income + practice, not a distraction.

---

## THE FOUR TRACKS AT A GLANCE

| Track | Name | Depth for you | Why it exists | AI allowed? |
|:--|:---|:---|:---|:---|
| **1** | Electronics & Embedded | Ultra | The device *is* firmware + analog + PCB. Your core craft. | ❌ **No-AI discipline** (same firmware rule as Germany plan) |
| **2** | Medical & Biosignal foundations | Working | You must understand the body signal you're measuring | ⚠️ AI for overview OK; the physiology you must truly know |
| **3** | Regulatory & Quality | Working | **This is your moat.** Free to learn, scares off amateurs, required to sell | ✅ AI fine (it's reading comprehension) |
| **4** | Clinical & market discovery | Working | A device with no validated need is a dead device | ✅ AI fine |

> **Why the no-AI rule on Track 1:** the same reason as the Germany roadmap — for firmware/hardware, AI-orchestration gives you *output without understanding*, and a medical device that fails because you didn't understand your own code can hurt someone. Track 1 you learn the hard way. Tracks 3–4 are reading/paperwork — use AI freely.

---

## TRACK 1 — ELECTRONICS & EMBEDDED (the spine)

You already have a C → STM32 → RTOS path (`06`, FastBit course, C-Practice). **That path does not change — it gains a biosignal payload.**

**1A. Solidify the base (you're partway):**
- C (pointers, memory, bit manipulation) → finish the FastBit/existing track
- ARM Cortex-M / STM32 bare-metal (registers, timers, interrupts, DMA, ADC)
- FreeRTOS (tasks, queues, timing) — real-time acquisition needs it

**1B. Analog front-end for biosignals (the new, critical skill):**
- Instrumentation amplifiers, gain, CMRR, right-leg-drive (why biopotentials need it)
- Filtering: high-pass (drift), low-pass (noise), notch (50 Hz mains — India-specific)
- Biopotential AFE chips: **AD8232** (learn on) → **ADS1292R** (ECG/resp) → **ADS1299** (EEG, 8-ch)
- Electrodes & the electrode–skin interface (Ag/AgCl, dry vs wet, impedance)

**1C. Wearable & connectivity:**
- BLE (Nordic nRF52 ecosystem), low-power design, battery management, LiPo charging safety
- PCB design in **KiCad** (free): 2-layer → 4-layer, grounding, shielding, mixed-signal layout

**1D. Signal processing & edge ML:**
- DSP: filtering, FFT, spectral analysis, wavelets, artifact removal
- Feature extraction from biosignals (heart-rate variability, tremor spectra, EEG bands)
- TinyML / edge inference (TensorFlow Lite Micro) — classify on-device (seizure? tremor severity?)

**Resources (free/cheap):** NPTEL *Biomedical Instrumentation* & *Embedded Systems*; ADI/TI application notes (the AFE datasheets ARE the textbook); KiCad official docs; Nordic DevAcademy (free); your existing FastBit course.

---

## TRACK 2 — MEDICAL & BIOSIGNAL FOUNDATIONS (know your signal)

You don't need an MBBS. You need **enough physiology to not design something clinically naïve** — and to talk to doctors credibly.

- **Bioelectricity & biopotentials:** how nerves/muscles/heart generate measurable signals
- **Cardiac:** ECG waveform, leads, arrhythmia basics, normal ranges
- **Neuro (your focus):** EEG bands (delta→gamma), neuroanatomy for engineers, what a seizure/tremor/sleep-stage *looks like* in signal, EMG for movement
- **Respiratory & metabolic:** SpO₂ principle, apnea, why sleep matters
- **Clinical measurement reality:** what units clinicians use, what "normal" is, what a false positive/negative *costs a patient* — this shapes your Class-B risk analysis

**Resources:** Webster, *Medical Instrumentation: Application and Design* (the standard); Enderle, *Introduction to Biomedical Engineering*; NPTEL biomedical courses; Coursera (audit free) for physiology; **your father** for anything bioprocess/lab-adjacent (but not clinical neuro — he's told you he can't go deep there, so that gap is filled by clinicians in `13`).

> **Father's stated limit, respected:** he advises on device/technical/quality judgement, NOT deep clinical neuro-biology. Track 2's deep clinical end is filled by the neurologists/clinicians you meet in Phase 1 (`13`), not by him.

---

## TRACK 3 — REGULATORY & QUALITY (your moat — start EARLY, it's free)

Most hobbyist engineers ignore this and die at the certification wall. **You learn it from Year 1** so your prototypes are "design-controlled from birth" — this alone puts you ahead of most first-time medtech founders.

| Standard | What it governs | Why you care |
|:---|:---|:---|
| **ISO 13485** | Quality Management System for medical devices | The master key — no QMS, no certification, no sale |
| **ISO 14971** | Risk management | You'll do this for your device from day one; defines your Class |
| **IEC 60601** | Electrical safety + EMC of medical electrical equipment | Every powered patient-contact device must pass; testing = ₹-lakhs (`14`) |
| **IEC 62304** | Medical device *software* lifecycle | Your firmware is regulated software — document it as such |
| **ISO 10993** | Biocompatibility (anything touching skin) | Electrodes/wearable straps need this — awareness now, testing later |
| **CDSCO / MDR 2017** | India's medical device regulation & classification | Defines your license path; **this is the India-specific rulebook** (`14`) |

**Design controls & the DHF (Design History File):** from your very first serious prototype, keep a **design history file** — requirements → design → verification → validation → risk. Auditors will ask for it. Starting it in Year 1 (when it's easy) instead of Year 3 (when it's a nightmare) is a genuine competitive edge.

**Resources:** CDSCO website + MDR 2017 text (free); ISO/IEC standard summaries; BIS (Bureau of Indian Standards); AdvaMed/med-device blogs; **when funded, a regulatory consultant** — but learn the vocabulary free first so you're not overcharged.

---

## TRACK 4 — CLINICAL & MARKET DISCOVERY (so the device is wanted)

Detailed method is in `13`. The *skill* to build here:
- How to **observe in a clinic** and spot an unmet need (structured, not random)
- How to **read clinical literature** (PubMed) to size a problem and check who's already solved it
- How to **talk to a clinician** — respect their time, ask about pain not features
- India-specific: **willingness/ability to pay**, reimbursement gaps, public vs private hospital reality

---

## WHO LEARNS WHAT

| Person | Tracks | Depth | Notes |
|:---|:---|:---|:---|
| **Khashyap** | 1, 2, 3, 4 (all) | Ultra on 1; working on 2–4 | Founder + lead engineer. Track 1 no-AI. |
| **Sister** (if ECE/BME/EEE — confirm Jul 10) | 1 (+2 basics) | Ultra, ramped | Co-engineer. Sem-1: 4–6 hrs/wk shadowing prototypes 1–2. From sem-2: 8–12 hrs/wk, owns a subsystem. **Degree first, always.** If she lands CSE/AI → she owns Track 1D (DSP/edge-ML) + firmware-software instead. |
| **Father** | Technical/quality advisor to Tracks 1–3 | Overview | Judges designs, warns of failure modes, brings GMP/quality discipline. **Not** clinical-neuro depth (his own stated limit). |
| **Mother** | — | — | Not on the technical curriculum. Ops/admin role stays as in `03` (registration, bookkeeping — but note: **no company to register in Year 1**, so her active role starts Phase 2). |

---

## PHASE MAP (which track dominates when — full dates in `14`)

| Phase | Window | Track focus |
|:---|:---|:---|
| **Phase 0** | Now → ~mid-2027 (during bond) | **Track 1 heavy** (prototypes 1→5) + Track 3 (learn standards) + start Track 2 |
| **Phase 1** | ~2027 | **Track 4 heavy** (clinical discovery, pick THE problem) + Track 2 deepens on chosen signal |
| **Phase 2** | Bond end → 2028 | Track 1 (build the real prototype) + Track 3 (apply design controls for real) |
| **Phase 3** | 2029–2031 | Track 3 dominates (certification), Track 1 productionizes |

➡️ **Next:** `13` — how to pick the ONE problem, with your father's criteria as a scorecard.
