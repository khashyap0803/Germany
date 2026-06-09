# JUNE 2026 — PHASE 1 START (Real Day 1: June 9)

> **Period**: June 9 (Tuesday) → June 30 (Tuesday)
> **Phase**: Phase 1 — C Programming Foundation (Weeks 1–4 of 11)
> **Goal**: C basics through pointers — understand deeply, write from memory
> **AI Status**: BANNED for code — AI only explains concepts, YOU write ALL code
> **Real Start**: June 9, 2026 (first actual day of the roadmap)
> **Last Updated**: June 8, 2026

---

## JUNE OVERVIEW

### What happens in June:
- **Week 1** (Jun 9–15): Environment setup + C basics (variables, loops, functions, arrays)
- **Week 2** (Jun 16–22): Functions deep + arrays + strings + sorting + multi-file
- **Week 3** (Jun 23–29): POINTERS — the most critical week of Phase 1
- **Week 4** (Jun 30): Structs + Bitwise begins (1 day only — continues in July Week 1)

### June exit goal:
By June 30, you should be able to:
- Write any basic-to-intermediate C program from scratch without AI
- Explain what a pointer is on paper with a full memory diagram
- Use malloc/free correctly (Valgrind clean)
- Write swap(), circular_buffer.c, my_strlen() from memory in under 20 min
- 60+ German words in Anki, Nicos Weg Lessons 1–20 done

---

## DAILY SCHEDULE TEMPLATE

### Weekday (Mon–Fri)

| Time | Activity |
|:---|:---|
| 5:00–5:25 AM | **PRE-GYM READING** — K.N. King on tablet (no coding needed, just read) |
| 5:25–5:30 AM | Gym prep |
| 5:30–6:30 AM | **GYM** |
| 6:30–7:00 AM | Shower, quick breakfast |
| 7:00–8:30 AM | **COMMUTE IN** — Nicos Weg German audio |
| 12:30–12:45 PM | **LUNCH ANKI** — German flashcards |
| 6:30–8:30 PM | **COMMUTE BACK** — Easy German podcast |
| 8:30–9:30 PM | Dinner, freshen up |
| 9:30–10:00 PM | **BED READING** — K&R or FastBit theory review |
| 10:00 PM | Sleep |

> All coding, debugging, and program-writing happens on WEEKENDS ONLY.
> Weekdays = theory reading + German immersion. Accept this — it is realistic and sustainable.

### Saturday (9.5 hours — PRIMARY CODING DAY)

| Time | Activity |
|:---|:---|
| 5:30–6:30 AM | Gym |
| 6:30–7:30 AM | Shower + breakfast |
| **7:30–12:30 PM** | **5 HOURS — C PROGRAMMING DEEP CODING** |
| 12:30–1:30 PM | Lunch + rest |
| **1:30–4:30 PM** | **3 HOURS — GERMAN (grammar + writing)** |
| 4:30–5:00 PM | Break |
| **5:00–6:30 PM** | **1.5 HOURS — GERMAN SPEAKING (ChatGPT Voice or italki)** |

### Sunday (7 hours)

| Time | Activity |
|:---|:---|
| 5:30–6:30 AM | Gym |
| 6:30–7:30 AM | Shower + breakfast |
| **7:30–10:30 AM** | **3 HOURS — C PROJECTS + MINI-REVIEW + GIT** |
| 10:30 AM–12:00 PM | Rest + lunch |
| **12:00–2:00 PM** | **2 HOURS — GERMAN REVIEW + ANKI BULK** |
| **2:00–4:00 PM** | **2 HOURS — EXTENDED C CODING** |
| 4:00 PM onwards | Rest |

---

## TOOLS & SETUP

### Development environment
- WSL2 (Ubuntu 22.04) on Windows — gcc, gdb, valgrind, make
- Compile standard: `gcc -Wall -Wextra -g -std=c99 program.c -o program`
- Rule: ZERO warnings allowed in all programs
- Debugging: GDB only (not printf-debugging)
- Memory check: Valgrind for every program that uses malloc/calloc/realloc

### Books + videos
- **K.N. King** "C Programming: A Modern Approach" 2nd ed — primary reading (pre-gym + bed)
- **K&R** "The C Programming Language" 2nd ed — bed reading alternate nights
- **FastBit Embedded C** at 1.5× — watch in Saturday warmup (before deep coding)
- **Neso Academy** YouTube — quick concept shots (7–12 min each)
- **mycodeschool** YouTube — Pointers playlist (15 videos, Week 3)
- **Jacob Sorber** YouTube — function pointers, volatile, multi-file, GDB

### AI Policy (STRICT — Phase 1)
- AI MAY: explain concepts, answer theory questions, explain error messages
- AI MAY NOT: write any code, show example programs, complete your partial code
- If tempted to ask AI to write code: write it wrong first, then debug it yourself

---

## GERMAN LANGUAGE (June)

### Daily routine
- Commute in: DW Nicos Weg app — 1–2 lessons per commute (download offline)
- Lunch: Anki — 5 new cards + review all pending
- Commute back: Easy German podcast (passive listening)
- Saturday afternoon: Grammar study + write 10 sentences from memory
- Saturday evening: ChatGPT Voice practice (A1 level conversations)

### June German targets
- Nicos Weg: Lessons 1–20 complete by end of June
- Anki deck: 60+ words reviewed with spaced repetition
- Self-introduction in German: "Ich heiße ___. Ich komme aus Indien. Ich arbeite als Ingenieur. Ich lerne Deutsch."
- Numbers 1–20, days of week, basic greetings

---

## WEEKLY FILES

- `11A_JUNE_WEEK1.md` — Jun 9–15: Setup + C Basics (Phase 1 Week 1)
- `11B_JUNE_WEEK2.md` — Jun 16–22: Functions + Arrays + Strings (Phase 1 Week 2)
- `11C_JUNE_WEEK3.md` — Jun 23–29: POINTERS — most important week (Phase 1 Week 3)
- `11D_JUNE_WEEK4.md` — Jun 30: Structs begins (Day 1 only — full Week 4 in July)

---

## JUNE EXIT CRITERIA (before moving to July Week 4)

- [ ] Write from MEMORY (no references): bubble_sort, my_strlen, swap (pointer version), binary_search
- [ ] Explain pointers on paper with memory diagram (draw addresses, pointer arrows)
- [ ] Use malloc/free in 3+ programs, all Valgrind clean
- [ ] Write a function that accepts a function pointer as argument
- [ ] Understand multi-file compilation (.h + .c separation)
- [ ] GitHub C-Practice: 15+ commits
- [ ] Nicos Weg: lessons 1–20 done
- [ ] Anki: 60+ German words

If any criterion is not met by June 30 → use the first week of July to finish before moving to structs.
