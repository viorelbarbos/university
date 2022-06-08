#include <iostream>
#include <fstream
using namespace std;

int n, m, ma[20][20], mi[20][40], au[40], bu[40], als[40], bls[40], alp[40], blp[40];

void citire_ma(){
    ifstream fina("mat_a");
    fina >> n;
    for (int i = 1; i <= n; i++){
        for(int j = 1; j <= n; ++){
            fina>>ma[i][j];
        }
    }
}

void ma_to_mi(){
    int k = 0;
    for (int i = 1; i <= n; i++){
        for(int j = 1; j <= n; ++){
            if(ma[i][j]){ // coloana noua in matricea dde incidenta
                k++;
                for(int l = 1; l <= n; l++)
                    mi[l][k] = 0;
                mi[i][k] = 1;
                mi[j][k] = -1;
            }
        }
    m = k;
}

void afisare_mi(){
    cout<<"Matricea de incidenta:"<<endl;
    for (int i = 1; i <= n; i++){
        for(int j = 1; j <= m; ++){
                cout<<mi[i][j] << " ";
        }
        cout<<endl;
}

int meniu() {

    cout<<endl<<endl<<"MENIU"<<endl;
    cout<< "1. Conversii de la matricea de adiacenta"<<endl;
    cout<< "2. Conversii de la matricea de incidenta"<<endl;
    cout<< "3. Conversii de la lista arcelor"<<endl;
    cout<< "4. Conversii de la lista succesorilor"<<endl;
    cout<< "5. Conversii de la lista predecesorilor"<<endl;
    cout<< "6. Terminare"<<endl;
    cout<< "Introduceti optiunea (1 - 6)";
    int x;
    cin >> x;
    return x;
}

/*void ma_to_all(){
    citire_ma();
    afisare_mat();

    ma_to_mi();
    afisare_mat();

    ma_to_la();
    afisare_lista();

    ma_to_ls();
    afisare_lista();

    ma_to_lp();
    afisare_lista();


}*/

int main()
{   int opt;
    opt = meniu();
    while(opt != 6){
        switch(opt){
        case 1:
            cout<<"conversie a";
            //ma_to_all();
            break;
        case 2:
            cout<<"conversie b";
           // mi_to_all();
            break;
        case 3:
            cout<<"conversie u";
            //la_to_all();
            break;
        case 4:
            cout<<"conversie a";
            //ls_to_all();
            break;
        case 5:
            cout<<"conversie a";
            //lp_to_all();
            break;
        }
        opt = meniu();
    }
    return 0;
}
