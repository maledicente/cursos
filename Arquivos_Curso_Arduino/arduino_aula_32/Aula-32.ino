#include <LiquidCrystal.h>

LiquidCrystal lcd(7,6,5,4,3,2);

void setup() {
  lcd.begin(16,2);
  lcd.clear();
}

void loop() {
  lcd.setCursor(3,0);
  lcd.print("CFB CURSOS");
  lcd.setCursor(4,1);
  lcd.print("Arduino");
  delay(3000);

  for(int pos=0;pos<3;pos++){
    lcd.scrollDisplayLeft();
    delay(100);
  }

  for(int pos=0;pos<6;pos++){
    lcd.scrollDisplayRight();
    delay(100);
  }

  for(int pos=0;pos<3;pos++){
    lcd.scrollDisplayLeft();
    delay(100);
  }
  delay(1000);
  lcd.noDisplay();
  delay(500);
  lcd.display();
  delay(500);
  lcd.noDisplay();
  delay(500);
  lcd.display();
  delay(500);
  lcd.noDisplay();
  delay(500);
  lcd.display();
  delay(500);

}
