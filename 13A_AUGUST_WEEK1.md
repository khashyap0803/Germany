# AUGUST WEEK 1 (Aug 1–3) — Phase 1 Week 8 END: STATE MACHINES + MEMORY LAYOUT

> **Topics**: State machines (enum + function pointer dispatch table), memory layout visualization, packed structs, bit fields, union type punning
> **K.N. King Reading**: Ch 18 (Declarations) + Ch 16 bit fields (weekday reading continues from July)
> **K&R Bed Reading**: Chapter 6 revisit (unions + bit-fields)
> **AI Policy**: BANNED for code — AI may only explain concepts
> **Dates**: Saturday August 1 → Monday August 3, 2026
> **Note**: Week 8 reading was done Jul 28–31 (see 12E_JULY_WEEK5.md). This file covers the coding weekend only.

---

## SATURDAY AUGUST 1 — STATE MACHINES + MEMORY LAYOUT (7:30 AM–6:30 PM)

### Warmup (7:30–8:00 AM): Jacob Sorber YouTube
- "State Machines in C" by Jacob Sorber (~10 min at 1.5×)
- Note the function pointer dispatch pattern — this is what you will code today

### BLOCK 1 (8:00–9:30 AM): State Machine — Traffic Light + Vending Machine
Write ALL from scratch. NO AI code.

```
week8/
├── traffic_light.c     — Simple enum state machine with state names + durations
├── sm_table.h          — Generic state machine table type
└── vending_machine.c   — Full state machine with function pointer dispatch table
```

**traffic_light.c** requirements:
```c
#include <stdio.h>

typedef enum { STATE_RED, STATE_GREEN, STATE_YELLOW, STATE_COUNT } TrafficState;

const char *state_names[] = {"RED", "GREEN", "YELLOW"};
const int state_durations_sec[] = {5, 4, 2};

// State transition table: next_state[current] = next
const TrafficState next_state[] = {
    STATE_GREEN,    // RED -> GREEN
    STATE_YELLOW,   // GREEN -> YELLOW
    STATE_RED       // YELLOW -> RED
};

int main(void) {
    TrafficState current = STATE_RED;
    printf("Traffic Light Simulation (3 cycles):\n");
    for (int cycle = 0; cycle < 3; cycle++) {
        printf("[%s] for %d seconds\n", state_names[current], state_durations_sec[current]);
        current = next_state[current];
    }
    return 0;
}
```

**vending_machine.c** requirements — full state machine with handler table:
```c
typedef enum {
    S_IDLE, S_HAS_COIN, S_ITEM_SELECTED, S_DISPENSING, S_CHANGE, S_COUNT
} VendState;

typedef enum {
    E_INSERT_COIN, E_SELECT_ITEM, E_CANCEL, E_DISPENSE_DONE, E_EVENT_COUNT
} VendEvent;

// Each state handler receives the event and returns the next state
typedef VendState (*StateHandler)(VendEvent event, int *balance);

// Implement all 5 handler functions — one per state
VendState handle_idle(VendEvent event, int *balance);
VendState handle_has_coin(VendEvent event, int *balance);
VendState handle_item_selected(VendEvent event, int *balance);
VendState handle_dispensing(VendEvent event, int *balance);
VendState handle_change(VendEvent event, int *balance);

// Dispatch table — maps state → handler function
StateHandler handlers[S_COUNT] = {
    handle_idle,
    handle_has_coin,
    handle_item_selected,
    handle_dispensing,
    handle_change,
};

int main(void) {
    VendState current = S_IDLE;
    int balance = 0;

    // Simulate a purchase sequence
    VendEvent sequence[] = {
        E_INSERT_COIN,    // insert coin
        E_INSERT_COIN,    // insert another coin (total: 50 cents)
        E_SELECT_ITEM,    // select item (costs 30 cents)
        E_DISPENSE_DONE,  // item dispensed, 20 cents change
    };

    for (int i = 0; i < 4; i++) {
        printf("State: %-15s + Event: %d → ", state_names[current], sequence[i]);
        current = handlers[current](sequence[i], &balance);
        printf("State: %s\n", state_names[current]);
    }
    return 0;
}
```

State name array: add `const char *state_names[S_COUNT] = {"IDLE", "HAS_COIN", ...};`

### BREAK (9:30–9:45)

### BLOCK 2 (9:45–11:15 AM): Memory Layout Visualization
```
week8/
├── memory_layout.c     — Print addresses of variables in each memory segment
└── section_sizes.sh    — Shell script to run `size` on compiled binaries
```

**memory_layout.c** requirements:
```c
#include <stdio.h>
#include <stdlib.h>

// Each of these goes to a different memory segment:
int global_init = 42;               // .data (initialized global)
int global_uninit;                  // .bss  (uninitialized global — zeroed at start)
const char *message = "embedded";   // message ptr in .data, string literal in .rodata
static int module_private = 99;     // .data (static — module scope)

void show_addresses(void) {
    int local_var = 7;              // stack
    int *heap_var = malloc(sizeof(int));  // heap
    *heap_var = 0xFF;

    printf("=== MEMORY SEGMENTS ===\n");
    printf("TEXT  (code):  main()         = %p\n", (void *)main);
    printf("RODATA:        \"embedded\"   = %p\n", (void *)message);
    printf("DATA:          global_init    = %p  (val: %d)\n", (void *)&global_init, global_init);
    printf("DATA:          module_private = %p  (val: %d)\n", (void *)&module_private, module_private);
    printf("BSS:           global_uninit  = %p  (val: %d)\n", (void *)&global_uninit, global_uninit);
    printf("HEAP:          heap_var       = %p  (val: %d)\n", (void *)heap_var, *heap_var);
    printf("STACK:         local_var      = %p  (val: %d)\n", (void *)&local_var, local_var);
    printf("\nAddress order: TEXT < RODATA < DATA < BSS << HEAP ... STACK\n");
    printf("HEAP grows UP. STACK grows DOWN.\n");

    free(heap_var);
}

int main(void) {
    show_addresses();
    return 0;
}
```

After running, draw the output on paper as a memory map (low addresses at bottom, high at top). Show where each variable lives.

Shell script `section_sizes.sh`:
```bash
#!/bin/bash
echo "=== Section sizes with `size` command ==="
echo "--- memory_layout ---"
size memory_layout

echo "--- tiny program (int main(){return 0;}) ---"
echo 'int main(){return 0;}' > /tmp/tiny.c
gcc -o /tmp/tiny /tmp/tiny.c
size /tmp/tiny

echo "--- with large BSS (1000 ints) ---"
echo 'int arr[1000]; int main(){return 0;}' > /tmp/bss.c
gcc -o /tmp/bss /tmp/bss.c
size /tmp/bss

echo "BSS is larger in the third one — because of the 4000-byte uninitialized array."
echo "On STM32: BSS goes in RAM. TEXT goes in flash. Each has a fixed size limit."
```

### BREAK (11:15–11:30)

### BLOCK 3 (11:30 AM–12:30 PM): Packed Structs + Union Type Punning
```
week8/
├── packed_structs.c    — Padding vs packed, struct size comparison
└── union_punning.c     — Union to access register bytes
```

**packed_structs.c** requirements:
```c
#include <stdio.h>
#include <stdint.h>

struct Normal   { char a; int b; char c; };       // 12 bytes (with padding)
struct Reordered { int b; char a; char c; };       // 8 bytes (less padding)
struct __attribute__((packed)) Packed { char a; int b; char c; };  // 6 bytes (no padding)

// Simulate a hardware register with bit fields
typedef struct __attribute__((packed)) {
    uint32_t enable   : 1;   // bit 0
    uint32_t mode     : 2;   // bits 1-2
    uint32_t speed    : 3;   // bits 3-5
    uint32_t reserved : 2;   // bits 6-7
    uint32_t data     : 8;   // bits 8-15
    uint32_t status   : 4;   // bits 16-19
    uint32_t pad      : 12;  // bits 20-31
} HWReg;

int main(void) {
    printf("sizeof Normal:    %zu\n", sizeof(struct Normal));    // 12
    printf("sizeof Reordered: %zu\n", sizeof(struct Reordered)); // 8
    printf("sizeof Packed:    %zu\n", sizeof(struct Packed));    // 6

    HWReg reg = {0};
    reg.enable = 1;
    reg.mode   = 2;
    reg.speed  = 5;
    reg.data   = 0xAB;
    reg.status = 0xF;
    printf("sizeof HWReg: %zu (should be 4)\n", sizeof(HWReg));

    uint32_t *raw = (uint32_t *)&reg;
    printf("raw value: 0x%08X\n", *raw);
    return 0;
}
```

**union_punning.c** requirements:
```c
// Union for register byte access:
typedef union {
    uint32_t raw;
    struct { uint8_t b0, b1, b2, b3; } bytes;
    struct { uint16_t low, high; } words;
} Reg32;

int main(void) {
    Reg32 r;
    r.raw = 0xDEADBEEF;

    printf("raw:   0x%08X\n", r.raw);
    printf("bytes: 0x%02X 0x%02X 0x%02X 0x%02X\n",
           r.bytes.b0, r.bytes.b1, r.bytes.b2, r.bytes.b3);
    printf("words: 0x%04X 0x%04X\n", r.words.low, r.words.high);

    // Modify just the high byte:
    r.bytes.b3 = 0x12;
    printf("after setting b3=0x12: raw = 0x%08X\n", r.raw);
    return 0;
}
```

Draw the union memory layout: show that all members share the same starting address.

### LUNCH (12:30–1:30 PM)

### GERMAN BLOCK 1 (1:30–4:30 PM)
- Nicos Weg Lessons 47–48
- Practice dass-clauses: "Ich weiß, dass ich viel lernen muss."
- Write 10 sentences with dass
- Anki: add 15 new cards

### GERMAN BLOCK 2 (5:00–6:30 PM)
- Nicos Weg Lesson 49
- AnkiDroid: review ALL pending cards
- Write from memory: 3-minute speech about yourself (present + past tense, modal verbs)

---

## SUNDAY AUGUST 2 — FUNCTION POINTER DEEP + GIT (7:30 AM–4:00 PM)

### BLOCK 1 (7:30–9:00 AM): Function Pointers as Callbacks
Watch: Jacob Sorber "Function Pointers" (~8 min) on YouTube first.

```
week8/
├── fn_pointers.c       — Function pointer declaration, array of function pointers, callbacks
└── generic_sort.c      — Sort with comparator function pointer (like qsort())
```

**fn_pointers.c** requirements:
```c
// Part 1: basic syntax
void print_int(int x) { printf("int: %d\n", x); }
void print_hex(int x) { printf("hex: 0x%X\n", x); }
void print_bin(int x) { /* print all 32 bits */ }

typedef void (*PrintFn)(int);

// Array of function pointers:
PrintFn formatters[] = { print_int, print_hex, print_bin };

// Call each formatter:
for (int i = 0; i < 3; i++) {
    formatters[i](255);
}

// Part 2: callback passed as argument
void process_array(int *arr, int n, PrintFn callback) {
    for (int i = 0; i < n; i++) callback(arr[i]);
}
```

**generic_sort.c** requirements:
```c
typedef int (*CompareFn)(const void *, const void *);

// Write bubble_sort that accepts a comparator:
void bubble_sort(void *arr, int n, int elem_size, CompareFn cmp);

// Comparators:
int cmp_int_asc(const void *a, const void *b);   // returns negative if a < b
int cmp_int_desc(const void *a, const void *b);
int cmp_str(const void *a, const void *b);        // strcmp-based

// Test with int array (ascending + descending) and string array
```

### BLOCK 2 (9:15–10:30 AM): State Machine From Memory
From a blank file, write a 3-state state machine with function pointer dispatch table from memory:
- States: IDLE, RUNNING, ERROR
- Events: START, STOP, FAULT, RESET
- Each state handler returns the next state
- Main loop dispatches: `current = handlers[current](event)`

Time yourself. Target: under 20 minutes.

### GIT PUSH (10:30–11:00 AM)
```bash
cd ~/C-Practice
git add week8/
git commit -m "Week 8: state machines (dispatch table), memory layout, packed structs, function pointer callbacks"
git push origin main
```

Write `week8/README.md` — list files, explain the state machine dispatch table pattern.

### REST + LUNCH (11:00 AM–12:00 PM)

### GERMAN (12:00–2:00 PM)
- Nicos Weg Lesson 50 — A1 COMPLETE!
- Anki mega review (aim for 105+ words total)
- Write from memory: 5 sentences about what you've built in C and why you're learning German

### EXTENDED CODING (2:00–4:00 PM): Integrate Everything
```
week8/
└── mini_firmware.c   — State machine + circular buffer + bit macros + file logger
```

Requirements:
- State machine: INIT → RUNNING → ALARM → RUNNING → SHUTDOWN
- RUNNING: every "tick", write to circular buffer + log to file
- ALARM: triggered when buffer fills to 80% — log "ALARM: buffer near full"
- SHUTDOWN: flush all remaining buffer to log file, close file
- Use your bit_macros.h for flag register
- Run under Valgrind: 0 leaks

---

## MONDAY AUGUST 3 — WEEK 8 WRAP (Reading Only)

### Pre-Gym (5:00–5:25 AM)
**Read**: K.N. King Chapter 18 (Declarations — re-read complex declaration syntax)
Focus on: `int (*fp)(int, int)` = pointer to function, `int *arr[5]` vs `int (*arr)[5]`

**Bed Reading (9:30–10:00 PM)**: K&R Chapter 6 — re-read bit-fields section

---

## WEEK 8 CHECKPOINT (Monday August 3, 4:00 PM)

Update PROGRESS.md.

| Checkpoint Item | Done? |
|:---|:---|
| State machine with function pointer dispatch table — written from memory | |
| State diagram drawn on paper for both examples | |
| Memory layout: can draw text/data/BSS/heap/stack from memory | |
| Used `size` command to verify section sizes | |
| Packed struct + bit fields — hardware register simulation | |
| Union type punning — access 32-bit register as bytes | |
| Function pointer as callback — array of callbacks | |
| mini_firmware.c: state machine + circular buffer + logger, Valgrind clean | |
| GitHub: week8 pushed with README | |
| Nicos Weg: Lessons 47–50 done — A1 COMPLETE | |
| Anki: 105+ German words total | |

**Self-rating (state machines + memory layout 1–10)**: ___ (minimum 6 before Week 9)

> Week 9 is the capstone. Everything you've built in Weeks 1–8 goes into one project.
