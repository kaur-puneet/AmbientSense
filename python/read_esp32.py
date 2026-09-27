import serial

PORT = "/dev/cu.usbserial-0001"
BAUD_RATE = 115200

ser = serial.Serial(PORT, BAUD_RATE, timeout=1)

print(f"Connected to ESP32 on {PORT}")

while True:
    line = ser.readline().decode("utf-8", errors="ignore").strip()

    if line:
        print(line)