#include <dht.h>
#include "Btn.h"
#include <LiquidCrystal_I2C.h>

#define pinoDHT11 7
#define btn_pin 3
#define tmp 2000;

LiquidCrystal_I2C lcd(0x27,2,1,0,4,5,6,7,3,POSITIVE);
dht sensorDHT11;
Btn btn=new Btn(btn_pin);

int tela=1;

byte num[8]={
  0b00100,
  0b01010,
  0b00100,
  0b00000,
  0b00000,
  0b00000,
  0b00000,
  0b00000
};

void setup() {
  pinMode(btn_pin,INPUT_PULLUP);
  lcd.begin(16,2);
  lcd.backlight();
  lcd.createChar(1,num);
}

void loop() {
  sensorDHT11.read11(pinoDHT11);
  btn.clique(mudaTela);
  imprimeDados(tela);
  delay(250);
}

void mudaTela(){
  tela=!tela;
  lcd.clear();
  imprimeDados(tela);
}

void imprimeDados(int t){
  if(t){
    lcd.home();
    lcd.print("Temperatura:");
    lcd.setCursor(13,0);
    lcd.print(sensorDHT11.temperature,0);
    lcd.setCursor(15,0);
    lcd.write((byte)1);
    lcd.setCursor(0,1);
    lcd.print("CFB Cursos");    
  }else{
    lcd.home();
    lcd.print("Umidade:");
    lcd.setCursor(9,0);
    lcd.print(sensorDHT11.humidity,0);
    lcd.setCursor(11,0);
    lcd.print("%");
    lcd.setCursor(0,1);
    lcd.print("CFB Cursos");     
  }
}

