#include <fstream>
using namespace std;
ifstream fin("colorare.in");
ofstream fout("colorare.out");

int A[101][101];// A[i][j]==1 pt tari vecine, 0 altfel
int X[101],n;//X[i]=indicele culorii tarii i
char C[5][21];//culorile

void afisare()
{
    for(int i=1;i<=n;i++)
        fout<<i<<" "<<C[X[i]]<<"\n";//afisez tara si culoarea
    fout<<endl;
}

int valid(int k)
{//1 daca tara k poate fi colorata cu X[k], 0 altfel
    for(int i=1;i<k;i++)//pt tarile colorate deja
        if(A[i][k]==1 && X[i]==X[k]) return 0;//exita tara invecinata care are aceeasi culoare=>0
    return 1;
}

int alege(int k)
{//alege culoarea minima valida
    for(int i=1;i<=4;i++)//am 4 culori
        {
            X[k]=i;//plasez culoarea
            if(valid(k)) return i;//daca e buna o returnez
        }
    return 0;//daca nu putem colora
}

void colorare()
{//plaseaza in X[i] culoarea tarii i
    for(int i=1;i<=n;i++)
        X[i]=alege(i);//culoarea minima
}

int main()
{
    int t1,t2;
    fin>>n;//citesc nr de tari
    for(int i=1;i<=4;i++)
        fin>>C[i];//citesc culorile
    while(fin>>t1>>t2)//pereche de tari vecine
    {
        A[t1][t2]=1;//pun 1 in matrice
        A[t2][t1]=1;
    }
    colorare();
    afisare();
    return 0;
}
