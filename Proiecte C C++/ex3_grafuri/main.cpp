#include <bits/stdc++.h>
using namespace std;
ifstream fin("date.txt");  // fin("harta");

int n, A[10][10], v[10], k;

void citire()
{
    fin >> n;
    for (int i = 1; i <= n; i++)
    {
        for (int j = 1; j <= n; j++)
        {
            fin >> A[i][j];
        }
    }
}

void init()
{
    v[k] = 0;
}

int valid()
{
    int i;
    if (k > 1)
    {
        i = 1;
        while((v[k] != v[i]) && (i < k))
            i++;  // while((v[k] != v[i]) ||(v[k] == v[i] && A[v[i]][v[k]] == 0)) i++;
        if (i == k) return 1;  // return 1  pt harta
        return 0;
    }
    return 1;
}

int succesor()
{
    if (v[k] < 4)    // < 4 pt harta
    {
        v[k]++;
        return v[k];
    }
    return 0;
}

int solutie()
{
    return (k == n);  // return (k == n && A[v[n]][v[1]] pt circuit
}

void tipar()
{
    cout << endl;
    for (int i = 1; i <= k; i++)
    {
        cout << v[i] << " ";
    }
    // cout v[1] pt circuit
}
int main()
{
    int AS;
    citire();
    k = 1;   // se completează stiva începând cu primul nivel
    init();  // se iniţializează primul nivel al stivei
    while (k > 0)
    {
        do    // se caută succesor pe nivelul k atâta timp cât există succesor care
        {
            // nu este valid
            AS = succesor();
        }
        while (AS && !valid());
        if (AS)           // există succesor şi e valid
            if (solutie())  // dacă s-a completat stiva
                tipar();      // se tipăreşte soluţia
            else            // stiva nu s-a completat
            {
                k++;          // se trece pe nivelul următor
                init();       // se iniţializează noul nivel
            }
        else
            k--;
    }
    return 0;
}
