#include <iostream>
using namespace std;
class Numar
{
    int n;
public:
    void afiseaza()
    {
        cout<<n<<" ";
    }
    Numar(int n=0):n(n) {}
};
template <class td> class Set
{
    td *x, *y;
public:
    Set(td *x, td *y):x(x), y(y) {}
    void afiseaza()
    {
        x->afiseaza();
        cout<<",";
        y->afiseaza();
    }
};

int main()
{
    Set<Numar> s1(new Numar(10), new Numar(3));
    s1.afiseaza();
    return 0;
}
