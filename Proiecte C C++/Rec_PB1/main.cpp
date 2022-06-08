#include <iostream>
using namespace std;

void cifre(int n, int &nr_par, int &nr_impar)
{
    if(n<=9)
        if(n%2==0) {
            nr_par=n; nr_impar=0;
        }
            else {
                nr_par=0; nr_impar=n;
            }
    else{

        cifre(n/10,nr_par,nr_impar);
        if(n%2==0)
            nr_par=nr_impar*10+n%10;
        else
            nr_impar=nr_impar*10+n%10;
    }
}

int main()
{
    int n, p, i;
    cifre(0, p, i);
    cout<<p<<" "<<i;
    return 0;
}
