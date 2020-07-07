#include "Btn.h"

#define led_pino 6
#define btn_pino 2

int estado_led=HIGH;

void toogle_led(){
  estado_led=!estado_led;
  digitalWrite(led_pino,estado_led);
}

Btn btn = new Btn(btn_pino);

void setup() {
  digitalWrite(led_pino,estado_led);
}

void loop() {
  
  btn.clique(toogle_led);

}


