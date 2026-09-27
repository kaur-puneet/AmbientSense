import serial
import time

PORT = "/dev/cu.usbserial-0001"
BAUD_RATE = 115200


def parse_sensor_data(line):
    parts = line.split(" | ")

    if len(parts) != 3:
        return None

    try:
        temperature = float(parts[0].split(": ")[1].replace(" °C", ""))
        humidity = float(parts[1].split(": ")[1].replace(" %", ""))
        light = int(parts[2].split(": ")[1])

        return temperature, humidity, light

    except (ValueError, IndexError):
        return None


ser = serial.Serial(PORT, BAUD_RATE, timeout=1)

time.sleep(2)
ser.reset_input_buffer()

print(f"Connected to ESP32 on {PORT}")

while True:
    line = ser.readline().decode("utf-8", errors="ignore").strip()

    if not line:
        continue

    sensor_data = parse_sensor_data(line)

    if sensor_data is None:
        continue

    temperature, humidity, light = sensor_data

    print(
        f"Temperature: {temperature} °C | "
        f"Humidity: {humidity} % | "
        f"Light: {light}"
    )