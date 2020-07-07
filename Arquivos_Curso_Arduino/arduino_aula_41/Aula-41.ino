#include <IRremote.h>

#define receptor 11

IRrecv recIR(receptor);
decode_results resultado;

void setup() {
  Serial.begin(9600);
  recIR.enableIRIn();//Inicializar receptor IR
}

void loop() {
  if(recIR.decode(&resultado)){
    Serial.print("Valor: ");
    Serial.println(resultado.value,HEX);
    recIR.resume();
  }
}
