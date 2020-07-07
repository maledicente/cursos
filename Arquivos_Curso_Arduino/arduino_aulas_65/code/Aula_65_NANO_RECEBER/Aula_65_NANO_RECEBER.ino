#include "Wire.h"

#define ledpino 13
#define meuEndereco 0x101

void setup() {
  Wire.begin(meuEndereco);
  Wire.onReceive(receptor);
  pinMode(ledpino,OUTPUT);
}

void loop() {
}

void receptor(int quantidade){
  if(Wire.available()){
    char recebido=Wire.read();
    digitalWrite(ledpino,recebido);
  }
}
