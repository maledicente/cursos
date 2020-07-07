//Referência Wire = https://www.arduino.cc/en/Reference/Wire
#include "Wire.h"

#define enderecoEscravo 0x100 //Pode ser um enredeço de 0 a 255
#define tmp 2000
bool led=HIGH;

void setup() {
  Wire.begin();
}

void loop() {
  Wire.beginTransmission(enderecoEscravo);
  Wire.write(led);
  Wire.endTransmission();
  led=!led;
  delay(tmp);
}
