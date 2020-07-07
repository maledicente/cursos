#include <IRremote.h>

#define receptor 11
#define mp1 2
#define mp2 3

IRrecv recIR(receptor);
decode_results resultado;

void setup() {
  pinMode(mp1,OUTPUT);
  pinMode(mp2,OUTPUT);
  Serial.begin(9600);
  recIR.enableIRIn();//Inicializar receptor IR
}

void loop() {
  if(recIR.decode(&resultado)){
    //Serial.print("Valor: ");
    //Serial.println(resultado.value,HEX);
    switch(resultado.value){
      case 0xFF629D: //Cima
        frente();
      break;
      case 0xFFA857://Baixo
        tras();
      break;
      case 0xFF02FD:;//OK
        parar();
      break;
    }
    recIR.resume();
  }

}

void parar(){
  digitalWrite(mp1,0);
  digitalWrite(mp2,0);
}
void frente(){
  digitalWrite(mp1,1);
  digitalWrite(mp2,0);
}
void tras(){
  digitalWrite(mp1,0);
  digitalWrite(mp2,1);
}



