#include <Servo.h>
#include <HCSR04.h>

#define p1m1 4
#define p2m1 5
#define pvelm1 3
#define p1m2 7
#define p2m2 8
#define pvelm2 6

#define pservo 10

#define p_trigger 12
#define p_echo 11

#define tmp 2000

Servo servo;
UltraSonicDistanceSensor distanceSensor(p_trigger, p_echo);

int vel;
float dist_cm;

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
  vel=128;
  servo.attach(pservo);
  servo.write(180);
}

void loop() {

  servo.write(180);
  dist_cm=distanceSensor.measureDistanceCm();
  if(dist_cm < 20){
  }
  
  md->tras(vel);
}

void verifica_dist(){
  
}

void esquerda(int v){
  md->frente(v);
  me->tras(v);
  delay(500);
}
void direita(int v){
  md->tras(v);
  me->frente(v);
  delay(500);
}
void frente(int v){
  md->frente(v);
  me->frente(v);
}
void tras(int v){
  md->tras(v);
  me->tras(v);
}
void tras(){
  md->para();
  me->para();
}




