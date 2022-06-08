#include <iostream>
using namespace std;

class coada
{
    int numar_elemente, indice_element, vector_coada[40];
public:
    void initializare(int n, int indice, int vec[40]);
    void introducere_variabila();
    void scoatere_variabila();
    void afisare_vector();
};
void coada::initializare(int n, int indice, int vec[40])//functie pentru a initializa variabilele
{
    int i;
    cout<<"Introduceti numarul de elemente ale cozii: ";
    cin>>n;
    for(i = 1; i<=n; i++)
    {
        cout<<"Introduceti un element in coada: ";
        cin>>vec[i];
    }
    numar_elemente = n;
    indice_element = i;
    for(i = 1; i<=n; i++)
        vector_coada[i] = vec[i];

}

void coada::afisare_vector()//functie pentru a afisa coada
{
    for(int i = 1; i <= numar_elemente; i++)
        cout<<vector_coada[i]<< " ";
}

void coada::introducere_variabila()//functie pentru a introduce o variabila
{
    int var;
    cout<<"\nIntroduceti variabila dorita pentru a fi adaugata cozii: ";
    cin>>var;//citim variabila
    numar_elemente++;//crestem numarul de elemente ale cozii
    vector_coada[numar_elemente] = var;// o adaugam la final
    cout<<"\nElementele din coada sunt: ";
    afisare_vector();
    cout<<endl;
}

void coada::scoatere_variabila()
{
    if(numar_elemente!=0)// verificam daca avem elemente pe care le putem scoate
    {
        for(int i = 1; i <= numar_elemente; i++)
            vector_coada[i] = vector_coada[i+1];
        numar_elemente--;
        cout<<"\nElementele din coada sunt: ";
        afisare_vector();
        cout<<endl;
    }

    else//in caz contrar afisam un mesaj
        cout<<"Nu mai exista elemente in coada, incercati sa mai adaugati!\n";
}

int main()
{
    int a,b,v[40];
    coada c;
    c.initializare(a,b,v);
    int choice;
    do
    {
        cout<<"--------------------------------------------\n";
        cout<<"MENIU\n";
        cout<<"1. Introduceti un element in coada;\n";
        cout<<"2. Stergeti un element din coada;\n";
        cout<<"3. Afisare coada;\n";
        cout<<"4. Iesire.\n\n";
        cout<<"--------------------------------------------\n";
        cout<<"Elementele din coada sunt: ";
        c.afisare_vector();
        cout<<endl;
        cout<<"Optiunea dumneavoastra este: ";
        cin>>choice;
        cout<<"-------------------------------------------\n";
        switch(choice)
        {
        case 1:
            c.introducere_variabila();
            break;
        case 2:
            c.scoatere_variabila();
            break;
        case 3:
            cout<<"`````````````````````````````````\n";
            c.afisare_vector();
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
