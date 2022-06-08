#include <iostream>
using namespace std;

class Clasa{
    int x;double y;
public:
    Clasa(int x, double y):x(x), y(y){}
    void af(){cout<<x<<y;}
};


int main()
{
    Clasa *p=new Clasa(1, 2);
    p->af();
    return 0;
}
