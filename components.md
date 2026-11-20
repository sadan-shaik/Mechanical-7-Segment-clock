# Hardware Components

This document lists the hardware used or planned for the mechanical seven-segment display. Confirm exact board revisions, quantities, and power ratings against the physical build before publishing.

## Main components

| Component | Role in the project | Details to verify |
|---|---|---|
| Arduino Uno R3 | Embedded controller for servo commands | Board revision and serial baud rate |
| NVIDIA Jetson Nano | Linux/Python host for time generation and sending commands | Jetson Nano model and connection method |
| PCA9685 16-channel PWM driver | Generates PWM signals for servo control | Number of boards and I2C addresses |
| SG90 micro servo motors | Move individual mechanical segments | Actual servo count and operating voltage |
| External regulated DC supply | Supplies servo power | Output voltage, current rating and polarity |
| Mechanical segment assemblies | Form the seven-segment digits | Material, dimensions and linkage design |
| Jumper wires/connectors | Electrical interconnections | Wire gauge and connector type |
| Mounting platform | Supports the display and electronics | Material and dimensions |

## Component roles

### Arduino Uno R3
Receives commands from the host computer and controls the PWM driver over I2C. The Arduino and PCA9685 logic must share a common ground.

### NVIDIA Jetson Nano
Runs the host-side Python program. In this project architecture, it can generate or obtain the time and send display commands to the Arduino over a serial connection. The Jetson Nano is an AI-capable edge-computing board, but AI inference is not required for this display-control task.

### PCA9685 servo driver
The PCA9685 provides 16 PWM channels per board. If the build uses more than 16 independently controlled servos, document the number of driver boards and their I2C addresses.

### SG90 servo motors
Each servo actuates a mechanical segment or linkage. Record the final servo count and the channel assigned to each segment. Calibrate safe movement limits individually; do not assume every servo has identical mechanical limits.

## Power and wiring notes

- Power the servos from a suitable external regulated supply, not from the Arduino 5 V pin.
- Connect the external servo-supply ground, PCA9685 ground, and Arduino ground together.
- Connect the PCA9685 logic-side VCC to the appropriate Arduino logic supply.
- Verify the exact supply voltage and current capacity against the servo specifications and measured load.
- Check polarity before powering the system.
- Keep high-current servo wiring appropriately sized and secure.

## Information to add before final publication

- [ ] Exact number of SG90 servos
- [ ] Number of PCA9685 boards
- [ ] I2C address of each board
- [ ] Servo channel-to-segment mapping
- [ ] External power-supply voltage and current rating
- [ ] Actual Arduino-to-Jetson serial connection and baud rate
- [ ] Clear photographs of each component and the wiring
