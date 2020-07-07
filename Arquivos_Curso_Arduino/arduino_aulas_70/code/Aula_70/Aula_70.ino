#define rele 7
#define tmp 2000

void setup() {
  pinMode(rele,OUTPUT);
}

void loop() {
  digitalWrite(rele,HIGH);
  delay(tmp);
  digitalWrite(rele,LOW);
  delay(tmp);
}
