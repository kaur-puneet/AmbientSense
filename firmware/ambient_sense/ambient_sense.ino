#include "DHT.h"

#define DHTPIN 4
#define DHTTYPE DHT11
#define LDR_PIN 34

DHT dht(DHTPIN, DHTTYPE);

void setup() {
  Serial.begin(115200);
  dht.begin();
}

void loop() {
  float humidity = dht.readHumidity();
  float temperature = dht.readTemperature();
  int lightValue = analogRead(LDR_PIN);

  if (isnan(humidity) || isnan(temperature)) {
    Serial.println("DHT11 read failed");
  } else {
    Serial.print("Temperature: ");
    Serial.print(temperature);
    Serial.print(" °C | Humidity: ");
    Serial.print(humidity);
    Serial.print(" % | Light: ");
    Serial.println(lightValue);
  }

  delay(2000);
}