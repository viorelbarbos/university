#include <iostream>

using namespace std;

struct Nod
{
    string info;
    Nod *urmator;
};

class Stiva
{
    Nod *varf;

public:
    Stiva()
    {
        varf = NULL;
    }

    void adauga(string);
    void extrage();
    void afis();
    Stiva(Stiva&);

};

Stiva::Stiva(Stiva &original)
{
    varf = NULL;
    Nod *a = original.varf;
    Nod *precedent, *b;
    while(a)
    {
        b = new Nod;
        b->info = a->info;
        if(varf)
            precedent->urmator = b;
        else
            varf = b;
        precedent = b;
        a = a->urmator;

    }
    b->urmator = NULL;
}

void Stiva::adauga(string info)
{
    Nod* nou = new Nod;
    nou->info = info;
    nou->urmator = varf;
    varf = nou;
}

void Stiva::extrage()
{
    struct Nod* aux;
    aux = varf;
    varf = varf->urmator;
    aux->urmator = NULL;
}

void Stiva::afis()
{

    Nod* curent = varf;

    while(curent)
    {
        cout << curent->info << "\n";
        curent = curent->urmator;
    }

}


int main()
{
    Stiva stiva;
    stiva.adauga("mere");
    stiva.adauga("pere");
    stiva.adauga("prune");
    stiva.afis();cout<<endl;
    stiva.adauga("ananas");
    stiva.afis();cout<<endl;
    Stiva copie(stiva);
    copie.extrage();
    copie.afis();


    return 0;
}
