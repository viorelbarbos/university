#include <iostream>
using namespace std;

class Vector{
    int *linie;
public:
    Vector(int *linie):linie(linie){}
};

int main()
{
    int a[] = {1,2,3,4,5,6};
    Vector v(a);

    for(int i = 0; i<6;i++)
        cout<<*v++<<", ";
    return 0;
}
