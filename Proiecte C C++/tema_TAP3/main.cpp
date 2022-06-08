#include <iostream>
#include <fstream>
using namespace std;

struct Nod
{
    int el,r,c;
    Nod*precedent, *urmator;
};

void init(Nod*&prim,Nod*&ultim)
{
    prim = ultim = NULL;
}

void adaugare_la_final(Nod*&prim,Nod*&ultim, int v_el,int v_l,int v_c)
{
    Nod*nou = new Nod;
    nou->el = v_el;
    nou->r = v_l;
    nou->c = v_c;
    nou->urmator = NULL;
    if(!prim)
    {
        nou->precedent = NULL;
        prim = nou;
    }
    else
    {
        nou->precedent = ultim;
        ultim->urmator = nou;
    }
    ultim = nou;
}

void afisare(Nod*prim, Nod*ultim, int d)
{
    Nod *a;
    if (d==1)
    {
        for(a = prim; a!=NULL; a = a->urmator)
            cout<<a->el<<" "<<a->r<<" " <<a->c<<"\n";

    }
    else
    {
        for(a = ultim; a!=NULL; a = a->precedent)
            cout<<a->el<<" "<<a->r<<" " <<a->c<<"\n";

    }
}

void afisare_diagonale(Nod*prim, int nr_el)
{
    cout<<"Elementele de pe diagonala principala sunt :\n";
    for(Nod*a = prim; a; a = a->urmator)
        if(a->r == a->c)
            cout<<a->el<<" "<<a->r<<" "<<a->c<<"\n";
    cout<<"Elementele de pe diagonala secundara sunt:\n";
    for(Nod*a = prim; a; a = a->urmator)
        if(a->r == nr_el - 1 - a->c)
            cout<<a->el<<" "<<a->r<<" "<<a->c<<"\n";
}

void schimabre_semn(Nod*prim, int nr_el)
{
    for(Nod*a = prim; a; a = a->urmator)
        if(a->r == nr_el - 1 - a->c)
            cout<<0-a->el<<" "<<0-a->r<<" "<<0-a->c<<"\n";


}

ifstream fin;
int main()
{
    int n,nr_el,v_el,v_r,v_c;
    fin.open("Matrice.in");

    fin>>n;
    cout<<"numarul de elemente: "<<n<<endl;
    fin>>nr_el;

    Nod*prim, *ultim;
    init(prim,ultim);
    for(int i = 0; i<n; i++)
    {
        fin>>v_el;
        fin>>v_r;
        fin>>v_c;
        adaugare_la_final(prim,ultim,v_el,v_r,v_c);
    }
    afisare(prim,ultim,1);
    afisare_diagonale(prim,nr_el);cout<<"\n\n";
    schimabre_semn(prim, nr_el);
    return 0;
}
