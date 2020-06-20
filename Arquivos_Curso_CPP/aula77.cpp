#include <iostream>
#include <functional>

using namespace std;

class Cfb{
public:
    int num;
    Cfb(int n):num(n){};
    int dobro(){
        return num*2;
    }
};

int main() {

    Cfb n1{10};
    Cfb n2{5};

    auto dobro2=mem_fn(&Cfb::dobro);

    cout << dobro2(n1) << endl;

	return 0;
}

