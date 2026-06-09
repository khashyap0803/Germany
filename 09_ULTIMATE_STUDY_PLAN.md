# ULTIMATE STUDY PLAN — Phase-by-Phase Detailed Schedule

> **Real Start Date**: June 9, 2026
> **Target**: Winter 2028 Germany Admission + Embedded Systems Mastery
> **Strategy**: Type 3 "AI Supervisor Engineer" — learn manually first, then AI-accelerate
> **Last Updated**: June 8, 2026 — Full rewrite: gym 5:30 AM, June 9 start, bond Oct 2027
>
> Note: Original plan started May 1. Actual start is June 9 (5.5 weeks later).
> All phase dates shifted accordingly. Winter 2028 target is still achievable.

---

## DAILY TIME BUDGET

### Weekday Template (Mon–Fri)

| Time | Duration | Block | Type |
|:---|:---|:---|:---|
| **5:00–5:25 AM** | 25 min | **PRE-GYM READING** — K.N. King / Mastering STM32 on tablet | Active reading |
| **5:30–6:30 AM** | 60 min | **GYM** | Gym (mandatory) |
| **6:30–7:00 AM** | 30 min | Shower + breakfast | Recovery |
| **7:00–8:30 AM** | 90 min | **COMMUTE IN** | German audio (Nicos Weg) |
| **12:30–12:45 PM** | 15 min | **LUNCH ANKI** | German flashcards |
| **6:30–8:30 PM** | 120 min | **COMMUTE BACK** | German audio (Easy German) |
| **9:30–10:00 PM** | 30 min | **BED READING** — theory only | Active reading |
| **10:00 PM** | — | SLEEP (7 hours) | Non-negotiable |

**Weekday active study: ~1.2 hrs (reading + Anki) + ~3.5 hrs passive audio**
**Weekday coding: ZERO — all coding happens on weekends only**

### Weekend Template

| Time | Duration | Block |
|:---|:---|:---|
| **5:30–6:30 AM** | 60 min | GYM |
| **6:30–7:30 AM** | 60 min | Shower + breakfast + prep |
| **Saturday 7:30 AM–12:30 PM** | 5 hrs | EMBEDDED DEEP CODING |
| **Saturday 1:30–4:30 PM** | 3 hrs | GERMAN (grammar + writing) |
| **Saturday 5:00–6:30 PM** | 1.5 hrs | GERMAN SPEAKING (AI/italki) |
| **Sunday 7:30–10:30 AM** | 3 hrs | EMBEDDED PROJECTS (hands-on) |
| **Sunday 12:00–2:00 PM** | 2 hrs | GERMAN (review + Anki bulk) |
| **Sunday 2:00–4:00 PM** | 2 hrs | IELTS prep (from Apr 2027) / Project work (before) |

**Weekend total: 9.5 hrs (Saturday) + 7 hrs (Sunday) = 16.5 hrs active**

### Weekly Total

| Source | Hours/Week | Type |
|:---|:---|:---|
| Pre-gym reading (5 × 25 min) | 2.1 hrs | Active |
| Bed reading (5 × 30 min) | 2.5 hrs | Active |
| Lunch Anki (5 × 15 min) | 1.25 hrs | Active |
| German commute audio | 17.5 hrs | Passive |
| Saturday | 9.5 hrs | Active |
| Sunday | 7 hrs | Active |
| **TOTAL ACTIVE** | **~22 hrs/week** | |
| **+ PASSIVE AUDIO** | **~17.5 hrs/week** | Bonus |

> The key insight: weekday mornings are now reading-only (no laptop/coding). All hands-on embedded work is concentrated on weekends. By Friday each week, you will have read the theory 5 times — Saturday coding becomes execution of what you already understand deeply.

---

## SUBJECT SPLIT RULES

### 60/20/20 Rule (Phases 1–4, Jun 2026–Aug 2027)

| Subject | % of Time | Allocation |
|:---|:---|:---|
| Embedded Systems (C → STM32 → RTOS → Linux) | **60%** | ~13 hrs/week |
| German Language | **20%** | ~4.5 hrs/week active + all commute passive |
| IELTS / Portfolio (from Apr 2027) | **20%** | ~4.5 hrs/week |

### 40/30/30 Rule (Phase 5, Aug–Dec 2027)

| Subject | % of Time |
|:---|:---|
| Embedded (VHDL + portfolio polish) | **40%** |
| German (B2 push) | **30%** |
| IELTS (Oct exam) | **30%** |

### 20/40/40 Rule (Phase 6, Jan–Oct 2028)

| Subject | % of Time |
|:---|:---|
| Embedded (portfolio maintenance) | **20%** |
| German (B2 exam + immersion) | **40%** |
| Applications (SOP, docs, uni applications) | **40%** |

---

## WEEKDAY THEORY ROTATION (Phases 1–4)

| Day | Pre-Gym Reading (5:00–5:25 AM) | Commute Audio | Bed Reading (9:30–10:00 PM) |
|:---|:---|:---|:---|
| **Mon** | K.N. King — current chapter | Nicos Weg A1/A2/B1 | K&R same topic |
| **Tue** | Mastering STM32 — preview material | DW Podcast | K.N. King — review |
| **Wed** | German grammar notes / offline lesson | Easy German | K&R reference |
| **Thu** | K.N. King — next chapter | Nicos Weg | Mastering STM32 hardware |
| **Fri** | Re-read hardest concept of the week | DW + Easy German | K&R or Elecia White |

---

---

# PHASE 1: C PROGRAMMING FOUNDATION

## June 9 – August 24, 2026 (11 weeks)

> **AI BANNED for code in Phases 1–2.** Write every line manually. AI may only explain concepts.
> Start Date: June 9, 2026. End Date: August 24, 2026 (Phase 2 starts Aug 25).

**Goal**: Write C programs confidently without AI. Understand memory, pointers, bitwise operations, state machines, makefiles, and GDB.

**Primary Book**: K.N. King "C Programming: A Modern Approach" 2nd Ed (read before coding)
**Reference**: K&R "The C Programming Language" 2nd Ed (bed reading nightly)
**Video Primary**: FastBit "Embedded C Programming" at 1.5× (after reading King)
**Video Supplement**: Neso Academy YouTube (7–12 min concept shots)
**Hardware**: PC with WSL2 + gcc + gdb (no microcontroller in Phase 1)

**Pipeline**: Read King → Do exercises → Watch FastBit → Code yourself → EXPLAIN out loud → GDB debug

---

### Phase 1 Week 1 (Jun 9–15): Setup + C Basics

**Pre-week setup (Jun 9 morning)**:
- WSL2 + gcc + gdb installed and working
- GitHub "C-Practice" repo created (public)
- AnkiDroid installed + German A1 deck downloaded
- DW Nicos Weg app installed on phone

| Day | Pre-Gym Reading (5:00–5:25 AM) | Weekend Coding Block |
|:---|:---|:---|
| **Tue Jun 9** | K.N. King Ch 1 (Introducing C) | — |
| **Wed Jun 10** | K.N. King Ch 2 (C Fundamentals) | — |
| **Thu Jun 11** | K.N. King Ch 3 (Formatted I/O) | — |
| **Fri Jun 12** | K.N. King Ch 4–5 (Expressions, Selection) | — |
| **Sat Jun 13** | — | **7:30–12:30 PM: Write 12+ programs**: hello.c, variables.c, all data types, printf formatting, scanf input, operators, conditions (if/else/switch), loops (for/while/do-while), nested loops, patterns, basic functions |
| **Sun Jun 14** | — | **7:30–10:30 AM**: Arrays — max/min/avg, bubble sort, search. Git push. |
| **Mon Jun 15** | K.N. King Ch 6 (Loops) review | — |

**Week 1 Checkpoint:**
- [ ] WSL2 + gcc working, can compile and run
- [ ] 12+ programs written from scratch
- [ ] Variables, operators, conditions, loops, arrays: comfortable
- [ ] GitHub C-Practice: first commit pushed
- [ ] Nicos Weg: lessons 1–5 done (commute)
- [ ] Anki: 20+ German words

---

### Phase 1 Week 2 (Jun 16–22): Functions Deep + Arrays + Strings

**Reading (pre-gym + bed)**: K.N. King Ch 7–10 (Functions, Arrays, Strings)

| Day | Pre-Gym Reading | Weekend Coding |
|:---|:---|:---|
| **Tue Jun 16** | K.N. King Ch 7 (Functions) | — |
| **Wed Jun 17** | K.N. King Ch 8 (Arrays) | — |
| **Thu Jun 18** | K.N. King Ch 9 (Functions of sorts) | — |
| **Fri Jun 19** | K.N. King Ch 10 (Strings) | — |
| **Sat Jun 20** | — | **7:30–12:30 PM**: Write 10+ programs — my_strlen(), my_strcpy(), my_strcmp(), my_strrev(), bubble sort, selection sort, binary search, 2D matrix operations, multi-file compilation (math_ops.h + math_ops.c + main.c) |
| **Sun Jun 21** | — | **7:30–10:30 AM**: Student Record System — 5 students, parallel arrays, menu-driven. GDB: compile with -g, set breakpoints, step through. |
| **Mon Jun 22** | Nicos Weg lesson review | — |

**Week 2 Checkpoint:**
- [ ] Can write string manipulation functions WITHOUT library
- [ ] Multi-file compilation (.h + .c separation) understood
- [ ] Student Record System working and GDB-debugged
- [ ] Bubble sort, binary search writable from memory
- [ ] Nicos Weg: lessons 6–10 done

---

### Phase 1 Week 3 (Jun 23–29): POINTERS — Most Important Week

> CRITICAL. If pointers are not understood deeply, everything in embedded will be impossible.
> Draw every memory diagram on paper. Print addresses. Visualize where data lives.

**Primary videos**: mycodeschool "Pointers in C/C++" playlist — ALL 15 VIDEOS
**Reading**: K.N. King Ch 11–12 (Pointers, Dynamic Allocation)

**Video schedule (watch during pre-gym reading time OR in the evening after dinner)**:
- Day 1 (Tue): mycodeschool #1 "Introduction" + #2 "Working with pointers"
- Day 2 (Wed): mycodeschool #3 "Pointer types, void pointers" + German day
- Day 3 (Thu): mycodeschool #4 "Pointers to Pointers" + #5 "As function arguments"
- Day 4 (Fri): mycodeschool #6 "Pointers and arrays" + #7 "Arrays as function arguments"
- Day 5 (Sat): mycodeschool #8 "Character arrays" + #9–#11 "Dynamic memory"
- Day 6 (Sun): mycodeschool #12–#14 "Function pointers, callbacks, returns"
- Day 7 (Mon): mycodeschool #15 "Memory leak" + review

| Sat Jun 27 | **7:30–12:30 PM**: Pointers all levels |
|:---|:---|
| | Program 1: pointer_basics.c — &x, *p, print address, sizeof, pointer arithmetic |
| | Program 2: swap.c — swap_wrong(a,b) vs swap_correct(*a,*b) — draw before/after diagram |
| | Program 3: double_pointer.c — int **pp chain |
| | Program 4: dynamic_array.c — malloc(N), check NULL, fill, free |
| | Program 5: realloc_demo.c — grow array with realloc |
| | Program 6: circular_buffer.c — head/tail/count, wrap-around — THIS GOES ON STM32 LATER |
| | Program 7: function_pointers.c — int (*op)(int,int) callback pattern |

| Sun Jun 28 | **7:30–10:30 AM**: Pointer memory test |
|:---|:---|
| | Close ALL references. From memory: write swap.c, circular_buffer.c, malloc_demo.c |
| | Write pointer_interview_answers.c: 8 Q&A verbally explained |

**Week 3 Checkpoint:**
- [ ] mycodeschool: ALL 15 videos watched
- [ ] Can explain pointers on paper with full memory diagram
- [ ] swap() written from memory
- [ ] circular_buffer.c working (will use on STM32)
- [ ] malloc/free understood, Valgrind clean
- [ ] Function pointers understood
- [ ] Pointer confidence self-rating: _/10 (must be ≥7 before continuing)

---

### Phase 1 Week 4 (Jun 30 – Jul 6): Structs + Bitwise → STM32 Bridge

**Reading**: K.N. King Ch 13–14 (Structures, Unions) + Ch 20 (Bitwise Operations)

**Wednesday Jun 30 (Day 1 only — rest continues in July)**:
- Pre-gym: K.N. King Ch 13 (Structures intro)
- This day starts the structs section

**The embedded connection**: structs = STM32 peripheral register layouts. Bitwise = reading/writing individual bits. This is EXACTLY what STM32 code looks like.

See `12A_JULY_WEEK1.md` for the full Week 4 schedule (July 1–7).

---

---

# PHASE 2: STM32 MICROCONTROLLER PROGRAMMING

## August 25 – November 23, 2026 (13 weeks)

> **AI BANNED for code in Phase 2.** Write every driver manually. AI may only explain concepts.
> Start Date: August 25, 2026.

**Goal**: GPIO, UART, Timers, Interrupts, ADC, SPI, I2C on real STM32 hardware. Both HAL AND register-level.

**Primary Book**: "Mastering STM32" by Carmine Noviello 2nd ed (910 pages)
**Primary Course**: FastBit MCU1 "Mastering MCU Driver Development" (28.5h)
**Secondary Course**: FastBit MCU2 "Timers/PWM/CAN" (29h) — starts Sep 2026
**Reference**: RM0383 STM32F411 Reference Manual (1700+ pages — dictionary, not cover-to-cover)
**Hardware**: STM32F411 Black Pill + Nucleo-L476RG + Robocraze ST-Link V2 + Sipeed SLogic

**Pipeline for EVERY peripheral**:
1. FastBit MCU1 video → watch the section
2. "Mastering STM32" → read the chapter
3. HAL implementation → understand every generated line
4. Register-level implementation → same thing using only registers
5. Reference Manual → verify your understanding of each register bit
6. GDB → step through code, inspect actual register values

---

### Phase 2 Weeks 1–2 (Aug 25 – Sep 7): STM32 Setup + GPIO + ARM Architecture

- Install STM32CubeIDE + first project for STM32F411
- ARM Cortex-M4 architecture: bus interfaces (AHB/APB1/APB2), vector table, boot sequence
- GPIO: modes (output push-pull, open-drain, input floating/pull-up/pull-down, alternate function)
- GPIO: MODER, OTYPER, OSPEEDR, PUPDR, IDR, ODR, BSRR, LCKR, AFR registers
- LED blink via HAL, then via register-level (RCC → GPIO → BSRR)
- Button input (HAL + register) with debouncing
- Multi-LED patterns (Knight Rider)

### Phase 2 Weeks 3–4 (Sep 8–21): UART (Theory + HAL + Register)

- UART frame format: start bit, 8 data bits, stop bit, parity
- Baud rate register (BRR) calculation: BRR = fCLK / baud
- UART via HAL: "Hello World" to PC serial terminal (Tera Term, 115200 baud)
- UART receive: echo back, command menu (LED ON/OFF/STATUS)
- Printf redirect (retarget `_write()` syscall) — use printf for STM32 debugging
- UART register-level: RCC enable → GPIO AF config (PA2/PA3, AF7) → BRR → CR1 → UE
- Logic analyzer: capture real UART waveform, verify baud rate

### Phase 2 Weeks 5–7 (Sep 22 – Oct 12): Timers + Interrupts + NVIC

- SysTick timer: non-blocking delays using HAL_GetTick()
- Hardware timers (TIM2): prescaler + ARR calculation, exact 1-second period
- Timer interrupt ISR: toggle LED at exact frequency
- NVIC: priorities (0 = highest), preemption, ISR rules
- External interrupts (EXTI): button debounce via interrupt
- UART interrupt RX: non-blocking receive into circular buffer (reuse from Phase 1!)
- Non-blocking multi-task pattern (no RTOS): multiple timers in main loop

### Phase 2 Weeks 8–9 (Oct 13–26): ADC + PWM + DMA

- ADC: resolution, sampling time, channels, HAL + register
- ADC continuous with DMA transfer (no CPU overhead)
- PWM: duty cycle calculation, LED dimming, ADC → PWM feedback
- SPI + I2C theory (preparation for sensor use)

### Phase 2 Weeks 10–13 (Oct 27 – Nov 23): PORTFOLIO PROJECT 1 + SPI/I2C

**PORTFOLIO PROJECT 1: "STM32 Environmental Monitor"**

- STM32F411 + BMP280 (I2C) or ADC potentiometer (simulated)
- Timer-based periodic sampling (1 second)
- Circular buffer from Phase 1 (unchanged — reuse it!)
- UART output: CSV format → PC can log data
- LED status indicators (mode, error, running)
- Button to change display mode
- Full documentation on GitHub: README + circuit diagram + demo video + what you learned

**SPI + I2C with Sipeed SLogic**:
- Capture actual SPI/I2C waveforms in PulseView
- Match what you see on the screen with what you coded
- This is real engineering debugging

**Deload Week 2: Last week of November** — review Phase 2, plan Phase 3

**Phase 2 Checkpoint — November 23:**
- [ ] GPIO, UART, Timers, Interrupts, ADC on STM32 — working and fully understood
- [ ] Both HAL and register-level implementations done
- [ ] Portfolio Project 1 on GitHub with full documentation
- [ ] Can explain each topic in an interview without preparation
- [ ] German A2 complete, B1 started
- [ ] Deload week done, ready for Phase 3

---

---

# PHASE 3: FreeRTOS + ZEPHYR RTOS

## November 24, 2026 – February 8, 2027 (11 weeks)

> **AI SUPERVISED from Phase 3.** AI generates boilerplate → YOU review, explain, verify every line.
> Start Date: November 24, 2026.

**Goal**: FreeRTOS on STM32. Zephyr RTOS. SPI/I2C mastery.
**FreeRTOS Course**: FastBit "FreeRTOS with STM32Fx" (14h) — buy Sep 2026
**FreeRTOS Book**: "Mastering the FreeRTOS Real Time Kernel" by Richard Barry (304 pages)
**Zephyr Course**: FastBit "Mastering Zephyr RTOS with DeviceTree" (9h) — already purchased

### Nov–Dec 2026: FreeRTOS Core (Weeks 1–5)

| Week | Topic | Hands-On |
|:---|:---|:---|
| 1 | Tasks: creation, states, priorities | 2 tasks: one blinks LED, one prints to UART |
| 2 | Queues: inter-task communication | ADC task → queue → UART print task |
| 3 | Semaphores: binary + counting | Button ISR → semaphore → processing task |
| 4 | Mutexes: shared resource protection | Two tasks sharing UART, protected by mutex |
| 5 | Priority inversion, watchdog, stack overflow | Understanding and preventing RTOS pitfalls |

### Jan 2027: Zephyr RTOS (Weeks 6–7)

- FastBit Zephyr course (9h at 1.5×)
- Zephyr toolchain setup on WSL2
- Port Blinky to STM32F411 Black Pill in Zephyr (from scratch, not copied from samples)
- Write DeviceTree for your board yourself
- Compare FreeRTOS vs Zephyr: same project, two different RTOS implementations

### Jan–Feb 2027: PORTFOLIO PROJECT 2 (Weeks 8–11)

**PORTFOLIO PROJECT 2: "FreeRTOS Multi-Sensor Dashboard"**

- 3 FreeRTOS tasks: sensor reading (I2C BMP280 or ADC), data processing (moving average filter), UART output (formatted table)
- Queue: sensor → processing → output pipeline
- Mutex: UART resource shared safely between tasks
- Timer task: periodic sampling at configurable rate
- **Bonus branch**: Re-implement core in Zephyr (two GitHub branches: freertos-main + zephyr-port)
- Full GitHub documentation

**Deload Week 3: Last week of February** — review Phase 3, plan Phase 4

**Phase 3 Checkpoint — February 8:**
- [ ] FreeRTOS: tasks, queues, semaphores, mutexes — working on real hardware
- [ ] Zephyr: Blinky + one sensor app on STM32
- [ ] Portfolio Project 2 on GitHub with both FreeRTOS and Zephyr branches
- [ ] Can explain every RTOS concept in an interview
- [ ] German B1 started

---

---

# PHASE 4: PROTOCOLS + LINUX + IoT

## February 9 – August 9, 2027 (26 weeks)

> **AI PARTNER from Phase 4.** Use AI like a senior engineer — generate, review, test, sign off.
> Start Date: February 9, 2027.

### Feb–Apr 2027: Protocols + ESP32 (Weeks 1–9)
- CAN bus: theory + implementation (if hardware available)
- RS485 multi-device UART communication
- ESP32-S3 N8R2: ESP-IDF setup, WiFi connection, MQTT basics
- Old Core 2 Duo PC: Linux From Scratch project starts

### Apr–Jun 2027: Linux Deep (Weeks 10–18)
- "Linux 100+ hours" Udemy course begins (Apr)
- Linux CLI mastery: WSL2 + Fedora VM + openSUSE VM
- Shell scripting (bash)
- Cross-compilation basics
- Linux device drivers (LDD3 book — Chapters 1–5)
- IELTS diagnostic test (April)

### Jun–Aug 2027: Portfolio Project 3 (Weeks 19–26)

**PORTFOLIO PROJECT 3: "ESP32 IoT Sensor Node"**
- ESP32-S3 + WiFi + MQTT + BMP280 + OLED display
- AI-accelerated: Claude/Copilot generates 60% → YOU verify, debug, sign off on 100%
- Cloud integration (MQTT broker → dashboard)
- Full GitHub documentation

**Deload Week 4: Last week of May** — Phase 4 midpoint recharge

**Phase 4 Checkpoint — August 9:**
- [ ] 3 portfolio projects on GitHub
- [ ] Linux command line confident
- [ ] German B1 → B2 bridge started
- [ ] IELTS prep foundation started

---

---

# PHASE 5: VHDL + IELTS INTENSIVE

## August 10, 2027 – February 8, 2028 (26 weeks)

> Start Date: August 10, 2027.
> Bond expires October 2027 — resign at expiry, free from January 2028.

### Aug–Sep 2027: IELTS INTENSIVE (VHDL paused) + APS Application
> ⚠️ **De-confliction**: These two months are IELTS-FIRST. VHDL heavy work is moved to AFTER the exam (Oct+). German drops to Anki-only. See `04_IELTS_PREP.md` for the full rule.
- **IELTS intensive** = #1 priority (full mock every weekend, 3-4 essays/week)
- VHDL = light reading only (syntax overview, no heavy projects yet)
- **Apply for APS Certificate** (August 2027 — paperwork, doesn't compete for study hours)

### Oct 2027: IELTS EXAM + DIGITAL LOGIC BRIDGE + BOND EXPIRY + RESIGN
- **TAKE IELTS EXAM** (target: 7.0 overall, minimum 6.5 in each section)
- After exam: **Digital Logic Bridge** (~2-3 weekends) — prerequisite for VHDL. See `15_FUNDAMENTALS_BRIDGE.md`
- **Bond expires ~October 2027** → **Submit resignation** at Unistring
- APS certificate should arrive (applied Aug, 3–4 weeks processing)

### Nov 2027 – Feb 2028: VHDL HEAVY WORK + Project 4
- VHDL syntax + simulation (GHDL or ModelSim)
- Counter, FSM, simple ALU designs (digital logic bridge makes this click)
- **Portfolio Project 4**: VHDL design + KiCad/Flux PCB
- From Jan 2028 (last working day done) you have free daytime hours — VHDL + applications accelerate

### Nov–Dec 2027: Applications Begin
- Goethe A1/A2 exam (for Bremerhaven certification)
- Write motivation letter drafts
- Create Europass CV
- **Submit Bremerhaven application** (deadline Dec 31, 2027)

**Portfolio Project 4**:
- VHDL design (counter + FSM) + KiCad/Flux AI PCB design
- GitHub documentation

**Deload Week 6: Last week of October** — post-IELTS + resignation week

**Phase 5 Checkpoint — February 8:**
- [ ] 4 portfolio projects on GitHub
- [ ] IELTS 7.0 achieved (or retake Dec 2027 / Jan 2028)
- [ ] APS certificate in hand
- [ ] German B2 level achieved
- [ ] Goethe A1/A2 certificate in hand
- [ ] Bremerhaven Summer 2028 application submitted
- [ ] LAST WORKING DAY ~January 2028

---

---

# PHASE 6: APPLICATIONS + FINAL PREP

## February 2028 – October 2028 (9 months free)

> Bond expired Oct 2027. Resigned. Last working day ~January 2028. FULLY FREE now.

### Jan 2028
- Submit remaining Summer 2028 applications (deadline ~Jan 15)
- **Take Goethe B2 exam**
- Get Arbeitszeugnis from Unistring

### Feb–Mar 2028
- Prepare all Winter 2028 application documents
- Portfolio polish
- Summer 2028 results may start arriving

### Apr 2028
- **Submit RWU application** (Winter 2028, deadline Apr 15)
- Pre-check email to Dortmund: service-esm@fh-dortmund.de
- Post-grad experience: Jul 2026 → Apr 2028 = ~21 months

### May–Jul 2028
- **Submit Winter 2028 applications** (Dortmund, FH Westküste, HAW Hamburg, others)
- Open blocked account (Expatrio / Fintiba)
- Deposit €11,904 into blocked account
- Get health insurance (incoming student plan)
- German B2 immersion (full-time now, no work)
- Final GitHub portfolio polish

### Aug–Sep 2028
- Accept admission offer
- VFS visa appointment
- Receive student visa
- Book flight, arrange housing

### October 2028
# FLY TO GERMANY. START WINTER SEMESTER 2028.

---

---

## FULL OVERVIEW TABLE

| Month | Embedded Focus | AI Policy | German | IELTS | Key Milestone |
|:---|:---|:---|:---|:---|:---|
| **Jun 2026** | C basics: K.N. King Ch 1–10 | BANNED | Nicos Weg A1 start | — | WSL2+gcc, GitHub repo |
| **Jul 2026** | C deep: pointers, structs, bitwise, Makefiles, GDB | BANNED | Nicos Weg A1 | — | Circular buffer, HW register sim |
| **Aug 2026** | Phase 1 capstone → Phase 2 starts Aug 25 | BANNED | A1 complete → A2 | — | Phase 1 exit test passed |
| **Sep 2026** | STM32: GPIO + UART | BANNED | Nicos Weg A2 | — | LED + UART on real hardware |
| **Oct 2026** | STM32: Timers + Interrupts + ADC | BANNED | A2 continue | — | ADC + timer working |
| **Nov 2026** | Project 1 + Phase 3 starts Nov 24 | SUPERVISED | A2 → B1 start | — | GitHub Project 1 |
| **Dec 2026** | FreeRTOS: tasks, queues | SUPERVISED | B1 grammar | — | FreeRTOS multi-task |
| **Jan 2027** | Zephyr RTOS + protocols intro | SUPERVISED | B1 deep | — | Zephyr blinky |
| **Feb 2027** | Project 2 + Phase 4 starts Feb 9 | PARTNER | B1 complete | — | GitHub Project 2 |
| **Mar 2027** | ESP32 + CAN/RS485 | PARTNER | B1→B2 bridge | — | ESP32 WiFi |
| **Apr 2027** | Linux CLI + shell scripting | PARTNER | B2 course | IELTS diagnostic | Linux confident |
| **May 2027** | Linux device drivers + Project 3 | PARTNER | B2 grammar | Foundation | GitHub Project 3 |
| **Jun 2027** | Linux deep + cross-compilation | PARTNER | B2 writing | Practice | LDD3 Chs 1–5 |
| **Jul 2027** | VHDL basics start | PARTNER | B2 speaking | Mock tests | VHDL counter/FSM |
| **Aug 2027** | ⚠️ MAINTENANCE (IELTS priority) | PARTNER | MAINTENANCE (Anki only) | **INTENSIVE — #1 priority** | APS applied |
| **Sep 2027** | ⚠️ MAINTENANCE (IELTS priority) | PARTNER | MAINTENANCE (Anki only) | **INTENSIVE — #1 priority** | APS received |
| **Oct 2027** | Portfolio polish | PARTNER | B2 continue | **IELTS EXAM** | Bond expires, resign |
| **Nov 2027** | — | PARTNER | Goethe A1/A2 | Results | Bremerhaven app prep |
| **Dec 2027** | — | PARTNER | B2 practice | — | **Bremerhaven app submitted** |
| **Jan 2028** | — | — | **Goethe B2 exam** | — | Last working day |
| **Feb–Apr 2028** | Portfolio maintenance | — | B2 immersion | — | RWU app, Winter prep |
| **May–Jul 2028** | Final polish | — | B2 immersion | — | All Winter apps submitted |
| **Oct 2028** | — | — | — | — | **FLY TO GERMANY** |

---

## THE AI STRATEGY: TYPE 3 ENGINEER

```
TYPE 1 — "Code Monkey" (DYING by 2028)
    Follows tutorials. Can't explain WHY the code works.
    AI replaces 80% of this role.

TYPE 2 — "Traditional Engineer" (SHRINKING)
    Understands hardware + software deeply.
    Refuses to use AI tools.
    2× slower than Type 3.

TYPE 3 — "AI Supervisor Engineer" (YOUR TARGET) ← GROWING
    Understands hardware + software deeply (Phase 1-2 foundation).
    USES AI to generate 80% of boilerplate (Phase 3+).
    VERIFIES every line because they understand fundamentals.
    DEBUGS what AI can't (hardware, timing, race conditions).
    SIGNS safety certifications (legally required human).
    5× more productive than Type 2 → highest salary tier.
```

**Phase 1–2 (Jun–Nov 2026)**: Build foundation WITHOUT AI. Every line is yours.
**Phase 3+ (Nov 2026+)**: USE AI to accelerate. You verify, debug, sign off.
**2028+**: You supervise AI output like a senior engineer.

---

## THE ONE RULE THAT MAKES THIS WORK

> Never break the chain. Every single day: minimum 1 active task.
>
> Sick? → Do 15 min of Anki from bed.
> Exhausted? → Read 10 pages of K.N. King.
> Travel? → German audio on phone.
> Festival? → 30 min pre-gym reading.
> Really can't? → See Contingency Protocols in `00_MASTER_ROADMAP.md`.
>
> Consistency beats intensity. 22 hrs/week × 100 weeks = 2,200 active hours.
> Combined with 17 hrs/week passive audio: more than enough for Germany.

---

## COURSE LIBRARY (All Purchased)

| # | Course | Hours | Phase |
|:---|:---|:---|:---|
| 1 | FastBit Embedded C Programming | 16.5h | Phase 1 (Jun 2026) |
| 2 | FastBit MCU Driver Development (MCU1) | 28.5h | Phase 2 (Aug 2026) |
| 3 | FastBit Timers/PWM/CAN (MCU2) | 29h | Phase 2–3 (Sep–Dec 2026) |
| 4 | FastBit Zephyr RTOS | 9h | Phase 3 (Jan 2027) |
| 5 | Linux 100+ hours | 100h+ | Phase 4 (Apr 2027) |
| **Buy Jun 2026** | FastBit ARM Cortex-M3/M4 | 15h | Phase 2 (Aug 2026) |
| **Buy Sep 2026** | FastBit FreeRTOS | 14h | Phase 3 (Nov 2026) |

See `10_RESOURCES.md` for complete book library (14 books, ~7,500 pages).
