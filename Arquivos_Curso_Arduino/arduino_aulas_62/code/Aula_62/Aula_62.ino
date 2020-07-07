#define p1m1 4
#define p2m1 5
#define pvelm1 3
#define p1m2 7
#define p2m2 8
#define pvelm2 6

int vel;

class Motor{
public:
  int p1,p2,pv;
  Motor(int p1, int p2, int v){
    this->p1=p1;
    this->p2=p2;
    this->pv=v;
    pinMode(p1,OUTPUT);
    pinMode(p2,OUTPUT);
    pinMode(pv,OUTPUT);
    digitalWrite(p1,LOW);
    digitalWrite(p2,LOW);
    analogWrite(pv,0);
  }
  void frente(int v){
    digitalWrite(p1,HIGH);
    digitalWrite(p2,LOW);
    analogWrite(pv,v);
  }
  void tras(int v){
    digitalWrite(p1,LOW);
    digitalWrite(p2,HIGH);
    analogWrite(pv,v);
  }
  void para(){
    digitalWrite(p1,LOW);
    digitalWrite(p2,LOW);
    analogWrite(pv,0);
  }
  void freia(){
    digitalWrite(p1,HIGH);
    digitalWrite(p2,HIGH);
    analogWrite(pv,128);
  }
};

Motor *md=new Motor(p1m1,p2m1,pvelm1);
Motor *me=new Motor(p1m2,p2m2,pvelm2);

void setup() {
  Serial.begin(9600);
  vel=255;
}

void loop() {
  char c=Serial.read();
  if(c=='F'){
    md->frente(vel);
    me->frente(vel);
  }
  if(c=='T'){
    md->tras(vel);
    me->tras(vel);
  }
  if(c=='E'){
    md->tras(vel);
    me->frente(vel);
  }
  if(c=='D'){
    md->frente(vel);
    me->tras(vel);
  }
  if(c=='P'){
    md->para();
    me->para(vel);
  }  
}
