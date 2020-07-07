#include <SoftwareSerial.h>

#define led1 6
#define led2 7

SoftwareSerial bt_serial(11,12);//RX e TX

void setup() {
  bt_serial.begin(9600);
  pinMode(led1,OUTPUT);
  pinMode(led2,OUTPUT);
}

void loop() {
  char c=bt_serial.read();
  if(c=='A'){digitalWrite(led1,HIGH);}
  if(c=='a'){digitalWrite(led1,LOW);}
}
