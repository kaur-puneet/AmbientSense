import serial
import time

PORT = "/dev/cu.usbserial-0001"
BAUD_RATE = 115200

ser = serial.Serial(PORT, BAUD_RATE, timeout=1)

# Give the ESP32 time to reset after opening the serial connection
time.sleep(2)

# Discard any partial/old data in the serial buffer
ser.reset_input_buffer()

print(f"Connected to ESP32 on {PORT}")

while True:
    line = ser.readline().decode("utf-8", errors="ignore").strip()

    if line:
        print(line)