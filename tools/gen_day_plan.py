# Generates the day-by-day plan (Oct 5, 2026 -> Oct 1, 2028) from real Udemy section lists.
import json, datetime as dt, io, sys

D = dt.date
def rng(a, b):
    d = a
    while d <= b:
        yield d
        d += dt.timedelta(days=1)

# ---------------------------------------------------------------- course queues (real sections, video minutes)
FASTBIT_C = [("§8 Microcontroller and Hello World",43),("§9 Build process",9),("§10 Analyzing Embedded C code",50),
 ("§13 Pointers",43),("§14 Importance of <stdint.h>",11),("§17 Bitwise operators",22),("§18 Embedded C exercise for LED",52),
 ("§19 Bitwise shift operators",16),("§21 Type qualifier 'const'",20),("§22 Pin-read",13),("§23 Optimization",15),
 ("§24 'volatile' type qualifier",25),("§25 Structures and Bit fields",72),("§26 Unions",11),("§27 Bit-fields in embedded code",22),
 ("§28 Keypad interfacing",38),("§31 Pre-processor directives",39)]
ARM = [("§1–4 Intro, IDE, Embedded Hello World",66),("§5 Access level and operation modes",43),("§6 ARM GCC inline assembly",39),
 ("§7 Reset sequence",7),("§8 Access level and T bit",22),("§9 Memory map and bus interfaces",41),("§10 Stack memory and placement",66),
 ("§11 Exception model",62),("§12 Interrupt priority and configuration",33),("§13 Exception entry and exit",17),
 ("§14 Fault handling and analysis",73),("§15 Exceptions for system-level services",55),("§16 Implementation of a task scheduler",153),
 ("§17 Bare-metal embedded and linker scripts",236)]
MCU1 = [("§1–5 Notes, board, CubeIDE project",55),("§6 Debugging tips and tricks",60),("§7–8 Memory map, bus interfaces",55),
 ("§9–10 Clocks and clock tree",76),("§11–12 Vector table, NVIC, interrupt design",55),("§13 'volatile' keyword",18),
 ("§14–18 GPIO concepts and registers",77),("§19–23 GPIO driver: headers, structures, API design",90),
 ("§24–27 GPIO driver: init, read/write, exercise",82),("§28–29 GPIO pin interrupts + exercise",94),("§30 MCU I/O pin specifications",44),
 ("§31–35 SPI bus, NSS, CPOL/CPHA, clock",66),("§36–40 SPI driver: init, send + exercise",101),("§41 STM32 master + Arduino slave",33),
 ("§42–47 SPI receive, interrupts, IRQ handling",117),("§48–52 I²C protocol basics",54),("§53–56 I²C driver: init, master send",83),
 ("§57–58 I²C pull-ups, rise time + exercise",51),("§59–60 I²C master receive + exercise",62),("§61–64 I²C interrupts, IRQ handler",97),
 ("§65–67 I²C slave + common problems",47),("§68–73 UART/USART driver, baud rate",97),("§74–75 USART interrupts, RTC on LCD",195)]
DMA = [("§1 DMA getting started, multi-AHB architecture",73),("§2,5 Board + STM32CubeMX code generation",55),
 ("§6 DMA exercises: GPIO polling and interrupt",52),("§7 DMA: UART to SRAM",31),("§8 DMA functional block diagram",33),
 ("§9 DMA: ADC to SRAM",37),("§10–11 Arbiter, priorities, transfer modes, FIFO",39),("§12 DMA from scratch (register level)",181)]
DSP = [("§1–2 Setting up, getting started",164),("§3 Signal statistics and noise",34),("§4 Quantization and sampling theorem",35),
 ("§5–6 Cortex-M DSP features, linear systems",28),("§7 Convolution",117),("§8 Discrete Fourier Transform",71),
 ("§9 Clock tree for maximum speed",57),("§10 Digital filter design",105),("§11 DSP on live sensor data",81),
 ("§12–13 FIFO + background sampling thread",56),("§14 DSP on blocks of sensor data",61),
 ("§25–27 (old version) FIR, IIR, windowed-sinc design",49),("§29–30 (old version) DSP instructions on Cortex-M",36)]
RTOS = [("§1–5 RTOS intro, FreeRTOS project for STM32",119),("§6 Task creation",81),("§7 Trace tool integration",66),
 ("§8–11 Idle/timer task, scheduler, context switching",69),("§12–13 SEGGER SystemView, LEDs and tasks",63),
 ("§14–16 Task states, delay APIs, notifications",58),("§17–19 Licensing, memory/stack, task deletion",74),
 ("§20–22 Interrupt vs task priority, ISR-safe APIs, hooks",83),("§23 Queue management",151),("§24–25 Semaphores, mutual exclusion",77)]
ORCAD = [("§1–3 Intro, install, introduction to PCBs",86),("§4 Introducing OrCAD/Allegro",148),("§5 Symbol creation (IEEE)",447),
 ("§6 Schematic creation in OrCAD Capture",218),("§7 Footprint creation",491),("§8 Switching to PCB Designer",103),
 ("§9 Board shapes and restrictions",80),("§10 Placement",104),("§11 Layer stack-up",35),("§12 Constraint Manager",71),
 ("§13 Routing",118),("§14 Vias",42),("§15 2-layer board assignments",25),("§16 4-layer board design",147),("§17 Gerbers and documentation",91)]
MCU2 = [("§6–7 STM32 HAL architecture and program flow",213),("§8 Clocks and PLL",118),("§9 Timers",106),
 ("§10 Input capture",94),("§11–12 Output compare, PWM",90),("§20–22 Low-power modes, WFI/WFE",121),
 ("§23–28 Voltage domains, current measurement, standby",134),("§29–32 RTC, alarms, interrupts",119)]
ISO = [("§1 Why risk management matters",123),("§2 Medical device development",256),("§3 Risk management per ISO 14971",263),
 ("§4 Production and post-production",170),("§5 Therac-25 case study",127)]
ENG_MIN = [48,101,7,3,0,54,62,68,63,55,75,59,52,35,43,33,60,47,55,48,52,49,0,46,42,46,44,35,34,1,36,38,35,0,45,40,41,34,34,29,34,27,38,38,33,1,57,40,0,51,31,29,29,38,34,26,27,0,35,35,33,31,26,35,30,24,1,30,32,38,31,29,25,30,36,0,28,35,36,23,38,24,24,1,40,38,27,31,32,25,1,24,28,25,23,24,22,1,29,19,22,23,25,25,0,29,53,0,28,22,17,2,18,163,2,18,17,26,25,29,19,24,28,30,29,22,30,30,32,37,34,26,28,24,33,31,52,36,34,28,33,25,105,43,76,92,81,88,0,0,0,34,0,0]
ENG = [(f"§{i+1}", m) for i, m in enumerate(ENG_MIN) if m > 0]
IELTS = [("§1–3 Overview, exam info, diagnostics",30),("§4 Listening basics",26),("§5 Listening Part 1",223),("§6 Listening Part 2",240),
 ("§7 Listening Part 3",159),("§8 Listening Part 4",160),("§9 Multiple-choice strategy",110),("§10 Fill-the-blank strategy",59),
 ("§11–12 Listening practice + exit tests",214),("§13–14 Academic Reading basics, scanning",45),("§15 Academic Reading question types",971),
 ("§16 Reading live class recordings",303),("§23 Computer-based test overview",208),("§24 Writing Task 1 (Academic)",352),
 ("§25 Task 1 live class",79),("§28 Writing Task 2 overview",83),("§29 Task 2 writing process",259),("§30 Speaking strategy",89),
 ("§31 Speaking Part 1",277),("§32 Speaking Part 2",81),("§33 Speaking Part 3",205),("§34 Full speaking test + AI role play",156),
 ("§35 Student speaking tests analysed",323)]

class Q:
    def __init__(s, name, secs, speed):
        s.name, s.items, s.speed, s.i, s.left = name, [list(x) for x in secs], speed, 0, (secs[0][1] if secs else 0)
    def done(s): return s.i >= len(s.items)
    def take(s, study_min):
        """consume study minutes; returns label like 'ARM Cortex-M: §5 ... ; §6 ... (cont.)' or None"""
        if s.done(): return None
        budget = study_min * s.speed  # video minutes coverable
        parts = []
        while budget > 0 and not s.done():
            title, total = s.items[s.i]
            use = min(budget, s.left)
            partial = use < s.left or s.left < total
            parts.append(title + (" (part)" if partial else ""))
            s.left -= use; budget -= use
            if s.left <= 0.5:
                s.i += 1
                if not s.done(): s.left = s.items[s.i][1]
        return f"{s.name}: " + " · ".join(parts)
    def peek(s):
        return None if s.done() else s.items[s.i][0]

qC   = Q("FastBit Embedded C", FASTBIT_C, 1.25)
qARM = Q("Udemy ARM Cortex-M3/M4", ARM, 0.75)
qM1  = Q("FastBit MCU1", MCU1, 0.75)
qDMA = Q("Udemy DMA Demystified", DMA, 0.75)
qDSP = Q("Udemy DSP From Ground Up", DSP, 0.75)
qRT  = Q("Udemy Mastering RTOS", RTOS, 0.75)
qOR  = Q("Udemy OrCAD/Allegro", ORCAD, 0.75)
qM2  = Q("FastBit MCU2", MCU2, 0.75)
qISO = Q("Udemy ISO 14971", ISO, 1.0)
qENG = Q("English Master Course", ENG, 1.25)
qIEL = Q("IELTS Band 7+ course", IELTS, 1.25)

P1 = ["Create repo `stm32-baremetal-drivers`: folders drivers/, examples/, docs/; README skeleton",
 "GPIO driver: register header (base addresses, GPIO_RegDef_t) + clock-control macros",
 "GPIO driver: init, read, write, toggle — LED + button example on Black Pill",
 "GPIO interrupt example (EXTI) — capture the edge on the logic analyzer, save screenshot",
 "SPI driver: init + send — capture CLK/MOSI on SLogic, check CPOL/CPHA",
 "SPI receive / loopback test",
 "I²C driver: master send/receive — read BMP280 chip-ID (0x58)",
 "I²C: read raw BMP280 temperature, print it",
 "USART driver: printf at 115200 baud — capture a frame, verify the bit time",
 "Clean-up: consistent naming, comments that explain WHY, zero warnings",
 "README: block diagram, wiring table, captures, what went wrong and how you fixed it",
 "Tag v1.0 and push — Project 1 done ✅"]
P2 = ["Read the AD8232 datasheet: block diagram, filters, RLD, lead-off — write 1 page of notes",
 "Wire AD8232 + electrodes. ⚠️ Laptop on battery only, never on mains while electrodes are attached",
 "ADC single conversion of AD8232 output → print over UART",
 "Timer-triggered ADC at 250 Hz",
 "ADC + DMA into a circular double buffer",
 "Stream samples to PC; live plot with Python (pyserial + matplotlib)",
 "Record 60 s of your own ECG to CSV; Design History File entry #1",
 "Design filters offline in Python: baseline high-pass + 50 Hz notch",
 "Port the high-pass to STM32 (CMSIS-DSP biquad)",
 "Add the 50 Hz notch on STM32; compare raw vs filtered",
 "FFT before/after filtering — confirm the 50 Hz peak is gone",
 "R-peak detection (derivative + threshold)",
 "Heart rate from R-R intervals; print bpm, compare with a pulse oximeter or your pulse",
 "Lead-off detection → LED",
 "README: block diagram, plots, filter design, failures and fixes",
 "DHF summary; tag v1.0 and push — Project 2 done ✅"]
P3 = ["Write requirements for the ECG board (power, AD8232, connector to Black Pill, test points)",
 "Create / import symbols in OrCAD Capture",
 "Schematic: power (USB + LDO), AD8232 reference circuit, headers, test points",
 "Schematic review against the AD8232 datasheet reference design",
 "Footprints for every part (check against datasheets)",
 "Placement: keep analog front-end away from digital/USB",
 "2-layer stack-up + constraints",
 "Routing + ground pour",
 "DRC + 3D view check; fix every error",
 "Gerbers + BOM; order 5 boards",
 "Assemble; first power-up on a current-limited supply",
 "Bring-up: run Project 2 firmware on the new board",
 "FreeRTOS: acquisition task, DSP task, UART task with queues",
 "Measure noise floor vs the breadboard version",
 "README + photos; DHF; tag v1.0 — Project 3 done ✅"]
P4 = ["Nordic DevAcademy: nRF Connect SDK Fundamentals — lessons 1–2 (setup, first app)",
 "nRF Connect SDK Fundamentals — lessons 3–4 (GPIO, logging)", "nRF Connect SDK Fundamentals — lessons 5–6 (I²C, multithreading)",
 "nRF Connect SDK Fundamentals — remaining lessons", "Bluetooth LE Fundamentals — lessons 1–2 (advertising)",
 "BLE Fundamentals — lessons 3–4 (connections, GATT)", "BLE Fundamentals — remaining lessons (custom service)",
 "Read about essential tremor vs Parkinson's tremor frequency bands (4–6 Hz vs 4–12 Hz); notes (`Startup/15`)",
 "IMU (e.g. MPU6050/LSM6DS3) on nRF52 over I²C; stream accelerometer data",
 "Sample IMU at 100 Hz; save recordings of still hand vs simulated tremor",
 "FFT of IMU data; dominant tremor frequency", "Stream tremor frequency over a custom BLE characteristic",
 "Phone app: nRF Connect / simple Python BLE client to log data",
 "Add EMG or ECG channel (AD8232) to the wearable", "Power: LiPo + charger, measure current, sleep between samples",
 "Enclosure: 3D print or strap", "Risk table for your prototype (ISO 14971 style)",
 "README + demo video + DHF", "Tag v1.0 — Project 4 done ✅"]

# ---------------------------------------------------------------- Phase 0 (from 18_RESTART_8_WEEKS.md)
P0_SAT = {D(2026,10,10):"K.N. King Ch 1–3. Check `gcc --version`. Rewrite your 7 week-1 programs properly (`int main(void)`, `return 0;`, `\\n`, zero warnings with `-Wall -Wextra`). Push.",
 D(2026,10,17):"K.N. King Ch 4–5 — expressions, if/else, switch. Write 4–5 programs.",
 D(2026,10,24):"K.N. King Ch 6 — loops. Patterns, prime check, digit reverse.",
 D(2026,10,31):"K.N. King Ch 7–8 — basic types, arrays. Max/min/average, bubble sort.",
 D(2026,11,7):"🪔 Diwali buffer — 1 hour if you can: redo anything weak from weeks 1–4.",
 D(2026,11,14):"K.N. King Ch 9–10 — functions, multi-file programs (.h + .c).",
 D(2026,11,21):"K.N. King Ch 11 — POINTERS. Draw every diagram on paper. `swap()` with pointers.",
 D(2026,11,28):"K.N. King Ch 12 — pointers & arrays. Then from memory: `swap()`, `my_strlen()`, bubble sort."}
P0_SUN = {D(2026,10,11):"Voltage, current, resistance, Ohm's law (Neso Academy). Measure a resistor and a battery with the multimeter.",
 D(2026,10,18):"Series & parallel, voltage divider — build one, measure Vout, check the formula.",
 D(2026,10,25):"KVL & KCL — build a 3-resistor circuit, measure, verify both laws.",
 D(2026,11,1):"LED + current-limiting resistor; pull-up / pull-down with a button.",
 D(2026,11,8):"🪔 Diwali — off.",
 D(2026,11,15):"Capacitors — charge/discharge, RC time constant (measure it).",
 D(2026,11,22):"RC low-pass filter — build it, see the corner frequency (same idea as ECG noise filtering).",
 D(2026,11,29):"Diode basics + transistor as a switch (drive an LED). Then the RESTART REVIEW (criteria in `18`)."}
P0_READ = {}  # weekday reading = next Saturday's chapters
P0_SHORT = {D(2026,10,10):"K.N. King Ch 1–3", D(2026,10,17):"K.N. King Ch 4–5", D(2026,10,24):"K.N. King Ch 6 (loops)",
 D(2026,10,31):"K.N. King Ch 7–8 (types, arrays)", D(2026,11,7):"re-read your weakest chapter so far", D(2026,11,14):"K.N. King Ch 9–10 (functions, program organisation)",
 D(2026,11,21):"K.N. King Ch 11 (pointers) — draw the diagrams", D(2026,11,28):"K.N. King Ch 12 (pointers and arrays)"}
for sat, txt in P0_SHORT.items():
    for k in range(1, 6):
        P0_READ[sat - dt.timedelta(days=k)] = txt

# ---------------------------------------------------------------- Phase 1 (Dec 2026 – Jan 2027)
P1_SAT = {D(2026,12,5):"K.N. King Ch 13 Strings — write my_strlen, my_strcpy, my_strcmp, my_strcat from scratch (content: `11B`)",
 D(2026,12,12):"K.N. King Ch 14–15 Preprocessor + writing large programs — multi-file calculator with header guards",
 D(2026,12,19):"K.N. King Ch 16 Structures, unions, enums — student DB, GPIO register struct, bit macros (content: `12A`)",
 D(2026,12,26):"Deload — rewrite 3 programs from memory (swap, my_strlen, bit macros). No new topics.",
 D(2027,1,2):"K.N. King Ch 17 Advanced pointers — malloc/free, singly linked list, Valgrind clean (content: `12D`)",
 D(2027,1,9):"K.N. King Ch 18–19 + Makefile for a 4-file project + GDB breakpoints/watch (content: `12B`, `12C`)",
 D(2027,1,16):"K.N. King Ch 20 Low-level programming — bitwise, bit-fields, circular buffer, register simulator",
 D(2027,1,23):"State machine with function-pointer dispatch (content: `13A`) + MOCK exit test (`13C`)",
 D(2027,1,30):"🎯 C EXIT TEST — 5 timed tests from memory (`13D`): circular buffer, linked list, Makefile, state machine, GDB bug hunt"}
P1_ELEC = {D(2026,12,6):"Op-amps 1: ideal op-amp, inverting/non-inverting amplifier (Neso + TI Precision Labs intro)",
 D(2026,12,13):"Op-amps 2: offset voltage, bias current (TI Precision Labs)",
 D(2026,12,20):"Op-amps 3: bandwidth, gain-bandwidth product (TI Precision Labs)",
 D(2026,12,27):"Deload — off",
 D(2027,1,3):"Instrumentation amplifier: why ECG front-ends use one (CMRR) — TI Precision Labs",
 D(2027,1,10):"Active filters: build a Sallen-Key low-pass on the breadboard",
 D(2027,1,17):"ADC basics: resolution, sampling, Nyquist (TI Precision Labs — ADCs)",
 D(2027,1,24):"Noise and grounding basics (TI Precision Labs)",
 D(2027,1,31):"Off — exit test weekend. Update PROGRESS.md with your scores."}

# ---------------------------------------------------------------- one-off milestones
MS = {D(2026,10,15):[("adm","Buy the Udemy cart — ✅ done (8 courses verified Oct 15)",0)],
 D(2026,10,16):[("adm","Ask HR for the bond end date (1 Oct 2027, +1 day per leave) in writing",10),("adm","Ask a colleague: does Unistring use OrCAD/Allegro? Confirm weekend learning on the office licence is OK",5)],
 D(2026,10,19):[("adm","Follow-up emails: Chemnitz + RWU (reply to your own sent mail), and Bremerhaven control-credit question if still unanswered",15)],
 D(2026,11,2):[("adm","Order a transistor + diode assortment (~₹100) for week 8",5)],
 D(2026,11,29):[("mile","🎯 RESTART REVIEW — tick it in PROGRESS.md (≥6/8 weeks, 20+ programs, swap() from memory, electronics explained)",30)],
 D(2027,1,4):[("adm","Install DW 'Nicos Weg' + AnkiDroid German A1 deck — German starts today on the commute",10)],
 D(2027,3,28):[("mile","🎯 English check: write 150 words in 20 min by hand; count spelling mistakes (target < 5)",25)],
 D(2027,4,4):[("ielts","Free full IELTS practice test (British Council / IDP) — your baseline band per section",180)],
 D(2027,4,5):[("adm","Book the Goethe-Zertifikat A1 exam for July (Goethe-Zentrum Hyderabad)",15)],
 D(2027,5,3):[("adm","Order AD8232 module + snap electrodes (~₹1,000)",10)],
 D(2027,6,7):[("adm","Apply for APS (aps-india.de): all memos with the CORRECTED Sem-1 memo, degree certificate, passport",60)],
 D(2027,6,14):[("adm","Request from CBIT: consolidated transcript + official grading scale + R22 syllabus",20)],
 D(2027,7,5):[("adm","Book IELTS Academic (computer-delivered) for Sat Oct 9, 2027",15)],
 D(2027,7,17):[("ger","🎯 Goethe-Zertifikat A1 exam (on the date you booked)",240)],
 D(2027,8,23):[("adm","Check APS status — follow up if not received",10)],
 D(2027,9,6):[("adm","Shortlist final universities; open `01_UNIVERSITIES.md` and confirm 2028 deadlines on each site",45)],
 D(2027,10,1):[("mile","🎯 BOND ENDS — submit resignation (notice to ≈1 Jan 2028, +leave days)",30)],
 D(2027,10,4):[("adm","Ask HR for an experience/service certificate (dates, title, duties) — needed for applications",10)],
 D(2027,10,9):[("ielts","🎯 IELTS ACADEMIC EXAM",240)],
 D(2027,10,18):[("adm","Create uni-assist account; check the Bremerhaven Summer 2028 round is open",30)],
 D(2027,10,23):[("app","Motivation letter draft #1 (structure in `05`)",120)],
 D(2027,10,24):[("app","Europass CV",90)],
 D(2027,11,1):[("app","Email TUHH again — reply in Sandra Steffens' thread (they asked for November 2027)",15)],
 D(2027,11,6):[("app","Bremerhaven: customise motivation letter; gather uni-assist documents",120)],
 D(2027,11,13):[("ielts","IELTS retake (only if below 6.5)",0)],
 D(2027,11,27):[("app","🎯 SUBMIT BREMERHAVEN via uni-assist (deadline 31 Dec)",120)],
 D(2027,12,1):[("app","Darmstadt (IMSEIT) portal open? Start the application",30)],
 D(2027,12,4):[("app","Darmstadt: customised motivation letter + upload",150)],
 D(2027,12,11):[("app","TUHH application (window 1 Dec – 1 Mar)",120)],
 D(2027,12,15):[("app","Loan research (SBI Scholar / HDFC Credila) — only as backup",30)],
 D(2027,12,31):[("mile","🎯 Last working day ≈ now (+leave days). Collect relieving letter + experience certificate",30)],
 D(2028,1,10):[("app","TH Lübeck Biomedical Engineering — apply (non-EU window 1 Jan – 1 May)",150)],
 D(2028,1,17):[("app","Dortmund Pre-Check portal (precheck.go-study-europe.de) — upload documents",120)],
 D(2028,2,7):[("app","Bremerhaven decision expected — if admitted: blocked account (€11,904), insurance, VFS visa appointment IMMEDIATELY",60)],
 D(2028,4,3):[("app","FH Dortmund — apply with your Pre-Check code (1 Apr – 15 Jun)",120)],
 D(2028,4,5):[("app","RWU Ravensburg-Weingarten — apply (deadline 15 Apr) — optional, €1,500/sem",120)],
 D(2028,4,20):[("app","TH Deggendorf — apply (15 Apr – 15 Jul)",120)],
 D(2028,5,10):[("app","FAU Erlangen Medical Engineering (Medical Robotics) — apply (deadline 31 May)",150)],
 D(2028,6,5):[("app","HAW Hamburg (VPD) + TU Chemnitz — apply (deadline 15 Jul)",180)],
 D(2028,6,20):[("ger","Goethe A2 exam (optional — Deggendorf needs A2 within 2 semesters)",240)],
 D(2028,7,15):[("mile","🎯 All Winter 2028 applications sent",0)],
 D(2028,8,1):[("app","Accept the best offer → open blocked account → health insurance → book VFS visa appointment",120)],
 D(2028,9,1):[("app","Visa in passport? → book flight, accommodation (Studierendenwerk / WG)",120)],
 D(2028,9,28):[("mile","✈️ Fly to Germany",0)],
 D(2028,10,1):[("mile","🎓 Winter semester 2028 starts",0)]}

PHASES = [("P0","Restart: C basics + electronics",D(2026,10,5),D(2026,11,29)),
 ("P1","Finish C + op-amps/ADC basics",D(2026,11,30),D(2027,1,31)),
 ("P2","STM32: ARM Cortex-M, drivers, ADC+DMA (Project 1)",D(2027,2,1),D(2027,5,31)),
 ("P3","ECG prototype + DSP (Project 2) · APS · Goethe A1",D(2027,6,1),D(2027,7,31)),
 ("IE","IELTS intensive → exam Oct 9 · bond ends Oct 1",D(2027,8,1),D(2027,10,17)),
 ("P4","FreeRTOS + PCB (Project 3) · applications wave 1",D(2027,10,18),D(2027,12,31)),
 ("P5","Free period: portfolio, German A2, applications, visa",D(2028,1,1),D(2028,10,1))]
def phase(d):
    for p in PHASES:
        if p[2] <= d <= p[3]: return p[0]
DELOAD = set()
for a,b in [(D(2026,12,26),D(2027,1,1)),(D(2027,4,24),D(2027,4,30)),(D(2027,7,24),D(2027,7,31)),(D(2027,10,10),D(2027,10,17))]:
    DELOAD |= set(rng(a,b))

i1 = i2 = i3 = i4 = 0
p4day = 0; fill = 0
FILL = ['Portfolio polish: improve one README (diagram, photos, results)','Interview prep: explain Project 2 aloud in English for 5 min, record it','Interview prep: 10 embedded C questions (volatile, ISR rules, DMA, RTOS priority inversion) — answer on paper','Read one paper on wearable tremor / ECG front-ends (PubMed); 5-line summary in Startup notes','Optional: FastBit Zephyr RTOS (owned) — next sections','German: 20 min extra speaking practice (AI voice) about your projects']
days = []
start, end = D(2026,10,5), D(2028,10,1)
for d in rng(start, end):
    wd = d.weekday()  # 0 Mon .. 6 Sun
    ph = phase(d); T = []
    def add(kind, text, mins, how=""):
        if not text: return
        T.append({"k":kind,"t":text,"m":int(round(mins)),"h":how})
    deload = d in DELOAD
    working = d <= D(2027,12,31)

    # ---------------- language (daily, weekdays mainly)
    if working and wd < 5:
        if D(2026,10,15) <= d and not qENG.done() and d < D(2027,5,1):
            add("eng", qENG.take(30), 30, "Commute or lunch, 1.25× speed. Pause and repeat sentences aloud.")
        elif D(2027,5,1) <= d <= D(2027,9,30) and not qIEL.done():
            mins = 40 if d < D(2027,8,1) else 60
            add("ielts", qIEL.take(mins), mins, "Commute/lunch, 1.25×. Skip all 'General Training' sections — you take Academic.")
        if d >= D(2026,10,15) and d < D(2027,10,9):
            add("eng", "Speak aloud 10 min: describe your day / a project / an opinion → record → listen once", 10, "Phone recorder. Listen for one mistake to fix tomorrow.")
        if D(2026,10,15) <= d < D(2027,4,1) and wd in (1,3):
            add("eng", "Handwritten paragraph (80–120 words) → AI marks ONLY mistakes → rewrite; add misspelled words to your spelling list", 20, "Autocorrect OFF. Don't let AI rewrite it for you.")
        if D(2027,1,4) <= d <= D(2027,7,16):
            add("ger", "Nicos Weg A1 — next lesson (commute) + 10 min Anki", 30, "Listen, repeat aloud quietly, note 5 new words.")
        elif D(2027,7,18) <= d <= D(2027,12,31):
            add("ger", "German maintenance: 10 min Anki or Easy German audio", 10, "Keep A1 alive while IELTS has priority.")
        if D(2027,8,1) <= d <= D(2027,10,8):
            drill = ["Listening: 1 full section, timed","Reading: 1 Academic passage, timed (20 min)","Writing Task 1: one graph description (20 min, by hand)","Speaking: AI examiner Parts 1–3, recorded","Reading: 1 passage + review every wrong answer"][wd]
            add("ielts", "IELTS drill — " + drill, 25, "Mark it honestly; log the band in PROGRESS.md.")

    # ---------------- weekday technical reading
    if working and wd < 5 and not deload:
        if d in P0_READ and d >= D(2026,10,5):
            add("read", "Read 15 min: " + P0_READ[d], 15, "Before gym or at bedtime. Highlight 3 things to try on Saturday.")
        elif ph == "P1":
            nxt = min([s for s in P1_SAT if s >= d], default=None)
            if nxt: add("read", "Read 15–20 min for Saturday: " + P1_SAT[nxt].split("—")[0], 20, "Read the chapter; try 2 end-of-chapter exercises in your head.")
        elif ph in ("P2","P3"):
            q = qARM if not qARM.done() else (qM1 if not qM1.done() else (qDMA if not qDMA.done() else qDSP))
            add("read", f"Read 20 min: preview '{q.peek() or 'next topic'}' in Mastering STM32 / RM0383 / Joseph Yiu", 20, "Find the registers involved; draw one diagram.")
        elif ph == "P4":
            q = qRT if not qRT.done() else qOR
            add("read", f"Read 20 min: preview '{q.peek() or 'next topic'}' (FreeRTOS book / OrCAD notes)", 20, "")

    # ---------------- weekends: technical work
    if wd >= 5 and working:
        if ph == "P0":
            if d in P0_SAT: add("c", P0_SAT[d], 120, "Watch/read → write it yourself → compile with -Wall -Wextra → explain it out loud. No AI code.")
            if d in P0_SUN: add("elec", P0_SUN[d], 60, "Neso Academy video first, then build it on the breadboard and measure.")
        elif ph == "P1":
            if d in P1_SAT: add("c", P1_SAT[d], 180, "Same 4 steps: read → code → test → explain. GDB, not printf.")
            if d in P1_ELEC: add("elec", P1_ELEC[d], 60, "")
            if wd == 6 and not deload and d != D(2027,1,31) and not qC.done():
                add("course", qC.take(75), 75, "Watch at 1.25× and run the examples on your STM32 board.")
        elif ph == "P2":
            if deload:
                add("rest", "Deload weekend — light review only", 0)
            elif wd == 5:
                if d == D(2027,2,6): add("elec", "Practical-electronics hands-on checklist (`15_FUNDAMENTALS_BRIDGE.md`) before wiring the STM32", 60)
                q = qARM if not qARM.done() else (qM1 if not qM1.done() else qDMA)
                add("course", q.take(240), 240, "Code along on the Nucleo/Black Pill. Verify every register against RM0383. No AI code.")
            else:
                q = qARM if not qARM.done() else (qM1 if not qM1.done() else qDMA)
                lab = q.take(120)
                if lab: add("course", lab, 120, "Continue the course; re-type the code yourself.")
                if d >= D(2027,3,7) and i1 < len(P1):
                    for _ in range(2 if d >= D(2027,3,21) else 1):
                        if i1 < len(P1): add("proj", "Project 1 — " + P1[i1], 60, "Small commit per step, clear message."); i1 += 1
                elif d >= D(2027,5,2) and i2 < len(P2):
                    add("proj", "Project 2 — " + P2[i2], 60, ""); i2 += 1
            if wd == 6: add("eng", "Weekly English: 1 handwritten paragraph + review your spelling list", 20)
        elif ph == "P3":
            if deload:
                add("rest", "Deload weekend — light review only", 0)
            elif wd == 5:
                if not qDMA.done(): add("course", qDMA.take(120), 120, "")
                add("course", qDSP.take(120 if qDMA.done() else 60), 120, "Do the exercises on your board; keep the CMSIS-DSP examples.")
                if i2 < len(P2): add("proj", "Project 2 — " + P2[i2], 60, ""); i2 += 1
            else:
                for _ in range(2):
                    if i2 < len(P2): add("proj", "Project 2 — " + P2[i2], 90, "Document as you go (DHF + README notes)."); i2 += 1
                if i2 >= len(P2) and not qDSP.done(): add("course", qDSP.take(120), 120, "")
            if wd == 6: add("ielts", "Writing Task 2 essay — 40 min, timed, by hand → AI band feedback → rewrite weakest paragraph", 60)
        elif ph == "IE":
            if D(2027,10,10) <= d <= D(2027,10,17):
                add("rest", "Post-exam / resignation week — rest", 0)
            elif d == D(2027,10,9):
                pass
            elif wd == 5:
                add("ielts", "Full timed IELTS mock (Listening + Reading + Writing) — Cambridge book or official sample", 180, "Exam conditions: no phone, timer, handwriting or computer-delivered practice.")
                add("course", "Embedded maintenance (1 h): tidy GitHub READMEs / small fixes only", 60)
            else:
                add("ielts", "Mock review: every wrong answer + 2 Task 2 essays (timed) + 1 Task 1 → feedback", 180)
                add("ielts", "Speaking mock (Parts 1–3), recorded; note fillers and grammar slips", 30)
        elif ph == "P4":
            if wd == 5:
                q = qRT if not qRT.done() else qOR
                add("course", q.take(180), 180, "")
                if d >= D(2027,11,20) and i3 < len(P3): add("proj", "Project 3 — " + P3[i3], 60, ""); i3 += 1
            else:
                q = qRT if not qRT.done() else qOR
                add("course", q.take(120), 120, "")

    # ---------------- free period 2028
    if not working and d < D(2028,9,20):
        if wd < 5:
            # deep work block 1: OrCAD -> Project 3 -> MCU2 -> Project 4
            if not qOR.done():
                add("course", qOR.take(150), 150, "Build the ECG board in parallel with the lessons.")
            elif i3 < len(P3):
                add("proj", "Project 3 — " + P3[i3], 150, ""); i3 += 1
            elif i4 < len(P4) and d >= D(2028,2,1):
                p4day += 1
                add("proj", f"Project 4 — {P4[i4]} (day {p4day}/3)", 150, "")
                if p4day == 3: i4 += 1; p4day = 0
            else:
                add("proj", FILL[fill % len(FILL)], 120, ""); fill += 1
            # block 2
            if not qM2.done():
                add("course", qM2.take(90), 90, "")
            elif not qDSP.done():
                add("course", qDSP.take(60), 60, "")
            elif d >= D(2028,3,1) and not qISO.done():
                add("course", qISO.take(60), 60, "Apply each idea to your own ECG prototype's risk table.")
            # block 3 German A2
            if d >= D(2028,1,10) and d < D(2028,6,20):
                add("ger", "German A2: next Nicos Weg A2 lesson + 15 min speaking/writing", 60, "")
            # NPTEL software engineering Jan–Apr
            if D(2028,1,17) <= d <= D(2028,4,24) and wd in (0,2,4):
                add("course", "NPTEL Software Engineering (IIT Kharagpur) — this week's lectures + assignment (for Dortmund's SE requirement)", 60, "Take the proctored exam (~₹1,000) at the end.")
        elif wd == 5:
            add("proj", "Weekly review: update PROGRESS.md, push all repos, plan next week", 45)
    if d >= D(2028,9,20) and not MS.get(d):
        add("adm", "Packing, documents, travel prep", 0)

    if wd == 6 and working and not deload:
        add("track", "Update PROGRESS.md / this tracker — honest note for the week", 10)

    for k, t, m in MS.get(d, []): add(k, t, m)
    if not T: add("rest", "Rest day — nothing planned. Sleep, family, gym.", 0)
    days.append({"d": d.isoformat(), "p": ph, "dl": deload, "t": T})

plan = {"generated": dt.date.today().isoformat(),
        "phases": [{"id":p[0],"name":p[1],"from":p[2].isoformat(),"to":p[3].isoformat()} for p in PHASES],
        "days": days}
left = {q.name: (len(q.items) - q.i) for q in [qC,qARM,qM1,qDMA,qDSP,qRT,qOR,qM2,qISO,qENG,qIEL]}
print("sections left per course:", left, file=sys.stderr)
print("projects done steps:", i1, len(P1), i2, len(P2), i3, len(P3), i4, len(P4), file=sys.stderr)
json.dump(plan, open(sys.argv[1], "w", encoding="utf-8"), ensure_ascii=False, separators=(",",":"))
