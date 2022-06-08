#include <iostream>
using namespace std;

class Tab{
    int *tab;
public:
    int dim;
    Tab(int dim=8){
    this->dim=dim;
    tab=new int[dim];
    }
};

int main(){
    Tab t1(5);
    Tab *p = new Tab;
   return 0;
}
