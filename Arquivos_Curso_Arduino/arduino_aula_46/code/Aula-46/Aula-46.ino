#include "Btn.h"

#define btn_pin 0 //Int 0 = Pino 2

//Btn btn=new Btn(btn_pin);

int cont;

void setup() {
  attachInterrupt(btn_pin,reset,RISING);
  //LOW
  //CHANGE
    //RISING: LOW - HIGH
    //FALLING: HIGH - LOW
  cont=100;
  pinMode(btn_pin,INPUT);
  Serial.begin(9600);
}

void loop() {
  for(cont=100;cont>0;cont--){
    Serial.println(cont);
    delay(500);
  }
  Serial.println("Reiniciando contagem");

  //btn.clique(reset); 

}

void reset(){
  cont=100;
}

