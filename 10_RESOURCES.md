# 📚 MASTER RESOURCE GUIDE — What to Learn From, Where, and When

> **Last Updated**: October 15, 2026 — final course list after the Oct 2026 Udemy sale; phase dates follow `07_MONTHLY_TIMELINE.md`
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

> **Location**: `F:\Documents\DEVELOP\STUDY\Books\` (PDFs are git-ignored)
> **Annotations**: Use Adobe Acrobat Reader Pro to highlight and annotate directly in PDF. Use paper notebook for memory diagrams, pointer chains, and register layouts.
> **College Library**: You have unlimited access — download whatever you need.

### 📋 COPY THESE TO YOUR BOOKS DIRECTORY NOW

All of these are already in `STUDY\Books\`:

#### ✅ Already in Books directory (ALL VERIFIED)
- [x] `C Programming - A Modern Approach - 2nd_Ed(C89, c99) - King by .pdf` — K.N. King 2nd edition (**PRIMARY for Phase 1**)
- [x] `The C Programming Language (Kernighan Ritchie).pdf` — K&R 2nd edition (reference)
- [x] `C_Programming.pdf` — K&R 2nd edition (scanned backup copy)
- [x] `mastering-stm32-2nd_docutr_com.pdf` — Mastering STM32 by Carmine Noviello, 2nd ed (910 pages)
- [x] `making_embedded_systems.pdf` — Making Embedded Systems by Elecia White, 2nd ed (428 pages)
- [x] `8051-microcontroller-and-embedded-systems-...pdf` — The 8051 Microcontroller by Mazidi, 2nd ed (641 pages)
- [x] `Mastering-the-FreeRTOS-Real-Time-Kernel.v1.1.0.pdf` — FreeRTOS official guide by Richard Barry (304 pages)
- [x] `toaz.info-yiu-j-the-definitive-guide-...pdf` — ARM Cortex-M3/M4 Definitive Guide by Joseph Yiu, 3rd ed (1,055 pages)
- [x] `Linux Device Drivers Third Edition.pdf` — LDD3 by Corbet et al. (638 pages)
- [x] `computer-system-architecture-morris-mano-third-edition.pdf` — Computer System Architecture by Mano, 3rd ed (524 pages)
- [x] `Azal2020-01-22-12-16-48-75016.pdf` — Digital Design with Verilog HDL by Mano & Ciletti, 5th ed (565 pages)
- [x] `M.-Morris-Mano-Digital-Design-Prentice-Hall-1995.pdf` — Digital Design by Mano (1995 edition, supplementary)
- [x] `computer-organization-and-design-risc-v-edition-...pdf` — Computer Organization & Design RISC-V by Patterson & Hennessy, 2nd ed (1,137 pages)
- [x] `books-library.net-07281709Ee1R6.pdf` — Test-Driven Development for Embedded C by James Grenning (365 pages)

> **Total: 14 books, ~7,500+ pages. Library is 100% complete. No additional purchases needed.**

---

### Phases 0–1 — C Programming (Oct 2026 – Jan 2027)

| # | Book | Location | Role |
|:---|:---|:---|:---|
| 1 | **"C Programming: A Modern Approach" (K.N. King, 2nd ed)** | `Books/C Programming - A Modern Approach - 2nd_Ed(C89, c99) - King by .pdf` | ⭐ **PRIMARY** — read chapters in order, do 5+ exercises per chapter. Covers C99. Best C learning book for self-study. |
| 2 | **"The C Programming Language" (K&R, 2nd ed)** | `Books/The C Programming Language (Kernighan Ritchie).pdf` | **REFERENCE** — bed-time reading. Read K&R's concise version of the same topic after learning from King. |
| 3 | **"Beej's Guide to C Programming"** | https://beej.us/guide/bgc/ | **Supplement** — modern reference, covers C11/C17, clearer explanations for some topics |
| 4 | **"Modern C" by Jens Gustedt** | https://gustedt.gitlabpages.inria.fr/modern-c/ (free PDF) | **Advanced reference** — modern C best practices, for Phase 3+ |

### Phase 2 — STM32 Microcontrollers (Feb – May 2027)

| # | Book | Location | Role |
|:---|:---|:---|:---|
| 5 | **"Mastering STM32" by Carmine Noviello (2nd ed)** | `Books/mastering-stm32-2nd_docutr_com.pdf` | ⭐ **PRIMARY for Phase 2** — 910 pages covering GPIO, UART, timers, DMA, everything on STM32. #1 STM32 book. |
| 6 | **"The 8051 Microcontroller" by Mazidi** | `Books/8051-microcontroller-...pdf` | **Supplementary** — compare 8051 architecture with ARM. Good for microcontroller fundamentals. |
| 7 | **"Making Embedded Systems" by Elecia White (2nd ed)** | `Books/making_embedded_systems.pdf` | **Design patterns** — how to structure firmware projects, HALs, state machines. #1 embedded design book. |

### Phase 4 — FreeRTOS (Nov 2027 – Mar 2028)

| # | Book | Location | Role |
|:---|:---|:---|:---|
| 8 | **"Mastering the FreeRTOS Real Time Kernel"** by Richard Barry | `Books/Mastering-the-FreeRTOS-Real-Time-Kernel.v1.1.0.pdf` | ⭐ **PRIMARY for Phase 3** — official guide by FreeRTOS creator. #1 and ONLY RTOS book needed. |
| 9 | **"Making Embedded Systems" by Elecia White** | (same as #7) | **Complement** — chapters on interrupts, memory management, debugging patterns |

### Optional / 2028 — ARM deep-dive, Linux, architecture

| # | Book | Location | Role |
|:---|:---|:---|:---|
| 10 | **"The Definitive Guide to ARM Cortex-M3/M4"** by Joseph Yiu | `Books/toaz.info-yiu-j-the-definitive-guide-...pdf` | **ARM architecture bible** — NVIC, MPU, exception handling. #1 ARM book, uncontested. |
| 11 | **"Linux Device Drivers" (LDD3)** by Corbet et al. | `Books/Linux Device Drivers Third Edition.pdf` | **Linux kernel concepts** — char devices, kernel modules. Supplement with free Bootlin training materials for modern APIs. |
| 12 | **"Computer System Architecture"** by Morris Mano | `Books/computer-system-architecture-morris-mano-third-edition.pdf` | **Computer architecture** — CPU design, memory hierarchy. Supplementary to Patterson & Hennessy. |

### Optional — Digital design / VHDL (only needed for RWU) + testing

| # | Book | Location | Role |
|:---|:---|:---|:---|
| 13 | **"Digital Design with Verilog HDL" (5th ed)** by Mano & Ciletti | `Books/Azal2020-01-22-12-16-48-75016.pdf` | **Digital logic** — combinational/sequential circuits, FSMs, Verilog. Latest edition (5th). |
| 14 | **"Computer Organization and Design: RISC-V Edition"** by Patterson & Hennessy | `Books/computer-organization-and-design-risc-v-edition-...pdf` | **#1 computer organization book** — pipelines, caches, memory systems. RISC-V edition is the gold standard. |
| 15 | **"Test Driven Development for Embedded C"** by Grenning | `Books/books-library.net-07281709Ee1R6.pdf` | **Portfolio differentiator** — TDD in firmware. The ONLY book in this category. German companies love structured testing. |

### Phase 6 — Applications (Jan-Jul 2028)

No new technical books. Focus on:
- University application guides (DAAD website)
- SOP writing resources
- German language exam prep materials (Goethe Institut practice books)

---

### Chapter-to-Week Mapping (K.N. King) — *old June 2026 mapping; the current mapping is in `18_RESTART_8_WEEKS.md` and `07`*

| K.N. King Chapter | Topics | Your Week |
|:---|:---|:---|
| **Ch 1-2**: Introducing C + C Fundamentals | History, program structure, comments, variables, types, assignment | **Week 1** |
| **Ch 3**: Formatted I/O | printf/scanf deep dive, format specifiers | **Week 1** |
| **Ch 4**: Expressions | Operators, type conversion, precedence | **Week 1** |
| **Ch 5**: Selection Statements | if/else, switch, conditional expressions | **Week 1-2** |
| **Ch 6**: Loops | while, for, do-while, break, continue | **Week 2** |
| **Ch 7**: Basic Types | Integer types, floating types, type conversion, typedef | **Week 2** |
| **Ch 8**: Arrays | 1D arrays, multi-dimensional arrays, sizeof with arrays | **Week 2** |
| **Ch 9**: Functions | Function definitions, arguments, return, recursion | **Week 2** |
| **Ch 10**: Program Organization | Header files, multi-file programs, scope, storage duration | **Week 2** |
| **Ch 11**: Pointers | Pointer variables, address/indirection operators, pointer arithmetic | **Week 3** ⚠️ CRITICAL |
| **Ch 12**: Pointers and Arrays | Pointer-array relationship, pointer as arguments, strings | **Week 3** ⚠️ CRITICAL |
| **Ch 13**: Strings | String literals, string library, arrays of strings | **Week 3** |
| **Ch 14**: The Preprocessor | #define, #include, conditional compilation, macros | **Week 4-5** |
| **Ch 16**: Structures, Unions, Enumerations | struct, typedef, unions, bit-fields, enums | **Week 4** |
| **Ch 17**: Advanced Uses of Pointers | Dynamic memory (malloc/free), linked lists, function pointers | **Week 3-4** |
| **Ch 22**: Input/Output | File I/O (fopen, fclose, fprintf, fscanf, fread, fwrite) | **Week 5** |

> **K&R Bed Reading Mapping**: Read K&R Ch 1-7 in parallel (30 min before sleep) for the concise "expert" perspective on the same topics.

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

## 💰 UDEMY COURSES

### Owned before Oct 2026 — embedded/electronics (use these)
| Course | Instructor | Use in |
|:---|:---|:---|
| Microcontroller Embedded C Programming: Absolute Beginners | FastBit | Phases 0–1, alongside K.N. King |
| Mastering Microcontroller and Embedded Driver Development (MCU1) | FastBit | Phase 2 (Mar–Apr 2027) |
| Mastering Microcontroller: Timers, PWM, CAN, Low Power (MCU2) | FastBit | Phase 4 (Jan 2028) |
| Mastering Zephyr RTOS with DeviceTree | FastBit | Optional (2028) |
| Learn everything about Linux! 100+ hours | Vitor Mazuco | Optional (2028) |
| Crash Course Electronics and PCB Design | Andre LaMothe | Reference for electronics/PCB |
| Master of Essential C++ Programming | Sayman | Optional (C++ for Darmstadt's "C/C++") |

*Also owned but not part of this plan:* ~13 AI/Python/data courses, Java Masterclass, C# Basics, DevOps, Google Sheets. Ignore them until after the move.

### Bought in the Oct 2026 sale (8 courses, ₹4,122)
| Price | Course | Size | Use in |
|:--|:---|:--|:---|
| ₹599 | Embedded Systems Programming on ARM Cortex-M3/M4 (FastBit) | 15 h | **Phase 2 — Feb 2027** |
| ₹529 | ARM Cortex M Microcontroller DMA Programming Demystified (FastBit) | 10 h | **Phase 2 — May 2027** |
| ₹539 | DSP From Ground Up on ARM Processors (BHM / Israel Gbati) | 25.5 h | **Phase 3 — Jun–Jul 2027** |
| ₹509 | Mastering RTOS: Hands on FreeRTOS and STM32Fx (FastBit) | 14 h | **Phase 4 — Nov 2027** |
| ₹479 | PCB Design in Cadence OrCAD/Allegro: Basics to Expert (Pradeep Raj) | 37 h | **Phase 4 — Nov 2027 → Mar 2028** |
| ₹469 | ISO 14971 Medical Device Development & Risk Management (Robert Ryan) | 15.5 h | **2028 free period** |
| ₹519 | The English Master Course: Grammar, Speaking (Scott Mendoza) | 83.5 h | **Now → Mar 2027** (30 min/day) |
| ₹479 | IELTS Band 7+ Complete Prep Course (Keino Campbell) | 97.5 h | **Apr → Sep 2027** |

**Rule:** one course at a time, in the order of `07_MONTHLY_TIMELINE.md`. Buying is done — finishing is the job.

### Considered and NOT bought (with the free alternative)
| Not bought | Use instead (free) |
|:---|:---|
| Complete Electronics: Analog Hardware Design | **Neso Academy** (theory) + **TI Precision Labs** (op-amps, noise, ADCs) + NPTEL *Analog Electronic Circuits* if needed |
| Op-amp circuits on LTSpice | **TI Precision Labs** |
| Embedded System Design using UML State Machines | **Miro Samek — "Modern Embedded Systems Programming"** (YouTube) |
| Bluetooth Low Energy From Ground Up | **Nordic DevAcademy** (nRF Connect SDK, BLE fundamentals) |
| ISO 13485 design-control course (3.5 h) | **FDA "Design Control Guidance for Medical Device Manufacturers"** (PDF) + Greenlight Guru articles |
| VHDL courses | **nandland.com** + **HDLBits** (only needed for RWU) |
| Udemy German A1 | **DW Nicos Weg** + **Goethe A1 exam** (a Udemy certificate is not accepted) |
| PCB with KiCad / Altium | Phil's Lab + Robert Feranec (YouTube); KiCad is free after you leave Unistring |
| Medical Device Software Process Blackbelt (IEC 62304) — ₹1,199 | Buy only if it drops below ₹600 |
| Unit Testing & Other Embedded Software Catalysts — ₹2,899 | Buy only if it drops below ₹600; Grenning's TDD book (owned) meanwhile |

---

## 🎓 FREE RESOURCES (better than paid for these topics)

| Topic | Resource |
|:---|:---|
| Analog/electronics theory | **Neso Academy** (YouTube) |
| Op-amps, noise, data converters | **TI Precision Labs** (ti.com, free videos) |
| University-level depth + certificates | **NPTEL / SWAYAM** — free to learn; proctored exam ≈ ₹1,000. Certificates don't add ECTS in Germany but are good supporting evidence. Candidates: *Control Engineering* (only if Bremerhaven says Control Systems is short), *Software Engineering* (for Dortmund, Jan–Apr 2028), *Biomedical Signal Processing* |
| State machines / embedded design | **Miro Samek** (YouTube) |
| RTOS concepts | **Shawn Hymel — Introduction to RTOS** (Digi-Key, YouTube) |
| PCB design habits | **Phil's Lab**, **Robert Feranec** (YouTube) |
| DSP | **Steven Smith — The Scientist & Engineer's Guide to DSP** (free online) |
| BLE / nRF52 | **Nordic DevAcademy** |
| Medical device regulation | FDA design-control guidance, CDSCO website, Greenlight Guru |
| IELTS | **British Council "Road to IELTS"**, **IELTS Liz**, free practice tests (British Council / IDP) |
| German | **DW Nicos Weg**, Goethe practice tests, Easy German |

---

## 🖥️ SOFTWARE USAGE TIMELINE

### Phases 0–1 (Oct 2026 – Jan 2027): C Programming

| Tool | Purpose | How |
|:---|:---|:---|
| **WSL2 + gcc** | Compile and run C programs | `wsl` → `cd /mnt/f/Documents/DEVELOP/C-Practice` → `gcc -o prog prog.c -Wall` |
| **VS Code** (+C/C++ extension) | Editor for code (better than nano for larger programs) | Open WSL folder in VS Code, use integrated terminal |
| **Anki PC + AnkiDroid** | German vocabulary flashcards (spaced repetition) | 5 new cards/morning + review at lunch + review on commute |
| **DW Learn German app** | Nicos Weg lessons A1 | Commute IN (7:00-8:30 AM) |
| **dict.cc app** | German dictionary | Whenever you encounter an unknown word → add to Anki |
| **Easy German podcast app** | Passive German listening | Commute BACK |
| **PomoDone** (GitHub Student Pack — only while still eligible, free 2yr) | Pomodoro timer for study sessions | Set 25-min timers during morning + evening blocks |
| **PROGRESS.md** (in this repo) | Sunday 4:00 PM weekly review | **ONE tracking system.** Hours, programs, German words, blockers — all here |
| **Google AI Pro** | Concept explanations ONLY (AI Detox!) | When stuck after 20 min of trying |

### Phase 2+ (Feb 2027 onward): STM32

| Tool | Purpose |
|:---|:---|
| **STM32CubeIDE** | STM32 project creation, HAL code generation, debugging |
| **Proteus 8 Professional** | Simulate STM32 circuits before wiring on breadboard |
| **Tera Term** | Serial terminal for UART communication with STM32 |
| **PulseView + Sigrok** | Capture SPI/I2C/UART signals from Sipeed SLogic analyzer |
| **PlatformIO (VS Code)** | Alternative STM32/ESP32 build system |

### Phase 4+ (Nov 2027 onward): RTOS — optional professional IDEs

| Tool | Purpose |
|:---|:---|
| **CLion** (JetBrains, free via GitHub Student Pack — only while still eligible) | Professional C/C++ IDE for multi-file RTOS projects |
| **Keil µVision 5** | Professional STM32 development (resume builder) |
| **IAR Embedded Workbench ARM** | Alternative professional IDE (resume builder) |

### 2027+ (Phase 4-6)

| Tool | Purpose |
|:---|:---|
| **Udemy Linux course** | Linux CLI mastery |
| **VMware Workstation Pro** | Linux VMs for embedded Linux development (Fedora Workstation + openSUSE Tumbleweed already installed, 40GB/6GB RAM each) |
| **Altium Designer** | PCB design for portfolio project |
| **MATLAB R2024b** | Signal processing, control systems (if needed) |
| **Arduino Cloud** (GitHub Student Pack — only while still eligible) | Arduino IoT projects |
| **DigitalOcean** ($200 credit, GitHub Student Pack — only while still eligible) | QEMU ARM emulation, MQTT broker hosting |
| **Microsoft Azure** ($100 credit, GitHub Student Pack — only while still eligible) | IoT Hub, cloud builds |

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
