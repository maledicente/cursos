#include <iostream>

using namespace std;

int main() {

    string veiculo="Carro";
    string *pv;

    pv=&veiculo; //Ponteiro PV recebe o endere�o da vari�vel veiculo

    cout << pv << "\n" << &veiculo;

    *pv="Moto"; //No endere�o apontado por *pv adicione o valor "Moto"

    cout << "\n" << veiculo << "\n" << *pv;

	return 0;

}
