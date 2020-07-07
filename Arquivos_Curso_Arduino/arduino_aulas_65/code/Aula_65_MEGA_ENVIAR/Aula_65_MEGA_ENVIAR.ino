#include "Wire.h"

#define enderecoUno 0x100 //Pode ser um enredeço de 0 a 255
#define enderecoNano 0x101 //Pode ser um enredeço de 0 a 255

#define tmp 2000
bool led1=HIGH;//Uno
bool led2=LOW;//Nano

void setup() {
  Wire.begin();
}

void loop() {
  Wire.beginTransmission(enderecoUno);
  Wire.write(led1);
  Wire.endTransmission();
  led1=!led1;
  Wire.beginTransmission(enderecoNano);
  Wire.write(led2);
  Wire.endTransmission();
  led2=!led2;
  delay(tmp);
}
