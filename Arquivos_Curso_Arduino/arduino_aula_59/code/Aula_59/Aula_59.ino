#include <Keypad.h>

#define linhas 4
#define colunas 3
char mapaTeclas[4][3]={{'1','2','3'},{'4','5','6'},{'7','8','9'},{'*','0','#'}};
byte pinos_linha[linhas]={6,7,8,9};
byte pinos_coluna[colunas]={10,11,12};

Keypad teclado=Keypad(makeKeymap(mapaTeclas),pinos_linha,pinos_coluna,linhas,colunas);
//Keypad keypad = Keypad( makeKeymap(), rowPins, colPins, rows, cols );

void setup() {
  Serial.begin(9600);
}

void loop() {
  char tecla=teclado.getKey();
  if(tecla != NO_KEY){
    Serial.println(tecla);
  } 
}
