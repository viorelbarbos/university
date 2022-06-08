#include <iostream>
#include <string.h>
using namespace std;
struct Nod
{
    int nr_nod;
    string titlu;
    double pret;
    Nod* leg;
};
void init(Nod* &prim, Nod* &ultim)
{
    prim = ultim = NULL;
}
void adaugare_la_sfarsit(Nod* &prim, Nod* &ultim, int nods, string tit, double
                         pt)
{
    Nod* a;
    a = new Nod;
    a->nr_nod = nods;
    a->titlu = tit;
    a->pret = pt;
    a->leg = NULL;
    if (prim==NULL)
    {
        prim = a;
    }
    else
    {
        ultim->leg = a;
    }
    ultim = a;
}
void afiseaza(Nod* prim)
{
    Nod* a = prim;
    while(a->leg != NULL)
    {
        cout<<a->nr_nod;
        cout<<", ";
        cout<<a->titlu;
        cout<<", ";
        cout<<a->pret;
        cout<<"| ";
        a = a->leg;
        cout<<endl;
    }
    cout<<a->nr_nod<<", "<<a->titlu<<", "<<a->pret<<endl;
}
void adaugare_la_inceput(Nod* &prim, Nod* &ultim, int nods, string tit, double
                         pt)
{
    Nod* a = new Nod;
    a->nr_nod = nods;
    a->titlu = tit;
    a->pret = pt;
    a->leg = NULL;
    if (prim==NULL)
    {
        ultim = a;
    }
    else
    {
        a->leg = prim;
    }
    prim = a;

}

Nod* cautare_beta(Nod* prim,int cautat)
{
    Nod* a = prim;
    while(a!= NULL)
    {
        if(cautat == a->leg->nr_nod) return a;
        a = a->leg;
    }
    return NULL;
}

void extragere_interior(Nod* &prim, Nod* &ultim, int cautat)
{
    Nod* q = cautare_beta(prim, cautat);
    if(q)
    {
        Nod*p = q->leg;
        q->leg = p->leg;
        delete p;
        cout<<"Nodul cu nr_nod "<<cautat<< " s-a extras";

    }
    else
    {
        if(!(q->leg))
            ultim = q;

        else
            cout<<"Nodul nu a fost gasit";
    }
}

void extragere_prim(Nod* &prim){
    Nod* a = prim;
    if(prim){
        prim = a->leg;
        delete a;
        cout<<"Primul nod s-a extras";
    }
    else
        cout<<"Lista este vida";
}

void extragere_ultim(Nod* &prim, Nod* &ultim) {
    Nod* q = prim;

        Nod*p = q->leg;
        q->leg = p->leg;
        delete p;
        cout<<"Nodul ultim s-a extras";


}

int main()
{
    Nod *prim, *ultim;
    init(prim, ultim);
    for(int i = 0; i<5; i++)
        adaugare_la_sfarsit(prim, ultim, i, "sf", i + 0.5);
    for(int i = 5; i<10; i++)
        adaugare_la_inceput(prim,ultim,i, "inc", i + 0.5);
    afiseaza(prim);
    cout<<"\n\n";
    extragere_interior(prim, ultim, 1);
    cout<<endl;
    afiseaza(prim);
    cout<<endl;
    extragere_prim(prim);
    cout<<endl;
    afiseaza(prim);
    cout<<"\n\n\n";
    extragere_ultim(prim, ultim);
    cout<<endl;
    afiseaza(prim);
    return 0;
}
