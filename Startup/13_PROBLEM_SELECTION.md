# 🎯 PROBLEM SELECTION (v3 — how to pick THE device, and the best candidates)

> Your honest starting point (your words, Jul 9 2026): *"I don't have any specific device in mind — it's ambition."* That is **normal and fine.** Devices don't start from a device idea; they start from a **validated clinical need.** This file turns "I want to build neuro wearables" into "I am building *this specific thing* because *this specific person* needs it."
> **The rule:** you do NOT lock the device now. You lock it at the end of Phase-1 discovery (~2027), using the scorecard below. Everything before that is learning + looking.

---

## YOUR FATHER'S CRITERIA → A SCORECARD

Your father set the bar (Jul 9): **high quality · no/very-less failure · really helpful · less competition · heavy market value · and YOU manage marketing + certification (he helps technically only, not deep biology).** Turned into a scoring tool — rate every candidate 1–5 on each:

| # | Criterion (from father) | What a 5 looks like | What a 1 looks like |
|:--|:---|:---|:---|
| **C1** | **Low failure-cost** ("no/very-less failure") | A wrong reading = re-test (screening/decision-support) | A failure = patient death (life-support) |
| **C2** | **Really helpful** | Solves a pain a clinician names unprompted | "Nice to have," nobody's asking |
| **C3** | **Less competition** | No Indian product does this well; novel | Commodity, 20 companies, price war |
| **C4** | **Heavy market value** | Large patient population + someone willing to pay | Tiny niche or nobody pays |
| **C5** | **Certifiable by YOU as a first-timer** | Class B, no human clinical trial to *launch* | Class C/D, mandatory trials, ₹-crores |
| **C6** | **Father can advise technically** | Electronics/measurement/quality he can judge | Exotic biology only a specialist understands |
| **C7** | **Fits your pull** (neuro / wearable / diagnostic) | Neuro + wearable core | Unrelated to your interest → you'll quit |

> **C1 and C5 are the gatekeepers.** They're why Device #1 must be a **measurement / screening / decision-support** device, not therapy or life-support. That single constraint satisfies half your father's list automatically.

---

## HOW TO ACTUALLY PICK IT — the discovery method (Phase 1, ~2027)

This is your **hardest gap**: you have no clinical network, and your father can't open clinical doors (pharma ≠ clinics). Here's how a person with zero network still finds a real problem in Hyderabad:

**1. Immersion — get near patients & clinicians (pick 2–3, cheap/free):**
- **Neurology/rehab OPD observation:** politely ask a mid-size hospital (NIMS Hyderabad is a govt neuro powerhouse; also Yashoda, KIMS, Care) if you can *observe* an OPD as an engineering student researching medical devices. Many say yes to a respectful, specific request. One morning a week for a month teaches more than a year of reading.
- **Physiotherapy / rehab centres** (you already scouted GuruNanak Physio, `10`) — repurpose those relationships from "sell a website" to "watch what breaks in rehab."
- **Patient support groups:** Parkinson's, epilepsy, diabetes associations in Hyderabad — patients tell you their daily pain directly and unfiltered.

**2. Literature — size it & check who's already there:**
- PubMed + Google Scholar: "how big is this problem in India?" and "what devices exist?"
- If a big company already owns it well → drop it (fails C3). If papers say "no good solution exists" → flag it.

**3. The 20-clinician question:** ask neurologists/physios/diabetologists one question — *"What do you wish you could measure or monitor in your patients but currently can't, cheaply?"* When **≥3 independent clinicians name the same gap**, that's your signal (same logic as v2's "pain log," now clinical).

**4. Score every candidate on the C1–C7 scorecard. Highest total that you'd happily spend 3 years on = Device #1.**

> **Discovery is not optional and not fast.** Budget ~6–9 months of Phase 1 for it. Building the wrong device perfectly is the #1 way medtech startups die. Your father's "really helpful + heavy market value" criteria literally *cannot* be judged from your bedroom — they're judged in an OPD.

---

## THE BEST CANDIDATE PROBLEMS (scored — these are HYPOTHESES to validate, not decisions)

Scored 1–5 on C1–C7 from current desk knowledge. **Field discovery can overturn any of these** — that's the point of Phase 1. Ranked by total.

> ⚠️ **Read `15` alongside this.** Real-time patent/product research (Jul 9 2026) found the Parkinson's-tremor space is **more crowded** than the scores below assumed — 5 NICE-endorsed international monitors, real patents, AND an Indian player (**Lifespark Technologies**, ISO 13485, Shark Tank). The competition (C3) scores below are the *original* desk estimates; `15` corrects them and proposes a **new front-runner (Essential Tremor / ET-vs-PD differentiation)** that reuses identical tech in a bigger, less-contested market.

### ⭐ #1 — Essential Tremor / ET-vs-PD differentiation + severity wearable  (NEW front-runner, post-`15` research)
*A wrist/hand wearable that objectively distinguishes essential tremor from Parkinson's tremor and tracks severity — attacking the 20–30% ET/PD misdiagnosis problem that the PD-focused incumbents don't solve.*

| C1 | C2 | C3 | C4 | C5 | C6 | C7 | **Total** |
|:--|:--|:--|:--|:--|:--|:--|:--|
| 5 | 5 | 4 | 5 | 5 | 4 | 5 | **33/35** |

- **Why it now leads:** identical hardware to the PD monitor (IMU + EMG + DSP) but aimed at a **bigger, less-contested** problem — ET is ~8× commoner than PD and heavily under-diagnosed, and the *differentiation* angle is a named clinical pain the crowded PD-monitoring players ignore. Decision-support → low failure-cost (C1) → Class B (C5). See `15` §6 Option A.
- **Rung-2 ladder:** same as PD — movement measurement → closed-loop neuromodulation = the Class C/D neuro dream.

### #2 — Parkinson's tremor & bradykinesia quantification wearable  (was #1 — downgraded after `15`)
*Objectively measure tremor, slowness and dyskinesia so neurologists can titrate medication and monitor remotely — instead of the subjective, once-in-6-months UPDRS exam.*

| C1 | C2 | C3 | C4 | C5 | C6 | C7 | **Total** |
|:--|:--|:--|:--|:--|:--|:--|:--|
| 5 | 5 | ~~4~~ **2** | 4 | 5 | 4 | 5 | **30/35** |

- **Why downgraded:** the tech and market are still excellent, but C3 (less competition) drops from 4→**2** — file `15` found 5 NICE-endorsed international monitors, real patents, AND an Indian player (Lifespark). Still viable, but only with a **sharp cost/niche edge**, not head-on. Everything else about it (neuro+wearable, decision-support, C/D ladder) stays strong.

### #3 — Diabetic Peripheral Neuropathy (DPN) early-screening device
*Quantitatively detect nerve damage in diabetics' feet early, before ulcers/amputations — replacing the subjective monofilament test.*

| C1 | C2 | C3 | C4 | C5 | C6 | C7 | **Total** |
|:--|:--|:--|:--|:--|:--|:--|:--|
| 5 | 5 | 4 | 5 | 5 | 4 | 3 | **31/35** |

- **Why it's strong:** India is the **diabetes capital** (~100M+ diabetics; ~half develop neuropathy), amputations are preventable with early detection, current screening is manual/subjective, screening = Class B, huge market. Slightly lower C7 (peripheral nerve, less "neuro-glamorous" than brain — but it IS neuro, and the market may be the biggest on this list).

### #4 — Home sleep-apnea (OSA) screening wearable
*Screen for obstructive sleep apnea at home (SpO₂ + effort + optional single-channel EEG) vs scarce, expensive sleep-lab polysomnography.*

| C1 | C2 | C3 | C4 | C5 | C6 | C7 | **Total** |
|:--|:--|:--|:--|:--|:--|:--|:--|
| 5 | 4 | 3 | 5 | 4 | 4 | 4 | **29/35** |

- **Why:** massively underdiagnosed in India, multimodal wearable (great skills fit), big market. **But** more global competition (C3 lower) and CPAP giants adjacent.

### #5 — Nocturnal seizure / epilepsy home-monitor
*Detect convulsive seizures at night and alert family (SUDEP risk reduction) via accelerometry/EMG.*

| C1 | C2 | C3 | C4 | C5 | C6 | C7 | **Total** |
|:--|:--|:--|:--|:--|:--|:--|:--|
| 3 | 5 | 4 | 4 | 4 | 4 | 5 | **29/35** |

- **Why it's compelling:** India has the **world's largest epilepsy burden** (~12M), no affordable home monitor, deeply **neuro**, emotionally powerful. **The catch (lower C1):** a *missed* seizure has a high perceived failure-cost, so it carries more liability and must be framed carefully as "an aid, not a guarantee." Great cause; handle the risk-class framing with extra care.

### #6 — Stroke / neuro hand-rehab biofeedback device
*Home rehab using EMG-biofeedback (or gentle FES) for stroke survivors, where rehab access is poor.*

| C1 | C2 | C3 | C4 | C5 | C6 | C7 | **Total** |
|:--|:--|:--|:--|:--|:--|:--|:--|
| 4 | 5 | 4 | 4 | 3 | 4 | 4 | **28/35** |

- **Why:** rehab access is genuinely poor in India, big stroke burden, neuro + wearable. **But** it edges toward *therapeutic* (FES) which raises the regulatory class/failure-cost (C5 lower) vs a pure measurement device. EMG-biofeedback-only version scores higher than FES.

---

## THE RECOMMENDATION (how to hold this — UPDATED after `15` research)

- **Aim your learning at the movement-disorder tremor wearable family** — this maximizes your father's criteria AND your neuro+wearable pull, and has the cleanest ladder to the Class-C/D neuro dream. Point Rung-0 prototype #5 (multimodal IMU+EMG wearable, `11`) at *movement signals* — you build toward it while you learn.
- **BUT the specific target shifts from "PD monitor" to "Essential-Tremor / ET-vs-PD differentiation + severity" (see `15`).** Reason: PD tremor monitoring is already crowded (5 international devices + Lifespark in India), whereas ET is ~8× more common, heavily under-diagnosed, and 20–30% of ET/PD cases are *misdiagnosed as each other* — a real, named, under-served clinical problem using the **same hardware.**
- **And still do NOT tattoo it on.** These are desk + web estimates. If Phase-1 discovery shows neurologists are desperate for something else, **the scorecard re-decides.** Validated need beats a pretty score.
- **The reassurance from `15`:** Lifespark proves an Indian team *can* reach ISO 13485 + a certified neuro wearable + revenue via the exact SINE/IIT-B incubator path we planned. The category is **proven and fundable** — your job is to out-execute on cost + a sharper niche, not to invent from scratch (the algorithms are open-source anyway).
- **Two convictions to keep:** (1) Device #1 must be **measurement/screening/decision-support** (protects C1+C5); (2) it must be something **you'd happily spend 3 years on** (C7) — because you will.

---

## PHASE-1 EXIT GATE (you may leave discovery only when ALL are true)

- [ ] ≥3 independent clinicians named the same unmet need
- [ ] Literature confirms it's real AND under-served in India (passes C3)
- [ ] It scores ≥28/35 on C1–C7, with **C1 and C5 both ≥4**
- [ ] You've built a **breadboard proof-of-concept** that captures the core signal for it
- [ ] You'd genuinely enjoy 3 years on it

Only then do you incorporate, apply for grants, and start the certified build (`14`).

➡️ **Next:** `14` — certification, funding ladder (PRAYAS→BIG), incubators, and the honest gate-by-gate odds.
