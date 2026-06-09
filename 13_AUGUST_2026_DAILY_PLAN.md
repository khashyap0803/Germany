# AUGUST 2026 — PHASE 1 FINISH + PHASE 2 START (STM32)

> **Period**: August 1 (Saturday) → August 31 (Monday)
> **Phase**: Phase 1 final weeks (Weeks 8–11) → Deload → Phase 2 starts Aug 25
> **Month Goal**: Complete C foundation, pass Phase 1 exit tests, set up STM32 + blink first LED
> **AI Status**: Phase 1 (Aug 1–24): BANNED for code | Phase 2 (Aug 25+): BANNED for code (still Phase 1-2 rule)
> **Real Context**: Working at Unistring, gym 5:30–6:30 AM daily
> **Last Updated**: June 8, 2026

---

## AUGUST OVERVIEW

### What happens in August:
- **Week 8 end** (Aug 1–3): State machines + memory layout + packed structs coding (Week 8 started Jul 28)
- **Week 9** (Aug 4–10): Phase 1 Capstone — Embedded System Simulator in C
- **Week 10** (Aug 11–17): Phase 1 deep review — all from-memory challenges
- **Week 11 / Deload** (Aug 18–24): Phase 1 exit tests, deload, FINAL day of Phase 1
- **Phase 2 Week 1** (Aug 25–31): STM32 starts — ARM architecture + CubeIDE setup + first LED blink

### August exit goal:
By August 31 (first week of Phase 2), you should have:
- Passed the Phase 1 exit test: write 5 programs from memory in under 90 minutes total
- Phase 1 capstone project on GitHub (multi-module embedded system simulator)
- STM32CubeIDE installed and first project created
- STM32F411 Black Pill blinking an LED (HAL method)
- Nucleo-L476RG or ST-Link connected and working
- 110+ German words in Anki, Nicos Weg A1 complete

---

## DAILY SCHEDULE TEMPLATE (August — same as June/July)

### Weekday (Mon–Fri)

| Time | Activity |
|:---|:---|
| 5:00–5:25 AM | **PRE-GYM READING** — K.N. King / Mastering STM32 (Phase 2) |
| 5:25–5:30 AM | Gym prep |
| 5:30–6:30 AM | **GYM** |
| 6:30–7:00 AM | Shower, quick breakfast |
| 7:00–8:30 AM | **COMMUTE IN** — German audio |
| 12:30–12:45 PM | **LUNCH ANKI** — German cards |
| 6:30–8:30 PM | **COMMUTE BACK** — German audio |
| 8:30–9:30 PM | Dinner, freshen up |
| 9:30–10:00 PM | **BED READING** |
| 10:00 PM | Sleep |

> All coding on WEEKENDS ONLY through August 24 (Phase 1).
> Phase 2 starts Aug 25: weekday mornings shift to STM32 study (board setup, reading RM0383).
> That change is detailed in 13E_AUGUST_WEEK5.md.

---

## AUGUST READING PLAN

### Phase 1 portion (Aug 1–24): K.N. King + K&R
| Week | Pre-Gym Reading | Bed Reading |
|:---|:---|:---|
| Week 8 end (Aug 1–3) | K.N. King Ch 18 (Declarations) | K&R Ch 6 (Unions, bit-fields) |
| Week 9 (Aug 4–10) | K.N. King Ch 17 (Advanced Pointers) review | K&R Ch 5 revisit |
| Week 10 (Aug 11–17) | Review any K.N. King chapters with low self-ratings | K&R Ch 4–6 review |
| Week 11/Deload (Aug 18–24) | Skim: "Mastering STM32" Ch 1–2 (preview) | K&R Ch 1 (re-read as experienced programmer) |

### Phase 2 portion (Aug 25–31): STM32 begins
| Day | Pre-Gym Reading | Bed Reading |
|:---|:---|:---|
| Aug 25–31 | Mastering STM32 Ch 1–3 (Introduction, Toolchain, Clock) | RM0383 Section 2 (Memory Map) |

---

## WEEKLY FILES

- `13A_AUGUST_WEEK1.md` — Aug 1–3: Week 8 end (state machines + memory layout coding)
- `13B_AUGUST_WEEK2.md` — Aug 4–10: Week 9 (Phase 1 Capstone project)
- `13C_AUGUST_WEEK3.md` — Aug 11–17: Week 10 (Phase 1 deep review + from-memory tests)
- `13D_AUGUST_WEEK4.md` — Aug 18–24: Week 11/Deload (Phase 1 exit tests + last day)
- `13E_AUGUST_WEEK5.md` — Aug 25–31: Phase 2 Week 1 (STM32 setup + first blink)

---

## PHASE 1 EXIT CRITERIA (must pass before calling Phase 1 complete)

All 5 tests, from memory, with only gcc and gdb (no references, no AI):

| Test | Time Limit | Target |
|:---|:---|:---|
| Write circular buffer (cbuf.h + cbuf.c) | 15 min | 0 Valgrind errors |
| Write singly linked list (insert, delete, reverse, free) | 25 min | 0 Valgrind errors |
| Write Makefile for 4-file project | 10 min | Builds cleanly |
| Write state machine with function pointer dispatch (3 states) | 15 min | Correct transitions |
| Debug buggy program using only GDB | 15 min | Find all 3 bugs |

Pass = all 5 done within the time limits.
If any fails: use Aug 18–24 buffer days to re-practice that topic.

---

## PHASE 2 HARDWARE REQUIREMENTS (have ready by Aug 25)

### Hardware setup
- STM32F411CEU6 (WeAct Black Pill) — order if not yet arrived
- Nucleo-L476RG — onboard ST-Link, use to program Black Pill
- Robocraze ST-Link V2 (metal shell) — backup programmer
- Sipeed SLogic — logic analyzer for UART signal verification
- FT232 USB-UART — serial communication to PC
- Breadboard + LEDs + 330Ω resistors + pushbuttons + 10K resistors + jumper wires

### Software setup (do during Deload week Aug 18–24)
- [ ] STM32CubeIDE installed and opened at least once
- [ ] First empty project created for STM32F411CEU6 in CubeIDE
- [ ] ST-Link/V2 drivers installed and recognized by Windows
- [ ] Tera Term or PuTTY installed (for UART serial monitor)
- [ ] RM0383 (STM32F411 Reference Manual) downloaded and bookmarked
- [ ] DS10314 (STM32F411 Datasheet) downloaded

---

## AUGUST GERMAN TARGETS

- Nicos Weg: Lessons 47–50 = A1 complete! (finish remaining lessons from July)
- Nicos Weg A2: Start Lessons 1–5 in the last week of August
- Anki: 110+ words total
- New grammar: simple past tense, dass-clauses ("Ich weiß, dass ich Deutsch lernen muss.")
- Speaking: can hold a 3-minute conversation about daily life in German

---

## DELOAD WEEK (Aug 18–24) — WHAT IS A DELOAD?

A deload week is intentionally lighter:
- Coding: only from-memory practice (no new topics)
- Reading: review only, no new chapters
- German: Anki review only, no new lessons
- Mental goal: consolidate everything, avoid burnout before Phase 2 begins
- Physical: maintain gym routine — this is NOT a rest week for your body

> "Deload" is a term from strength training: reduce volume to let adaptation catch up.
> You have studied 11 weeks straight. One lighter week before Phase 2 makes the next 13 weeks better.
