#include <VirtualWire.h>

#define led 13

uint8_t buf[1];
uint8_t buftam=1;

void setup() {
  vw_set_rx_pin(5);
  vw_setup(2000);//Bits por segundo
  vw_rx_start();
  pinMode(led,OUTPUT);
}

void loop() {
  //vw_get_message(uint8_t *buf, uint8_t *len);
  if(vw_get_message(buf,&buftam)){
    if(buf[0]=='A'){
      digitalWrite(led,HIGH);
    }else{
      digitalWrite(led,LOW);
    }
  }
  

}
