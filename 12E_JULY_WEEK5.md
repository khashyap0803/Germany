# JULY WEEK 5 (Jul 28–31) — Phase 1 Week 8 START: STATE MACHINES + MEMORY LAYOUT

> **Topics**: State machines with enum + function pointer dispatch, memory layout (text/data/BSS/heap/stack), packed structs, bit fields
> **K.N. King Reading**: Chapter 16 revisit (bit fields) + Chapter 18 (Declarations)
> **K&R Bed Reading**: Chapter 6 revisit (Structures — unions section)
> **YouTube**: Jacob Sorber "State Machines in C" (~10 min)
> **AI Policy**: BANNED for code — AI may only explain concepts
> **Dates**: Tuesday July 28 → Friday July 31, 2026
> **Note**: Only 4 days (Tue–Fri). Week 8 continues in 13A_AUGUST_WEEK1.md.

---

## WEEKDAY READING SCHEDULE (Jul 28–31)

### Tuesday July 28 — Pre-Gym (5:00–5:25 AM)
**Read**: K.N. King Chapter 18 (Declarations — pages 1–20)
- Storage class specifiers: auto, register, static, extern — what each means
- Type qualifiers: const, volatile — review + deepen
- `register` keyword: hint to compiler to use CPU register (mostly ignored by modern compilers)
- Alignment: `_Alignas` (C11) — force a variable to be aligned on N-byte boundary
- Understanding a complex declaration: `int (*fp)(int, int)` = pointer to function taking 2 ints

**Bed Reading (9:30–10:00 PM)**: K&R Chapter 6 pages 165–185 (Unions, Bit-fields)

### Wednesday July 29 — Pre-Gym (5:00–5:25 AM)
**Read**: State machines (search online: "State Machine in C embedded tutorial" — read 1-2 short articles)
Key concepts to understand:
- States: the distinct conditions a system can be in (IDLE, RUNNING, ERROR, SHUTDOWN)
- Events: triggers that cause state transitions (BUTTON_PRESS, TIMER_TICK, ERROR_DETECTED)
- Transitions: rules that say "in state X, on event Y, go to state Z"
- State diagram: circles = states, arrows = transitions (always draw this before coding)
- Implementation patterns:
  - Simple: `switch(current_state)` with nested `switch(event)` — works but gets messy
  - Better: function pointer array — `handlers[current_state](event)` — scales cleanly

**Bed Reading**: K&R Chapter 6 — re-read unions and bit-fields

### Thursday July 30 — Pre-Gym (5:00–5:25 AM)
**Read**: Memory layout (search online: "C program memory layout text data bss heap stack" — any clear article)
- TEXT segment: compiled machine code — read-only, loaded from executable
- RODATA: string literals and const globals — read-only
- DATA segment: initialized global variables — loaded from executable, writable
- BSS segment: uninitialized globals — zero-filled at startup, writable
- HEAP: dynamic allocations (malloc) — grows upward from BSS
- STACK: local variables, function parameters, return addresses — grows downward from top

Draw this diagram on paper — you will be asked to reproduce it from memory.

Key embedded relevance: STM32 has 128KB flash (holds TEXT + RODATA + DATA copy) and 128KB RAM (holds DATA + BSS + HEAP + STACK). If your program is too large — it doesn't fit. No swap. No VM.

**Bed Reading**: K.N. King Chapter 18 pages 20–end

### Friday July 31 — Pre-Gym (5:00–5:25 AM)
**Read**: K.N. King Chapter 16 — bit fields section (re-read)
- Bit field syntax: `uint32_t enable : 1; uint32_t mode : 3;` — fields fit into single uint32_t
- `__attribute__((packed))` vs natural alignment — why packed matters for hardware registers
- Unions for type punning: access same memory as different types
  - `union { uint32_t raw; struct { uint8_t b0, b1, b2, b3; }; }` — access 32-bit word as 4 bytes

**Bed Reading**: K&R Chapter 6 — unions (final read for this month)

---

## SATURDAY AUGUST 1 → Week 8 continues in 13A_AUGUST_WEEK1.md

The first coding session for Week 8 is on **Saturday August 1**.
See `13A_AUGUST_WEEK1.md` for the full Saturday/Sunday plan.

This week (Jul 28–31) is reading-only — all 4 days are weekdays.

---

## JULY END-OF-MONTH REVIEW (Friday July 31, evening)

Update PROGRESS.md now. Be honest about ALL of July.

### July Complete Checklist

| Achievement | Done? |
|:---|:---|
| **Week 4**: Struct + typedef + arrow operator — written from scratch | |
| **Week 4**: SET_BIT / CLEAR_BIT / TOGGLE_BIT / READ_BIT macros from memory | |
| **Week 5**: volatile — can explain why needed for hardware registers | |
| **Week 5**: Preprocessor macros with arguments written correctly | |
| **Week 5**: File I/O — text and binary read/write | |
| **Week 5**: Logger module using static file pointer | |
| **Week 6**: Makefile — can write from memory for 3-file project | |
| **Week 6**: GDB — found at least 2 bugs using only GDB | |
| **Week 7**: Singly linked list — ALL operations, Valgrind clean | |
| **Week 7**: Circular buffer — from memory in under 20 min | |
| **Week 7**: Dynamic array with auto-resize | |
| **GitHub**: 4+ commits in July (one per week) | |
| **Nicos Weg**: Lessons 23–46 done | |
| **Anki**: 100+ German words total | |
| **K.N. King**: Ch 14–18 + Ch 20 read | |
| **K&R**: Ch 4–7 read | |

### July Self-Ratings

| Topic | Rating (1–10) | Need more work? |
|:---|:---|:---|
| Structs + bitwise | | |
| volatile + const + extern | | |
| Makefiles | | |
| GDB debugging | | |
| Dynamic memory / Valgrind | | |
| Linked lists + circular buffer | | |

Any topic below 6: add extra time in August Week 8 before moving to Week 9 (capstone).

---

## BRIDGE TO AUGUST

Week 8 content (state machines, memory layout, packed structs, function pointer dispatch):
- **Saturday Aug 1**: State machine coding — traffic light, vending machine, handler table
- **Sunday Aug 2**: Memory layout visualization, packed structs, bit fields, union type punning

See `13A_AUGUST_WEEK1.md` for full details.

---

## WEEKDAY THEORY FOCUS (Week 8 Start)

| Day | Read Before Gym | Bed Read |
|:---|:---|:---|
| Tue Jul 28 | K.N. King Ch 18 pp. 1–20 | K&R Ch 6 pp. 165–185 |
| Wed Jul 29 | State machine articles (online) | K&R Ch 6 — unions |
| Thu Jul 30 | Memory layout article (online) | K.N. King Ch 18 pp. 20–end |
| Fri Jul 31 | K.N. King Ch 16 — bit fields | K&R Ch 6 — unions final |

> These 4 days are reading only — the coding comes Saturday Aug 1.
> Use this week to build a strong mental model of state machines before coding them.
