# 💻 EMBEDDED LEARNING PATH — C → STM32 → biosignals → RTOS → PCB

> **Rebuilt**: October 15, 2026. Dates follow `07_MONTHLY_TIMELINE.md`; current weeks are in `18_RESTART_8_WEEKS.md`.
> **Aim:** by **December 2027**, prove Darmstadt's four requirements with GitHub projects — **excellent C/C++, 32-bit microcontrollers, systems engineering, hardware design** — in the **medical-device** direction.
> **What changed from the June 2026 plan:** start moved to Oct 2026; Zephyr, CAN/RS485, Linux drivers and VHDL are now **optional**; biosignals (ADC + DMA + DSP) and PCB design moved to the centre, because that's the medical-device skill set.

---

## AI POLICY FOR CODE

| Phase | Dates | Rule |
|:---|:---|:---|
| 0–2 | Oct 2026 – May 2027 | 🔴 **No AI-written code.** AI may explain concepts and error messages only |
| 3 | Jun – Oct 2027 | 🟡 **Supervised:** AI may draft boilerplate; you explain and test every line |
| 4–5 | Nov 2027 onward | 🟢 **Partner:** use AI like a senior colleague — you review, test, own the result |

---

## THE PATH

### Phase 0–1 — C (Oct 2026 – Jan 2027)
| Topic | Learn from | Practice |
|:---|:---|:---|
| C fundamentals → pointers (Ch 1–12) | **K.N. King** + FastBit *Embedded C* (owned) | `C-Practice/` on GitHub, `gcc -Wall -Wextra`, zero warnings |
| Structs, bitwise, `volatile`, preprocessor (Ch 13–20) | K.N. King Ch 13–20 + FastBit | Bit macros, register simulator |
| Makefiles, GDB, linked list, circular buffer | Content in `12C`, `12D` weekly files | From-memory tests (`13D`) |
| State machines | **Miro Samek — "Modern Embedded Systems Programming"** (free, YouTube) | Function-pointer dispatch |
| Electronics basics alongside | **Neso Academy** (theory) + breadboard; **TI Precision Labs** (op-amps) | Measure everything you build |

### Phase 2 — STM32 (Feb – May 2027)
| Topic | Learn from | Practice |
|:---|:---|:---|
| ARM Cortex-M architecture, NVIC, startup | **Udemy ARM Cortex-M3/M4** (FastBit) + Joseph Yiu (book, owned) | Blink HAL + register level |
| GPIO, interrupts, UART, I²C, SPI drivers | **FastBit MCU1** (owned) + *Mastering STM32* (book) + RM0383 | **Project 1** |
| ADC + DMA | **Udemy DMA Programming Demystified** | Continuous ADC → DMA → buffer |

### Phase 3 — Biosignals (Jun – Jul 2027)
| Topic | Learn from | Practice |
|:---|:---|:---|
| Biopotential front-end (AD8232), electrodes | AD8232 datasheet + TI Precision Labs | **Project 2** |
| Digital filters, FFT, CMSIS-DSP | **Udemy DSP From Ground Up on ARM** + Steven Smith *DSP Guide* (free) | 50 Hz notch, baseline removal, heart rate |

### Phase 4 — RTOS + PCB (Nov 2027 – Mar 2028)
| Topic | Learn from | Practice |
|:---|:---|:---|
| FreeRTOS tasks, queues, semaphores | **Udemy Mastering RTOS** (FastBit) + Richard Barry's book (owned) | Port Project 2 to tasks |
| PCB design | **Udemy OrCAD/Allegro** (37 h) — practise on your licensed install; Phil's Lab (YouTube) for layout habits | **Project 3** |
| Timers, PWM, low power | **FastBit MCU2** (owned) | Battery-friendly firmware |

### Phase 5 — Free period (Jan – Sep 2028)
| Topic | Learn from | Practice |
|:---|:---|:---|
| BLE (nRF52) | **Nordic DevAcademy** (free) | **Project 4** |
| IMU + EMG, sensor fusion | Datasheets + DSP course | Tremor-wearable direction (`Startup/11`, `13`, `15`) |
| Medical device risk | **Udemy ISO 14971** | Risk table for your own prototype |
| Optional | Zephyr (owned), Linux 100+ h (owned), VHDL (only for RWU: nandland / HDLBits) | — |

---

## PORTFOLIO PROJECTS (what admissions will actually see)

| # | Project | Done by | Proves (Darmstadt's list) |
|:--|:---|:---|:---|
| 1 | **`stm32-baremetal-drivers`** — GPIO/UART/I²C/SPI register-level, logic-analyzer captures | **Apr 2027** | C, 32-bit MCU |
| 2 | **`stm32-ecg-monitor`** — AD8232 → ADC + DMA → on-chip DSP → heart rate, with plots + design notes | **Jul 2027** | C, 32-bit MCU, systems engineering, medical |
| 3 | **`ecg-board`** — custom PCB (OrCAD) + FreeRTOS firmware | **Mar 2028** (in progress at Dec 2027 applications) | Hardware design, systems engineering |
| 4 | **`wearable-tremor`** — IMU + EMG/ECG + BLE | **Sep 2028** | Medical wearable direction; thesis seed |

**Every README:** what it does · block diagram · how to build/flash · photos/plots · what went wrong and how you fixed it · what you'd do next. Hand-written code in Phases 0–2.

---

## 🔧 HARDWARE

| Item | Status |
|:---|:---|
| STM32F411CEU6 (Black Pill), Nucleo-L476RG | ✅ Owned |
| ESP32-S3 N8R2 | ✅ Owned |
| ST-Link V2, Sipeed SLogic logic analyzer, multimeter | ✅ Owned |
| Breadboards, resistor kit, LEDs, capacitors, buttons, sensors (BMP280, ADXL345, DHT11…) | ✅ Owned |
| Transistor + diode assortment | Buy before Nov 23, 2026 (~₹100) |
| AD8232 ECG module + snap electrodes | Buy May 2027 (~₹1,000) |
| PCB fabrication (5 boards) | ~₹1,500–3,000, Jan 2028 |
| nRF52 dev kit + IMU | Buy Mar 2028 |

## 🖥️ SOFTWARE
- **WSL2 / Ubuntu + gcc, gdb, valgrind, make** — C phase
- **STM32CubeIDE**, Tera Term, PulseView — STM32 phase
- **OrCAD/Allegro** (office licence — confirm weekend-learning use is allowed; don't use it for your own startup work) · **KiCad** (free, for after you leave Unistring)

## 📚 OWNED COURSES USED HERE
FastBit *Embedded C* · FastBit *MCU1* · FastBit *MCU2* · FastBit *Zephyr* (optional) · *Linux 100+ hours* (optional) · *Crash Course Electronics & PCB Design* (LaMothe) · **plus the Oct 2026 cart** (ARM Cortex-M, DMA, FreeRTOS, DSP, OrCAD/Allegro, ISO 14971). Full list in `10_RESOURCES.md`.
