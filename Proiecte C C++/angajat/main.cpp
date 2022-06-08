#include <iostream>
#include <string.h>
using namespace std;

class Angajat
{
private:
    string *nume;
    string prenume;
public:
    Angajat();
    Angajat(string *n, string pn)
    {
        nume = n;
        prenume = pn;
    }
    Angajat(Angajat& r);
    void display()
    {
        cout<<"Numele si prenumele angajatului sunt: "<<nume<<" "<<prenume;
    }
    ~Angajat()
    {
        cout<<"Obiect distrus";
    }
    friend class CuOra;
    friend class Permanent;

};

class CuOra:public Angajat
{
    double salariu;
    double ore_lucrate;
public:
    CuOra(string n, string pn, double sal, double ol)
    {
        nume = n;
        prenume = pn;
        prenume = pn;
        salariu = sal;
        ore_lucrate = ol;
    }
    void getSalariu()
    {
        cout<<"Salariul saptamanal este: "<<salariu * ore_lucrate;
    }
    void display()
    {
        display();
        cout<<"Salariul saptamanal este: "<<salariu * ore_lucrate;

    }
    friend class Angajat;
};

class Permanent:public Angajat
{
    float sectie;
    float salariu;
public:
    Permanent(string n, string pn, float sal, float sec)
    {
        nume = n;
        prenume = pn;
        salariu = sal;
        sectie = sec;
    }
    void getSalariu()
    {
        cout<<"Salariul lunar este: "<<salariu;
    }
    void display()
    {
        display();
        cout<<"Salariul si sectia in care lucreaza sunt: "<<salariu<< " " << sectie;
    }
    friend class Angajat;
};

int main()
{
    CuOra ora("Andrei", "Vint", 15, 40);
    Permanent per("Ionut", "Muresan", 2000, 1);
    ora.display();
    per.display();
    return 0;
}
