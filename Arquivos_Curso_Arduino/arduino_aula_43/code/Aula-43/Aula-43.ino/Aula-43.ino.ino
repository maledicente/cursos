#include <IRremote.h>

#define bt1 8
#define bt2 9

IRsend irsend;
unsigned long valor;
decode_results res;
decode_type_t tipo;

void setup() {
  Serial.begin(9600);
  pinMode(bt1,INPUT);
  pinMode(bt2,INPUT);
}

void loop() {
  if(digitalRead(bt1)==1){//Esquerda
    valor=0xFF22DD;  
    irsend.sendRC5(valor,12);
    Serial.println(valor,HEX);
    tipo=res.decode_type;
    Serial.println(tipo);
    delay(100);
  }else if(digitalRead(bt2)==1){//Direita
    valor=0xFFC23D;
    irsend.sendRC5(valor,12);
    Serial.println(valor,HEX);
    tipo=res.decode_type;
    Serial.println(tipo);    
    delay(100);
  }

}
/*FORMATOS DE ENVIO
 * NEC - 32bits
 * RC5 - 12bits
 * RC6 - 20bits
 * SONY - 20bits
 * UNKNOWN
 */
