#include <iostream>

using namespace std;

struct limonada
{
    int nr_lamai, nr_cuburi_zahar, suma_incasata;

};

void citire(limonada &ex) {
    cout << "\nIntroduceti numarul de lamai si numarul de cuburi de zahar: ";
    cin>>ex.nr_lamai>>ex.nr_cuburi_zahar;

}

void limonada_indulcita(limonada &ex) {
    if(ex.nr_lamai == 0) {
        cout<<"Ingrediente lipsta!\n";
        cout<<"Suma incasata este: "<<ex.suma_incasata<<" lei\n";
        exit(0);
    }
    else if(ex.nr_cuburi_zahar <= 1)
    {   cout<<"Ingrediente lipsta!\n";
        cout<<"Suma incasata este: "<<ex.suma_incasata<<" lei\n";
        cout<<"Incercati o limonada neindulcita!\n";
    }
    else
    {   ex.nr_lamai -=1;
        ex.nr_cuburi_zahar -= 2;
        ex.suma_incasata +=3;
        cout<<"`````````````````````````````````\n";
        cout<<"Ai primit o limodata indulcita!\n";
        cout<<"`````````````````````````````````\n";
    }
}

void limonada_neindulcita(limonada &ex) {
    if(ex.nr_lamai <= 0)
    {   cout<<"Ingrediente lipsta!\n";
        cout<<"Suma incasata este: "<<ex.suma_incasata<<" lei\n";
        exit(0);
    }
    else
    {
        ex.nr_lamai--;
        ex.suma_incasata +=3;
        cout<<"`````````````````````````````````\n";
        cout<<"Ai primit o limodata neindulcita!\n";
        cout<<"`````````````````````````````````\n";
    }
}

int main()
{
    struct limonada ex = {0, 0, 0};
    citire(ex);
    int choice;
    do{
    cout<<"--------------------------------------------\n";
    cout<<"MENIU\n";
    cout<<"1. Limonada indulcita;\n";
    cout<<"2. Limonada neindulcita;\n";
    cout<<"3. Total incasari;\n";
    cout<<"4. Iesire.\n\n";
    cout<<"--------------------------------------------\n";
    cout<<"Ingredientele disponibile sunt: "<<ex.nr_lamai<<" lamai si "<<ex.nr_cuburi_zahar<<" cuburi de zahar.\n";
    cin>>choice;
    cout<<"-------------------------------------------\n";
    switch(choice)
    {
    case 1:
        limonada_indulcita(ex);
        break;
    case 2:
        limonada_neindulcita(ex);
        break;
    case 3:
        cout<<"`````````````````````````````````\n";
        cout<<"Suma incasata este: "<<ex.suma_incasata<<" lei\n";
        cout<<"`````````````````````````````````\n";
        break;
    case 4:
        exit(0);
    default:
        cout<<" Alegeti una dintre optiunile mentionate!";
    }
    }while(choice != 4);

    return 0;
}
