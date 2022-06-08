#include <fstream>
#include <iomanip>
#include <iostream>

using namespace std;
ifstream f("date.txt");
#define INF 1000

int nr_noduri, nod_pornire, mat_valori[50][50], s[50], lambda[50], d[50], prima_linie[50], a_doua_linie [50], m;

void citire_graf() {
  f >> nr_noduri >> nod_pornire;
  for (int i = 1; i <= nr_noduri; i++) {
    for (int j = 1; j <= nr_noduri; j++) {
      f >> mat_valori[i][j];
      if (!mat_valori[i][j] && i != j) mat_valori[i][j] = INF;
    }
  }
}

// S = X - { nod pornire }
// lambda[i] = valoarea arcului de la nodul de pornire la nodul i
void initializare() {
  for (int i = 1; i <= nr_noduri; i++) {
    lambda[i] = mat_valori[nod_pornire][i];
    s[i] = 1;
  }
  s[nod_pornire] = 0;
}

void afisare(int v[], int l) {
  for (int i = 1; i <= l; i++)
    if (v[i] == INF)
      cout << "  INF";
    else
      cout << setw(5) << v[i];
  cout << endl;
}

int nod_lambda_min() {
  int lmin = INF, nod_min = 0;
  for (int i = 1; i <= nr_noduri; i++) {
    if (s[i] && lambda[i] != INF && lambda[i] < lmin) {
      lmin = lambda[i];
      nod_min = i;
    }
  }
  return nod_min;
}

void atribuire_linie(){
    for(int i = 1; i<=nr_noduri;i++)
        prima_linie[i] = mat_valori[1][i];
}

void bellman() {
    atribuire_linie();
    int pasi = 1, continuare = 1;
    while(continuare){

         afisare(prima_linie, nr_noduri);
        continuare = 0;
        a_doua_linie[1] = 0;
        for(int i = 2; i <= nr_noduri; i++)
        {
            int val_min = INF;
            for(int j = 1; j <= nr_noduri; j++)
            {
                if(prima_linie[j] != INF && mat_valori[j][i] != INF && prima_linie[j]+ mat_valori[j][i] < val_min)
                {
                    val_min = prima_linie[j] + mat_valori[j][i];
                }
            }
            a_doua_linie[i] = val_min;
        }
        for(int i = 1; i <= nr_noduri; i++)
        {
            if(prima_linie[i] != a_doua_linie[i])
            {
                continuare = 1;
                break;
            }
        }
        if (continuare)
        {
            pasi++;
            for(int i = 1; i <= nr_noduri; i++)
            {
                prima_linie[i] = a_doua_linie[i];
            }
            if(pasi > m)
            {
                cout << "Exista circuit de valoare negativa";
                continuare = 0;
            }
        }


    }
     if(pasi <= m)
    {
        for(int i = 1; i <= nr_noduri; i++)
        {
            lambda[i] = prima_linie[i];
        }
        afisare(lambda, nr_noduri);
    }
}




void drum(int nod_final, int &ldrum) {
  if (lambda[nod_final] == INF) {
    ldrum = 0;
  } else {
    int k = 1;
    d[k] = nod_final;
    while (nod_final != nod_pornire) {
      for (int i = 1; i <= nr_noduri; i++) {
        if (mat_valori[i][nod_final] && mat_valori[i][nod_final] != INF &&
            lambda[i] + mat_valori[i][nod_final] == lambda[nod_final]) {
          k++;
          d[k] = i;
          nod_final = i;
          break;
        }
      }
    }
    ldrum = k;
  }
}

int main() {
  citire_graf();
  bellman();
  for (int nod = 1; nod <= nr_noduri; nod++) {
    int lungime;
    drum(nod, lungime);
    cout << "Drumul de la nodul " << nod_pornire << " la nodul " << nod << ": ";
    if (lungime == 0)
      cout << "Nu exista drum.\n";
    else
      afisare(d, lungime);
  }
  return 0;
}
