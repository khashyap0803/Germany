# AUGUST WEEK 2 (Aug 4–10) — Phase 1 Week 9: CAPSTONE PROJECT

> **Topics**: Full embedded system simulator in C — combines state machine, circular buffer, linked list, file I/O, Makefile, multi-file architecture, bit macros, logger, dynamic memory
> **K.N. King Reading**: Chapter 17 review (linked lists) + Chapter 22 (I/O review)
> **K&R Bed Reading**: Chapter 5 revisit (Pointers) — re-read as experienced programmer
> **AI Policy**: BANNED — you write every line of this capstone yourself
> **Dates**: Tuesday August 4 → Monday August 10, 2026

---

## WEEKDAY READING SCHEDULE (Aug 4–8)

### Tuesday August 4 — Pre-Gym (5:00–5:25 AM)
**Read**: K.N. King Chapter 17 (review — linked lists + function pointers, pages 1–25)
- Re-read with fresh eyes after implementing linked lists in Week 7
- Focus on: the double pointer pattern, ordered list insertion, function pointer callbacks

**Bed Reading (9:30–10:00 PM)**: K&R Chapter 5 pages 93–130 — re-read with your current knowledge. What makes sense now that didn't before?

### Wednesday August 5 — Pre-Gym (5:00–5:25 AM)
**Read**: K.N. King Chapter 22 (I/O review — pages 1–25)
- Re-read file I/O — anything that wasn't clear in Week 5
- Focus on: fseek, ftell, rewind, fflush — when you actually need them

**Bed Reading**: K&R Chapter 5 pages 130–167 (Pointer arrays, multi-dimensional arrays, complex declarations)

### Thursday August 6 — Pre-Gym (5:00–5:25 AM)
**Read**: Review your own Week 4–8 code (not a book — review your own GitHub files)
- Re-read your GPIO simulator, your logger, your state machine, your circular buffer
- Ask: is the code clean? Are the header guards correct? Is every malloc free'd?
- Note anything you'd do differently now

**Bed Reading**: K.N. King Chapter 17 pages 25–end (re-read)

### Friday August 7 — Pre-Gym (5:00–5:25 AM)
**Read**: Plan the capstone project architecture on paper (see CAPSTONE DESIGN below)
- Draw the module diagram: boxes = .c files, arrows = which modules include which headers
- List every function in every module (just the names)
- Write the Makefile header (CC, CFLAGS, SRCS, OBJS) mentally

**Bed Reading**: K&R Chapter 5 — re-read final section (complex declarations)

### Monday August 10 — Pre-Gym (5:00–5:25 AM)
**Read**: Skim "Mastering STM32" Chapter 1 (Introduction) — PREVIEW ONLY
- Get the big picture: what is STM32, what is HAL, what is CMSIS, what is CubeMX
- Do NOT start studying yet — just get a sense of what Phase 2 involves
- Bed Reading: K&R Chapter 1 (A Tutorial Introduction) — re-read as an experienced C programmer

---

## CAPSTONE DESIGN — READ THIS BEFORE SATURDAY

### Project: Embedded System Simulator

Build a complete multi-module C project that simulates a sensor monitoring system. This is not a toy — it has real architecture, real separation of concerns, and runs clean under Valgrind.

```
week9/sensor_sim/
├── Makefile
├── config.h              — All constants (#define SAMPLE_RATE_HZ, ALARM_THRESHOLD, etc.)
├── bit_macros.h          — Your bit macros from Week 4
├── cbuf.h + cbuf.c       — Circular buffer from Week 7
├── gpio_sim.h + gpio_sim.c — GPIO simulation from Week 4 (reuse or rewrite from memory)
├── sensor.h + sensor.c   — Simulated sensor: random ADC values 0–4095
├── logger.h + logger.c   — File logger from Week 5 (reuse or rewrite from memory)
├── sm.h + sm.c           — State machine from Week 8 (reuse or rewrite from memory)
└── main.c                — Main loop: init, run, shutdown
```

### System behavior:

1. **States** (state machine in `sm.c`):
   - INIT: set up all modules, print "System initializing..."
   - CALIBRATE: read 10 sensor samples, calculate baseline average
   - RUNNING: every "tick", read sensor → write to cbuf → check threshold → log if alarm
   - ALARM: log "ALARM: sensor reading = X", toggle error LED, auto-recover after 3 ticks
   - SHUTDOWN: flush cbuf remaining data to log file, close log, print "System shutdown."

2. **Sensor** (`sensor.c`):
   - `sensor_init()`: seed random number generator
   - `int sensor_read()`: return rand() % 4096 (simulates 12-bit ADC)
   - After calibration, occasionally inject a spike: if (rand() % 20 == 0) return 4095

3. **GPIO simulation** (`gpio_sim.c`):
   - Status LED (pin 5): ON when RUNNING
   - Error LED (pin 6): ON when in ALARM state
   - Heartbeat LED (pin 7): TOGGLE every tick in RUNNING state

4. **Logger** (`logger.c`):
   - `logger_init("sim_log.txt")`: open file for writing
   - `logger_write(level, message)`: write `[TIMESTAMP][LEVEL] message`
   - `logger_close()`: flush and close file
   - Levels: LOG_INFO, LOG_WARNING, LOG_ERROR

5. **Config** (`config.h`):
```c
#define SAMPLE_COUNT      100    // how many ticks to simulate
#define ALARM_THRESHOLD   3500   // sensor values above this trigger ALARM
#define CBUF_CAPACITY     32     // circular buffer size
#define CALIBRATION_SAMPLES 10   // samples for baseline
```

### What the output should look like:
```
System initializing...
Calibrating... (10 samples, baseline = 2048)
[tick  1] reading=1923  status=RUNNING
[tick  2] reading=2341  status=RUNNING
...
[tick 17] reading=4095  status=ALARM *** THRESHOLD EXCEEDED ***
[tick 18] reading=1842  status=ALARM (recovering 2/3)
[tick 19] reading=2100  status=ALARM (recovering 3/3)
[tick 20] reading=1950  status=RUNNING (recovered)
...
[tick 100] reading=2200  status=RUNNING
Shutdown: flushing 15 buffered samples to log...
System shutdown. See sim_log.txt for full log.
```

---

## SATURDAY AUGUST 8 — CAPSTONE BUILD DAY 1 (7:30 AM–12:30 PM)

### Warmup (7:30–8:00 AM)
Review your capstone design notes from Friday. Draw the module dependency diagram one more time on paper (which .c files include which .h files). This is your architecture — do not change it mid-build.

### BLOCK 1 (8:00–9:30 AM): Scaffold + Makefile + Config
Create all files. Write headers first (declarations only), then config.h, then Makefile.

**Do not write any .c implementations yet** — just the structure:
```bash
mkdir -p week9/sensor_sim
cd week9/sensor_sim
touch Makefile config.h bit_macros.h
touch cbuf.h cbuf.c sensor.h sensor.c logger.h logger.c
touch gpio_sim.h gpio_sim.c sm.h sm.c main.c
```

Write all .h files first with proper include guards. Write Makefile. Write config.h. Verify `make` tries to compile (will fail — no implementations yet, but that's expected).

### BREAK (9:30–9:45)

### BLOCK 2 (9:45–11:15 AM): Core Modules
Implement `cbuf.c`, `sensor.c`, `gpio_sim.c` — these have no dependencies on each other.

Write each from scratch WITHOUT looking at previous weeks' code. This is the test:
- `cbuf.c`: circular buffer, all operations, use `uint8_t` internally
- `sensor.c`: init with `srand(time(NULL))`, `sensor_read()` returns rand() % 4096
- `gpio_sim.c`: GPIO register + bit macros, `gpio_write_pin`, `gpio_toggle_pin`, `gpio_print_state`

Compile each module individually to check for warnings: `gcc -Wall -Wextra -g -std=c99 -c cbuf.c -o cbuf.o`

### BREAK (11:15–11:30)

### BLOCK 3 (11:30 AM–12:30 PM): Logger + State Machine Skeleton
Implement `logger.c` (file I/O module) and write the state machine skeleton in `sm.c`:
- `logger.c`: static file pointer, log_init/log_write/log_close
- `sm.c`: define states enum, events enum, handler function signatures — leave handler bodies as stubs that just return the next state

### SATURDAY AFTERNOON — GERMAN (1:30–6:30 PM)
- Nicos Weg A2 Lesson 1 (start A2!)
- Practice: "Ich habe A1 Deutsch abgeschlossen." (I completed A1 German)
- Write 10 sentences about your past week in German (past tense)
- Anki: add 15 new cards
- ChatGPT Voice: 30 min A1/A2 conversation

---

## SUNDAY AUGUST 9 — CAPSTONE BUILD DAY 2 + GIT (7:30 AM–4:00 PM)

### BLOCK 1 (7:30–9:00 AM): Complete State Machine + Main Loop
Implement all 5 state handler functions in `sm.c`. Then write `main.c`:
```c
#include "config.h"
#include "cbuf.h"
#include "sensor.h"
#include "logger.h"
#include "gpio_sim.h"
#include "sm.h"

int main(void) {
    // Init all modules
    sensor_init();
    logger_init("sim_log.txt");
    gpio_sim_init();
    CircBuf cbuf;  cbuf_init(&cbuf);
    SystemState sm_state = SM_INIT;
    StateHandler handlers[] = { handle_init, handle_calibrate, handle_running,
                                  handle_alarm, handle_shutdown };

    // Main loop
    for (int tick = 0; tick < SAMPLE_COUNT && sm_state != SM_SHUTDOWN; tick++) {
        sm_state = handlers[sm_state](tick, &cbuf);
        gpio_sim_print_leds();  // print LED state each tick
    }

    // Force shutdown if didn't reach it naturally
    if (sm_state != SM_SHUTDOWN) {
        handle_shutdown(SAMPLE_COUNT, &cbuf);
    }

    logger_close();
    return 0;
}
```

### BLOCK 2 (9:15–10:30 AM): Debug + Valgrind
Run the program. Fix any compilation errors or logic bugs.

Debug checklist:
- [ ] Runs for exactly SAMPLE_COUNT ticks (or until SHUTDOWN)
- [ ] ALARM triggered when sensor_read() > ALARM_THRESHOLD
- [ ] State recovers to RUNNING after 3 ALARM ticks
- [ ] sim_log.txt created and has correct format
- [ ] `valgrind --leak-check=full ./sensor_sim` — 0 leaks, 0 errors
- [ ] `make clean && make` — rebuilds from scratch with 0 warnings

### GIT PUSH (10:30–11:00 AM)
```bash
cd ~/C-Practice
git add week9/
git commit -m "Week 9: Phase 1 capstone — sensor simulator, state machine, circular buffer, file logger, GPIO sim"
git push origin main
```

Write `week9/README.md`:
- Project description
- How to build and run
- What each module does
- Simulation → Real STM32 mapping table:

| Simulator (PC C code) | Real STM32 (Phase 2) |
|:---|:---|
| `printf()` | `HAL_UART_Transmit()` |
| `rand() % 4096` | `HAL_ADC_GetValue()` |
| `gpio_sim` bit operations | `GPIOA->BSRR`, `GPIOA->ODR` |
| `cbuf_write/read` | Same code! Runs on both PC and STM32 |
| `fopen("sim_log.txt")` | Flash write or SD card |
| `while(tick < 100)` | `while(1)` running forever on chip |

### REST + LUNCH (11:00 AM–12:00 PM)

### GERMAN (12:00–2:00 PM)
- Nicos Weg A2 Lessons 2–3
- Anki mega review (aim for 110+ words total)
- Write German from memory: describe the capstone project in German (Auf Deutsch!)

### EXTENDED CODING (2:00–4:00 PM): Code Quality Pass
Return to the capstone and improve quality:
1. Add `#pragma GCC diagnostic` or fix any remaining warnings
2. Add a `--help` command-line argument: `./sensor_sim --help` prints usage
3. Add `--ticks N` argument: `./sensor_sim --ticks 200` runs for 200 ticks instead of 100
4. Add statistics at end: min/max/avg sensor reading, total alarm activations

---

## WEEK 9 CHECKPOINT (Monday August 10, 4:00 PM)

Update PROGRESS.md.

| Checkpoint Item | Done? |
|:---|:---|
| Capstone project compiles with 0 warnings (`-Wall -Wextra`) | |
| All 5 state handlers implemented and tested | |
| Circular buffer, logger, GPIO sim written from scratch (no Week 7 copy-paste) | |
| Valgrind: 0 memory leaks, 0 invalid reads | |
| sim_log.txt created with correct timestamped entries | |
| README with simulation→STM32 mapping table | |
| GitHub: week9 capstone pushed | |
| Nicos Weg A2: Lessons 1–3 done | |
| Anki: 110+ German words total | |

**Self-rating (capstone 1–10)**: ___

> If you got through this week: you have built a complete, multi-module C project from scratch.
> That is a real portfolio artifact. The GitHub link to this project goes in your SOP.
