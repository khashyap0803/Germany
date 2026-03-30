# 💻 EMBEDDED SYSTEMS LEARNING PLAN

## Goal: Build real skills (not copy-paste) + GitHub portfolio
## Time: Evenings + weekends, alternating with German study

---

## LEARNING PATH (Priority Order)

### 1. C Programming DEEP (Apr - May 2026) — 8 weeks
**Why**: Foundation of ALL embedded work. You MUST know C properly.

| Topic | Resource | Practice |
|:---|:---|:---|
| Pointers, memory, structs | "C Programming" by K&R | Write code from scratch |
| Bitwise operations | YouTube: Jacob Sorber | Solve 5 problems/week |
| Linked lists, queues | Neetcode / LeetCode Easy | Implement from memory |
| Makefiles, compilation | GCC on WSL2 | Build projects without IDE |
| Debugging | GDB on WSL2 | Debug real bugs |

**AI Usage**: When stuck, ask Claude/ChatGPT to EXPLAIN, not give you the answer. Then try again yourself.

### 2. Microcontroller Programming (Jun - Sep 2026) — 16 weeks
**Why**: Core of embedded systems. You have STM32 + ESP32.

| Topic | Resource | Hardware |
|:---|:---|:---|
| GPIO, timers, interrupts | STM32CubeIDE tutorials | STM32 board |
| ADC, DAC, PWM | Fastbit Embedded (YouTube) | STM32 + sensors |
| SPI, I2C, UART | Controller Tech (YouTube) | STM32 + modules |
| ESP-IDF framework | Espressif docs | ESP32 |
| WiFi/BLE projects | ESP-IDF examples | ESP32 |

**Portfolio Project 1**: Build a real sensor data logger with STM32 + I2C sensor + UART output → document on GitHub

### 3. RTOS (Oct - Dec 2026) — 12 weeks
**Why**: Required for many embedded roles and masters programs.

| Topic | Resource |
|:---|:---|
| FreeRTOS basics | "Mastering the FreeRTOS Real Time Kernel" (free PDF) |
| Tasks, queues, semaphores | Hands-on with STM32 + FreeRTOS |
| Mutexes, event groups | Practice exercises |
| RTOS on ESP32 | ESP-IDF (uses FreeRTOS internally) |

**Portfolio Project 2**: Multi-task embedded application using FreeRTOS on STM32

### 4. Communication Protocols Deep Dive (Jan - Mar 2027) — 12 weeks
| Protocol | Level |
|:---|:---|
| SPI — master/slave, modes, timing | Deep |
| I2C — addressing, multi-slave | Deep |
| UART — baud, framing, RS232/485 | Deep |
| CAN bus — automotive focus | Intermediate |
| USB basics | Awareness |

### 5. Linux Embedded Basics (Apr - Jun 2027) — 12 weeks
**Use WSL2 on your Windows PC for this!**

| Topic | Resource |
|:---|:---|
| Linux command line mastery | Linux Journey (free website) |
| Shell scripting (bash) | WSL2 practice |
| Cross-compilation | Build for ARM on x86 |
| Buildroot / Yocto basics | Awareness level |
| Device drivers concept | Reading + videos |

### 6. VHDL/Verilog Basics (Jul - Sep 2027) — 12 weeks
**Why**: Required prerequisite for RWU application.

| Topic | Resource |
|:---|:---|
| Digital logic review | Neso Academy (YouTube) |
| VHDL basics | Free VHDL tutorials online |
| Verilog basics | HDLBits (free interactive) |
| Simple designs | Counter, FSM, ALU |

**Portfolio Project 3**: Simple FPGA project in VHDL (can simulate without hardware using online tools)

---

## PC SETUP FOR EMBEDDED DEVELOPMENT

### Windows (Primary OS — 1TB Gen4 SSD)
- **STM32CubeIDE** — STM32 development
- **VS Code + PlatformIO** — ESP32 + general embedded
- **KiCad** — PCB design (good for portfolio)
- **Git** — version control for all projects

### WSL2 (Ubuntu 22.04)
```powershell
# Install WSL2
wsl --install -d Ubuntu-22.04

# Inside Ubuntu, install embedded tools:
sudo apt update
sudo apt install gcc-arm-none-eabi gdb-multiarch make cmake git
```

### Delete Linux Dual Boot
- Boot into Windows
- Open Disk Management
- Delete the Linux partitions
- Extend Windows or create a data partition
- Free up 1TB Gen3 SSD for project files

### Storage Organization
- **1TB Gen4 SSD**: Windows + WSL2 + all installed software
- **1TB Gen3 SSD**: Projects, German resources, IELTS material, documents
- **512GB SATA SSD**: Backups of important documents
- **512GB HDD**: ⚠️ FAILING — stop using it, replace when budget allows

---

## GITHUB PORTFOLIO STRATEGY

### Create repositories with PROPER documentation:
```
README.md should include:
- Project description
- Hardware used (with photos)
- Circuit diagram (KiCad)
- How to build and flash
- Demo video/GIF
- What you learned
```

### Target: 3-4 solid projects by mid-2028
1. **Sensor Data Logger** (STM32 + I2C + UART) — Jun-Aug 2026
2. **FreeRTOS Multi-task System** (STM32 + FreeRTOS) — Nov 2026-Jan 2027
3. **IoT Device** (ESP32 + WiFi + sensors) — Apr-Jun 2027
4. **VHDL/Verilog Design** (simulation) — Aug-Sep 2027

### Key Rule:
> **WRITE EVERY LINE OF CODE YOURSELF. Use AI to EXPLAIN, not to WRITE FOR YOU. The goal is LEARNING, not impressing GitHub visitors with AI-generated code.**
