#include <iostream>
#include <fstream>
using namespace std;

int nr_noduri, nr_muchii, mat_adiacenta[10][10];

void citire_ma() {
    ifstream fin("mat_adiacenta.in.txt");
    fin >> nr_noduri;
    fin >> nr_muchii;

    for(int i = 1; i <= nr_noduri; i++) {
        for(int j = 1; j <= nr_noduri; j++)
            fin >> mat_adiacenta[i][j];
    }
    fin.close();
}// functie pentru citirea matricii de adiacenta

int grad(int linie[10], int nr_nods) {
    int grad_nod = 0;
    for(int i = 1; i <= nr_nods; i++) {
        grad_nod += linie[i];
    }
    return grad_nod;
}//functie pentru gasirea gradului unui nod

void afisare_matrice(int mat[10][10], int n, int m) {
    cout<<"Matricea de adiacenta este:\n";
    for(int i = 1; i <= n; i++) {
        for(int j = 1; j <=m; j++) {
            cout<<mat[i][j]<<" ";
        }
        cout<<"\n";
    }
}//functie pentru afisarea matricii

int main()
{
    citire_ma();//citim matricea
    afisare_matrice(mat_adiacenta, nr_noduri, nr_noduri);//afisam matricea
cout<<"\n----------------------------------------------------";
    cout<<"\n\na) Gradele tuturor varfurilor sunt:";
    for(int i = 1; i <= nr_noduri; i++) {
       cout<<"\ng("<<i<<") = "<<grad(mat_adiacenta[i], nr_noduri);//afisam gradele nodurilor
    }
cout<<"\n----------------------------------------------------";
    cout<<"\n\nb) Varfurile cu grad par sunt:";
    for(int i = 1; i <= nr_noduri; i++) {
        if(grad(mat_adiacenta[i], nr_noduri) % 2 == 0)//afisam doar nodurile cu grad par
            cout<<"\ng("<<i<<") = "<<grad(mat_adiacenta[i], nr_noduri)<<" ==> varful "<<i;
    }
cout<<"\n----------------------------------------------------";
    cout<<"\n\nc) Varfurile izolate sunt:";
    for(int i = 1; i <= nr_noduri; i++) {
        if(grad(mat_adiacenta[i], nr_noduri) == 0)//afisam nodurile izolate ( nu formeaza arce, au gradul 0)
            cout<<"\ng("<<i<<") = "<<grad(mat_adiacenta[i], nr_noduri)<<" ==> varful "<<i;
    }
cout<<"\n----------------------------------------------------";
    cout<<"\n\nd) Varfurile terminale sunt:";
    for(int i = 1; i <= nr_noduri; i++) {
        if(grad(mat_adiacenta[i], nr_noduri) == 1)//afisam nodurile terminale (au doar un arc)
            cout<<"\ng("<<i<<") = "<<grad(mat_adiacenta[i], nr_noduri)<<" ==> varful "<<i;
    }
cout<<"\n----------------------------------------------------";
    int ok = 0;
    cout<<"\n\ne) Verifica daca graful are varfuri izolate:";
    for(int i = 1; i <= nr_noduri && ok == 0; i++) {
        ok = 0;
        if(grad(mat_adiacenta[i], nr_noduri) == 0)//verificam daca in graf avem vf izolate
            ok = 1;
    }
    if( ok == 1)
        cout<<"\nGraful are varfuri izolate.";
    else
        cout<<"\nGraful nu are varfuri izolate.";
cout<<"\n----------------------------------------------------";
    ok = 0;
    cout<<"\n\nf) Verifica daca graful are varfuri terminale:";
    for(int i = 1; i <= nr_noduri && ok == 0; i++) {
        ok = 0;
        if(grad(mat_adiacenta[i], nr_noduri) == 1)//verificam daca in graf avem vf terminale
            ok = 1;
    }
    if( ok == 1)
        cout<<"\nGraful are varfuri terminale.";
    else
        cout<<"\nGraful nu are varfuri terminale.";
cout<<"\n----------------------------------------------------";
    ok = 0;
    cout<<"\n\ng) Verifica daca graful are varfuri interioare:";
    for(int i = 1; i <= nr_noduri && ok == 0; i++) {
        ok = 0;
        if(grad(mat_adiacenta[i], nr_noduri) != 1 && grad(mat_adiacenta[i], nr_noduri) != 0)//verificam daca in graf avem vf interioare
            ok = 1;
    }
    if( ok == 1)
        cout<<"\nGraful are varfuri interioare.";
    else
        cout<<"\nGraful nu are varfuri interioare.";
cout<<"\n----------------------------------------------------";
    ok = 0;
    cout<<"\n\nh) Verifica daca graful are toate varfurile izolate:";//verificam daca toate nodurile sunt izolate
    for(int i = 1; i <= nr_noduri; i++) {
        if(grad(mat_adiacenta[i], nr_noduri) == 0)
            ok++;
    }
    if( ok == nr_noduri)
        cout<<"\nGraful are toate varfurile izolate.";
    else
        cout<<"\nGraful nu are toate varfurile izolate.";
cout<<"\n----------------------------------------------------";
    ok = 0;
    cout<<"\n\ni) Verifica daca graful are toate varfurile interioare:";
    for(int i = 1; i <= nr_noduri; i++) {
        if(grad(mat_adiacenta[i], nr_noduri) != 1 && grad(mat_adiacenta[i], nr_noduri) != 0)//verificam daca toate nodurile sunt interioare
            ok++;
    }
    if( ok == nr_noduri)
        cout<<"\nGraful are toate varfurile interioare.";
    else
        cout<<"\nGraful nu are toate varfurile interioare.";
cout<<"\n----------------------------------------------------";
    int vf;ok=1;
    while(ok) {
        cout<<"\nj) Nodurile sunt: ";for(int i=1;i<=nr_noduri;i++)cout<<i<<" " ;
        cout<<"\nIntroduceti varful pentru care doriti sa-i gasiti gradul: ";cin>>vf;//afisam gradul pentru un nod dat
        if(vf > nr_noduri || vf <= 0) cout<<"\nS-a introdus un varf inexistent!";
        else { ok = 0;  cout<<"g("<<vf<<") = "<<grad(mat_adiacenta[vf], nr_noduri);}
    }
cout<<"\n----------------------------------------------------";
    ok=1;
    while(ok) {
        cout<<"\nk) Nodurile sunt: ";for(int i=1;i<=nr_noduri;i++)cout<<i<<" " ;
        cout<<"\nIntroduceti varful pentru care doriti sa-i gasiti vecinii: ";cin>>vf;//afisam vecini pentru un nod dat
        if(vf > nr_noduri || vf <= 0) cout<<"\nS-a introdus un varf inexistent!";
        else {
                ok = 0;
                cout<<"Vecini varfului "<<vf<<" sunt:";
                for(int i = 1; i <= nr_noduri; i++)
                    if(mat_adiacenta[vf][i] == 1)
                        cout<<"\nnodul "<<i;
        }
    }
cout<<"\n----------------------------------------------------";
    vf;ok=1;
    while(ok) {
        cout<<"\nl) Nodurile sunt: ";for(int i=1;i<=nr_noduri;i++)cout<<i<<" " ;
        cout<<"\nIntroduceti varful pentru care doriti sa-i gasiti tipul: ";cin>>vf;//afisam tipul pentru un nod dat
        if(vf > nr_noduri || vf <= 0) cout<<"\nS-a introdus un nod inexistent!";
        else {
                ok = 0;
                if(grad(mat_adiacenta[vf], nr_noduri) == 0)
                    cout<<"Varful " << vf << " este izolat.";
                else if(grad(mat_adiacenta[vf], nr_noduri) == 1)
                    cout<<"Varful " << vf << " este terminal.";
                else cout<<"Varful " << vf << " este interior.";
        }
    }
cout<<"\n----------------------------------------------------";
    ok = 0;
    cout<<"\nm) Varful si nodurile care au gradul cel mai mare: ";
    int grad_max = 0, nod_grad_max;
    for(int i = 1; i <= nr_noduri; i++)
        if(grad_max < grad(mat_adiacenta[i], nr_noduri))
            {grad_max = grad(mat_adiacenta[i], nr_noduri); nod_grad_max = i;}//gasim nodul cu gradul maxim, si afisam daca mai avem noduri cu grad maxim
    cout<<"\nVarful "<<nod_grad_max<<" are gradul: "<<grad_max<<"\n";
    for(int i = 1; i <= nr_noduri; i++)
        if(grad_max == grad(mat_adiacenta[i], nr_noduri) && nod_grad_max != i) {
            cout<<"nodul " << i << " cu gradul: " << grad_max<<"\n";
            ok=1;
        }
    if(!ok)
        cout<<"Avem un singur nod cu grad maxim!";


    return 0;
}
