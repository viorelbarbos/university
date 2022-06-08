#include <iostream>
using namespace std;

void citire(int vec[], int n) { // functie recursiva de citire

    if(n>0)
    {
        citire(vec,n-1);
        cin>>vec[n];
    }
}

int sum_paritate(int n, int p) {

    if(n==0)
        return 0;
    else if(n%2==p)
        return sum_paritate(n/10,p)+n%10;
    else
        return sum_paritate(n/10,p);
}

void inlocuire(int vec[], int n) {

    if(n>0)
    {
        inlocuire(vec,n-1);
        vec[n]=sum_paritate(vec[n],n%2);
    }
}

void afisare(int vec[], int n)
{
    if(n>0)
    {
        afisare(vec,n-1);
        cout<<vec[n]<<" ";
    }
}

int main()
{
    int vec[101],n;
    cout<<"Introduceti numarul de elemente ale vectorului: ";cin>>n;
    cout<<"\nIntroduceti elementele vectorului: ";
    citire(vec,n);
    inlocuire(vec,n);
    cout<<"\nVectorul dupe prelucrare este: ";
    afisare(vec,n);
    return 0;
}
