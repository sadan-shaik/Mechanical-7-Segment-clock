"""
Jetson Nano -> Arduino serial communication starter.

Install dependency:
    python3 -m pip install pyserial

Run:
    python3 communication.py

Check and edit SERIAL_PORT and BAUD_RATE for your actual setup.
This script sends a single servo test command; it does not implement
the complete clock/time-to-segment mapping.
"""

import time
import serial

SERIAL_PORT = "/dev/ttyUSB0"   # Change to the actual Arduino serial device
BAUD_RATE = 115200             # Must match the Arduino sketch


def main():
    with serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=2) as board:
        time.sleep(2)  # Allow the Arduino to reset after serial connection
        print("Connected to Arduino")

        # Example only: move PCA9685 channel 0 to 90 degrees.
        # Confirm the servo is mechanically safe before testing.
        command = "S,0,90\n"
        board.write(command.encode("utf-8"))

        response = board.readline().decode("utf-8", errors="replace").strip()
        print("Arduino response:", response)


if __name__ == "__main__":
    main()
