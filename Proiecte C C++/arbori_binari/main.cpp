#include <iostream>

using namespace std;

int n , stanga[101], dreapta[101]; // initializari

struct Nod {
    int info;
    Nod *stanga, *dreapta;
};

void Creare(Nod *&r, int x) // funtie pentru creare nod
{
    if(x != 0) // cat timp informatia din nod este diferita de 0
    {
        r = new Nod; // alocam spatiu pentru un nod
        r->info = x; // introducem informatia
        r->stanga = r->dreapta = NULL; // initializam nodul din stanga si cel din dreapta
        int y; // informatia noua
        cout << "stanga[" << x << "]="; cin >> y;// citim  informatia pentru nodul stanga
        Creare(r -> stanga , y); // daca este diferita de 0 o sa o adaugam, si o sa facem acelasi lucru si pentru ea
        cout << "dreapta[" << x << "]="; cin >> y;/// citim  informatia pentru nodul drept
        Creare(r -> dreapta , y);// daca este diferita de 0 o sa o adaugam, si o sa facem acelasi lucru si pentru ea
    }
}

/*afisam informatia de la radacina, in stanga cat timp exista trecand apoi si in dreapta, iar mai apoi trecem in dreapta radacinii,
afisand prima data informatia din stanga nodurilor cat timp exista apoi trecand in dreapta lor*/
void Preordine(Nod * r)
{
    if(r != NULL)
    {
        cout << r->info << " ";
        Preordine(r->stanga);
        Preordine(r->dreapta);
    }
}

int main()
{
    Nod * R = NULL; // initializam radacina
    int radacina_info; // informatia din radacina
    cout << "Eticheta radacinii: "; cin >> radacina_info;// citim informatia
    Creare(R , radacina_info);//incepem sa realizam arborele binar
    Preordine(R); cout << endl; // afisam in preordine arborele
    return 0;
}
