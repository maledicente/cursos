#include <TimerOne.h>

#define led_alarme_pino 7
#define led_armado_pino 13
#define btn 2

int led_alarme=LOW;
int led_armado=LOW;
bool armado=false;

void setup() {
  pinMode(led_alarme_pino,OUTPUT);
  pinMode(led_armado_pino,OUTPUT);
  attachInterrupt(digitalPinToInterrupt(btn),toogle_alarme,FALLING);
}

void loop() {}

void alarme(){
  digitalWrite(led_alarme_pino,!digitalRead(led_alarme_pino));
}

void toogle_alarme(){
  if(armado){
    digitalWrite(led_armado_pino,LOW);
    armado=false;
    Timer1.detachInterrupt();
    digitalWrite(led_alarme_pino,LOW);
  }else{
    digitalWrite(led_armado_pino,HIGH);
    armado=true;
    Timer1.initialize(1000000);
    Timer1.attachInterrupt(alarme);
  }
}

