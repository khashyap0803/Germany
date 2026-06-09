# 💻 EMBEDDED SYSTEMS LEARNING PLAN

## Strategy: Type 3 "AI Supervisor Engineer" — manual foundations → AI-accelerated mastery
## Real Start: June 9, 2026 (not May — gym 5:30-6:30 AM daily eliminates weekday morning coding)
## Time: Pre-gym reading (5:00-5:25 AM) + Weekends (~16.5 hrs coding) + Commute audio (~17 hrs/week)
## See `09_ULTIMATE_STUDY_PLAN.md` for the DETAILED daily/weekly schedule

---

## AI DETOX PROTOCOL

| Phase | Period | AI Rule |
|---|---|---|
| **Phase 1** | Jun 9–Aug 24, 2026 | 🔴 **AI BANNED for code.** AI only explains concepts. YOU write ALL code. |
| **Phase 2** | Aug 25–Nov 23, 2026 | 🔴 **AI BANNED for code.** Same rule — hardware work, zero AI code. |
| **Phase 3** | Nov 24, 2026–Feb 8, 2027 | 🟡 **Supervised AI.** AI generates boilerplate. You REVIEW and EXPLAIN every line. |
| **Phase 4+** | Feb 9, 2027+ | 🟢 **AI Partner.** Generate, review, test, sign off — like a senior engineer. |

---

## ⚠️ ECE FUNDAMENTALS — READ `15_FUNDAMENTALS_BRIDGE.md` FIRST

You do NOT need to relearn your B.E. degree (Thevenin/Norton/mesh/EDC/Signals/Control). For admission it changes nothing; for embedded work, the only basics that matter are **practical electronics** and **digital logic**. Two small bridges are inserted into the timeline — total ~5 weekends, no phase delay:

| Bridge | When | Why |
|:---|:---|:---|
| **Practical Electronics** (Ohm's law, voltage divider, pull-ups, logic levels, reading datasheets) | Aug 18–29, 2026 (deload + first Phase 2 weekend) | So you understand/wire the STM32 without frying it |
| **Digital Logic** (number systems, Boolean, gates, flip-flops, FSM) | Oct 2027 (after IELTS exam, before VHDL) | Prerequisite for VHDL (Phase 5) |

**Everything else from your degree: skip unless a specific job/course forces it.** Full detail + resources in `15_FUNDAMENTALS_BRIDGE.md`.

---

## LEARNING PATH (Priority Order)

### 1. C Programming DEEP (Jun 9 – Aug 24, 2026) — 11 weeks
**Why**: Foundation of ALL embedded work. You MUST know C properly.

| Topic | Primary Resource | Secondary Resource | Practice |
|:---|:---|:---|:---|
| C fundamentals, types, operators | K.N. King "C Programming: A Modern Approach" 2nd Ed | FastBit "Embedded C" course at 1.5× | King exercises (3-5 per chapter) |
| Pointers, memory, structs | K.N. King Ch 11-19 | Neso Academy YouTube (7-min concepts) | Draw memory diagrams on paper |
| Bitwise operations | K.N. King Ch 20 + FastBit bitwise sections | Jacob Sorber YouTube | Solve 5 problems/week |
| Linked lists, queues | K.N. King Ch 17 + practice | Exercism C track | Implement from scratch, no AI |
| Makefiles, compilation pipeline | GCC on WSL2 | FastBit build system sections | Build multi-file projects |
| Debugging | GDB on WSL2 | See `10_GOLDEN_RULES.md` GDB cheat sheet | Debug real bugs manually |

**Reference (Bed Reading)**: K&R "The C Programming Language" 2nd Ed — concise expert perspective

**Pipeline**: Read King → Do exercises → Watch FastBit → Code yourself → EXPLAIN out loud

### 2. Microcontroller Programming (Aug 25 – Nov 23, 2026) — 13 weeks
**Why**: Core of embedded systems. Register-level understanding.

| Topic | Primary Resource | Course | Hardware |
|:---|:---|:---|:---|
| GPIO, UART (HAL + Register) | "Mastering STM32" by Carmine Noviello | FastBit MCU1 (28.5h) | STM32F411 Black Pill + Nucleo-L476RG |
| Timers, Interrupts, ADC | Reference Manual RM0383/RM0351 | FastBit MCU2 (29h) | STM32 boards + sensors |
| PWM, DMA basics | Mastering STM32 book | FastBit MCU2 | Breadboard + LEDs + potentiometer |
| SPI, I2C protocols | Mastering STM32 + datasheets | FastBit MCU1/MCU2 | Logic analyzer (Sipeed SLogic) |

**Debugger Setup**:
- Nucleo onboard ST-Link/V2-1 (primary — SWD only, rock solid)
- Robocraze metal ST-Link V2 (backup/portable — SWD only)
- Both connect to STM32CubeIDE or OpenOCD+GDB

**Portfolio Project 1**: "STM32 Environmental Monitor" — ADC + timer + UART + circular buffer → GitHub

### 3. RTOS + Zephyr (Nov 24, 2026 – Feb 8, 2027) — 11 weeks
**Why**: Required for embedded roles. Industry moving to Zephyr.

| Topic | Primary Resource | Course |
|:---|:---|:---|
| FreeRTOS: tasks, queues, semaphores | "Mastering the FreeRTOS Real Time Kernel" (free PDF, 304p) | FastBit "FreeRTOS with STM32Fx" (14h) — buy Sep 2026 |
| FreeRTOS: mutexes, priority inversion | FreeRTOS book + STM32 hands-on | FastBit FreeRTOS course |
| Zephyr RTOS: setup, DeviceTree, board porting | Zephyr official docs | FastBit "Mastering Zephyr RTOS" (9h) — already purchased |
| Zephyr: custom board bring-up | FastBit course + Zephyr docs | Port to STM32F411 + Nucleo-L476RG |

**AI Tools Introduction**: Start using Copilot/Ember for FreeRTOS boilerplate (YOU verify every line)

**Portfolio Project 2**: "FreeRTOS Multi-Sensor Dashboard" + Zephyr re-implementation → GitHub
**Note**: Bond expires Oct 2027 → resign → last working day ~Jan 2028 → 9 months free for applications

### 4. Protocols + Linux + AI Tools Mastery (Feb 9 – Aug 9, 2027) — 26 weeks
**Why**: Complete the embedded stack. Master AI tools as a supervisor.

| Topic | Resource | AI Tool to Learn |
|:---|:---|:---|
| CAN bus, RS485 | FastBit MCU2 + books | Ember AI for firmware iteration |
| ESP32 + IoT (WiFi/MQTT) | ESP-IDF docs + ESP32-S3 board | Copilot for boilerplate |
| Linux CLI, shell scripting | "Linux 100+ hours" Udemy course | — |
| Linux device drivers | LDD3 book + Bootlin training | — |
| Cross-compilation | WSL2 + Fedora VM + openSUSE VM | — |
| PCB design basics | KiCad + Flux AI | Flux AI for auto-routing |

**Old PC Project**: Deploy Linux From Scratch on Core 2 Duo (real hardware kernel experience)
**Linux VMs**: Fedora Workstation + openSUSE Tumbleweed (already installed, VMware, 40GB/6GB RAM each)

**Portfolio Project 3**: ESP32 IoT device — AI-accelerated (generate 60%, verify 100%) → GitHub

### 5. VHDL + IELTS + Portfolio Polish (Aug 10, 2027 – Feb 8, 2028) — 26 weeks

> 🔴 **De-confliction**: Aug–Sep 2027 = **IELTS INTENSIVE** (everything else on maintenance). VHDL heavy work is moved to AFTER the IELTS exam (Oct 2027+). The **Digital Logic Bridge** (`15_FUNDAMENTALS_BRIDGE.md`) runs in Oct 2027 right after the exam, as the lead-in to VHDL.

| Topic | When | Resource |
|:---|:---|:---|
| **Digital logic bridge** (gates, flip-flops, FSM) | Oct 2027 (post-IELTS) | Neso Academy Digital Electronics + Morris Mano — see `15_FUNDAMENTALS_BRIDGE.md` |
| VHDL basics + simulation | Nov 2027+ | Free VHDL tutorials, HDLBits, GHDL |
| Counter, FSM, ALU designs | Nov 2027 – Feb 2028 | Practice + Joseph Yiu ARM book |

**Portfolio Project 4**: VHDL/Verilog design + AI-assisted PCB (Flux) → GitHub

---

## 🔧 HARDWARE INVENTORY

| Hardware | Status | Use For |
|:---|:---|:---|
| STM32F411CEU6 (WeAct Black Pill) | ✅ Owned | Phase 2-3: bare-metal + FreeRTOS + Zephyr |
| Nucleo-L476RG | ✅ Owned | Phase 2-3: HAL + onboard ST-Link for debugging both boards |
| ESP32-S3 N8R2 | ✅ Owned | Phase 4: IoT + WiFi/BLE projects |
| Robocraze ST-Link V2 (metal shell) | ✅ Owned | Backup/portable SWD programmer |
| Sipeed SLogic analyzer | ✅ Owned | Protocol debugging (SPI/I2C/UART waveforms) |
| Core 2 Duo PC (LGA775, 4GB DDR2) | ✅ Found | Phase 4: Linux From Scratch target |
| Raspberry Pi 4 | ❌ Buy late 2026 | Phase 4: Embedded Linux |

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

### VMware VMs (Phase 4)
- **Fedora Workstation**: 40GB disk, 6GB RAM — main Linux dev VM
- **openSUSE Tumbleweed**: 40GB disk, 6GB RAM — secondary (rolling release)

### Storage Organization
- **1TB Gen4 SSD**: Windows + WSL2 + all installed software
- **1TB Gen3 SSD**: Projects, German resources, IELTS material, documents
- **512GB SATA SSD**: Backups of important documents
- **512GB HDD**: ⚠️ FAILING — stop using it, replace when budget allows

---

## 📚 COURSE LIBRARY (All Purchased — 183+ Hours)

| # | Course | Hours | Phase |
|:---|:---|:---|:---|
| 1 | FastBit Embedded C Programming | 16.5h | Phase 1 (Jun–Aug 2026) |
| 2 | FastBit MCU Driver Development (MCU1) | 28.5h | Phase 2 (Aug–Nov 2026) |
| 3 | FastBit Timers/PWM/CAN (MCU2) | 29h | Phase 2-3 (Sep 2026–Feb 2027) |
| 4 | FastBit Zephyr RTOS | 9h | Phase 3 (Feb 2027) |
| 5 | Linux 100+ hours | 100h+ | Phase 4 (Feb–Aug 2027) |
| **Buy Aug 2026** | FastBit ARM Cortex-M3/M4 | 15h | Phase 2 (Aug 2026) |
| **Buy Nov 2026** | FastBit FreeRTOS | 14h | Phase 3 (Nov 2026) |

See `10_RESOURCES.md` for complete book + platform library.

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

### Target: 4 solid projects by mid-2028
1. **STM32 Environmental Monitor** (STM32 + ADC + UART + timer) — Nov 2026
2. **FreeRTOS Multi-Sensor Dashboard** + Zephyr branch (STM32 + RTOS) — Feb 2027
3. **IoT Device** (ESP32 + WiFi + MQTT + sensors, AI-accelerated) — May 2027
4. **VHDL Design** + AI-assisted PCB (Flux) — Oct 2027

### Key Rules:
> **Phase 1-2**: WRITE EVERY LINE OF CODE YOURSELF. No AI code generation. No copy-paste.
> **Phase 3+**: AI generates boilerplate → YOU review, verify, debug, and sign off on every line.
> **Always**: The goal is UNDERSTANDING, not impressing GitHub visitors with AI-generated code.
