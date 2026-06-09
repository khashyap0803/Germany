# JULY WEEK 1 (Jul 1–6) — Phase 1 Week 4: STRUCTS + BITWISE OPERATORS

> **Topics**: Struct declaration, member access, pointer to struct (->), struct arrays, typedef, bitwise AND/OR/XOR/NOT/shifts, bit manipulation macros
> **K.N. King Reading**: Ch 16 (Structures — complete) + Ch 20 first half (Low-Level Programming)
> **K&R Bed Reading**: Chapter 6 (Structures)
> **AI Policy**: BANNED for code — AI may only explain concepts
> **Dates**: Wednesday July 1 → Monday July 6, 2026
> **Note**: Week 4 Day 1 was June 30 (Tuesday). See 11D_JUNE_WEEK4.md for that day's reading.

---

## WEEKDAY READING SCHEDULE (Jul 1–4)

### Wednesday July 1 — Pre-Gym (5:00–5:25 AM)
**Read**: K.N. King Chapter 16 pages 20–40
- Nested structs: `struct Address` inside `struct Person`
- Array of structs: `struct Student class[50]` — how to loop through
- Passing struct by pointer to function: `void update_age(struct Person *p)`
- Arrow operator: `p->age` is shorthand for `(*p).age` — ALWAYS use `->`

**Bed Reading (9:30–10:00 PM)**: K&R Chapter 6 pages 127–145 (Basics of Structures, Structures and Functions)

### Thursday July 2 — Pre-Gym (5:00–5:25 AM)
**Read**: K.N. King Chapter 16 pages 40–end
- `typedef struct { ... } TypeName;` — convenience alias so you don't write `struct` every time
- Self-referential structs: `struct Node { int data; struct Node *next; }` — foundation of linked lists
- Size of struct is NOT sum of members — compiler adds padding for alignment
- `offsetof()` macro: tells you where in memory a member lives

**Bed Reading**: K&R Chapter 6 pages 145–165 (Arrays of Structures, Pointers to Structures, Self-referential Structures)

### Friday July 3 — Pre-Gym (5:00–5:25 AM)
**Read**: K.N. King Chapter 20 pages 1–20 (Low-Level Programming)
- Bitwise AND `&`: both bits must be 1 → used to CLEAR bits and READ bits
- Bitwise OR `|`: either bit must be 1 → used to SET bits
- Bitwise XOR `^`: bits must differ → used to TOGGLE bits
- Bitwise NOT `~`: inverts all bits
- Left shift `<<`: multiply by 2^n (fast); Right shift `>>`: divide by 2^n
- Compound assignment: `x &= ~mask;` clears bits in mask

Draw on paper (before gym):
```
SET bit 3:    reg |=  (1 << 3)     // OR with bit mask
CLEAR bit 3:  reg &= ~(1 << 3)     // AND with inverted mask
TOGGLE bit 3: reg ^=  (1 << 3)     // XOR with bit mask
READ bit 3:   (reg >> 3) & 1       // shift down, mask lowest bit
```

**Bed Reading**: K&R Chapter 2 pages 48–53 (Bitwise Operators)

### Monday July 6 — Pre-Gym (5:00–5:25 AM)
**Read**: K.N. King Chapter 20 pages 20–40
- Bit fields inside structs (already previewed in K.N. King Ch 16)
- `volatile` keyword: what it means, why you need it for hardware registers
- `const` with pointers: `const int *p` vs `int *const p` vs `const int *const p`

**Bed Reading**: K&R Chapter 6 — re-read self-referential structs section

---

## SATURDAY JULY 4 — STRUCTS + TYPEDEF (7:30 AM–6:30 PM)

### Warmup (7:30–8:00 AM): Watch Neso Academy Videos
- "Structures in C" (~12 min at 1.5×)
- "Array of Structures" (~8 min at 1.5×)
- "Structures and Pointers" (~10 min at 1.5×)

### BLOCK 1 (8:00–9:30 AM): Basic Struct Programs
Write ALL from scratch. NO AI code.

```
week4/
├── structs_basic.c     — Point, Rectangle, Circle structs with area/perimeter functions
├── student_db.c        — Array of 5 students: name, roll, 3 marks; sort by average
└── employee.c          — Employee struct: name, id, salary; raise(), print_all(), find_by_id()
```

**structs_basic.c** requirements:
```c
typedef struct { float x, y; } Point;
typedef struct { Point top_left; Point bottom_right; } Rectangle;
typedef struct { Point center; float radius; } Circle;

// Functions to implement (NO AI):
float   point_distance(Point a, Point b);
float   rect_area(Rectangle r);
float   rect_perimeter(Rectangle r);
float   circle_area(Circle c);       // PI = 3.14159265
float   circle_circumference(Circle c);
int     rect_contains_point(Rectangle r, Point p);  // 1 if point inside, 0 if not
```

**student_db.c** requirements:
- Define `Student` with `name[50]`, `roll`, `marks[3]` (float), `average` (float)
- `calc_average(Student *s)` — fills s->average from s->marks
- `print_student(const Student *s)` — formatted table row
- `sort_by_average(Student arr[], int n)` — bubble sort descending
- `find_by_roll(Student arr[], int n, int roll)` — returns index or -1
- Hard-code 5 students, call calc_average for each, sort, print ranked list

**employee.c** requirements:
- Define `Employee` with `name[50]`, `id` (int), `salary` (float)
- `void raise_salary(Employee *e, float percent)` — e->salary *= (1 + percent/100)
- `void print_all(Employee arr[], int n)` — formatted table
- `int find_by_id(Employee arr[], int n, int id)` — return index or -1
- Test with 4 employees: give 10% raise to ID 1002, print before and after

### BREAK (9:30–9:45)

### BLOCK 2 (9:45–11:15 AM): Bitwise Operators
```
week4/
├── bitwise_demo.c      — All 6 operators with examples and printed binary
├── bit_macros.h        — SET_BIT, CLEAR_BIT, TOGGLE_BIT, READ_BIT macros
└── bit_flags.c         — Use your macros to simulate GPIO register + LED flags
```

**bitwise_demo.c** — write a `print_binary(unsigned int n)` helper first, then show:
```c
void print_binary(unsigned int n) {
    // print all 32 bits from MSB to LSB
    // hint: loop from bit 31 down to bit 0
    // ((n >> i) & 1) gives the value of bit i
}

int main(void) {
    unsigned int a = 0b10110011;   // = 179
    unsigned int b = 0b01101101;   // = 109

    printf("a         = "); print_binary(a); printf("\n");
    printf("b         = "); print_binary(b); printf("\n");
    printf("a & b     = "); print_binary(a & b);  printf("  (AND)\n");
    printf("a | b     = "); print_binary(a | b);  printf("  (OR)\n");
    printf("a ^ b     = "); print_binary(a ^ b);  printf("  (XOR)\n");
    printf("~a        = "); print_binary(~a);      printf("  (NOT a)\n");
    printf("a << 2    = "); print_binary(a << 2);  printf("  (left shift 2)\n");
    printf("a >> 2    = "); print_binary(a >> 2);  printf("  (right shift 2)\n");
    return 0;
}
```

**bit_macros.h** — write these macros:
```c
#ifndef BIT_MACROS_H
#define BIT_MACROS_H

#define SET_BIT(reg, bit)     ((reg) |=  (1U << (bit)))
#define CLEAR_BIT(reg, bit)   ((reg) &= ~(1U << (bit)))
#define TOGGLE_BIT(reg, bit)  ((reg) ^=  (1U << (bit)))
#define READ_BIT(reg, bit)    (((reg) >> (bit)) & 1U)
#define WRITE_BIT(reg, bit, val) \
    ((val) ? SET_BIT(reg, bit) : CLEAR_BIT(reg, bit))

#endif
```

**bit_flags.c** — simulate a GPIO output register:
```c
#include <stdint.h>
#include "bit_macros.h"

// Simulate STM32 GPIO ODR (Output Data Register)
// Bit 5 = LED1 (like Nucleo PA5)
// Bit 6 = LED2
// Bit 7 = LED3
// Bit 0 = Button (input, read only)

void print_gpio_state(uint32_t reg, const char *label);

int main(void) {
    uint32_t gpio_reg = 0;

    // Turn on LED1 (pin 5)
    SET_BIT(gpio_reg, 5);
    print_gpio_state(gpio_reg, "LED1 ON");

    // Turn on LED2 (pin 6)
    SET_BIT(gpio_reg, 6);
    print_gpio_state(gpio_reg, "LED2 ON");

    // Toggle LED1 (should turn off)
    TOGGLE_BIT(gpio_reg, 5);
    print_gpio_state(gpio_reg, "LED1 toggled OFF");

    // Read LED2 state
    printf("LED2 is %s\n", READ_BIT(gpio_reg, 6) ? "ON" : "OFF");

    // Clear all LEDs
    CLEAR_BIT(gpio_reg, 5);
    CLEAR_BIT(gpio_reg, 6);
    CLEAR_BIT(gpio_reg, 7);
    print_gpio_state(gpio_reg, "All LEDs OFF");

    return 0;
}
```

### BREAK (11:15–11:30)

### BLOCK 3 (11:30 AM–12:30 PM): Linked List Node (Struct + Pointer Preview)
```
week4/
└── list_node.c     — struct Node with self-reference; manually build 3-node chain
```

**list_node.c** requirements — manually wire up 3 nodes WITHOUT malloc yet (use stack arrays):
```c
typedef struct Node {
    int data;
    struct Node *next;  // Self-referential!
} Node;

int main(void) {
    // Create 3 nodes on the stack
    Node n1 = {10, NULL};
    Node n2 = {20, NULL};
    Node n3 = {30, NULL};

    // Wire them together manually
    n1.next = &n2;
    n2.next = &n3;
    // n3.next is already NULL

    // Traverse the list
    Node *p = &n1;
    while (p != NULL) {
        printf("%d -> ", p->data);
        p = p->next;
    }
    printf("NULL\n");   // Expected: 10 -> 20 -> 30 -> NULL
}
```

**Key insight**: `p->data` means "the data member of the node that p points to." Draw this diagram on paper — boxes connected by arrows. This is the foundation for Week 7 (full dynamic linked list with malloc).

### LUNCH (12:30–1:30 PM)

### GERMAN BLOCK 1 (1:30–4:30 PM)
- Nicos Weg Lessons 23–25
- New grammar: accusative case (direct object) — "Ich habe einen Stift. Ich sehe den Computer."
- Write 10 sentences using accusative case
- Anki: add 15 new cards

### GERMAN BLOCK 2 (5:00–6:30 PM)
- Nicos Weg Lessons 26–27
- AnkiDroid: review ALL pending cards
- ChatGPT Voice: "I'm an A1 German learner. Ask me questions about my day and what I'm doing."

---

## SUNDAY JULY 5 — BITWISE DEEP + STRUCT REVIEW + GIT (7:30 AM–4:00 PM)

### BLOCK 1 (7:30–9:00 AM): Bitwise Practice Programs
Watch: Jacob Sorber "Bitwise Operations in C" (~10 min) first.

```
week4/
├── number_utils.c      — is_power_of_two, count_set_bits, swap_without_temp, reverse_bits
└── bitmask_ops.c       — RGB color packing/unpacking, flag register simulation
```

**number_utils.c** requirements:
```c
int is_power_of_two(unsigned int n);  // trick: n & (n-1) == 0 if power of 2
int count_set_bits(unsigned int n);   // Brian Kernighan: while(n) { n &= n-1; count++; }
void swap_without_temp(int *a, int *b);  // a ^= b; b ^= a; a ^= b;
unsigned int reverse_bits(unsigned int n);  // reverse all 32 bits

// Test all 4 functions with multiple inputs
// Verify swap_without_temp against the standard temp-based swap
```

**bitmask_ops.c** requirements:
```c
// Pack RGB color into a 32-bit integer:
// Bits 23-16 = Red, Bits 15-8 = Green, Bits 7-0 = Blue

uint32_t pack_rgb(uint8_t r, uint8_t g, uint8_t b);
uint8_t  get_red(uint32_t color);
uint8_t  get_green(uint32_t color);
uint8_t  get_blue(uint32_t color);
uint32_t set_red(uint32_t color, uint8_t r);  // Change only the red channel

// Test:
// uint32_t orange = pack_rgb(255, 165, 0);
// Extract and print r, g, b
// Change red to 200, verify g and b unchanged
```

### BLOCK 2 (9:15–10:30 AM): Struct Review — Write from Memory
From a blank file, write BOTH of these from memory (no references):
1. `Student` struct + `calc_average()` + `sort_by_average()` — should take under 15 min
2. `bit_macros.h` — SET_BIT, CLEAR_BIT, TOGGLE_BIT, READ_BIT — should take under 5 min

If you can do both without looking → you've solidified Week 4.

### GIT PUSH (10:30–11:00 AM)
```bash
cd ~/C-Practice
git add week4/
git commit -m "Week 4: structs (Student, Employee, geometry), bitwise macros, linked list node preview"
git push origin main
```

Write `week4/README.md`:
- List every file in week4/
- One sentence per file
- Section "Key insight": explain the arrow operator `->` in your own words

### REST + LUNCH (11:00 AM–12:00 PM)

### GERMAN (12:00–2:00 PM)
- Nicos Weg Lessons 28–29
- Anki mega review (clear all pending — aim for 65+ words total)
- Write German from memory: daily routine + what you are studying

### EXTENDED CODING (2:00–4:00 PM): GPIO Register Simulator
```
week4/
├── gpio_sim.h      — GPIO struct + function declarations
├── gpio_sim.c      — Implementation
└── gpio_main.c     — Demo: configure pins, set/clear/toggle, read state
```

**gpio_sim.h** — simulate a real GPIO peripheral:
```c
#ifndef GPIO_SIM_H
#define GPIO_SIM_H

#include <stdint.h>
#include "bit_macros.h"

typedef enum {
    GPIO_MODE_INPUT  = 0b00,
    GPIO_MODE_OUTPUT = 0b01,
    GPIO_MODE_ALTFN  = 0b10,
    GPIO_MODE_ANALOG = 0b11
} GPIO_Mode;

typedef struct {
    uint32_t MODER;   // Mode register (2 bits per pin)
    uint32_t ODR;     // Output Data Register (1 bit per pin)
    uint32_t IDR;     // Input Data Register  (1 bit per pin, read-only in hardware)
    uint32_t BSRR;    // Bit Set/Reset Register
} GPIO_Regs;

void gpio_set_mode(GPIO_Regs *gpio, uint8_t pin, GPIO_Mode mode);
void gpio_write_pin(GPIO_Regs *gpio, uint8_t pin, uint8_t value);
void gpio_toggle_pin(GPIO_Regs *gpio, uint8_t pin);
uint8_t gpio_read_pin(const GPIO_Regs *gpio, uint8_t pin);
void gpio_print_state(const GPIO_Regs *gpio, const char *name);

#endif
```

Implement all functions. Use your bit macros wherever possible. The MODER register uses 2 bits per pin (so pin N uses bits 2N and 2N+1).

> This is the EXACT same struct layout as real STM32 GPIO registers. In July Phase 2 (August), the only change will be: `GPIO_Regs *gpio = (GPIO_Regs *)0x40020000;` — the struct pointer will point to real hardware memory.

---

## WEEK 4 CHECKPOINT (Monday July 6, 4:00 PM)

Update PROGRESS.md now. Be honest.

| Checkpoint Item | Done? |
|:---|:---|
| Struct with members, constructor, typedef — written from scratch | |
| Arrow operator -> understood and used correctly | |
| Array of structs: sort by field using bubble sort | |
| Bitwise: AND, OR, XOR, NOT, shifts — all demonstrated | |
| SET_BIT / CLEAR_BIT / TOGGLE_BIT / READ_BIT macros written from memory | |
| GPIO register simulator using struct + bit macros | |
| struct Node with self-referential pointer built | |
| GitHub: week4 pushed with README | |
| Nicos Weg: Lessons 23–29 done | |
| Anki: 65+ German words total | |
| K.N. King Ch 16 + Ch 20 (first half) read | |

**Self-rating (structs + bitwise 1–10)**: ___ (minimum 6 before Week 5)

---

## WEEKDAY THEORY FOCUS (Week 4)

| Day | Read Before Gym | Bed Read |
|:---|:---|:---|
| Wed Jul 1 | K.N. King Ch 16 pp. 20–40 | K&R Ch 6 pp. 127–145 |
| Thu Jul 2 | K.N. King Ch 16 pp. 40–end | K&R Ch 6 pp. 145–165 |
| Fri Jul 3 | K.N. King Ch 20 pp. 1–20 | K&R Ch 2 pp. 48–53 |
| Mon Jul 6 | K.N. King Ch 20 pp. 20–40 | K&R Ch 6 — re-read self-referential structs |

> Bitwise operations feel abstract until you see them control hardware.
> The GPIO simulator this week makes them concrete. After writing SET_BIT/CLEAR_BIT, you will never forget them.
