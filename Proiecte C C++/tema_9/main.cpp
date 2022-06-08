#include <iostream>
#include <cmath>
using namespace std;

int calcul_latura(int X_A, int Y_A, int X_B, int Y_B)
{
    float distanta = sqrt(((X_A - X_B) * (X_A - X_B)) + ((Y_A - Y_B) * (Y_A - Y_B)));
    return distanta;

}

class trapez
{
protected:
    int coord1_x, coord1_y, coord2_x, coord2_y, coord3_x, coord3_y, coord4_x, coord4_y;
    float AB, BC, CD, DA;
public:
    trapez(int a_x, int a_y, int b_x, int b_y, int c_x, int c_y, int d_x, int d_y)
    {

        coord1_x = a_x;
        coord1_y = a_y;
        coord2_x = b_x;
        coord2_y = b_y;
        coord3_x = c_x;
        coord3_y = c_y;
        coord4_x = d_x;
        coord4_y = d_y;

        AB = calcul_latura(coord1_x, coord1_y, coord2_x, coord2_y);
        BC = calcul_latura(coord2_x, coord2_y, coord3_x, coord3_y);
        CD = calcul_latura(coord3_x, coord3_y, coord4_x, coord4_y);
        DA = calcul_latura(coord4_x, coord4_y, coord1_x, coord1_y);
    }

    bool validare()
    {
        if(coord1_y!= coord2_y || coord3_y != coord4_y)
        {
            cout<<"coordonatele nu sunt corecte!";
            return false;
        }
        return true;
    }

    void perimetru()
    {
        float suma = AB+BC+CD+DA;
        cout<<"\nPerimetrul trapezului este: "<<suma;

    }
    void arie()
    {
        float h=calcul_latura(coord1_x, coord1_y, coord1_x, coord4_y);
        float arie =((AB+CD) * h)/2;
        cout<<"\nAria trapezului este: "<<arie;
    }
    friend class paralelogram;
    friend class dreptunghi;
};

class paralelogram : public trapez
{
public:
    using trapez::trapez;
    bool validare1()
    {
        if(coord1_y == coord2_y && coord3_y  == coord4_y && AB == CD && BC == DA)
            return true;
        return false;

    }
    void perimetru1(){
        float s = AB + BC + CD + DA;
        cout<<"\nPerimetrul paralelogramului este: "<<s;
    }
    void arie1(){
        float h=calcul_latura(coord1_x, coord1_y, coord1_x, coord4_y);
        float arie = AB * h;
         cout<<"\nAria paralelogramului este: "<<arie;
    }
};

class dreptungi : public trapez {
public:
    using trapez::trapez;
    bool validare2()
    {
        if(coord1_x == coord4_x && coord2_x  == coord3_x && AB == CD && BC == DA)
            return true;
        return false;

    }
    void perimetru2(){
        int suma = AB + BC + CD + DA;
        cout<<"\nPerimetrul dreptunghiului este: "<<suma;

    }
    void arie2(){
        int arie = AB * BC;
        cout<<"\nAria dreptunghiului este: "<<arie;
    }

};

class patrat : public trapez {
public:
    using trapez::trapez;
    bool validare3()
    {
        if(AB == CD && AB == BC)
            return true;
        return false;

    }
    void perimetru3(){
        int suma = AB + BC + CD + DA;
        cout<<"\nPerimetrul patratului este: "<<suma;

    }
    void arie3(){
        int arie = AB * BC;
        cout<<"\nAria dreptunghiului este: "<<arie;
    }

};

int main()
{
    trapez trapez1(2, 6, 9, 6, 11, 2, 5, 2);
    trapez1.perimetru();
    trapez1.arie();

    paralelogram paralelogram1(3, 3, 6, 3, 2, 1, 5, 1);
    paralelogram1.perimetru1();
    paralelogram1.arie1();

    dreptungi dreptungi1(2, 2, 5, 2, 2, 0, 5, 0);
    dreptungi1.perimetru2();
    dreptungi1.arie2();

    patrat patrat1(4, 4, 7, 4, 1, 4, 1, 7);
    patrat1.perimetru3();
    patrat1.arie3();



    return 0;
}
