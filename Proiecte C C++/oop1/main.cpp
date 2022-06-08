#include <iostream>
#include <string.h>
#include <stdio.h>
using namespace std;

class A{
    int x;
public:
    A(int x):x(x){cout<<x<<' ';}
    class B{
        int y;
    public:
        B(int y):y(y){cout<<y<<' ';}
        void test(){A a(1);}
    };
    void test(){B b(2);}
};


int main()
{
    A a(3);
    a.test();
    B b(4);
    b.test();
        return 0;
}
