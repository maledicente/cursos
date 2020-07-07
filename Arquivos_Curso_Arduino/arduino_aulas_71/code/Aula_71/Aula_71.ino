#define rele 7

void setup() {
  pinMode(rele,OUTPUT);
  Serial.begin(9600);
}

void loop() {
  char c=Serial.read();
  if(c=='A'){digitalWrite(rele,HIGH);}
  if(c=='a'){digitalWrite(rele,LOW);}
}
