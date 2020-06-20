#include <iostream>
#include <fstream>

using namespace std;

int main() {

    //ofstream, ifstream, fstream

    ofstream arquivo;

    arquivo.open("cfbcursos.txt");

    arquivo << "CFB Cursos\n";
    arquivo << "Curso de C++\n";
    arquivo << "cfbcursos.com.br\n";
    arquivo << "youtube.com/cfbcursos\n";

    arquivo.close();


	return 0;
}
