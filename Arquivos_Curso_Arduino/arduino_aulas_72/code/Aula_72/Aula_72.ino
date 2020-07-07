#define pinorele 7
#define pinosom 4

bool rele;

void setup() {
  pinMode(pinorele,OUTPUT);
  pinMode(pinosom,INPUT);
  rele=false;
  digitalWrite(pinorele,rele);
}

void loop() {
  if(digitalRead(pinosom)==HIGH){
    rele=!rele;
  }
  digitalWrite(pinorele,rele);
}
