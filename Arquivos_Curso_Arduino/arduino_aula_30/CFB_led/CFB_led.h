#ifndef CFB_LED_H_INCLUDED
#define CFB_LED_H_INCLUDED

#include <Arduino.h>

class CFB_led{
public:
    CFB_led(int pin);
    void acender();
    void apagar();
    void acender_t(int tmp);
    void apagar_t(int tmp);
    void piscar(int tmp,int loop);
private:
    int pino_led;
};

#endif // CFB_LED_H_INCLUDED
