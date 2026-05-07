# 📅 JUNE 2026 — MASTER OVERVIEW

> **Period**: June 1 (Monday) → June 30 (Tuesday)
> **Month Goal**: Complete C mastery — Makefiles, GDB, data structures, state machines, Phase 1 capstone
> **AI Status**: 🔴 **BANNED for code** — AI only explains concepts, YOU write ALL code
> **Status**: Working at Unistring (9 AM - 7/8 PM, 4hr commute)
> **Phase**: Phase 1 Final Month — After June, you move to STM32 (Phase 2) in July
>
> **K.N. King Chapters**: Ch 15-22, 24, 26 (Large Programs, Advanced Pointers, Low-Level, I/O, Error Handling)
> **K&R Bed Reading**: Ch 4 (finish), Ch 5 (Pointers revisit), Ch 6 (Structures revisit), Ch 7 (I/O), Ch 8 (UNIX System Interface)
> **FastBit Udemy**: Remaining sections + review entire course
>
> **End-of-Month Goal**: You can write ANY C program from scratch — linked lists, queues, state machines,
> multi-file projects with Makefiles, debug with GDB, and EXPLAIN every concept on a whiteboard.
> **If you cannot do this by June 30, you are NOT ready for STM32.**

---

## ⏰ DAILY TEMPLATES (Same as May)

### 🟦 WEEKDAY (Mon-Fri)

| Time | Duration | Activity | Tool |
|:---|:---|:---|:---|
| **5:00 AM** | 10 min | Wake up. Water. Wash face. **NO PHONE.** | Alarm |
| **5:10 - 6:30 AM** | 1h 20m | 🔶 **MORNING BLOCK — C study** | WSL + gcc + K.N. King book |
| **6:30 - 7:00 AM** | 30m | Get ready, breakfast | — |
| **7:00 - 8:30 AM** | 1.5h | 🎧 **COMMUTE IN — German audio** | DW Nicos Weg + AnkiDroid |
| **12:30 - 12:45 PM** | 15m | 📱 **LUNCH ANKI — German cards** | AnkiDroid |
| **7:00 - 8:30 PM** | 1.5h | 🎧 **COMMUTE BACK — German audio** | Easy German / DW podcasts |
| **9:30 - 10:00 PM** | 30m | 📖 **BED READING — K&R book** | K&R PDF |
| **10:00 PM** | — | **SLEEP. Non-negotiable.** | — |

### 🟩 SATURDAY — 9 hour deep study day

| Time | Duration | Activity |
|:---|:---|:---|
| **6:00 AM** | — | Wake up. Coffee/tea. |
| **6:30 - 7:30 AM** | 1h | 💻 C warmup — review yesterday's concepts |
| **7:30 - 7:45** | 15m | Break |
| **7:45 - 9:15 AM** | 1.5h | 💻 **C Deep Session 1** — new topic |
| **9:15 - 9:30** | 15m | Break + snack |
| **9:30 - 11:00 AM** | 1.5h | 💻 **C Deep Session 2** — practice programs |
| **11:00 - 11:15** | 15m | Break |
| **11:15 AM - 12:45 PM** | 1.5h | 💻 **C Deep Session 3** — harder exercises |
| **12:45 - 2:00 PM** | 1.25h | Lunch + rest |
| **2:00 - 3:30 PM** | 1.5h | 🇩🇪 **German Session 1** — Nicos Weg + writing |
| **3:30 - 3:45** | 15m | Anki review |
| **3:45 - 5:00 PM** | 1.25h | 🇩🇪 **German Session 2** — speaking with Google AI |
| **5:00 PM+** | — | Free. Gym, family, relax. |

### 🟨 SUNDAY — 7 hour study + review day

| Time | Duration | Activity |
|:---|:---|:---|
| **7:00 AM** | — | Sleep in 1 extra hour |
| **7:30 - 9:00 AM** | 1.5h | 💻 C practice — solve problems from the week |
| **9:15 - 10:45 AM** | 1.5h | 💻 C mini-project — combine week's concepts |
| **11:00 AM - 12:30 PM** | 1.5h | 💻 Git push + code cleanup + README |
| **12:30 - 2:00 PM** | 1.5h | Lunch + rest |
| **2:00 - 3:00 PM** | 1h | 🇩🇪 German review — write sentences, test yourself |
| **3:00 - 4:00 PM** | 1h | 🇩🇪 Anki mega review + add new cards |
| **4:00 - 4:30 PM** | 30m | 📋 Weekly review — what worked, what didn't, plan next week |

---

## 📚 BOOKS & RESOURCES FOR JUNE

### Primary Resources

| Resource | Format | How to Use |
|:---|:---|:---|
| **K.N. King Ch 15-22, 24, 26** | PDF | PRIMARY textbook. Large programs, advanced pointers, low-level programming, I/O |
| **K&R Ch 4-8** | PDF | BED READING. Expert-level perspective on functions, pointers, structures, I/O |
| **FastBit Embedded C (remaining)** | Udemy (16.5h) | Watch remaining sections at 1.5× AFTER reading King. Focus on embedded-specific C patterns. |
| **Beej's Guide to C** | Free web | Supplement for file I/O and networking concepts |

### Practice Platforms

| Platform | Use For | URL |
|:---|:---|:---|
| **Exercism C Track** | Data structures + algorithms | exercism.org/tracks/c |
| **HackerRank C** | Problem solving | hackerrank.com/domains/c |
| **LeetCode Easy (C)** | Interview prep | leetcode.com/problemset/ (filter by C) |
| **Codeforces** | Competitive thinking | codeforces.com (sort by difficulty 800-1000) |

---

## 🛡️ JUNE FOCUS: WHY THESE TOPICS MATTER FOR STM32

| June Topic | Direct STM32 Application (July+) |
|:---|:---|
| **Makefiles** | STM32 bare-metal projects use Makefiles (not just IDE build) |
| **GDB debugging** | `gdb-multiarch` + OpenOCD = how you debug on real hardware |
| **Multi-file projects** | Every STM32 project has 20+ files (drivers, HAL, app, headers) |
| **Linked lists** | FreeRTOS task scheduler uses linked lists internally |
| **Queues / Circular buffers** | UART receive buffers, sensor data pipelines |
| **State machines** | 90% of embedded firmware IS a state machine |
| **Memory layout** | You MUST know where your code/data lives on a 128KB MCU |
| **Packed structs** | Hardware register maps ARE packed structs |
| **Bit fields** | Register bit definitions use bit fields |
| **Memory-mapped I/O** | STM32 registers ARE memory-mapped addresses (`volatile uint32_t *`) |

> **Every single June topic maps directly to real STM32 work. This isn't academic — this is your career foundation.**

---

## 📊 MONTHLY TARGETS

| Metric | Target |
|:---|:---|
| C programs written from scratch | **25+** |
| GitHub commits | **20+** |
| Programs you can re-write from MEMORY | **15+** (including May's) |
| K.N. King chapters completed | **Ch 15-22, 24, 26** |
| K&R chapters read (bed reading) | **Ch 4-8** (finish the book) |
| Bugs found and fixed using `gcc -Wall` + `gdb` (NOT AI) | **25+** |
| Data structures implemented from scratch | **5+** (linked list, queue, stack, circular buffer, hash table) |
| Memory diagrams drawn on paper | **20+** |
| Nicos Weg lessons completed | **25-50 (A1 finish → A2 start)** |
| German words in Anki | **150+ total** (100 from May + 50 new) |
| Days where you woke at 5 AM | **≥ 25 of 30** |
| Total active study hours | **~100 hours** |
| **CAPSTONE PROJECT** | **1 polished multi-file C project on GitHub** |

---

## 🎯 PHASE 1 EXIT CRITERIA (Must Pass by June 30)

Before starting STM32 in July, you MUST be able to:

```
□ Write a linked list (insert, delete, search, reverse) from scratch in < 30 min
□ Write a circular buffer with read/write/isFull/isEmpty from scratch
□ Implement a state machine using enum + function pointers
□ Write a Makefile for a 5-file project with proper dependencies
□ Debug a segfault using GDB (breakpoints, backtrace, print) without AI
□ Draw the memory layout (text, data, BSS, heap, stack) of any C program on paper
□ Explain: volatile, const, static, extern, typedef, struct padding
□ Explain: stack vs heap, dangling pointer, memory leak, buffer overflow
□ Write a multi-file project with proper .h/.c separation and include guards
□ Answer 15 C interview questions on a whiteboard (no computer)
```

**If any answer is NO → you need 1 more week of C before starting STM32.**

---

## 📅 WEEKLY BREAKDOWN — SEE SEPARATE FILES

> **📚 RESOURCE GUIDE**: See **`10_RESOURCES.md`** for the complete list of books, YouTube playlists, practice platforms, and tools.

| File | Dates | Topic |
|:---|:---|:---|
| **`11A_JUNE_WEEK1.md`** | Jun 1-8 (Mon-Sun) | Makefiles + GDB + Multi-file projects + Compilation pipeline |
| **`11B_JUNE_WEEK2.md`** | Jun 9-15 (Mon-Sun) | Dynamic memory deep + Linked lists + Queues + Circular buffer |
| **`11C_JUNE_WEEK3.md`** | Jun 16-22 (Mon-Sun) | State machines + Advanced C patterns + Memory layout |
| **`11D_JUNE_WEEK4.md`** | Jun 23-30 (Mon-Tue) | Phase 1 CAPSTONE project + Month test + STM32 prep |

---

## 🔑 JUNE MINDSET

> **May was about learning C syntax. June is about MASTERING C patterns.**
>
> In May, you learned what a pointer is. In June, you'll build a linked list with pointers.
> In May, you learned what a struct is. In June, you'll simulate STM32 registers with structs.
> In May, you compiled with `gcc`. In June, you'll write Makefiles and debug with GDB.
>
> **June is where boys become engineers. Don't slack off just because you "already know C."**

---

> **Print this page. June 1st, 5:00 AM. Makefile from scratch. Let's go.**
