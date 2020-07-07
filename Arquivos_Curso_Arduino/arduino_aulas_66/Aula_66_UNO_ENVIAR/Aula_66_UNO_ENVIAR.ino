#include <VirtualWire.h>

#define tmp 2000

char comando[1];

void setup() {
  vw_set_tx_pin(8);
  vw_setup(2000);//Bits por segundo
  comando[0]=='a';
}

void loop() {
  if(comando[0]=='a'){
    comando[0]='A';
  }else{
    comando[0]='a';
  }
  //vw_send (uint8_t *buf, uint8_t len)
  vw_send((uint8_t *)comando,strlen(comando));
  vw_wait_tx();
  delay(tmp);
}
