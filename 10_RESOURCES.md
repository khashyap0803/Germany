# 📚 MASTER RESOURCE GUIDE — What to Learn From, Where, and When

> **Last Updated**: April 18, 2026
> **Purpose**: Every learning session needs a source. This file maps EXACT resources to every topic in your roadmap.
> **Rule**: Before you code, you WATCH or READ. Before you move on, you TEST yourself.

---

## 🔁 THE LEARNING PIPELINE (Every Single Session)

```
┌─────────────────────────────────────────────────────────┐
│  STEP 1 — WATCH/READ  (15-20 min)                      │
│  Learn the concept from a video or book chapter.        │
│  Take notes. Draw diagrams.                             │
│                                                         │
│  STEP 2 — CODE  (40-50 min)                             │
│  Write programs yourself. NO copy-paste. NO AI code.    │
│  If stuck: re-read, re-watch, ask AI to EXPLAIN.        │
│                                                         │
│  STEP 3 — TEST  (10-15 min)                             │
│  Solve a challenge on HackerRank/Exercism/learn-c.org.  │
│  If you fail → go back to STEP 1 for that topic.        │
│                                                         │
│  STEP 4 — EXPLAIN  (2-3 min)                            │
│  Close everything. Explain the concept OUT LOUD as if   │
│  teaching someone. If you can't explain it without      │
│  looking at code → you don't truly understand it.       │
│  THIS is what makes you irreplaceable by AI.            │
└─────────────────────────────────────────────────────────┘
```

---

## 📕 COMPLETE BOOK LIBRARY — Phase-by-Phase

> **Location**: Keep all books in `f:\Documents\DEVELOP\Books\`
> **Printing**: Print the chapters you're actively using. Physical pages > PDF for bed-reading.
> **College Library**: You have unlimited access — download whatever you need.

### 📋 COPY THESE TO YOUR BOOKS DIRECTORY NOW

Find these on your external drive or download from your college online library. Place them all in `f:\Documents\DEVELOP\Books\`:

#### ✅ Already in Books directory
- [x] `The C Programming Language (Kernighan Ritchie).pdf` — K&R 2nd edition
- [x] `C_Programming.pdf` — Comprehensive C reference
- [x] `mastering-stm32-2nd_docutr_com.pdf` — Mastering STM32 by Carmine Noviello

#### 📦 Copy from external drive (you said you have these)
- [ ] **"Computer System Architecture"** by Morris Mano — digital logic, CPU architecture
- [ ] **"Digital Design"** by Morris Mano — combinational/sequential logic, FSMs
- [ ] **"The 8051 Microcontroller and Embedded Systems"** by Muhammad Ali Mazidi (2nd ed) — assembly + C, peripheral interfacing
- [ ] Any other Mazidi books you have (8086, ARM, PIC, AVR)

#### 📥 Download from college library
- [ ] **"Making Embedded Systems"** by Elecia White (O'Reilly, 2nd ed 2024) — embedded design patterns, THE bridge book
- [ ] **"The Definitive Guide to ARM Cortex-M3 and Cortex-M4 Processors"** by Joseph Yiu (3rd ed) — ARM architecture deep dive
- [ ] **"Mastering the FreeRTOS Real Time Kernel"** by Richard Barry — also **FREE** at https://freertos.org/Documentation/161204_Mastering_the_FreeRTOS_Real_Time_Kernel-A_Hands-On_Tutorial_Guide.pdf
- [ ] **"Test Driven Development for Embedded C"** by James W. Grenning — TDD for firmware (portfolio gold)
- [ ] **"Linux Device Drivers"** by Corbet, Rubini, Kroah-Hartman (3rd ed) — also **FREE** at https://lwn.net/Kernel/LDD3/ — for Phase 4
- [ ] **"Computer Organization and Design: RISC-V Edition"** by Patterson & Hennessy — modern computer architecture, better than Mano for understanding pipelines/caches

---

### Phase 1 — C Programming (May-June 2026)

| # | Book | Location | Role | Print? |
|:---|:---|:---|:---|:---|
| 1 | **"The C Programming Language" (K&R, 2nd ed)** | `Books/The C Programming Language (Kernighan Ritchie).pdf` | **PRIMARY** — read chapters in order | ✅ Print Ch 1-7 |
| 2 | **"C Programming" (comprehensive)** | `Books/C_Programming.pdf` | **Supplement** — more examples than K&R | No |
| 3 | **"Beej's Guide to C Programming"** | https://beej.us/guide/bgc/ | **Modern reference** — clearer than K&R, covers C11/C17 | No (use online) |
| 4 | **"Modern C" by Jens Gustedt** | https://gustedt.gitlabpages.inria.fr/modern-c/ (free PDF) | **Advanced reference** — modern C best practices | No |

### Phase 2 — STM32 Microcontrollers (Jul-Sep 2026)

| # | Book | Location | Role | Print? |
|:---|:---|:---|:---|:---|
| 5 | **"Mastering STM32" by Carmine Noviello (2nd ed)** | `Books/mastering-stm32-2nd_docutr_com.pdf` | ⭐ **PRIMARY for Phase 2** — 700+ pages covering GPIO, UART, timers, DMA, everything on STM32. Best STM32 book. | ✅ Print the chapter you're on |
| 6 | **"The 8051 Microcontroller" by Mazidi** | `Books/` (copy from external) | **Context** — compare 8051 architecture with ARM. Many Indian companies still use 8051. | No |
| 7 | **"Making Embedded Systems" by Elecia White** | `Books/` (download) | **Design patterns** — how to structure firmware projects, hardware abstraction layers, state machines | No |

### Phase 3 — FreeRTOS (Oct-Dec 2026)

| # | Book | Location | Role | Print? |
|:---|:---|:---|:---|:---|
| 8 | **"Mastering the FreeRTOS Real Time Kernel"** by Richard Barry | `Books/` (free download) | ⭐ **PRIMARY for Phase 3** — official guide by FreeRTOS creator. Tasks, queues, semaphores, mutexes. | ✅ Print task/queue chapters |
| 9 | **"Making Embedded Systems" by Elecia White** | (same as #7) | **Complement** — chapters on interrupts, memory management, debugging patterns | — |

### Phase 4 — Protocols + Linux (Jan-Jun 2027)

| # | Book | Location | Role | Print? |
|:---|:---|:---|:---|:---|
| 10 | **"The Definitive Guide to ARM Cortex-M3/M4"** by Joseph Yiu | `Books/` (download) | **ARM architecture** — NVIC, MPU, exception handling, bus system. Deep understanding for interviews. | No |
| 11 | **"Linux Device Drivers" (LDD3)** by Corbet et al. | `Books/` (free download) | **Linux kernel** — device drivers, char devices, kernel modules. For embedded Linux phase. | No |
| 12 | **"Computer System Architecture"** by Morris Mano | `Books/` (copy from external) | **Computer architecture** — CPU design, memory hierarchy, I/O — deepens understanding of how MCUs work internally | No |

### Phase 5 — VHDL + Advanced (Jul-Dec 2027)

| # | Book | Location | Role | Print? |
|:---|:---|:---|:---|:---|
| 13 | **"Digital Design"** by Morris Mano | `Books/` (copy from external) | **Digital logic** — combinational/sequential circuits, FSMs, VHDL foundations | No |
| 14 | **"Computer Organization and Design: RISC-V Edition"** by Patterson & Hennessy | `Books/` (download) | **Modern architecture** — pipelines, caches, memory systems. Better than Mano for FH interviews. | No |
| 15 | **"Test Driven Development for Embedded C"** by Grenning | `Books/` (download) | **Portfolio differentiator** — TDD in firmware. German companies love structured testing. | No |

### Phase 6 — Applications (Jan-Jul 2028)

No new technical books. Focus on:
- University application guides (DAAD website)
- SOP writing resources
- German language exam prep materials (Goethe Institut practice books)

---

### Chapter-to-Week Mapping (K&R) — May 2026

| K&R Chapter | Pages | Topics | Your Week |
|:---|:---|:---|:---|
| **Ch 1**: A Tutorial Introduction | pp. 1-35 | Hello World, variables, loops, functions, arrays, character I/O | **Week 1-2** |
| **Ch 2**: Types, Operators, Expressions | pp. 36-53 | Data types, operators, type conversion, bitwise ops | **Week 1 + Week 4** |
| **Ch 3**: Control Flow | pp. 54-66 | if/else, switch, loops, break/continue, goto | **Week 2** |
| **Ch 4**: Functions and Program Structure | pp. 67-92 | Functions, scope, headers, preprocessor, multi-file | **Week 2 + Week 5** |
| **Ch 5**: Pointers and Arrays | pp. 93-126 | Pointers, pointer arithmetic, arrays, multi-dim arrays, function pointers | **Week 3** ⚠️ CRITICAL |
| **Ch 6**: Structures | pp. 127-150 | struct, typedef, self-referential structs, bit-fields | **Week 4** |
| **Ch 7**: Input and Output | pp. 151-168 | printf/scanf deep, file I/O, fopen/fclose/fread/fwrite | **Week 5** |

---

## 📺 YOUTUBE — PRIMARY VIDEO RESOURCES

### 1. Neso Academy — "C Programming" Playlist
- **URL**: https://www.youtube.com/playlist?list=PLBlnK6fEyqRggZZgYpPMUxdY1CYkZtARR
- **Videos**: ~150+, each 7-15 min
- **Quality**: ★★★★★ — Best structured free C course on YouTube
- **Style**: Whiteboard + theory + examples. Indian accent, very clear.
- **Use**: Watch 1-2 videos BEFORE each morning coding session
- **Covers**: Variables → Data types → Operators → Control flow → Functions → Arrays → Strings → Pointers → Structs → Unions → File I/O → Dynamic memory → Preprocessor

#### Neso Academy — Topic-to-Video Mapping (for your May plan)

| Your Topic | Neso Videos to Watch | Approx Time |
|:---|:---|:---|
| **Hello World, printf** | "Getting Started with C", "First C Program", "printf and Format Specifiers" | ~25 min |
| **Variables & Data Types** | "Variables in C", "Data Types in C", "Type Modifiers", "sizeof Operator" | ~35 min |
| **Operators** | "Arithmetic Operators", "Relational & Logical Operators", "Bitwise Operators (Part 1-4)" | ~45 min |
| **Conditions (if/else, switch)** | "If Statement", "If-Else", "Nested If-Else", "Switch Statement" | ~30 min |
| **Loops** | "While Loop", "For Loop", "Do-While Loop", "Nested Loops", "Break & Continue" | ~40 min |
| **Functions** | "Functions in C", "Function Declaration", "Call by Value", "Recursion" | ~35 min |
| **Arrays** | "1D Arrays", "2D Arrays", "Passing Arrays to Functions" | ~30 min |
| **Strings** | "Strings in C", "String Functions (strlen, strcmp, strcpy, strcat)" | ~25 min |
| **Pointers** | "Introduction to Pointers", "Pointer Arithmetic", "Pointers & Arrays" (BUT use mycodeschool for Week 3) | ~60 min |
| **Structs** | "Structures in C", "Typedef", "Pointer to Structure", "Nested Structures" | ~40 min |
| **File I/O** | "File Handling", "fopen/fclose", "fread/fwrite", "fprintf/fscanf" | ~35 min |
| **Preprocessor** | "#define", "#include", "Conditional Compilation", "Macros" | ~25 min |
| **Enums, Unions** | "Enumeration in C", "Unions in C" | ~15 min |

---

### 2. mycodeschool — "Pointers in C/C++" Playlist ⭐ WEEK 3 ESSENTIAL
- **URL**: https://www.youtube.com/playlist?list=PL2_aWCzGMAwLZp6LMUKI3cc7pgGsasm2_
- **Videos**: ~15, each 10-20 min
- **Quality**: ★★★★★ — THE BEST pointers tutorial on the entire internet. Legendary.
- **Style**: Clean diagrams, step-by-step memory visualization, builds concept layer by layer
- **Use**: Watch ALL 15 videos during Week 3 (Pointers Week). 1-2 per day.
- **Playlist order (watch in this exact sequence)**:
  1. Introduction to pointers in C/C++
  2. Working with pointers
  3. Pointer types, pointer arithmetic, void pointers
  4. Pointers to Pointers (double pointers)
  5. Pointers as function arguments — call by reference
  6. Pointers and arrays
  7. Arrays as function arguments
  8. Character arrays and pointers (strings)
  9. Pointers and 2-D arrays
  10. Pointers and multi-dimensional arrays
  11. Dynamic memory allocation (malloc, calloc, realloc, free)
  12. Pointers as function returns
  13. Function pointers
  14. Function pointers and callbacks
  15. Memory leak

---

### 3. Jacob Sorber — Deep Dives
- **URL**: https://www.youtube.com/@JacobSorber
- **Videos**: Individual topic deep-dives, 8-20 min each
- **Quality**: ★★★★★ — University professor, explains the WHY behind everything
- **Style**: Terminal-based coding, real compiler output, practical
- **Use**: Watch AFTER you've tried something and want deeper understanding

#### Key Jacob Sorber Videos for Your May Plan

| Topic | Video Title to Search | When |
|:---|:---|:---|
| How compilation works | "How do C programs get compiled?" | Week 1, Day 1 |
| Arrays | "Arrays in C (the full story)" | Week 2 |
| Pointers basics | "Pointers in C — finally understand them" | Week 3 |
| malloc and free | "Dynamic Memory Allocation in C (malloc, calloc, realloc, free)" | Week 3 |
| Function pointers | "Function Pointers in C" | Week 3 |
| Structs | "Structs in C — everything you need to know" | Week 4 |
| Bit manipulation | "Bit manipulation in C" | Week 4 |
| volatile keyword | "The volatile keyword in C" | Week 5 |
| const keyword | "const in C — what does it really mean?" | Week 5 |
| Makefiles | "How to write a Makefile" | Week 5-6 |
| GDB debugging | "GDB Tutorial: Finding Bugs in C Programs" | Week 3+ |
| Enums | "Enums in C" | Week 5 |
| State machines | "State Machines in C" | Week 5 |
| Multi-file projects | "Splitting your C code into multiple files" | Week 2+ |

---

### 4. Additional YouTube Channels (Backup / Alternative Explanations)

| Channel | Best For | When to Use |
|:---|:---|:---|
| **Bro Code** — "C Programming Full Course" (~4 hrs, single video) | Complete overview in one sitting | Watch BEFORE May 1st as a weekend preview |
| **Jenny's Lectures CS IT** — "C Programming" playlist | Alternative explanation if Neso doesn't click on a topic | When confused |
| **CodeVault** | Makefiles, processes, threads, advanced C | Week 6+ (June) |
| **Low Level Learning** | How computers actually work at hardware level | Motivational + context |
| **Ben Eater** | Building a computer from scratch (logic gates → CPU) | Weekend inspiration viewing |

---

## 🌐 INTERACTIVE PRACTICE PLATFORMS

| Platform | URL | Cost | What | When to Use |
|:---|:---|:---|:---|:---|
| **learn-c.org** | https://www.learn-c.org/ | Free | Interactive C lessons with in-browser compiler | After watching videos — practice each concept with guided exercises |
| **HackerRank C** | https://www.hackerrank.com/domains/c | Free | Graded C challenges sorted by topic | End of each day — test yourself with 1-2 challenges |
| **Exercism C Track** | https://exercism.org/tracks/c | Free | 90+ exercises with optional mentor feedback | Weekly challenges (2-3 per week) |
| **Programiz C** | https://www.programiz.com/c-programming | Free | Clean tutorials + online compiler | Quick reference when writing code |
| **W3Schools C** | https://www.w3schools.com/c/ | Free | Simple reference with "Try It Yourself" | Quick lookups for syntax |
| **LeetCode Easy (C)** | https://leetcode.com/problemset/?difficulty=EASY&languageTags=c | Free tier | Algorithm problems in C | From Week 6+ (after C basics are solid) |

### Practice Platform Mapping by Week

| Week | learn-c.org Lessons | HackerRank Challenges | Exercism Exercises |
|:---|:---|:---|:---|
| **Week 1** | "Hello World", "Variables and Types", "Conditions", "Loops" | "Hello World", "Playing With Characters", "Sum and Difference", "Conditional Statements" | `hello-world`, `resistor-color` |
| **Week 2** | "Functions", "Arrays", "Strings" | "Functions in C", "Array Reversal", "Printing Tokens", "Digit Frequency" | `isogram`, `hamming`, `rna-transcription` |
| **Week 3** | "Pointers", "Dynamic Allocation" | "Pointers in C", "Printing Pattern", "Dynamic Array in C" | `grains`, `word-count` |
| **Week 4** | "Structures", "Linked Lists" | "Bitwise Operators", "Boxes through a Tunnel (structs)", "Small Triangles, Large Triangles" | `binary`, `nucleotide-count` |
| **Week 5** | "File I/O", "Recursion" | "Variadic functions in C", "Sorting Array of Strings" | `phone-number`, `circular-buffer` |

---

## 💰 RECOMMENDED PURCHASES (Phase 2+, Not for May)

### Udemy Courses (Buy individually, NOT subscription)

| # | Course | Instructor | Normal/Sale | Buy When | Use When | Why |
|:---|:---|:---|:---|:---|:---|:---|
| 1 | **"Microcontroller Embedded C Programming: Absolute Beginners"** | FastBit Embedded Brain Academy | ₹549 / ₹399 | June 2026 | July 2026 (Phase 2 start) | Bridges pure C → embedded C. Covers STM32 register-level programming. |
| 2 | **"Mastering Microcontroller and Embedded Driver Development"** | FastBit Embedded Brain Academy | ₹549 / ₹399 | June 2026 | July 2026 (Phase 2) | GPIO, SPI, I2C, UART, interrupt drivers from scratch on STM32. THE course for driver development. |

> **Why NOT subscription**: You only need 2 courses from Udemy. At ₹549 each = ₹1,098 total, permanent ownership, lifetime access. Subscription at ₹4,500/year means you lose access if you cancel, and you're paying 4× more for only 2 courses.
>
> **How to catch sales**: Add courses to Udemy wishlist → Udemy emails you when they go on sale. Or check every Sunday during weekly review. Sales happen every 2-3 weeks. Both courses will drop to ₹399.

---

## 🎓 FREE COURSES (From Your Subscriptions)

### Educative (6 Months Free via GitHub Student Pack)

| Course | Hours | Use When | Priority |
|:---|:---|:---|:---|
| **"Operating Systems: Virtualization, Concurrency & Persistence"** | 40h | Phase 3 (Oct 2026) — FreeRTOS concepts, scheduling, memory management | ⭐ HIGH — claim now |
| **"Learn C++: The Complete Course for Beginners"** | 10h | Phase 5 (Jul 2027) — C++ after mastering C | 🟡 Medium |

> **Action**: Claim your Educative access NOW via GitHub Student Pack. Even if you won't use it until October, activate the 6-month window so it covers Oct 2026.

### Udemy Courses You Already Own (Relevant)

| Course | Use When |
|:---|:---|
| **"Learn everything about Linux! 100+ hours"** | Phase 4 (Apr 2027) — Linux CLI, shell scripting |
| **"Master of Essential C++ Programming"** | Phase 5 (Jul 2027) — C++ fundamentals |

---

## 🖥️ SOFTWARE USAGE TIMELINE

### May 2026 (Phase 1: C Programming)

| Tool | Purpose | How |
|:---|:---|:---|
| **WSL2 + gcc** | Compile and run C programs | `wsl` → `cd /mnt/f/Documents/DEVELOP/C-Practice` → `gcc -o prog prog.c -Wall` |
| **VS Code** (+C/C++ extension) | Editor for code (better than nano for larger programs) | Open WSL folder in VS Code, use integrated terminal |
| **Anki PC + AnkiDroid** | German vocabulary flashcards (spaced repetition) | 5 new cards/morning + review at lunch + review on commute |
| **DW Learn German app** | Nicos Weg lessons A1 | Commute IN (7:00-8:30 AM) |
| **dict.cc app** | German dictionary | Whenever you encounter an unknown word → add to Anki |
| **Easy German podcast app** | Passive German listening | Commute BACK |
| **PomoDone** (GitHub Pack, free 2yr) | Pomodoro timer for study sessions | Set 25-min timers during morning + evening blocks |
| **Notion** (GitHub Pack, Education plan) | Weekly reviews, study notes, habit tracking | Sunday 4:00 PM weekly review |
| **Google AI Pro** | Concept explanations ONLY (AI Detox!) | When stuck after 20 min of trying |

### July 2026+ (Phase 2: STM32)

| Tool | Purpose |
|:---|:---|
| **STM32CubeIDE** | STM32 project creation, HAL code generation, debugging |
| **Proteus 8 Professional** | Simulate STM32 circuits before wiring on breadboard |
| **Tera Term** | Serial terminal for UART communication with STM32 |
| **PulseView + Sigrok** | Capture SPI/I2C/UART signals from Sipeed SLogic analyzer |
| **PlatformIO (VS Code)** | Alternative STM32/ESP32 build system |

### October 2026+ (Phase 3: RTOS)

| Tool | Purpose |
|:---|:---|
| **Educative** | "Operating Systems" course for RTOS theory |
| **CLion** (JetBrains, free via GitHub Pack) | Professional C/C++ IDE for multi-file RTOS projects |
| **Keil µVision 5** | Professional STM32 development (resume builder) |
| **IAR Embedded Workbench ARM** | Alternative professional IDE (resume builder) |

### 2027+ (Phase 4-6)

| Tool | Purpose |
|:---|:---|
| **Udemy Linux course** | Linux CLI mastery |
| **VMware Workstation Pro** | Linux VM for embedded Linux development |
| **Altium Designer** | PCB design for portfolio project |
| **MATLAB R2024b** | Signal processing, control systems (if needed) |
| **Arduino Cloud** (GitHub Pack) | Arduino IoT projects |
| **DigitalOcean** ($200 credit, GitHub Pack) | QEMU ARM emulation, MQTT broker hosting |
| **Microsoft Azure** ($100 credit, GitHub Pack) | IoT Hub, cloud builds |

---

## 🇩🇪 GERMAN LANGUAGE RESOURCES

| Resource | Type | Level | When | How |
|:---|:---|:---|:---|:---|
| **DW Nicos Weg** (app + web) | Structured video course | A1 → B1 | Commute IN (every day) | Watch lesson, repeat phrases, do exercises |
| **Easy German** (YouTube + podcast) | Real street conversations | A2+ | Commute BACK (from Jul 2026) | Passive listening, catch words you know |
| **Learn German with Anja** (YouTube) | Grammar explanations in English | A1 → B2 | Saturday German session | When Nicos Weg grammar is unclear |
| **Deutsch für Euch** (YouTube) | Grammar deep-dives | A2+ | When struggling with a grammar rule | Detailed grammar explanations |
| **AnkiDroid** (shared decks) | Spaced repetition flashcards | A1 → B2 | 3× daily (morning, lunch, commute) | 5 new cards + review old ones |
| **dict.cc** (app + web) | German-English dictionary | All | Whenever you see an unknown word | Look up → add to Anki immediately |
| **Google AI Pro** (voice mode) | Speaking practice | A1+ | Saturday 3:45-5:00 PM | "Speak to me in simple German. Correct my mistakes." |
| **italki** (paid tutors) | Human conversation practice | B1+ | From Mar 2027 | ₹500-1000 per 45-min session, 1x/week |

---

## ⚡ QUICK REFERENCE: "I'm stuck on X, where do I go?"

| Stuck On | Go To |
|:---|:---|
| "I don't understand the concept at all" | Neso Academy video for that topic → then Beej's Guide chapter |
| "I watched the video but still confused" | Jacob Sorber video (different explanation) → then Jenny's Lectures |
| "I can't write the code" | look at learn-c.org interactive exercise for that topic |
| "My code has errors I can't fix" | Read `gcc -Wall` output carefully → Google the exact error → ask Google AI to EXPLAIN the error (not fix it) |
| "I want to test if I really understand" | HackerRank challenge for that topic |
| "I need more practice problems" | Exercism C track |
| "I need quick syntax reference" | Programiz C or W3Schools C |
| "I forgot a German word" | dict.cc → add to Anki |
| "German grammar makes no sense" | Learn German with Anja (YouTube) for that specific rule |
