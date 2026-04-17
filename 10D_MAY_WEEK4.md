# 📅 WEEK 4 — May 19-25 (Tue-Mon): STRUCTS + BITWISE — Gateway to STM32

> **Topics**: struct, typedef, nested structs, pointer to struct, bitwise operators, bit manipulation, register simulation
> **K&R Chapters**: Chapter 6 (Structures), Chapter 2 revisit (Bitwise section pp. 48-53)
> **Programs to write**: 10-12
> **German**: Nicos Weg Lessons 16-20, food vocab, daily routine sentences
> **Embedded Connection**: THIS week is the bridge to hardware. Structs = how STM32 peripheral registers are organized. Bitwise = how you read/write individual register bits.

---

## DAY 19 — Tuesday, May 19

### 🔶 Morning (5:10-6:30 AM) — struct Basics

**What to learn**: A struct groups related data together. Instead of separate arrays for name, CGPA, branch — you create ONE `struct Student` that holds all three.

**How to learn**:
1. **(5:10-5:20)** Read **K&R Chapter 6** pages 127-133 (Structure basics). Notice how K&R introduces structs for representing points and rectangles — very elegant.

2. **(5:20-5:50)** Write `struct_basics.c`:
   - Define: `struct Student { char name[50]; float cgpa; char branch[30]; int year; };`
   - Use `typedef` to create a cleaner alias: `typedef struct Student Student;` — now you write `Student s;` instead of `struct Student s;`
   - Create a student, fill in values, print everything
   - Create an array of 3 students, fill them, print in table format
   - **What to understand**: Struct members are stored contiguously in memory (with possible padding for alignment). Draw the memory layout on paper!
   - **Ask Google AI**: "Explain struct padding and alignment in C. Why does `sizeof(struct)` sometimes give a larger number than I expect?"

3. **(5:50-6:20)** Write `struct_functions.c`:
   - Write `void print_student(Student s)` — pass struct by VALUE (copies entire struct!)
   - Write `void print_student_ptr(Student *s)` — pass by POINTER (efficient, no copy)
   - Use arrow operator for pointer: `s->name` instead of `(*s).name`
   - **KEY**: In embedded, you ALWAYS pass structs by pointer (by reference) because RAM is limited. Copying a 100-byte struct every function call wastes stack.
   - Write `void update_cgpa(Student *s, float new_cgpa)` — modifying through pointer

4. **(6:20-6:30)** Draw memory diagram comparing `Student s` (on stack) vs `Student *s` (pointer to struct, struct might be on heap).

### 🎧 Commute: Nicos Weg Lesson 16 (food vocabulary: das Brot, die Milch) | 📱 Lunch: Anki | 📖 Bed: K&R pp. 133-140

### ✅ Day 19: `struct_basics.c` + `struct_functions.c`. Understand `->` operator.

---

## DAY 20 — Wednesday, May 20

### 🔶 Morning (5:10-6:30 AM) — Array of Structs + Real-World Data

**What to learn**: Arrays of structs are HOW data is organized in every embedded system — sensor readings, configuration parameters, task lists, peripheral descriptors.

**How to learn**:
1. **(5:10-5:45)** Rewrite your Week 2 student records program using structs:
   Write `student_system.c`:
   - `Student students[MAX_STUDENTS];`
   - Functions: `add_student()`, `find_by_name()`, `sort_by_cgpa()`, `print_all()`
   - Compare with the parallel arrays version — how much CLEANER is the struct version?
   - **This is the difference between beginner and intermediate C.** Structs make code readable and maintainable.

2. **(5:45-6:15)** Write `university_db.c`:
   - Define nested structs:
     ```
     struct Requirement { float min_cgpa; float min_ielts; int need_experience; };
     struct University { char name[50]; char city[30]; struct Requirement req; };
     ```
   - Create an array of YOUR target universities (FH Dortmund, HS Bremerhaven, etc.)
   - Write a function `int check_eligibility(University *uni, float my_cgpa, float my_ielts)`
   - **Nested structs** = how STM32 peripheral definitions work. `GPIO->MODER` is a struct member of a struct.

3. **(6:15-6:30)** Write `sizeof_struct.c`:
   - Print sizeof for each of your structs
   - Try `__attribute__((packed))` — see how it changes size (removes padding)
   - **Embedded insight**: Packed structs are used when you need exact memory layout (parsing protocol packets, reading sensor registers)

### 🎧 Commute: Nicos Weg Lesson 17 | 📱 Lunch: Anki (German articles quiz yourself) | 📖 Bed: K&R pp. 140-148

### ✅ Day 20: `student_system.c` + `university_db.c` + `sizeof_struct.c`. Nested structs mastered.

---

## DAY 21 — Thursday, May 21

### 🔶 Morning (5:10-6:30 AM) — Dynamic Structs + Linked List Preview

**What to learn**: Allocating structs dynamically with malloc. Self-referential structs (a struct that contains a pointer to itself = linked list node).

**How to learn**:
1. **(5:10-5:40)** Write `dynamic_structs.c`:
   - Allocate a single student: `Student *s = malloc(sizeof(Student));`
   - Fill values using `->` operator
   - Allocate an array of N students: `Student *arr = malloc(n * sizeof(Student));`
   - Access using `arr[i].name` or `(arr + i)->name`
   - Free everything. Run Valgrind.

2. **(5:40-6:15)** Write `linked_list_intro.c`:
   - Define: `typedef struct Node { int data; struct Node *next; } Node;`
   - Draw on paper:
     ```
     [data=10|next] → [data=20|next] → [data=30|next] → NULL
     ```
   - Create 3 nodes manually (malloc each one), link them, traverse and print
   - Don't implement insert/delete yet — just understand the CONCEPT
   - **Why linked lists matter for embedded**: FreeRTOS task lists, message queues, timer lists — ALL are linked lists internally

3. **(6:15-6:30)** Re-draw the linked list on paper. Can you visualize what `head->next->next->data` means?

### 🎧 Commute: Nicos Weg Lesson 18 | 📱 Lunch: Anki | 📖 Bed: K&R pp. 148-155 (Self-referential structures)

### ✅ Day 21: `dynamic_structs.c` + `linked_list_intro.c`. Valgrind clean. Paper diagrams done.

---

## DAY 22 — Friday, May 22

### 🔶 Morning (5:10-6:30 AM) — BITWISE OPERATORS 🔧

**What to learn**: `&` (AND), `|` (OR), `^` (XOR), `~` (NOT), `<<` (left shift), `>>` (right shift). These are HOW you talk to hardware registers.

**How to learn**:
1. **(5:10-5:20)** Read **K&R pages 48-53** (Bitwise operators section). ALSO read **Beej's Guide** section on bitwise — it has better diagrams.

2. **(5:20-5:50)** Write `bitwise_basics.c`:
   - Print numbers in binary using a function: `void print_binary(unsigned int n, int bits)`
   - Test ALL operators:
     - `0b1100 & 0b1010` = `0b1000` (AND — both bits must be 1)
     - `0b1100 | 0b1010` = `0b1110` (OR — either bit can be 1)
     - `0b1100 ^ 0b1010` = `0b0110` (XOR — exactly one bit must be 1)
     - `~0b1100` = flip all bits
     - `1 << 3` = `0b1000` (shift 1 left by 3 positions = bit 3)
   - **KEY INSIGHT**: `1 << n` = "set bit n". This is the MOST USED pattern in embedded C.

3. **(5:50-6:20)** Write `bit_macros.c` — THE 4 macros you'll use on every STM32 project:
   - `SET_BIT(reg, bit)` — set a bit to 1: `reg |= (1 << bit)`
   - `CLEAR_BIT(reg, bit)` — set a bit to 0: `reg &= ~(1 << bit)`
   - `TOGGLE_BIT(reg, bit)` — flip a bit: `reg ^= (1 << bit)`
   - `CHECK_BIT(reg, bit)` — read a bit: `(reg >> bit) & 1`
   - Test each macro, print binary before and after
   - **THESE 4 MACROS ARE THE FOUNDATION OF ALL EMBEDDED PROGRAMMING.** Memorize them.

4. **(6:20-6:30)** Test: Can you write all 4 macros from memory? If not, practice until you can.

### 🎧 Commute: Nicos Weg Lesson 19 | 📱 Lunch: Anki | 📖 Bed: K&R bitwise exercises

### ✅ Day 22: `bitwise_basics.c` + `bit_macros.c`. ALL 4 bit macros memorized.

---

## DAY 23 — Saturday, May 23 🟩 BIG DAY

### 💻 Warmup (6:30-7:30 AM) — Bit Manipulation Patterns

**What to learn**: Common bit manipulation patterns used in embedded firmware — bit fields, masks, extracting values from registers.

**How to learn**:
1. **(6:30-6:55)** Write `bit_patterns.c`:
   - Set multiple bits at once using a mask: `reg |= (0b11 << 4)` — sets bits 4 and 5
   - Clear specific bits using a mask: `reg &= ~(0b11 << 4)` — clears bits 4 and 5
   - Extract a field: `value = (reg >> 4) & 0b11` — get bits 5:4 as a 2-bit number
   - **Real embedded example**: STM32 GPIO MODER register uses 2 bits per pin.
     - Pin 5 mode is at bits [11:10]
     - To set pin 5 as output: `GPIOA->MODER |= (0b01 << (5 * 2))`
     - To clear pin 5 mode first: `GPIOA->MODER &= ~(0b11 << (5 * 2))`

2. **(6:55-7:20)** Write `flags.c`:
   - Use a single `uint8_t` to store 8 boolean flags (instead of 8 separate `int` variables)
   - Define: `#define FLAG_LED    (1 << 0)`, `#define FLAG_MOTOR  (1 << 1)`, `#define FLAG_BUZZER (1 << 2)`
   - Set flag: `status |= FLAG_LED;`
   - Check flag: `if (status & FLAG_LED) { ... }`
   - Clear flag: `status &= ~FLAG_LED;`
   - **Memory saved**: 1 byte for 8 flags vs 32 bytes for 8 ints. On a micro with 20KB RAM, this matters!

3. **(7:20-7:45)** Write `rgb_color.c`:
   - Pack RGB color into a single `uint32_t`: `color = (r << 16) | (g << 8) | b`
   - Extract components: `r = (color >> 16) & 0xFF`, `g = (color >> 8) & 0xFF`, `b = color & 0xFF`
   - This is EXACTLY how display drivers encode pixel colors

4. **(7:50-8:00)** Quick test: Given `uint32_t reg = 0x0000F0F0`, what are bits 15:12? Calculate by hand, then verify with code.

### 📖 Evening: Beej's Guide — bitwise section review

### ✅ Day 23: `bit_patterns.c` + `flags.c` + `rgb_color.c`. Bit field extraction understood.

> **Note**: Day 23 is Saturday. Use the full Saturday template from the overview for time slots. The morning session times above are just the warmup — continue with Deep Sessions 1-3 (7:45 AM-12:45 PM) working on these programs. German 2:00-5:00 PM.

---

## DAY 24 — Sunday, May 24 🟨 REVIEW + GPIO SIMULATOR

### 💻 Warmup (7:30-8:30) — Struct + Bitwise Review
- Write all 4 bit macros from memory
- Create a struct from memory
- Quick 20-min review of toughest concepts

### 💻 Deep Session 1-3 (8:45 AM-12:45 PM) — GPIO Register Simulator

**THE CAPSTONE PROJECT for Weeks 3-4.** This combines structs + bitwise and simulates a real STM32 GPIO port.

Write `register_simulator.c`:

**What you're building**: A simulation of the STM32 GPIO peripheral — same registers, same bit fields, same operations — running on your PC.

**Approach** (spend 4-5 hours on this):
1. Define a GPIO struct with registers: MODER, ODR, IDR, BSRR
2. Each register is a `uint32_t` (32 bits, just like real STM32)
3. Implement functions:
   - `gpio_set_mode(GPIO *port, int pin, int mode)` — set pin mode (input/output/alt/analog)
   - `gpio_write_pin(GPIO *port, int pin, int value)` — set pin high or low
   - `gpio_read_pin(GPIO *port, int pin)` — read pin state
   - `gpio_toggle_pin(GPIO *port, int pin)` — toggle pin
4. ADD `print_register(uint32_t reg, char *name)` — print register in binary with bit labels
5. Write a `main()` that simulates: set PA5 as output → turn on LED → toggle it 5 times → read state

**Reference**: Open the STM32F411 reference manual (you have CubeIDE installed → Help → Reference Manual), look at GPIO chapter. Compare YOUR register layout with the REAL one.

**Why this matters**: When you start STM32 in July, you'll write `GPIOA->MODER |= (1 << 10);` and you'll ALREADY know what it does. Most people hit STM32 with zero bitwise knowledge and get stuck for weeks.

**Tracker Roadmap Connection**: This directly maps to your Embedded_Systems_Tracker Week 04 "ARM Cortex-M Architecture & STM32 MCU Deep Dive" and Week 05-06 C foundations.

### 🇩🇪 German (2:00-5:00) — Sunday template
- Nicos Weg Lessons 19-20
- Google AI: Practice describing your daily routine in German:
  - "Ich stehe um fünf Uhr auf" (I wake up at 5)
  - "Ich gehe zur Arbeit" (I go to work)
  - "Ich lerne C-Programmierung" (I learn C programming)
- Anki: mega review + 10 new daily routine cards

### ✅ Day 24: `register_simulator.c` COMPLETE. This is your most important program of the month.

---

## DAY 25 — Monday, May 25 🟦 WEEKDAY

### 🔶 Morning (5:10-6:30 AM) — Quick Struct + Bitwise Drill

From memory, write:
1. A struct for sensor data (timestamp, temp, humidity)
2. The 4 bit manipulation macros (SET, CLEAR, TOGGLE, CHECK)

> **Note**: Full polish, Git push, and German mega review happen next Saturday (Day 30). This is a quick reinforcement.

### 🎧 Commute: Review Nicos Weg 16-20 | 📱 Lunch: Anki | 📖 Bed: K&R Chapter 6 review

---

## 📊 WEEK 4 SUMMARY

| Metric | Target | Done? |
|:---|:---|:---|
| Programs written | 10+ (cumulative 40+) | [ ] |
| Register simulator | COMPLETE and on GitHub | [ ] |
| Bit macros | All 4 from MEMORY | [ ] |
| K&R Chapter 6 | Read completely | [ ] |
| Nicos Weg lessons | 16-20 (cumulative: 20) | [ ] |
| German words in Anki | 70+ (cumulative) | [ ] |
| German sentences | Say 15 from memory | [ ] |
