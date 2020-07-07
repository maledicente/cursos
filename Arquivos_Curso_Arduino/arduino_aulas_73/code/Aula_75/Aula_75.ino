#define rs_a A0
#define rs_d 2
#define led 13

void setup() {
  pinMode(rs_d,INPUT);
  pinMode(led,OUTPUT);
}

void loop() {
  int valor_d=digitalRead(rs_d);
  int valor_a=analogRead(rs_a);

  if(valor_d == 1){
    digitalWrite(led,HIGH);
  }else{
    digitalWrite(led,LOW);
  }
}
