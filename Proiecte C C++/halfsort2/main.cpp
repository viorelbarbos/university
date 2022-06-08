#include <iostream>
#include <fstream>
using namespace std;

ifstream f("halfsort2.in");
ofstream g("halfsort2.out");

int main()
{
    int v[101],i, aux, n,ok,imp[51],par[51],k=0,l=0;
    f>>n;
    for(i=1; i<=n; i++)
        f>>v[i];
    do
    {
        ok=1;
        for(i=2; i<=n-2; i+=2)
            if(v[i]>v[i+2])
            {
                aux=v[i];
                v[i]=v[i+2];
                v[i+2]=aux;
                ok=0;
            }
    }
    while(ok==0);
    do
    {
        ok=1;
        for(i=1; i<n-2; i+=2)
            if(v[i]<v[i+2])
            {
                aux=v[i];
                v[i]=v[i+2];
                v[i+2]=aux;
                ok=0;
            }
    }
    while(ok==0);

    for(i=1; i<=n; i++)
    {
        cout<<v[i]<<" ";
    }
    return 0;
}
