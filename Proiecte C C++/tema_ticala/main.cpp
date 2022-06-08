#include <iostream>
using namespace std;

class Scris
{
private:
    bool prezent;
    float nota;
public:
    Scris(bool p = false, int n = 1)
    {
        prezent = p;
        nota = n;

    }
    Scris(const Scris &st1)
    {
        prezent = st1.prezent;
        nota = st1.nota;
    }
    ~Scris(void)
    {
        cout<<"Obiectul a fost distrus!"<<endl;
    }

    void afisare()
    {
        if(prezent)
            cout<<"Studentul are prezenta completa!"<<endl;
        else
            cout<<"Studentul nu are prezenta completa!"<<endl;
        cout<<"Nota studentului este: "<<nota<<endl;
    }

    void restanta()
    {
        cout<<"introduceti 0 pentru RESTANTA si 1 pentru REUSIT\n";
        int ok;
        cin>>ok;
        if(ok)
            nota = 10;
        else nota = 4;
    }
    friend class Oral;
};

class Oral : public Scris
{
private:
    float nota1,medie;
public:
    Oral(float nota, float n1, float m1)
    {
        n1 =  2;
        m1 = (nota+n1)/2;
        nota1 = n1;
        medie = m1;
    }
    Oral(const Oral &o1)
    {
        nota1 = o1.nota1;
        medie = o1.medie;
    }
    ~Oral(void)
    {
        cout<<"DD!"<<endl;
    }
    void afisare(){
        cout<<"Nota1 este: "<<nota1<<endl;
        cout<<"Media celor doua note este: "<<medie<<endl;
    }
    bool status_student(){
        if(medie < 5)
            return false;
        return true;
    }

} ;

int main()
{
    bool p;
    int n;
    cout<<"Introduceti 1 pentru prezenta completa sau 0 pentru prezenta incompleta: ";
    cin>>p;
    cout<<"Introduceti nota studentului: ";
    cin>>n;
    Scris s1(p, n);
    s1.afisare();
    s1.restanta();
    s1.afisare();
    Scris s2=s1;
    s2.afisare();
    Oral or1(n, 2, 0);
    or1.afisare();


    return 0;
}
