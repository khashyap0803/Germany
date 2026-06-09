# AUGUST WEEK 3 (Aug 11–17) — Phase 1 Week 10: DEEP REVIEW + FROM-MEMORY CHALLENGES

> **Topics**: No new topics — this week is 100% review and from-memory practice for every skill learned in Weeks 1–9
> **K.N. King Reading**: Review any chapters with self-ratings below 7
> **K&R Bed Reading**: Chapter 2 (Types) + Chapter 3 (Control Flow) — re-read as an experienced programmer
> **AI Policy**: BANNED — no AI assistance for any code this week
> **Dates**: Tuesday August 11 → Monday August 17, 2026

---

## WEEKDAY REVIEW SCHEDULE (Aug 11–15)

### Tuesday August 11 — Pre-Gym (5:00–5:25 AM)
**Review target**: Pointers + Dynamic Memory
- Re-read K.N. King Ch 11 (Pointers) — specifically pointer arithmetic and the double pointer pattern
- Ask yourself: can you explain `int **pp` and why `insert_front` needs `Node **head`?

**Bed Reading**: K&R Chapter 5 — re-read pointer arithmetic section (pp. 95–105)

### Wednesday August 12 — Pre-Gym (5:00–5:25 AM)
**Review target**: Strings + Multi-file + Makefiles
- Re-read K.N. King Ch 13 (Strings) pages 1–20 and Ch 15 (Program Organization)
- Ask yourself: can you write `my_strlen` using pointer traversal from memory?

**Bed Reading**: K&R Chapter 4 — re-read header files and separate compilation

### Thursday August 13 — Pre-Gym (5:00–5:25 AM)
**Review target**: Structs + Bitwise + State Machines
- Re-read K.N. King Ch 16 (Structures) — focus on self-referential structs and bit fields
- Ask yourself: can you write SET_BIT, CLEAR_BIT, TOGGLE_BIT, READ_BIT from memory in 2 minutes?

**Bed Reading**: K&R Chapter 2 (Types, Operators, Expressions)

### Friday August 14 — Pre-Gym (5:00–5:25 AM)
**Review target**: Data Structures + Valgrind
- Re-read K.N. King Ch 17 (Advanced Pointers — linked lists) pages 1–30
- Ask yourself: can you implement circular buffer cbuf.h + cbuf.c in under 15 minutes?

**Bed Reading**: K&R Chapter 3 (Control Flow)

### Monday August 17 — Pre-Gym (5:00–5:25 AM)
**Review target**: File I/O + volatile + GDB
- Re-read K.N. King Ch 22 (I/O) pages 1–20 and K.N. King Ch 20 (Low-Level — volatile section)
- Ask yourself: can you set a breakpoint in GDB, step into a function, print a variable?

**Bed Reading**: K.N. King Ch 14 (Preprocessor) — re-read the macro pitfalls section

---

## SATURDAY AUGUST 15 — FROM-MEMORY CHALLENGE DAY (7:30 AM–12:30 PM)

### Rules for today:
- Clean terminal. No previous files open.
- Close all browser tabs with documentation.
- Just you, a text editor, gcc, gdb, and valgrind.
- Time each challenge.

### Challenge 1 (7:30–7:45 AM): Bit Macros (15 min)
Write `bit_macros.h` from memory. It must compile and the macros must work:
```c
SET_BIT(reg, 3)     // sets bit 3 of reg
CLEAR_BIT(reg, 3)   // clears bit 3
TOGGLE_BIT(reg, 3)  // toggles bit 3
READ_BIT(reg, 3)    // reads bit 3 (returns 0 or 1)
```

**Pass**: Written in under 5 min, no compilation errors.

### Challenge 2 (7:50–8:05 AM): Swap by Pointer + my_strlen (15 min)
Write from memory in `challenge2.c`:
```c
void swap(int *a, int *b);
int my_strlen(const char *s);  // pointer traversal version
```

Test both. Print results. **Pass**: Both correct, both written in under 5 min total.

### Challenge 3 (8:10–8:40 AM): Circular Buffer (30 min)
Write `cbuf.h` and `cbuf.c` completely from memory.
Include: `cbuf_init`, `cbuf_write`, `cbuf_read`, `cbuf_is_full`, `cbuf_is_empty`, `cbuf_count`.
Test with: write 10 bytes, read 5, write 8 more (test wraparound).
Run under Valgrind: 0 leaks.

**Pass**: Complete, correct, Valgrind clean, under 20 min.

### Challenge 4 (8:45–9:25 AM): Singly Linked List (40 min)
Write `list.h` and `list.c` completely from memory.
Include: `insert_front`, `insert_back`, `delete_node`, `reverse_list`, `free_list`, `print_list`.
Test with 5 nodes. Reverse and verify. Free and verify NULL.
Run under Valgrind: 0 leaks.

**Pass**: Complete, correct, Valgrind clean, under 30 min.

### Challenge 5 (9:30–9:50 AM): Makefile (20 min)
Write a Makefile from memory for a 3-file project:
- CC, CFLAGS, TARGET, SRCS, OBJS variables
- Pattern rule `%.o: %.c` with `$@` and `$<`
- `all`, `clean`, `.PHONY` targets

**Pass**: Correct Makefile, written in under 10 min.

### Challenge 6 (9:55–10:25 AM): State Machine (30 min)
Write a 3-state state machine with function pointer dispatch from memory:
- States: IDLE, RUNNING, ERROR
- Events: START, STOP, FAULT
- Handler functions return next state
- Dispatch: `current = handlers[current](event)`

**Pass**: Correct transitions, compiles clean, written in under 20 min.

### SCORING (10:30–11:00 AM)
Count your passes:
- 6/6: You are ready for Phase 2. Consider starting STM32 setup today.
- 4-5/6: Almost there. Use Sunday to fix the 1-2 failures.
- Below 4/6: Identify what failed, spend the afternoon drilling those topics.

Write your scores in PROGRESS.md: which challenges passed, which failed, how long each took.

### GIT CLEANUP (11:00–11:30 AM)
Review your entire C-Practice repo. By now you should have:
```
C-Practice/
├── week1/    (C basics — variables, loops, functions)
├── week2/    (strings, 2D arrays, multi-file, binary search)
├── week3/    (pointers, swap, malloc/free, Valgrind)
├── week4/    (structs, bitwise macros, GPIO simulator)
├── week5/    (volatile, macros, file I/O, logger)
├── week6/    (Makefile, GDB debugging, multi-file project)
├── week7/    (linked list, circular buffer, queue, dynamic array)
├── week8/    (state machines, memory layout, function pointers)
└── week9/    (capstone: sensor_sim)
```

For any folder missing a README.md: write one now.
Push everything: `git add -A && git commit -m "Week 10: from-memory challenges + repo cleanup" && git push`

### LUNCH (11:30 AM–1:30 PM)

### GERMAN BLOCK (1:30–4:30 PM)
- Nicos Weg A2 Lessons 4–5
- Grammar: Perfekt tense with "haben" and "sein" — "Ich habe gelernt. Ich bin gegangen."
- Write 10 sentences in Perfekt tense
- Anki: add 15 new cards

### GERMAN BLOCK 2 (5:00–6:30 PM)
- Nicos Weg A2 Lesson 6
- AnkiDroid: review ALL pending
- Write from memory: describe what you did last week in Perfekt tense

---

## SUNDAY AUGUST 16 — WEAK AREAS + PHASE 1 PREVIEW (7:30 AM–4:00 PM)

### BLOCK 1 (7:30–9:30 AM): Fix Any Failed Saturday Challenges
Whatever you failed on Saturday — redo it now. Still from memory.
If circular buffer failed: write it again, differently, until it clicks.
If state machine failed: draw the diagram first, THEN code.

### BLOCK 2 (9:45–11:15 AM): Phase 1 Exit Test — Dry Run
Simulate the real Phase 1 exit test (which happens Aug 22):

| Test | Time Limit |
|:---|:---|
| Write circular buffer (cbuf.h + cbuf.c) | 15 min |
| Write singly linked list (insert, delete, reverse, free) | 25 min |
| Write Makefile for 4-file project | 10 min |
| Write state machine with dispatch table (3 states) | 15 min |
| Debug buggy program with GDB only (3 bugs) | 15 min |

Total: 80 minutes. No references. No AI.

Score your dry run. If you pass all 5 → you will pass the real test on Aug 22.

### GIT PUSH (11:15–11:30 AM)
```bash
git add .
git commit -m "Week 10: Phase 1 exit test dry run — from-memory challenges complete"
git push origin main
```

### REST + LUNCH (11:30 AM–12:30 PM)

### GERMAN (12:30–2:30 PM)
- Nicos Weg A2 Lessons 7–8
- Anki mega review (aim for 115+ words)
- Write 3 full paragraphs in German: who you are, what you study, what you want

### EXTENDED CODING (2:30–4:00 PM): GDB Interview Prep
Write a buggy program with 5 different bug types. Practice finding each using ONLY GDB.

Bug types to include:
1. Off-by-one loop (reads past array end)
2. Memory leak (malloc without free)
3. Null pointer dereference
4. Stack buffer overflow (char buf[5] = "hello!" — writes 6 chars)
5. Integer overflow (INT_MAX + 1)

Document in comments: exact GDB commands used to find each bug.

---

## WEEK 10 CHECKPOINT (Monday August 17, 4:00 PM)

Update PROGRESS.md.

| Checkpoint Item | Done? |
|:---|:---|
| Saturday challenge scores written in PROGRESS.md | |
| Any failed challenges re-attempted and fixed on Sunday | |
| Phase 1 exit test dry run: all 5 passed | |
| C-Practice repo: all 9 week folders have README.md | |
| GitHub: all weeks pushed and clean | |
| Nicos Weg A2: Lessons 1–8 done | |
| Anki: 115+ German words total | |

> If Phase 1 exit test dry run failed any test → use Monday and Tuesday to fix those gaps before Deload week.
