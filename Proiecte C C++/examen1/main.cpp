#include <iostream>
using namespace std;

class Punct
{
    double x,y;
public:
    void afiseaza()
    {
        cout<<"\nx="<<x<<", y="<<y;
    }
    void init(double, double);
};
void Punct::init(double abs, double ord)
{
    x=abs;
    y=ord;
}

int main()
{
    Punct a,b, *p;
    p=new Punct;
    a.init(3,4);
    p->init(5,6);
    a.afiseaza();
    p->afiseaza();
    b=a;
    b.afiseaza();
    delete p;
    return 0;
}
