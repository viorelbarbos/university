#include <bits/stdc++.h>
using namespace std;
ifstream fin("date.in.txt");
int p = 0, n, a[100][100];
int conexa[100];
int nodnemarcat()
{
    int i = 1;
    while (conexa[i] != 0 && i <= n)
        i++;
    if (i<=n)
        return i;
    return 0;
}

int main()
{

    fin >> n;

    for (int i = 1; i < n; i++)
    {
        for (int j = i + 1; j <= n; j++)
        {
            fin >> a[i][j];
            a[j][i] = a[i][j];
        }
        a[i][i] = 0;
    }

    int existan = 1;
    while (existan)
    {
        existan = 0;
        int x = nodnemarcat();
        if (x != 0)
        {
            p++;
            cout << " x = " << x << " p = " << p << endl;
            conexa[x] = p;
            int exista = 1;
            while (exista)
            {
                exista = 0;
                for (int i = 1; i <= n; i++)
                    for (int j = 1; j <= n; j++)
                    {
                        if (a[i][j] && (conexa[i] == 0 && conexa[i] != 0 || conexa[i] != 0 && conexa[j] == 0))
                        {
                            int s = conexa[i] + conexa[j];
                            conexa[i] = s;
                            conexa[j] = s;
                            exista = 1;
                        }
                    }
            }
            existan = 1;
        }
    }
    cout << " p= " << p << endl;
    for (int i = 1; i <= n; i++)
    {
        cout << conexa[i] << " ";
    }
    return 0;
}
