# 🔁 RESTART — 8 WEEKS (Oct 5 → Nov 29, 2026)

> **One page. No other plan files are opened, edited or created during these 8 weeks.**
> Goal: **prove you can study consistently.** Not to catch up. Not to finish Phase 1.
> Why this exists: June–Sept 2026 produced zero study and ~10 planning commits. This plan is deliberately small enough that you can't fail it.

---

## THE WEEKLY MINIMUM (~3.5 hrs/week)

| When | What | Time |
|:---|:---|:---|
| **Mon–Fri** | Read the K.N. King chapter for this Saturday. Exhausted? **Read one page.** That counts. | 15 min/day |
| **Saturday** | **C programming** — write programs, compile with `gcc -Wall -Wextra`, push to GitHub | **2 hrs** |
| **Sunday** | **Electronics basics** — one concept, built on a breadboard, measured with your multimeter. Use your sister's *Basic Electrical Engineering* notes/textbook — she's studying the same things this semester. | **1 hr** |
| **Sunday, last 10 min** | Tick this week's row in `PROGRESS.md`. Honest. | 10 min |

**Rules**
1. **Sleep beats study.** Never cut sleep to hit a target.
2. **Missed a Saturday? Don't double up.** Just do next Saturday's session. Missing is fine; quitting isn't.
3. **Missed two in a row?** Cut the Saturday session to 1 hour. Keep going.
4. **No AI-written code.** Asking AI to *explain* a concept or an error message is fine.
5. **No new plans, research or roadmap edits** until the Week 8 review. If an idea comes up, write one line in `PROGRESS.md` and move on.

---

## THE 8 WEEKS

| Wk | Dates | Saturday — C (K.N. King) | Sunday — Electronics | One-off task |
|:--|:---|:---|:---|:---|
| **1** | Oct 5–11 | **Ch 1–3.** Check `gcc --version` works. **Rewrite your 7 week-1 programs properly** (`int main(void)`, `return 0;`, `\n`, zero warnings). Push. | Voltage, current, resistance, **Ohm's law**. Measure a resistor and a battery with the multimeter. | **Ask HR for your bond end date in writing.** |
| **2** | Oct 12–18 | **Ch 4–5** — expressions, if/else, switch. 4–5 programs. | **Series & parallel**, **voltage divider** — build one, measure Vout, check against the formula. | — |
| **3** | Oct 19–25 | **Ch 6** — loops. Patterns, prime check, digit reverse. | **KVL & KCL** — build a 3-resistor circuit, measure, verify both laws. | — |
| **4** | Oct 26–Nov 1 | **Ch 7–8** — basic types, arrays. Max/min/average, bubble sort. | **LED + current-limiting resistor**; **pull-up / pull-down** with a button. | — |
| **5** | Nov 2–8 | 🪔 **Diwali week (Nov 8) — buffer.** Do 1 hour if you can: redo anything from Weeks 1–4 that felt weak. | **Off.** | — |
| **6** | Nov 9–15 | **Ch 9–10** — functions, multi-file programs (`.h` + `.c`). | **Capacitors** — charge/discharge, the **RC time constant**. | — |
| **7** | Nov 16–22 | **Ch 11** — **pointers.** Draw every diagram on paper. `swap()` with pointers. | **RC low-pass filter** (concept + build). *This is the same idea as the noise filter on an ECG.* | — |
| **8** | Nov 23–29 | **Ch 12** — pointers & arrays. Then **from memory**: `swap()`, `my_strlen()`, bubble sort. | **Diode** basics + **transistor as a switch** (drive an LED from a transistor). | **Week 8 review** (below) |

**Hardware you already own** (from your inventory): breadboards, resistor kit, LEDs, capacitors, push-buttons, digital multimeter, jumper wires. Transistors/diodes: buy a ₹100 assortment pack before Week 8 if you don't have one.

---

## WEEK 8 REVIEW — Sunday Nov 29 (30 min max)

**Passed if:**
- [ ] **≥ 6 of 8** weeks ticked in `PROGRESS.md` (Week 5 counts if you did anything)
- [ ] **20+ C programs** on GitHub, all compiling with zero warnings
- [ ] Can write **`swap()` with pointers** from memory and explain it on paper
- [ ] Can explain **Ohm's law, KVL, KCL, voltage divider and RC time constant** out loud — and you've built each one
- [ ] **Bond end date confirmed** in writing

**Then (and only then):** write the *next* 8 weeks on one page — Dec 2026 → Jan 2027: K.N. King Ch 13–17 (strings, preprocessor, structs, bitwise), op-amps, and the **first STM32 blink**. That's the start of Darmstadt's requirement #2 ("experience in 32-bit microcontrollers").

**If you didn't pass:** that's information, not failure. Look at *why* (time? energy? motivation?), shrink the minimum again, and run another 8 weeks. Don't add more.

---

## WHY THIS IS ENOUGH

Darmstadt's coordinator told you what they want for embedded: **excellent C/C++ · 32-bit microcontrollers · systems engineering · hardware design.** These 8 weeks start the first and the last. **3.5 hrs × 8 weeks ≈ 28 hours** — more than you did in the last 4 months combined, and it builds the habit everything else depends on.
