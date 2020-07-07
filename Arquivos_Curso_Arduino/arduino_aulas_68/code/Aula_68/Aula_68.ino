/*
  0V = 0
  5V = 1023
  Cada G.C.:10mV/°C

  Tensão em A0 = (Valor lido em A0)*(5.0/1023)
  Temp = Tensão em A0 / 10mV

  Logo

  temp=(Valor_lido_A0*(5.0/1023))/10mV
  temp=(Valor_lido_A0*(5.0/1023))/0.01
*/
#define pino A0
int temp=0,ultimatemp=0;
int media[10];

void setup() {
  Serial.begin(9600);
}

void loop() {
  for(int i=0;i<10;i++){
    media[i]=(analogRead(pino)*(5.0/1023))/0.01;
    temp=temp+media[i];
    delay(100);
  }
  temp=temp/10.0;
  
  if(temp!=ultimatemp){
    ultimatemp=temp;
    Serial.print("Temp: ");
    Serial.print(temp);
    Serial.println("°C");
  }
  delay(1000);
}
