#define btn_pin 3
#define led_pin 4

void setup() {
  pinMode(btn_pin,INPUT_PULLUP);
  pinMode(led_pin,OUTPUT);
}

void loop() {
  if(digitalRead(btn_pin)){
    digitalWrite(led_pin,digitalRead(btn_pin));
  }else{
    digitalWrite(led_pin,digitalRead(btn_pin));
  }

}

