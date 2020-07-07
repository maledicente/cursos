int portas_led[2]={6,7};

void setup() {
  for(int pinos_led=0;pinos_led<2;pinos_led++){
    pinMode(portas_led[pinos_led],OUTPUT);
  }
  Serial.begin(9600);
}

void loop() {
  char c=Serial.read();
  if(c=='A'){digitalWrite(portas_led[0],HIGH);}//Quadrado
  if(c=='a'){digitalWrite(portas_led[0],LOW);}//Triangulo

}
