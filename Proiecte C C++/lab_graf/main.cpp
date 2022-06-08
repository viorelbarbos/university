#include <iostream>
#include <fstream>
#include <iomanip>
using namespace std;
#define INF 1000
ifstream fin("data.in");
int n, mat_valori[50][50], t[50][50];

void citire_matrice()//functie de citirea a matricii de valori
{
    fin>>n;
    for(int i = 1; i<=n; i++)
        for(int j = 1; j<=n; j++)
        {
            fin>>mat_valori[i][j];
            if (mat_valori[i][j] == 1000)
                mat_valori[i][j] = INF;
        }
}

void afisare_matrice(int v[][50], int l)//functie pentru afisare a unei matrice
{
    for(int i = 1; i<=l; i++)
    {
        for(int j = 1; j<=l; j++)
        {
            if(v[i][j] == INF)
                cout<<"  INF";
            else

                cout<<setw(5)<<v[i][j];
        }
        cout<<endl;
    }
    cout<<endl;
}

void init_t()//functie de initializare a matricei t
{
    for(int i=1; i<=n; i++)
        for(int j=1; j<=n; j++)
        {
            if(mat_valori[i][j]<INF && i!=j)
                t[1][j] =1;
            else
                t[i][j] =0;
        }
}

void drumuri(int initial, int final)
{
    cout << "Drumul de la nodul " << initial << " la nodul " << final << ": ";
    int poz = final, ok = 1;
    while (poz != initial)
    {
        cout << poz << " ";
        poz = t[initial][poz];
    }
    if (ok) cout << initial << endl;
}

void fwh()
{
    for(int pas = 1; pas<=n; pas++)
    {
        for(int i = 1; i<=n; i++)
        {
            for(int j = 1; j<=n; j++)
            {
                if (mat_valori[i][pas] < INF && mat_valori[pas][j] < INF &&
                        mat_valori[i][pas] + mat_valori[pas][j] < mat_valori[i][j])
                {
                    //verificam daca avem drum intre nodul i la intermediar, si intermediar si j
                    // daca avem verificam daca suma celor doua drumuri este mai mica decat
                    //valoare din drumul direct, si daca ii schimbam acea valoare cu suma respectiva
                    mat_valori[i][j] = mat_valori[i][pas] + mat_valori[pas][j];
                    t[i][j] = pas;
                }
            }
        }
        afisare_matrice(mat_valori, n);

    }

}
int main()
{
    citire_matrice();
    afisare_matrice(mat_valori,n);
    init_t();
    afisare_matrice(t,n);
    fwh();
    for (int i = 1; i <= n; i++)
        for (int j = 1; j <= n; j++)
        {
            if (i != j)
            {
                if (mat_valori[i][j] == INF)
                    cout << "Nu exista drum de la " << i << " la " << j << endl;
                else
                {
                    cout << "Valoarea minima a drumurilor de la " << i << " la " << j
                         << " este ";
                    cout << mat_valori[i][j] << endl;
                    drumuri(i, j);
                    cout << endl;
                }
            }
        }
    return 0;
}
