
#include <iostream>
using namespace std;
/*
functie care face adaugarea unui element;
functie care face listarea elementelor listei;
functe care face extragerea unui element cu o informatie utila data.
*/

struct nod
{
    int informatie;
    nod *urmator,*inapoi;
};

//initializare
void init(nod* &cap, nod* &coada)
{
    cap = coada = NULL;
}

//afisam lista de la cap la coada
void afisareLista(nod *cap,nod *coada)
{
    if(cap == NULL)
    {
        cout<<"Lista nu are elemente!!!\n\n";
    }
    else
    {
        cout<<"Lista circulara dublu inlantuita este: ";
        while(cap != NULL)
        {
            cout<<cap->informatie<<", ";
            if(cap == coada)
                cap = NULL;
            else
                cap = cap->urmator;
        }
        cout<<"\n\n";
    }
}

//extragerea ultimului element adaugat in lista
void extragereUltim(nod* &cap, nod* &coada)
{
    if(cap == NULL)
    {
        cout<<"Lista nu are elemente!!!\n\n";
    }
    else if(cap == coada)
    {
        cout<<"Informatia extrasa este: "<<cap->informatie<<"\n\n";
        nod* del = cap;
        cap = cap->urmator;
        cap->inapoi = coada;
        delete del;
        cap=coada=NULL;
    }
    else
    {
        cout<<"Informatia extrasa este: "<<cap->informatie<<"\n\n";
        nod* del = cap;
        cap = cap->urmator;
        cap->inapoi = coada;
        delete del;
    }


}


//adaugam un element in fata capului listei
void inserareLista(nod* &cap,nod* &coada,int informatie)
{
    nod *New = new nod;
    New->informatie = informatie;

    if(cap == NULL)  //daca lista este goala capul si coada sunt aceleasi
    {
        cap = coada = New;
        New->urmator = coada;
        New->inapoi = cap;
    }
    else if(cap == coada) //daca avem un singur element
    {
        New->urmator = coada;
        New->inapoi = coada;
        cap = New;
        coada->urmator = New;
        coada->inapoi = New;
    }
    else
//in caz contrar noul element devine capul listei
    {
        New->urmator = cap;
        cap->inapoi = New;
        New->inapoi = coada;
        coada->urmator = New;
        cap = New;
    }
}





int main()
{
    nod *cap;
    nod *coada;
    init(cap, coada);
    inserareLista(cap, coada, 10);
    inserareLista(cap, coada, 20);
    inserareLista(cap, coada, 30);
    inserareLista(cap, coada, 40);
    inserareLista(cap, coada, 50);
    afisareLista(cap, coada);
    extragereUltim(cap, coada);
    afisareLista(cap, coada);
    extragereUltim(cap, coada);
    afisareLista(cap, coada);
    return 0;
}
