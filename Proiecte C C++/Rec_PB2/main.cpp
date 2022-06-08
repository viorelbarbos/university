#include <iostream>
using namespace std;

void citire(int matrice[][101], int n, int m, int i, int j) {
    if(i<=n) {
        cin>>matrice[i][j];
        if(j<m)
            citire(matrice,n,m,i,j+1);
        else
            citire(matrice,n,m,i+1,1);
    }
}

void afisare(int matrice[][101], int n, int m, int i, int j) {
    if(i<=n) {
        cout<<matrice[i][j]<<" ";
        if(j<m)
            afisare(matrice,n,m,i,j+1);
        else {
            cout<<endl;
            afisare(matrice,n,m,i+1,1);
        }
    }
}

int main()
{
    int mat[101][101],n,m;
    cout<<"Introduceti numarul de linii: "; cin>>n;
    cout<<"Introduceti numarul de coloane: "; cin>>m;
    cout<<"\nIntroduceti elementele matricii:\n";
    citire(mat,n,m,1,1);
    cout<<"\nMatricea este:\n";
    afisare(mat,n,m,1,1);
    return 0;
}
