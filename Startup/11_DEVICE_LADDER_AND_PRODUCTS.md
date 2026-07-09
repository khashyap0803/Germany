# 🔬 DEVICE LADDER & PRODUCTS (v3 — the all-in medical-devices plan)

> **Created**: July 9, 2026 · **Decision**: go all-in on biomedical devices; no Layer-1/Layer-2 software-services detour.
> **Two locked strategy choices (Jul 9, 2026):**
> 1. **Novel Class B first → ladder to Class C/D later** (NOT "directly C/D").
> 2. **Year 1 = zero selling, zero company registration** — pure skill-building + problem discovery.
> ⚠️ Regulatory/cost figures here are approximate (India, 2026) — confirm with a regulatory consultant / CDSCO / a notified body before spending. See `14`.

---

## WHY NOT "DIRECTLY CLASS C/D" — the correction you accepted

Your instinct ("commodity Class A/B is a price war I can't win, so jump to C/D") mixed two different axes:

| Axis | What it means | Where the money/competition really is |
|:---|:---|:---|
| **Risk class** (A→D) | How much a patient is harmed if the device fails | C/D = life-support/implant = clinical trials, ₹1–5 Cr+, notified bodies, 5–8 yrs |
| **Novelty** (commodity ↔ novel) | How new the *problem* you solve is | The competition you fear lives in **commodity A/B**, NOT in **novel B** |

**A first-of-its-kind neuro wearable is Class B/C with almost no Indian competitor.** That is the sweet spot: novel enough to avoid the price war, low-risk enough to actually reach the market as a first-timer.

You **cannot** skip to C/D because:
- Human clinical investigations are legally mandatory for C/D — the single most expensive, slowest gate.
- No grant scales to fund a first-timer's Class-D device; investors won't back a founder with zero device track record.
- Hospitals will not put an unknown vendor's device on a critical-care patient — your father's "trust/liability fortress" at maximum strength (here failure = **death**, not a lost batch).

**The Indian proof this ladder works:** Dozee (contactless vitals), Bempu (newborn hypothermia bracelet), Niramai (breast-cancer thermal screening), EzeRx (non-invasive anemia) — every one started with a **novel, low-risk-class** device, earned a QMS + track record + clinical relationships, *then* climbed. That is the ladder. It is not a compromise of ambition; it is the only route regulators, hospitals and investors accept.

---

## THE LADDER (three rungs)

```
RUNG 0  —  LEARNING PROTOTYPES  (uncertified, built at home / T-Works)
           Purpose: master the craft. Never sold, never on a patient.
                     │
                     ▼
RUNG 1  —  DEVICE #1: a NOVEL CLASS B  (neuro + wearable/diagnostic)
           Purpose: first real product. Grant-funded, certified, sold.
           Earns: QMS (ISO 13485), CDSCO track record, clinical partners, revenue.
                     │
                     ▼
RUNG 2  —  DEVICE #2+: climb to CLASS C/D  (the dream — neuro/critical)
           Now fundable & trustable BECAUSE Rung 1 built the credibility.
```

You do not choose your final destination now. You choose **Rung 0 skills** and a **Rung 1 problem** — and Rung 2 becomes reachable *because* of what Rung 1 earns you.

---

## RUNG 0 — THE LEARNING PROTOTYPES (build these to master the craft)

These are **not products**. They are how you go from "embedded engineer" to "biomedical-device engineer." Build each on a breadboard / dev-board, get the signal clean, log it, plot it, understand it. Uncertified, never touched to a patient beyond yourself for a waveform. Total parts budget for all of them: **≤ ₹30–40k** (see `14` money rules).

| # | Prototype | Key chip / board | What it teaches you | Neuro relevance |
|:--|:---|:---|:---|:---|
| 1 | **ECG front-end** | AD8232 (starter) → ADS1292R (real) | Biopotential acquisition, instrumentation amp, right-leg drive, filtering, noise | The gentlest biosignal — your on-ramp |
| 2 | **PPG / SpO₂** | MAX30102 | Optical biosignals, motion artifact, wearable form-factor | Powers most wrist wearables |
| 3 | **EMG** | ADS1292 / MyoWare | Muscle signals, electrode placement, envelope detection | Direct path to **rehab** devices |
| 4 | **EEG acquisition** ⭐ | **ADS1299** (8-ch, the gold-standard EEG AFE) | Multi-channel low-noise neuro acquisition, shielding, artifact rejection | **The neuro entry point** |
| 5 | **Multimodal wearable** | your MCU + IMU + one of the above, over BLE | Sensor fusion, low-power, BLE streaming, battery mgmt, on-device DSP | **neuro + wearable = your stated dream, in miniature** |

**Order:** 1 → 2 → 3 → 4 → 5. Each reuses the last one's skills. By prototype 5 you can acquire, clean, stream and classify a biosignal on a battery-powered wearable — that is the entire technical core of a Rung-1 product.

> These map 1:1 to your existing firmware track (C → STM32 → RTOS) — that track doesn't change, it just gets a **biosignal payload**. See `12`.

---

## RUNG 1 — DEVICE #1: a NOVEL CLASS B (your first real product)

You do **not** pick this from a wishlist — you pick it from a **validated clinical need** (that's the entire point of Phase 1 discovery, `13`). But so you can aim your learning, here are the **candidate problem-spaces** that fit your interests (neuro, neuro+wearable, wearable+diagnostic) AND your father's criteria. Full scoring is in `13`; the shortlist:

| Candidate | One-line | Why it fits Class-B-novel |
|:---|:---|:---|
| **Parkinson's / movement-disorder tremor quantification wearable** ⭐ front-runner | Objectively measure tremor & slowness to help doctors titrate medication | Neuro + wearable + **decision-support (low failure-cost)** + huge aging market + weak India competition |
| **Diabetic peripheral neuropathy (DPN) screening device** | Catch nerve damage early in diabetics before foot ulcers/amputation | India = diabetes capital; screening = Class B; massive market; father can grasp peripheral nerve |
| **Nocturnal seizure / epilepsy home-monitor** | Alert family to convulsive seizures at night (SUDEP risk) | India = largest epilepsy burden; neuro core; emotionally compelling (carries more liability — handle carefully) |
| **Home sleep-apnea screening wearable** | Screen for OSA at home vs scarce/expensive sleep labs | Big underdiagnosed market; multimodal wearable; screening = Class B |
| **Stroke / neuro hand-rehab biofeedback device** | Home rehab with EMG-biofeedback for stroke survivors | Rehab access poor in India; therapeutic but low-risk; neuro + wearable |

**Why a *measurement/screening/decision-support* device is the ideal Rung 1:** it informs a clinician's decision rather than keeping a patient alive, so a failure is a *missed reading*, not a death. That keeps it **Class B**, keeps certification affordable, and keeps your father's "no/very-less failure" bar achievable. Life-support (Rung 2) waits until you've earned the right to attempt it.

---

## RUNG 2 — LADDER TO CLASS C/D (the dream, structurally reachable)

After Device #1 is certified and selling, you will possess four things you do **not** have today — and each is exactly what a C/D device requires:

| What Device #1 earns you | Why C/D needs it |
|:---|:---|
| **An ISO 13485 QMS already running** | C/D certification demands a mature quality system — you'll already have it, audited |
| **A CDSCO manufacturing track record** | Regulators & hospitals trust a proven manufacturer, not a first-timer |
| **Clinical partners (neurologists, hospitals)** | C/D clinical investigations *require* clinical-site collaborators — you'll already have relationships |
| **Revenue + investor credibility** | C/D needs ₹-crores; you can now raise it because you've shipped before |

**The climb:** Device #2 targets a higher-risk neuro problem (e.g. from a *screening* wearable to an *active therapeutic* or *implantable-adjacent* neuro device). Registered as a **separate entity** (clean liability — its risk can never touch Device #1's company; same rule as v2's hardware-fund logic). Funded by Device #1's revenue + a proper VC round, not family money, **never the house.**

**Neuro end-state (the far horizon):** closed-loop neuromodulation, BCI, implantable neuro monitoring — Class C/D. That is Rung 2/3, 2032+. It is the destination, not the starting line.

---

## THE ONE-PARAGRAPH SUMMARY

Build 5 biosignal learning prototypes to become a biomedical-device engineer (Rung 0). Use clinical discovery to lock ONE novel neuro/wearable **Class B** measurement device as Device #1, get it grant-funded, certified and selling (Rung 1) — this earns you the QMS, track record, clinical partners and capital that make a **Class C/D** neuro device actually attainable (Rung 2). Family money only funds Rung 0. Grants/investors fund Rung 1+. The house is never startup fuel.

➡️ **Next:** `12` (what exactly to learn), `13` (how to pick THE problem), `14` (certify + fund + honest odds).
