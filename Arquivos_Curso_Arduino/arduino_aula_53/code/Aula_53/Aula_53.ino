#include <dht.h>

#define pinoDHT11 7
#define tmp 2000

dht sensorDHT11;

void setup() {
  Serial.begin(9600);
  delay(tmp);
}

void loop() {
  sensorDHT11.read11(pinoDHT11);
  Serial.print("Umidade: ");
  Serial.print(sensorDHT11.humidity);
  Serial.println("%");
  Serial.print("Temperatura: ");
  Serial.print(sensorDHT11.temperature,0);
  Serial.println("C");
  Serial.println("-------------------------------------");
  delay(tmp);
}
