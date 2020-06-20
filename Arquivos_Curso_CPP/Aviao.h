#ifndef AVIAO_H_INCLUDED
#define AVIAO_H_INCLUDED

class Aviao{
public:
    int vel=0;
    int velMax;
    std::string tipo;
    Aviao(int tp);
    void imprimir();
private:

};

Aviao::Aviao(int tp){//1=Jato  2=Monomotor  3=Planador
    if(tp==1){
        tipo="Jato";
        velMax=800;
    }else if(tp==2){
        tipo="Monomotor";
        velMax=350;
    }else if(tp==3){
        tipo="Planador";
        velMax=180;
    }
}

void Aviao::imprimir(){
    std::cout << "Tipo.............: " << tipo << std::endl;
    std::cout << "Velocidade máxima: " << velMax << std::endl;
    std::cout << "Velocidade atual.: " << vel << std::endl;
    std::cout << "-----------------------------------------" << std::endl;
}


#endif // AVIAO_H_INCLUDED
