# System Architecture

## Intended control flow

```text
NVIDIA Jetson Nano
    |
    | Python host program
    | Generates/obtains time and display commands
    v
Serial connection (USB or the verified interface)
    |
    v
Arduino Uno
    |
    | I2C
    v
PCA9685 PWM servo driver(s)
    |
    | PWM signals
    v
Servo motors
    |
    v
Mechanical seven-segment assemblies
```

## Responsibilities

- **Jetson Nano:** Host-side Python logic and command generation. AI inference is not required for this project's basic display operation.
- **Arduino Uno:** Receives serial commands and updates the PWM driver.
- **PCA9685:** Generates PWM signals for connected servos.
- **Servos and mechanics:** Physically move the display segments.

## Verify before publishing

This is a reference architecture. Update it to match the actual cable/interface, number of PCA9685 boards, I2C addresses, servo count, and channel allocation in the completed prototype.
