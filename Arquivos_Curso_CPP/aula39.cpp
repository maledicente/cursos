#include <iostream>
#include <stdio.h> //Para fun��o gets
#include <stdlib.h> //Para fun��o malloc

using namespace std;

int main(){

    char *vnome;
    vnome = (char *) malloc(sizeof(char)+1);

    gets(vnome);

    cout << vnome;

	return 0;
}
