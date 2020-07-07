#include <Keypad.h>

#define linhas 4
#define colunas 3
#define led_vermelho 2
#define led_verde 3
#define led_amarelo 4

char mapaTeclas[linhas][colunas]={{'1','2','3'},{'4','5','6'},{'7','8','9'},{'*','0','#'}};
String senha="123";
String digitada;
int estado=0;
byte pinos_linha[linhas]={6,7,8,9};
byte pinos_coluna[colunas]={10,11,12};

Keypad teclado = Keypad(makeKeymap(mapaTeclas),pinos_linha,pinos_coluna,linhas,colunas);

void setup() {
  pinMode(led_vermelho,OUTPUT);
  pinMode(led_verde,OUTPUT);
  pinMode(led_amarelo,OUTPUT);
}

void loop() {
  char tecla=teclado.getKey();
  if(tecla != NO_KEY){
    estado=1;
    if(tecla=='#'){
      if(verifcaSenha(senha,digitada)){
        estado=3;
        leds(estado);
        delay(3000);
        estado=0;
      }else{
        estado=2;
        leds(estado);
        delay(3000);
        estado=0;
      }
      digitada="";
    }else{
      digitada+=tecla;
    }
    leds(estado);
  }
}

bool verifcaSenha(String sa, String sd){
  bool resultado=false;
  if(sa.compareTo(sd)==0){
    resultado=true;
  }else{
    resultado=false;
  }
  return resultado;
}

void leds(int e){//0=Aguardando / 1=Digitando / 2=Negado / 3=Aceito
  if(e==0){
    digitalWrite(led_vermelho,LOW);
    digitalWrite(led_verde,LOW);
    digitalWrite(led_amarelo,LOW);
  }else if(e==1){
    digitalWrite(led_vermelho,LOW);
    digitalWrite(led_verde,LOW);
    digitalWrite(led_amarelo,HIGH);
  }else if(e==2){
    digitalWrite(led_vermelho,HIGH);
    digitalWrite(led_verde,LOW);
    digitalWrite(led_amarelo,LOW);
  }else if(e==3){
    digitalWrite(led_vermelho,LOW);
    digitalWrite(led_verde,HIGH);
    digitalWrite(led_amarelo,LOW);
  }
}
