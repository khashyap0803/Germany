# AUGUST WEEK 4 (Aug 18–24) — Phase 1 Week 11 + DELOAD: EXIT TESTS + PHASE 1 COMPLETE

> **Topics**: Phase 1 exit tests, deload (lighter week), STM32CubeIDE setup, Mastering STM32 Ch 1–2 preview
> **K.N. King Reading**: Light review only — any weak chapters
> **K&R Bed Reading**: Chapter 1 (Tutorial Introduction) — re-read as experienced programmer
> **AI Policy**: BANNED for C code. OK to use AI to explain STM32 concepts (preview only).
> **Dates**: Tuesday August 18 → Monday August 24, 2026 — LAST WEEK OF PHASE 1

---

## WHAT IS A DELOAD WEEK?

A deload week is intentionally lighter on new content:
- NO new topics. Only review and consolidation.
- Coding sessions shorter than usual.
- Reading: lighter pace, re-reading favorites.
- German: Anki review only, no new grammar.
- Physical: keep gym routine. Body continues adapting.

Purpose: after 11 weeks of intensive C, let the knowledge settle before Phase 2's intensive hardware work begins.

---

## WEEKDAY SCHEDULE (Aug 18–22 — Deload)

### Tuesday August 18 — Pre-Gym (5:00–5:25 AM)
**Review**: K.N. King — pick your LOWEST self-rated week topic and re-read its chapter.
If GDB was weak: re-read the GDB cheat sheet and mentally practice the commands.
If pointers were weak: re-read K.N. King Ch 11, pages 1–20.

**Bed Reading**: K&R Chapter 1 — A Tutorial Introduction. Read it like a story about a language you now know.

### Wednesday August 19 — Pre-Gym (5:00–5:25 AM)
**Preview**: Skim "Mastering STM32" by Carmine Noviello — Chapter 1 (Introduction to STM32 Ecosystem)
- What is ARM Cortex-M4? What is HAL? What is CMSIS? What is CubeMX?
- Don't study details — just orient yourself.

**Bed Reading**: K&R Chapter 1 — pages 10–30 (re-read with fresh eyes)

### Thursday August 20 — Pre-Gym (5:00–5:25 AM)
**Read**: Mastering STM32 Chapter 2 (Setting up the Toolchain) — first 15 pages
- What STM32CubeIDE is and how it differs from regular gcc
- The build pipeline for embedded: compile → link → flash
- What ST-Link is, what SWD means (Serial Wire Debug)

**Bed Reading**: K&R Chapter 1 — pages 30–52

### Friday August 21 — Pre-Gym (5:00–5:25 AM)
**Read**: Mastering STM32 Chapter 3 (Hello World — Blink LED)
- Read through the HAL blink example — don't code it yet
- Understand: `HAL_GPIO_WritePin()`, `HAL_Delay()`, `SystemClock_Config()` — what role each plays

**Bed Reading**: K&R Chapter 2 (Types, Operators, Expressions) — re-read as experienced programmer

### Monday August 24 — Pre-Gym (5:00–5:25 AM)
**This is the last pre-gym reading of Phase 1.**
Re-read your Phase 1 PROGRESS.md checklist. Mark every item you've completed.
If anything is missing: make a note for Phase 2's first week to finish it.

**Bed Reading**: Last night of Phase 1. Read K.N. King Chapter 1 again — "Introducing C."
You are a different person than when you first read it.

---

## SATURDAY AUGUST 22 — PHASE 1 EXIT TEST (7:30 AM–12:30 PM)

### IMPORTANT: This is the real test. Same rules as the dry run.
- Clean terminal, no references, no AI, no browser
- Just you, gcc, gdb, valgrind
- Time each test with a phone timer

### TEST 1 — Circular Buffer (15 min)
From a blank file: write `cbuf.h` + `cbuf.c`

Requirements:
- `cbuf_init`, `cbuf_write`, `cbuf_read`, `cbuf_is_full`, `cbuf_is_empty`, `cbuf_count`
- CBUF_SIZE = 8
- Test: write 6, read 3, write 5 (tests wraparound), read all remaining

**Grade yourself**: Pass = compiles cleanly, correct FIFO behavior, Valgrind 0 leaks, ≤ 15 min

### TEST 2 — Singly Linked List (25 min)
From a blank file: write `list.h` + `list.c`

Requirements:
- `create_node`, `insert_front`, `insert_back`, `delete_node`, `print_list`, `reverse_list`, `free_list`
- Test: insert 5 nodes, delete middle, reverse, verify, free

**Grade yourself**: Pass = all ops correct, Valgrind 0 leaks, ≤ 25 min

### TEST 3 — Makefile (10 min)
From scratch: write a Makefile for a project with `main.c`, `math.c`, `io.c`:

Requirements:
- CC, CFLAGS, TARGET, SRCS, OBJS defined
- Pattern rule `%.o: %.c` with automatic variables
- `all`, `clean`, `.PHONY` targets
- `make clean && make` — builds without warnings

**Grade yourself**: Pass = correct Makefile, ≤ 10 min

### TEST 4 — State Machine with Function Pointer Dispatch (15 min)
From scratch: write a 3-state state machine in one file

Requirements:
- States: IDLE, RUNNING, ERROR (use typedef enum)
- Events: START, STOP, FAULT, RESET
- State handlers return next state
- Dispatch table: `StateHandler handlers[STATE_COUNT]`
- Main: run sequence of events through the dispatch loop

**Grade yourself**: Pass = correct transitions, compiles cleanly, ≤ 15 min

### TEST 5 — GDB Bug Hunt (15 min)
Find all 3 bugs in this program using ONLY GDB (no printf debugging):
```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Bug 1: returns pointer to local stack variable
char *get_greeting(const char *name) {
    char buf[50];
    snprintf(buf, 50, "Hello, %s!", name);
    return buf;
}

// Bug 2: off-by-one in loop
int sum_array(int *arr, int n) {
    int sum = 0;
    for (int i = 0; i <= n; i++) {
        sum += arr[i];
    }
    return sum;
}

int main(void) {
    printf("%s\n", get_greeting("Khashyap"));

    int nums[5] = {10, 20, 30, 40, 50};
    printf("Sum: %d\n", sum_array(nums, 5));

    // Bug 3: double free
    int *p = malloc(sizeof(int) * 3);
    p[0] = 1; p[1] = 2; p[2] = 3;
    free(p);
    free(p);

    return 0;
}
```

**Grade yourself**: Pass = all 3 bugs identified with GDB commands, fixes written in comments, ≤ 15 min

---

### SCORING — 7:30 AM → ~9:40 AM total (all 5 tests = 80 min)

| Test | Result | Time |
|:---|:---|:---|
| Circular buffer | PASS / FAIL | ___ min |
| Linked list | PASS / FAIL | ___ min |
| Makefile | PASS / FAIL | ___ min |
| State machine | PASS / FAIL | ___ min |
| GDB bug hunt | PASS / FAIL | ___ min |

**5/5 PASS**: Phase 1 is complete. You are ready for Phase 2. Write a note in PROGRESS.md.
**4/5 PASS**: Phase 1 is functionally complete. Fix the 1 failure on Monday morning.
**3/5 or below**: Use Aug 25 morning to re-attempt the failures before starting Phase 2 hardware work.

### REST BLOCK (9:45–11:00 AM)
You just completed an 11-week C programming course entirely by yourself, without AI writing code for you. Take 75 minutes to do nothing related to study.

### GITHUB — PHASE 1 COMPLETE COMMIT (11:00–11:30 AM)
```bash
cd ~/C-Practice
git add .
git commit -m "Phase 1 COMPLETE: 11 weeks of C — exit tests passed. Phase 2 begins Aug 25."
git push origin main
```

### ⭐ FUNDAMENTALS BRIDGE 1 — PRACTICAL ELECTRONICS (interleaved this weekend + next)
> Full module: see `15_FUNDAMENTALS_BRIDGE.md`. This is the one ECE bridge you need BEFORE touching the STM32.
> Goal: understand voltage/current/pins so you don't fry your Black Pill in Phase 2.

**This deload weekend, do the THEORY half (~3 hrs across Sat/Sun):**
- Watch Paul McWhorter Electronics videos 1–5 (Ohm's law, LEDs, resistors, breadboard)
- Read SparkFun guides: "Voltage Current Resistance", "LEDs", "Pull-up Resistors", "Logic Levels"
- Learn the 3 formulas that matter: V=IR, LED resistor R=(Vsupply−Vled)/Iled, voltage divider Vout=Vin×R2/(R1+R2)
- Find PA5 and PC13 max current ratings in the STM32F411 datasheet (DS10314)

**The HANDS-ON half happens on the first Phase 2 weekend (Aug 29-30)** — woven into the LED blink session in `13E_AUGUST_WEEK5.md`:
- Light an external LED with a calculated resistor (not just the onboard LED)
- Build + measure a voltage divider with your multimeter
- Wire a button with a pull-up, measure pin voltage pressed vs released

### STM32 SETUP — Part 1 (11:30 AM–12:30 PM)
Install STM32CubeIDE if not yet done:
- Download from st.com/stm32cubeide
- Install and open — verify it launches
- Create an empty project for STM32F411CEU6
- Don't write any code yet — just see the file structure CubeIDE generates
- Connect your ST-Link/V2 via USB — verify Windows recognizes it (check Device Manager)

### LUNCH (12:30–1:30 PM)

### GERMAN BLOCK (1:30–4:30 PM)
- Nicos Weg A2 Lessons 9–10
- Full Anki review — clear all pending cards
- Write: "Ich habe die Phase 1 meines Lernpfads abgeschlossen. Nächste Woche beginne ich mit STM32."
  (I have completed Phase 1 of my learning path. Next week I start with STM32.)
- ChatGPT Voice: 30 min A2-level conversation

---

## SUNDAY AUGUST 23 — STM32 SETUP + DELOAD (7:30 AM–2:00 PM)

### BLOCK 1 (7:30–9:00 AM): Mastering STM32 Ch 1–3 Deep Read
Read these 3 chapters carefully — not skimming, not coding, just reading:
- Chapter 1: Introduction to STM32 family — what STM32F4 is, what Cortex-M4 means
- Chapter 2: Setting up the toolchain — CubeIDE overview, project structure
- Chapter 3: Hello World — blink LED via HAL. Read every line of the generated code. Ask: what does each line do?

Draw on paper: the connection between PC (ST-Link) → SWD pins → STM32 chip → GPIO → LED

### BLOCK 2 (9:15–10:15 AM): Wire Up Hardware
If you have your Black Pill and Nucleo:
- Wire the Nucleo ST-Link to Black Pill SWD pins (see 12_JULY_2026_DAILY_PLAN.md hardware section)
- Power the Black Pill via USB
- In CubeIDE: try to detect the board (Debug → Connect → should show STM32F411)
- Do NOT flash yet — just verify the connection works

If hardware not yet arrived: skip this block and add extra German time.

### GIT (10:15–10:30 AM)
```bash
git commit -m "Deload week: STM32CubeIDE setup, Mastering STM32 Ch 1-3 read, hardware wired"
git push
```

### REST + LUNCH (10:30 AM–12:00 PM)

### GERMAN (12:00–2:00 PM)
- Full Anki mega review — clear everything
- Write 3 paragraphs in German: past, present, future (was ich gemacht habe, was ich mache, was ich machen will)
- This is the last Sunday before Phase 2 — celebrate with good German practice

---

## MONDAY AUGUST 24 — LAST DAY OF PHASE 1

### Pre-Gym (5:00–5:25 AM)
Re-read PROGRESS.md. Mark every Phase 1 exit criterion as done or not done. Be honest.

### Evening (9:30–10:00 PM — Bed Reading)
Read K&R Chapter 1 one final time.
You started your journey reading this chapter as a beginner.
You end Phase 1 reading it as someone who has written 60+ programs, debugged with GDB, and built a multi-module project. See how much more you understand.

Tomorrow is Phase 2. The microcontrollers are waiting.

---

## PHASE 1 EXIT CRITERIA — FINAL CHECKLIST

Update PROGRESS.md with honest YES/NO for each:

| Phase 1 Criterion | Status |
|:---|:---|
| Write bubble_sort from memory | |
| Write my_strlen (pointer version) from memory | |
| Write swap(int *a, int *b) from memory | |
| Write binary_search from memory | |
| Explain pointers on paper with memory diagram | |
| Use malloc/free in 3+ programs, all Valgrind clean | |
| Write a function that accepts a function pointer as argument | |
| Understand multi-file compilation (.h + .c separation) | |
| Can write a Makefile for a 4-file project from memory | |
| Can find a bug with GDB without printf debugging | |
| Can implement circular buffer from memory in under 15 min | |
| Can implement singly linked list from memory in under 25 min | |
| C-Practice GitHub: 8+ commits (one per week) | |
| Nicos Weg A1 complete (Lessons 1–50) | |
| Nicos Weg A2: Lessons 1–10 started | |
| Anki: 120+ German words | |

If ALL criteria are met → Phase 1 is complete. You are ready.
If any criterion is not met → fix it during Aug 25 Phase 2 Week 1 before starting hardware work.

> Phase 2 starts tomorrow (August 25). The code you wrote in Phase 1 is your foundation.
> STM32 is just C — the same C you've been writing for 11 weeks.
> The only difference: the memory you write to controls real hardware.

---

## WEEKDAY THEORY FOCUS (Deload Week 11)

| Day | Read Before Gym | Bed Read |
|:---|:---|:---|
| Tue Aug 18 | K.N. King — lowest self-rated chapter | K&R Ch 1 pp. 1–30 |
| Wed Aug 19 | Mastering STM32 Ch 1 (skim) | K&R Ch 1 pp. 30–52 |
| Thu Aug 20 | Mastering STM32 Ch 2 (toolchain) | K&R Ch 2 |
| Fri Aug 21 | Mastering STM32 Ch 3 (blink LED — just read) | K&R Ch 2 |
| Mon Aug 24 | PROGRESS.md review — Phase 1 final check | K&R Ch 1 — final read |
