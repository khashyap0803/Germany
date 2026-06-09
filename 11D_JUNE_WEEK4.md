# JUNE WEEK 4 (Jun 30) — Phase 1 Week 4 Day 1: STRUCTS BEGIN

> **Topics**: Introduction to structs — struct declaration, member access, struct as function argument
> **K.N. King Reading**: Chapter 16 (Structures — first 20 pages today, continue in July)
> **AI Policy**: BANNED for code — AI may only explain concepts
> **Date**: Tuesday June 30, 2026 (one day only — Week 4 continues in 12A_JULY_WEEK1.md)

---

## TUESDAY JUNE 30 — Week 4 Day 1 (Weekday — Theory Only)

### Pre-Gym (5:00–5:25 AM)
**Read**: K.N. King Chapter 16 (Structures — pages 1–20)

Topics to understand from today's reading:
- `struct` keyword: grouping related variables under one name
- Member declaration: `struct Person { char name[50]; int age; float salary; };`
- Creating a struct variable: `struct Person p1;`
- Accessing members: dot operator `p1.name`, `p1.age`
- Initializing at declaration: `struct Person p1 = {"Khashyap", 23, 37000.0};`
- Struct assignment: `p2 = p1;` copies ALL members (unlike arrays)
- Passing struct to function: struct is copied (just like int) — not by reference
- Passing struct by pointer: `void update(struct Person *p)` + `p->age = 25;`
- Arrow operator `->`: shorthand for `(*ptr).member`

Draw on paper (before gym):
```
struct Person p = {"Khashyap", 23, 37000.0};

Memory (stack):
┌──────────────────────┐
│ name: "Khashyap\0..." │  (50 bytes)
│ age: 23              │  (4 bytes + padding)
│ salary: 37000.0      │  (4 bytes)
└──────────────────────┘
p.age  = direct access
p->age = invalid (p is not a pointer)

struct Person *ptr = &p;
ptr->age  = valid (pointer + arrow)
(*ptr).age = valid but ugly
```

**Bed Reading (9:30–10:00 PM)**: K.N. King Ch 16 pages 20–40
- Nested structs: struct inside struct
- Array of structs: `struct Person employees[100];`
- Why `employees[i].name` works
- typedef with struct: `typedef struct { ... } Person;` — then use `Person` not `struct Person`
- When to pass by value vs by pointer (hint: if struct is large, pass by pointer to avoid copying)

---

## BRIDGE TO JULY

Week 4 continues in `12A_JULY_WEEK1.md` (Jul 1–7).

| What's coming in Jul 1–7 (Week 4 full): |
|:---|
| Saturday Jul 5: Write 5+ struct programs (Student, Point, Complex, Employee, Linked list node) |
| Sunday Jul 6: Bitwise operations — AND, OR, XOR, NOT, shifts, set/clear/toggle bit macros |
| K.N. King Ch 16 (Structures complete) + Ch 20 (Low-Level Programming — bitwise) |
| FIRST struct program: `student_db.c` — array of structs, sort by grade, find by name |

> Today (June 30) is reading only. No coding on weekdays.
> The struct coding blocks are in the July files.

---

## JUNE 2026 — PHASE 1 WEEKS 1–3 COMPLETE

By end of June 30 you should have:

| June Achievement | Status |
|:---|:---|
| WSL2 + gcc working, ZERO-warning builds | |
| 15+ C programs written (Weeks 1-3 weekend coding) | |
| Understood and can explain: variables, loops, functions, arrays | |
| Strings: my_strlen, my_strcmp, my_strcpy from scratch | |
| Multi-file: .h + .c separation, include guards | |
| POINTERS: swap by pointer, pointer arithmetic, malloc/free | |
| Valgrind: all programs 0 leaks | |
| mycodeschool 15 pointer videos watched | |
| GitHub C-Practice: at least 3 commits (Week 1 + Week 2 + Week 3) | |
| Nicos Weg: Lessons 1–22 complete | |
| Anki: 50+ German words | |
| K.N. King Ch 1–13 + K&R Ch 1–5 read | |

> July begins tomorrow. The first coding weekend of July is Jul 4–5 (Sat–Sun).
> See `12A_JULY_WEEK1.md` for the full Week 4 plan.
