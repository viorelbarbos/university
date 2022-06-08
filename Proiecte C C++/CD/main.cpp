#include <iostream>
#include <string.h>
using namespace std;

int numar_cd = 0;
class CD
{

private:
    char interpret[30];//stocam numele interpretului
    char titlu[30];//titlul albumului
    char melodii[30][50];//vector care contine melodiile
    int nr_melodii = 0;//numarul de melodi de pe CD
public:
    friend void introducere_informatii(CD magazin[101]);//functie de introducere de CD-uri
    friend  void afisare_cd(CD magazin[101]);//functie pentru a afisa continutul unui CD
    friend void ordonare(CD magazin[101], int nr_ord);// Ordoneaza piesele unui CD alfabetic
    friend void stergere_cd(CD magazin[101], int nr_ord);// Sterge CD-ul si elementele acestuia
};

void introducere_informatii(CD magazin[101])
{
    cin.get();
    int n;
    cout<<"Introduceti numele interpretului: ";
    cin.get(magazin[numar_cd].interpret, 30);
    cin.get();
    cout<<"Introduceti titlul albumului: ";
    cin.get(magazin[numar_cd].titlu, 30);
    cin.get();
    cout<<"Introduceti numarul melodiilor: " ;
    cin>>n;
    magazin[numar_cd].nr_melodii = n;
    for(int i = 0; i < n; i++)
    {
        cout<<"Introduceti numele piesei: ";
        cin.get();
        cin.get(magazin[numar_cd].melodii[i], 30);
    }
    numar_cd++;


}

void afisare_cd(CD magazin[101])
{
    for( int i = 0; i < numar_cd; i++)
    {
        cout<<"CD-ul "<<i+1<<" contine: \n";
        cout<<"Titlul albumului este: ";
        cout<<magazin[i].titlu;
        cout<<"\nNumele interpretului este: ";
        cout<<magazin[i].interpret;
        cout<<"\nPiesele de pe acest album sunt: ";
        for(int j = 0; j < magazin[i].nr_melodii; j++)
            cout<<magazin[i].melodii[j]<< " ";
        cout<<endl;
        cout<<"\n\n";
    }
    cout<<"\n";

}

void ordonare(CD magazin[101], int nr_ord)
{
    for(int i = 0; i < magazin[nr_ord].nr_melodii; i++)
    {
        for(int j = i + 1; j < magazin[nr_ord].nr_melodii; j++)
        {
            if(strcmp(magazin[nr_ord].melodii[i], magazin[nr_ord].melodii[j]) > 0)
            {
                char aux[30];
                strcpy(aux, magazin[nr_ord].melodii[i]);
                strcpy(magazin[nr_ord].melodii[i], magazin[nr_ord].melodii[j]);
                strcpy(magazin[nr_ord].melodii[j], aux);
            }
        }
    }
    cout<<"Piesele de pe cd-ul " << nr_ord + 1 <<" sunt: ";
    for(int j = 0; j < magazin[nr_ord].nr_melodii; j++)
        cout<<magazin[nr_ord].melodii[j]<< " ";
    cout<<endl;
    cout<<"\n\n";
}

void stergere_cd(CD magazin[101], int nr_ord)
{
    if(nr_ord == numar_cd-1)
    {
        numar_cd--;
        cout<<"\nSingurul CD din sistem a fost sters, va rugam introduceti altele!\n";
    }
    else
    {
        for(int i = nr_ord; i < numar_cd - 1; i++)
        {
            strcpy( magazin[i].interpret,  magazin[i + 1].interpret);
            strcpy( magazin[i].titlu, magazin[i + 1].titlu);
            magazin[i].nr_melodii = magazin[i + 1].nr_melodii;
            for(int j = 0; j < magazin[i].nr_melodii; j++)
            {
                strcpy(magazin[i].melodii[j], magazin[i + 1].melodii[j]);
            }
        }
        numar_cd--;
        cout<<"CD-urile care au ramas sunt: ";
        afisare_cd(magazin);
    }
}

int main()
{
    CD magazin[101];
    int choice;
    do
    {
        cout<<"--------------------------------------------\n";
        cout<<"MENIU\n";
        cout<<"1. Introduceti un CD nou;\n";
        cout<<"2. Afisati toate CD-urile, cu componenta acestora;\n";
        cout<<"3. Ordonare piese;\n";
        cout<<"4. Stergere CD;\n";
        cout<<"5. Iesire.\n\n";
        cout<<"--------------------------------------------\n";
        cout<<"Optiunea dumneavoastra este: ";
        cin>>choice;
        cout<<"-------------------------------------------\n";
        switch(choice)
        {
        case 1:
            introducere_informatii(magazin);
            break;
        case 2:
            if(numar_cd == 0)
                cout<<"Nu exista CD-uri introduse! Incercati sa adaugati!\n";
            else
                afisare_cd(magazin);
            break;
        case 3:
            cout<<"`````````````````````````````````\n";
            if(numar_cd == 0)
                cout<<"Nu exista CD-uri introduse! Incercati sa adaugati!\n";
            else
            {
                int nr_cd;
                cout<<"Introduceti CD-ul unde doriti sa ordonati crescator piesele: ";
                cin>>nr_cd;
                ordonare(magazin, nr_cd-1);
            }
            cout<<"`````````````````````````````````\n";
            break;
        case 4:
            cout<<"`````````````````````````````````\n";
            if(numar_cd == 0)
                cout<<"Nu exista CD-uri introduse! Incercati sa adaugati!\n";
            else
            {
                cout<<"Introduceti CD-ul pe care doriti sa-l stergeti: ";
                int nr_cd;
                cin>>nr_cd;
                stergere_cd(magazin,nr_cd-1);
            }
            cout<<"`````````````````````````````````\n";
            break;
        case 5:
            exit(0);
        default:
            cout<<" Alegeti una dintre optiunile mentionate!\n";
        }
    }
    while(choice != 5);



    return 0;
}
