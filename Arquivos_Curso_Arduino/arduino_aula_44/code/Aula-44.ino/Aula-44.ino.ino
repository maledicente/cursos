#define led 3
int valor_lido;

void setup() {
  Serial.begin(9600);
  pinMode(led,OUTPUT);
}

void loop() {
  if(Serial.available()>0){
    valor_lido=Serial.read();
  }

  if(valor_lido=='1'){
    digitalWrite(led,HIGH);
  }else{
    digitalWrite(led,LOW);
  }

}
