#include <CFB_led.h>

CFB_led ld1(13);
CFB_led ld2(7);

void setup() {
  ld2.acender();
}

void loop() {
  
  delay(3000);
  ld2.apagar_t(2000);
  delay(10000);

}
