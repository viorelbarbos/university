#include <iostream>

using namespace std;

class Lemon
{
    int lamai, zahar;
    float suma;
public:
    void init(int l, int c, float s);
    void afisare_ingrediente();
    void limonada_neindulcita();
    void limonada_indulcita();
    void suma_incasata();

};

void Lemon::init(int l, int c, float s = 0)
{   cout<<"Introduceti numarul de lamai: ";cin>>l;
    cout<<"Introduceti numarul de cuburi de zahar: ";cin>>c;cout<<endl;
    lamai  = l;
    zahar = c;
    suma = s;
}

void Lemon::limonada_neindulcita()
{
    if(lamai <= 0)
    {
        cout<<"Ingrediente lipsta!\n";
        cout<<"Suma incasata este: "<<suma<<" lei\n";
        exit(0);
    }
    else
    {
        lamai--;
        suma +=3;
        cout<<"`````````````````````````````````\n";
        cout<<"Ai primit o limodata neindulcita!\n";
        cout<<"`````````````````````````````````\n";
    }

}

void Lemon::limonada_indulcita()
{
    if(lamai == 0)
    {
        cout<<"Ingrediente lipsta!\n";
        cout<<"Suma incasata este: "<<suma<<" lei\n";
        exit(0);
    }
    else if(zahar <= 1)
    {
        cout<<"Ingrediente lipsta!\n";
        cout<<"Suma incasata este: "<<suma<<" lei\n";
        cout<<"Incercati o limonada neindulcita!\n";
    }
    else
    {
        lamai -=1;
        zahar -= 2;
        suma +=3;
        cout<<"`````````````````````````````````\n";
        cout<<"Ai primit o limodata indulcita!\n";
        cout<<"`````````````````````````````````\n";
    }

}

void Lemon::afisare_ingrediente()
{
    cout<<"Mai sunt "<<lamai<<" lamai si "<<zahar<<" cuburi de zahar\n";
}

void Lemon::suma_incasata(){
    cout<<"S-au incasat "<<suma<<" lei"<<endl;
}
int main()
{   int a,b;
    Lemon limonada;
    limonada.init(a, b);
    int choice;
    do
    {
        cout<<"--------------------------------------------\n";
        cout<<"MENIU\n";
        cout<<"1. Limonada indulcita;\n";
        cout<<"2. Limonada neindulcita;\n";
        cout<<"3. Total incasari;\n";
        cout<<"4. Iesire.\n\n";
        cout<<"--------------------------------------------\n";
        limonada.afisare_ingrediente();
        cin>>choice;
        cout<<"-------------------------------------------\n";
        switch(choice)
        {
        case 1:
            limonada.limonada_indulcita();
            break;
        case 2:
            limonada.limonada_neindulcita();
            break;
        case 3:
            cout<<"`````````````````````````````````\n";
            limonada.suma_incasata();
            cout<<"`````````````````````````````````\n";
            break;
        case 4:
            exit(0);
        default:
            cout<<" Alegeti una dintre optiunile mentionate!\n";
        }
    }
    while(choice != 4);
    return 0;
}
