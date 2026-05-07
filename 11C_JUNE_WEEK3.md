# 📅 WEEK 3 — Jun 15-21 (Mon-Sun): STATE MACHINES + ADVANCED C + MEMORY LAYOUT

> **Topics**: State machines with enum + function pointers, memory layout (text/data/BSS/heap/stack), typedef patterns, packed structs, bit fields, function pointers deep
> **K.N. King Chapters**: Ch 16 (Structures, Unions, Enumerations deep), Ch 20 (Low-Level Programming)
> **K&R Bed Reading**: Chapter 6 (Structures — deep revisit)
> **FastBit Udemy**: Structures, bitfields, embedded-specific sections
> **Programs to write**: 6-8
> **German**: Nicos Weg Lessons 36-40, daily Anki, more past tense
> **🎯 THIS WEEK**: You learn the patterns that 90% of embedded firmware is built on.
> **📚 Full resource details**: See `10_RESOURCES.md`

---

## DAY 15 — Monday, Jun 15

### 🔶 Morning Block (5:10 - 6:30 AM) — STATE MACHINES (Part 1)

#### 📺 WATCH FIRST (10 min)

**Search YouTube**: "State Machine in C embedded" — pick any short video that shows the enum + switch pattern.

#### 💻 CODE (1h 10m)

**What is a state machine?** Almost every embedded system IS a state machine:
- Traffic light: RED → GREEN → YELLOW → RED
- Washing machine: IDLE → FILL → WASH → RINSE → SPIN → DONE
- UART receiver: IDLE → START_BIT → DATA_BITS → STOP_BIT

**Exercise 1 — Traffic light state machine (5:20-5:50):**

Create `week8/state_machine_basic.c`:
```c
#include <stdio.h>
#include <unistd.h>  // for sleep()

typedef enum {
    STATE_RED,
    STATE_GREEN,
    STATE_YELLOW,
    STATE_COUNT  // Trick: always put this last to get total count
} TrafficState;

const char *state_names[] = {"RED", "GREEN", "YELLOW"};
const int state_durations[] = {5, 4, 2};  // seconds

int main(void) {
    TrafficState current = STATE_RED;
    
    printf("Traffic Light State Machine\n");
    printf("==========================\n");
    
    for (int cycle = 0; cycle < 3; cycle++) {
        printf("\n--- Cycle %d ---\n", cycle + 1);
        
        // Process each state
        for (int s = 0; s < STATE_COUNT; s++) {
            current = (TrafficState)s;
            printf("[%s] for %d seconds\n", state_names[current], state_durations[current]);
            sleep(state_durations[current]);
        }
    }
    
    return 0;
}
```

**Exercise 2 — Vending machine state machine (5:50-6:20):**

Create `week8/vending_machine.c`:
```c
#include <stdio.h>

typedef enum {
    STATE_IDLE,
    STATE_COIN_INSERTED,
    STATE_ITEM_SELECTED,
    STATE_DISPENSING,
    STATE_CHANGE_RETURN,
    STATE_ERROR
} VendingState;

typedef enum {
    EVENT_INSERT_COIN,
    EVENT_SELECT_ITEM,
    EVENT_DISPENSE_DONE,
    EVENT_CANCEL,
    EVENT_ERROR,
    EVENT_RESET
} VendingEvent;

// State handler function type
typedef VendingState (*StateHandler)(VendingEvent event, int *balance);

// Implement a handler for each state
VendingState handle_idle(VendingEvent event, int *balance) {
    switch (event) {
        case EVENT_INSERT_COIN:
            *balance += 25;
            printf("  Coin inserted. Balance: %d cents\n", *balance);
            return STATE_COIN_INSERTED;
        default:
            printf("  Waiting for coin...\n");
            return STATE_IDLE;
    }
}

// YOU: implement handle_coin_inserted, handle_item_selected,
// handle_dispensing, handle_change_return, handle_error

int main(void) {
    VendingState current = STATE_IDLE;
    int balance = 0;
    
    // State handler table (function pointer array!)
    StateHandler handlers[] = {
        handle_idle,
        // handle_coin_inserted,
        // handle_item_selected,
        // handle_dispensing,
        // handle_change_return,
        // handle_error
    };
    
    // Simulate events
    VendingEvent events[] = {
        EVENT_INSERT_COIN,
        EVENT_INSERT_COIN,
        EVENT_SELECT_ITEM,
        EVENT_DISPENSE_DONE,
    };
    
    for (int i = 0; i < 4; i++) {
        printf("State: %d, Event: %d\n", current, events[i]);
        current = handlers[current](events[i], &balance);
    }
    
    return 0;
}
```

**What to understand**: The `handlers[]` array maps state → function. This eliminates giant switch-case blocks. This is the **industry-standard pattern** for embedded firmware.

#### 📖 READ (6:20-6:30)
- K.N. King Ch 16 — Sections on enumerations and unions

### ✅ Day 15 Checklist
- [ ] Traffic light state machine working
- [ ] Vending machine with function pointer dispatch table started
- [ ] Can explain: enum, function pointer, state transition
- [ ] Drew state diagram on paper (circles + arrows)

---

## DAY 16 — Tuesday, Jun 16

### 🔶 Morning Block (5:10 - 6:30 AM) — STATE MACHINES (Part 2) + FUNCTION POINTERS DEEP

#### 💻 CODE (1h 20m)

**Exercise 1 — Complete the vending machine** (5:10-5:40):
- Implement ALL state handler functions
- Add proper event processing for each state
- Test with multiple event sequences

**Exercise 2 — Callback functions (5:40-6:10):**

Create `week8/callbacks.c`:
```c
#include <stdio.h>

// Callback type: function that processes an integer
typedef void (*DataCallback)(int value);

// These are callback functions
void print_value(int value) {
    printf("Value: %d\n", value);
}

void print_squared(int value) {
    printf("Squared: %d\n", value * value);
}

void print_hex(int value) {
    printf("Hex: 0x%X\n", value);
}

// This function takes a callback — it doesn't know WHAT the callback does
void process_array(int *arr, int size, DataCallback callback) {
    for (int i = 0; i < size; i++) {
        callback(arr[i]);
    }
}

// Generic sort with comparator callback (like qsort!)
typedef int (*Comparator)(int a, int b);

int ascending(int a, int b) { return a - b; }
int descending(int a, int b) { return b - a; }

void bubble_sort(int *arr, int size, Comparator cmp) {
    for (int i = 0; i < size - 1; i++) {
        for (int j = 0; j < size - i - 1; j++) {
            if (cmp(arr[j], arr[j+1]) > 0) {
                int temp = arr[j];
                arr[j] = arr[j+1];
                arr[j+1] = temp;
            }
        }
    }
}

int main(void) {
    int data[] = {42, 17, 8, 255, 100};
    int n = 5;
    
    printf("=== Print values ===\n");
    process_array(data, n, print_value);
    
    printf("\n=== Print squared ===\n");
    process_array(data, n, print_squared);
    
    printf("\n=== Print hex ===\n");
    process_array(data, n, print_hex);
    
    printf("\n=== Sort ascending ===\n");
    bubble_sort(data, n, ascending);
    process_array(data, n, print_value);
    
    printf("\n=== Sort descending ===\n");
    bubble_sort(data, n, descending);
    process_array(data, n, print_value);
    
    return 0;
}
```

**What to understand**: Callbacks decouple WHAT from HOW. STM32 HAL uses callbacks everywhere: `HAL_UART_RxCpltCallback()`, `HAL_TIM_PeriodElapsedCallback()`, etc. This IS how embedded firmware works.

### ✅ Day 16 Checklist
- [ ] Vending machine complete with all states
- [ ] Callback pattern understood — process_array with different callbacks
- [ ] Custom sort with comparator callback working
- [ ] Can explain: how does `qsort()` use function pointers?

---

## DAY 17 — Wednesday, Jun 17

### 🔶 Morning Block (5:10 - 6:30 AM) — MEMORY LAYOUT

#### 💻 CODE (1h 20m)

**Exercise 1 — Visualize memory layout (5:10-5:50):**

Create `week8/memory_layout.c`:
```c
#include <stdio.h>
#include <stdlib.h>

// Global initialized (goes to .data section)
int global_init = 42;

// Global uninitialized (goes to .bss section)
int global_uninit;

// Constant (goes to .rodata section)
const char *message = "Hello, embedded world!";

// Static (goes to .data or .bss)
static int static_var = 100;

void show_addresses(void) {
    // Local variable (stack)
    int local_var = 7;
    
    // Dynamic allocation (heap)
    int *heap_var = malloc(sizeof(int));
    *heap_var = 99;
    
    printf("=== MEMORY LAYOUT ===\n\n");
    printf("TEXT (code):\n");
    printf("  main()         = %p\n", (void *)main);
    printf("  show_addresses = %p\n", (void *)show_addresses);
    
    printf("\nRODATA (constants):\n");
    printf("  message        = %p  (\"%s\")\n", (void *)message, message);
    
    printf("\nDATA (initialized globals):\n");
    printf("  global_init    = %p  (value: %d)\n", (void *)&global_init, global_init);
    printf("  static_var     = %p  (value: %d)\n", (void *)&static_var, static_var);
    
    printf("\nBSS (uninitialized globals):\n");
    printf("  global_uninit  = %p  (value: %d)\n", (void *)&global_uninit, global_uninit);
    
    printf("\nHEAP (dynamic):\n");
    printf("  heap_var       = %p  (value: %d)\n", (void *)heap_var, *heap_var);
    
    printf("\nSTACK (local):\n");
    printf("  local_var      = %p  (value: %d)\n", (void *)&local_var, local_var);
    
    printf("\n=== Address order (low to high): TEXT < RODATA < DATA < BSS < HEAP ... STACK ===\n");
    
    free(heap_var);
}

int main(void) {
    show_addresses();
    return 0;
}
```

**MANDATORY**: Draw the memory layout on paper:
```
High Address
┌──────────────┐
│    STACK      │ ← local variables, function args, return addresses
│    ↓ grows    │
│              │
│    ↑ grows    │
│    HEAP       │ ← malloc/calloc
├──────────────┤
│    BSS        │ ← uninitialized globals (zeroed)
├──────────────┤
│    DATA       │ ← initialized globals
├──────────────┤
│    RODATA     │ ← string literals, const data
├──────────────┤
│    TEXT       │ ← your compiled code (instructions)
└──────────────┘
Low Address
```

**Exercise 2 — Check sizes with `size` command (5:50-6:10):**
```bash
gcc -o layout memory_layout.c
size layout   # Shows: text, data, bss sections sizes

# Compare with a minimal program
echo 'int main(){return 0;}' > tiny.c
gcc -o tiny tiny.c
size tiny     # Much smaller!
```

**What to understand**: On STM32 with 128KB flash + 128KB RAM:
- TEXT + RODATA + DATA → must fit in FLASH (128KB)
- DATA (copy) + BSS + HEAP + STACK → must fit in RAM (128KB)
- If your program is too big → it doesn't fit. No virtual memory. No swap.

### ✅ Day 17 Checklist
- [ ] memory_layout.c running — see all section addresses
- [ ] Drew memory layout diagram on paper
- [ ] Used `size` command to check section sizes
- [ ] Can explain: text, data, bss, heap, stack + what goes where

---

## DAY 18 — Thursday, Jun 18

### 🔶 Morning Block (5:10 - 6:30 AM) — PACKED STRUCTS + BIT FIELDS

#### 💻 CODE (1h 20m)

**Exercise 1 — Struct padding (5:10-5:35):**

Create `week8/struct_padding.c`:
```c
#include <stdio.h>
#include <stdint.h>

// Normal struct — compiler adds padding for alignment
struct Normal {
    char a;     // 1 byte + 3 padding
    int b;      // 4 bytes
    char c;     // 1 byte + 3 padding
};              // Total: 12 bytes (not 6!)

// Reordered — less padding
struct Reordered {
    int b;      // 4 bytes
    char a;     // 1 byte
    char c;     // 1 byte + 2 padding
};              // Total: 8 bytes

// Packed — no padding (used in embedded for hardware registers)
struct __attribute__((packed)) Packed {
    char a;     // 1 byte
    int b;      // 4 bytes
    char c;     // 1 byte
};              // Total: 6 bytes (exact)

int main(void) {
    printf("Normal:    sizeof = %zu\n", sizeof(struct Normal));
    printf("Reordered: sizeof = %zu\n", sizeof(struct Reordered));
    printf("Packed:    sizeof = %zu\n", sizeof(struct Packed));
    
    return 0;
}
```

**Exercise 2 — Bit fields (5:35-6:00):**

Create `week8/bit_fields.c`:
```c
#include <stdio.h>
#include <stdint.h>

// Simulating a hardware register with bit fields
typedef struct {
    uint32_t enable     : 1;   // Bit 0
    uint32_t mode       : 2;   // Bits 1-2
    uint32_t speed      : 3;   // Bits 3-5
    uint32_t reserved   : 2;   // Bits 6-7
    uint32_t data       : 8;   // Bits 8-15
    uint32_t status     : 4;   // Bits 16-19
    uint32_t reserved2  : 12;  // Bits 20-31
} PeripheralReg;

int main(void) {
    PeripheralReg reg = {0};
    
    printf("sizeof(PeripheralReg) = %zu bytes\n", sizeof(PeripheralReg));
    
    // Set fields
    reg.enable = 1;
    reg.mode = 2;       // Mode 2
    reg.speed = 5;      // Speed 5
    reg.data = 0xAB;    // Data byte
    reg.status = 0xF;   // All status bits set
    
    printf("enable: %u\n", reg.enable);
    printf("mode:   %u\n", reg.mode);
    printf("speed:  %u\n", reg.speed);
    printf("data:   0x%X\n", reg.data);
    printf("status: 0x%X\n", reg.status);
    
    // Print raw 32-bit value
    uint32_t *raw = (uint32_t *)&reg;
    printf("Raw register value: 0x%08X\n", *raw);
    
    return 0;
}
```

**What to understand**: THIS is exactly how STM32 peripheral registers are organized. CMSIS headers define register structs with bit fields.

**Exercise 3 — Memory-mapped I/O preview (6:00-6:20):**

Create `week8/memory_mapped_io.c`:
```c
#include <stdio.h>
#include <stdint.h>

// Simulating STM32 GPIO register (memory-mapped at a fixed address)
typedef struct {
    volatile uint32_t MODER;    // Mode register
    volatile uint32_t OTYPER;   // Output type register
    volatile uint32_t OSPEEDR;  // Output speed register
    volatile uint32_t PUPDR;    // Pull-up/pull-down register
    volatile uint32_t IDR;      // Input data register
    volatile uint32_t ODR;      // Output data register
    volatile uint32_t BSRR;     // Bit set/reset register
} GPIO_TypeDef;

// On real STM32: #define GPIOA ((GPIO_TypeDef *)0x40020000)
// Here we simulate with a local struct:
GPIO_TypeDef fake_gpioa = {0};

int main(void) {
    GPIO_TypeDef *GPIOA = &fake_gpioa;
    
    // "Configure" pin 5 as output (like LED on Nucleo)
    GPIOA->MODER |= (1 << 10);   // Set bit 10 (pin 5, mode = 01 = output)
    
    // "Turn on" pin 5
    GPIOA->ODR |= (1 << 5);
    
    // "Turn off" pin 5
    GPIOA->ODR &= ~(1 << 5);
    
    // Better way: use BSRR (atomic set/reset)
    GPIOA->BSRR = (1 << 5);       // Set pin 5
    GPIOA->BSRR = (1 << 21);      // Reset pin 5 (bit 21 = reset for pin 5)
    
    printf("MODER: 0x%08X\n", GPIOA->MODER);
    printf("ODR:   0x%08X\n", GPIOA->ODR);
    
    return 0;
}
```

> **⚠️ THIS IS EXACTLY WHAT YOU'LL DO IN JULY ON REAL STM32 HARDWARE.**
> The only difference: `GPIOA` will point to `0x40020000` (real hardware address) instead of a local variable.

### ✅ Day 18 Checklist
- [ ] Understand struct padding — why sizeof differs from expected
- [ ] Bit fields working — simulated hardware register
- [ ] Memory-mapped I/O pattern understood — struct pointer to fixed address
- [ ] Can explain: volatile, packed, why BSRR is better than ODR

---

## DAY 19 — Friday, Jun 19

### 🔶 Morning Block (5:10 - 6:30 AM) — UNIONS + ADVANCED PATTERNS

#### 💻 CODE (1h 20m)

**Exercise 1 — Union for type punning:**
```c
typedef union {
    uint32_t raw;
    struct {
        uint8_t byte0;
        uint8_t byte1;
        uint8_t byte2;
        uint8_t byte3;
    } bytes;
    struct {
        uint16_t low;
        uint16_t high;
    } words;
} Register32;
```

Use this to extract individual bytes from a 32-bit value. Draw the memory layout.

**Exercise 2 — Tagged union (variant type):**
```c
typedef enum { TYPE_INT, TYPE_FLOAT, TYPE_STRING } DataType;

typedef struct {
    DataType type;
    union {
        int i;
        float f;
        char s[32];
    } value;
} Variant;
```

Create an array of Variant and process each based on its type tag.

### ✅ Day 19 Checklist
- [ ] Union for register byte access working
- [ ] Tagged union pattern understood
- [ ] Drew union memory layout (all members share same address)

---

## DAY 20-21 — Saturday-Sunday, Jun 20-21 (DEEP STUDY + REVIEW)

### Saturday (6:30 AM - 12:45 PM)

**Session 1**: Build a "Hardware Register Simulator" — combine structs, bit fields, function pointers, state machine:
- Create a fake peripheral with configuration registers
- Write `configure()`, `enable()`, `read_status()`, `write_data()` functions
- Use a state machine for the peripheral lifecycle (RESET → INIT → RUNNING → ERROR)

**Session 2**: K.N. King Ch 16 + Ch 20 exercises

**Session 3**: Interview prep — write answers for:
1. "What is a state machine? Draw one for an elevator."
2. "Explain struct padding and how to avoid it"
3. "What is volatile and when must you use it?"
4. "How are hardware registers accessed in C?" (memory-mapped I/O)
5. "What is a callback function? Give an example from embedded systems."

### Sunday (7:30 AM - 12:30 PM)

**7:30-9:00**: Implement state machine from memory (no reference)
**9:15-10:45**: Implement memory-mapped I/O simulator from memory
**11:00-12:30**: Git push all week 8 code. Write READMEs.

### 🇩🇪 German (both days, afternoon)
- Nicos Weg lessons 38-40
- Anki review (140+ cards)
- Practice: daily routine in German with past tense

---

## 📋 WEEK 3 CHECKPOINT

- [ ] ✅ State machine with enum + function pointer dispatch — can build from scratch
- [ ] ✅ Callbacks / function pointers — understand the pattern, can explain
- [ ] ✅ Memory layout — can draw text/data/BSS/heap/stack from memory
- [ ] ✅ Packed structs, bit fields — understand struct padding
- [ ] ✅ Memory-mapped I/O — can simulate GPIO register access in pure C
- [ ] ✅ Unions — type punning, tagged unions
- [ ] ✅ All code pushed to GitHub
- [ ] ✅ Nicos Weg lessons 36-40, 140+ Anki cards
