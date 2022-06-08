#include <iostream>

using namespace std;

class Tab{
    int *tab;
public:
    int dim;
    Tab(){
        dim=5;
        int t[] = {1, 2, 3 ,4 ,5};
        tab = t;
}
void afiseaza(){
    cout<<'\n';
    for(int i =0 ;i<dim;i++)
        cout<<tab[i]<<", ";
    }
    operator int(int*){
        int s=tab[0];
        for(int i=1;i<dim;i++)
            s+=tab[i];
        return s;
    }

};

int main()
{
    Tab t1;
    cout<<t1;
    return 0;
}
