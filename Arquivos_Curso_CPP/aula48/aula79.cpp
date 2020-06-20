#include <iostream>
#include <ctime> //time.h

using namespace std;

int main() {

    clock_t c;
    size_t tam;
    time_t t;
    struct tm * infoTempo;

    char buffer[80];

    time(&t);
    infoTempo=localtime(&t);

    strftime(buffer,80,"%d/%m/%Y",infoTempo);

    cout << buffer << endl;

 	return 0;
}
