/*
grupa 143
Mindruleanu Matei Daniel
laborant Florin Bilbie
Visual Studio
*/

#include <iostream>
#include <string>
#include <vector>

using namespace std;

class Masca
{
protected:
    bool loggo;
public:
    virtual double getPrice() const =0;
    bool getLoggo();
    void setLoggo(bool);
};
bool Masca::getLoggo()
{
    return this->loggo;
}
void Masca::setLoggo(bool l)
{
    this->loggo = l;
}

class MascaChirurgicala final :public Masca
{
    string protectie;
    string culoare;
    unsigned nrPliuri;
public:
    MascaChirurgicala(string, string, unsigned);
    MascaChirurgicala() = default;
    double getPrice() const override;
    string getProtectie();
    void setProtectie(string);
    string getCuloare();
    void setCuloare(string);
    unsigned getNrPliuri();
    void setNrPliuri(unsigned);

    friend std::ostream& operator<<(std::ostream& out, const MascaChirurgicala& m)
    {
        out << "tip de protectie: " << m.protectie << endl;
        out << "culoare: " << m.culoare << endl;
        out << "nr pliuri: " << m.nrPliuri << endl;
        out << "pret: " << m.getPrice() << std::endl;
        out << std::endl;
        return out;
    }
    friend std::istream& operator>>(std::istream& in, MascaChirurgicala& m)
    {
        in >> m.protectie >> m.culoare >> m.nrPliuri;
        return in;
    }
};
MascaChirurgicala::MascaChirurgicala(string p, string c, unsigned n) :protectie(p), culoare(c), nrPliuri(n)
{
}
double MascaChirurgicala::getPrice() const
{
    double m = 0;
    if (protectie == "ffp1")
        m = 5;
    else if (protectie == "ffp2")
        m = 10;
    else
        m = 15;
    if (loggo)
        m = 1.5 * m;
    return m;
}
string MascaChirurgicala::getProtectie()
{
    return this->protectie;
}
void MascaChirurgicala::setProtectie(string p)
{
    this->protectie = p;
}
string MascaChirurgicala::getCuloare()
{
    return this->culoare;
}
void MascaChirurgicala::setCuloare(string c)
{
    this->culoare = c;
}
unsigned MascaChirurgicala::getNrPliuri()
{
    return this->nrPliuri;
}
void MascaChirurgicala::setNrPliuri(unsigned n)
{
    this->nrPliuri = n;
}

class MascaPolicarbonat final :public Masca
{
    string protectie = "ffp0";
    string prindere;
public:
    MascaPolicarbonat() = default;
    MascaPolicarbonat(string);
    double getPrice() const override;
    string getPrindere();
    void setPrindere(string);

    friend std::ostream& operator<<(std::ostream& out, const MascaPolicarbonat& m)
    {
        out << "tip de protectie: " << m.protectie << endl;
        out << "tip prindere: " << m.prindere << endl;
        out << "pret: " << m.getPrice() <<" lei" << std::endl;
        out << std::endl;
        return out;
    }
    friend std::istream& operator>>(std::istream& in, MascaPolicarbonat& m)
    {
        in >> m.prindere;
        return in;
    }
};
MascaPolicarbonat::MascaPolicarbonat(string p):prindere(p)
{
}
double MascaPolicarbonat::getPrice() const
{
    double m = 20;
    if (loggo)
        m = 1.5 * m;
    return m;
}
void MascaPolicarbonat::setPrindere(string p)
{
    this->prindere = p;
}
string MascaPolicarbonat::getPrindere()
{
    return this->prindere;
}

class Dezinfectant
{
protected:
    long int nrSpecii;
    vector<string> ingrediente;
    vector<string> suprafete;
public:
    Dezinfectant(long int, vector<string>, vector<string>);
    virtual double getEficienta() const = 0; 
    double getPrice() const;

    friend std::ostream& operator<<(std::ostream& out, const Dezinfectant& d)
    {
        out << "nr. specii ucise: " << d.nrSpecii << endl;
        out << "ingrediente: ";
        out << "eficienta: " << d.getEficienta() <<"%";
        out << "pret: " << d.getPrice();
        out << std::endl;
        return out;
    }
};
Dezinfectant::Dezinfectant(long int n, vector<string> i, vector<string> s) :nrSpecii(n), ingrediente(i), suprafete(s)
{
}
double Dezinfectant::getPrice() const
{
    double m = 0;
    if (getEficienta() == 100)
        return(100);//pretul pt dezinfectantul total care nu era scris in cerinta
    else if (getEficienta() < 99.99 && getEficienta() > 99)
        return(50);
    else if (getEficienta() < 99 && getEficienta() > 97.5)
        return(40);
    else if (getEficienta() < 97.5 && getEficienta() > 95)
        return(30);
    else if (getEficienta() < 95 && getEficienta() > 90)
        return(20);
    return(10);
}

class DezinfectantBacterii : virtual public Dezinfectant
{
public:
    DezinfectantBacterii(long int n, vector<string> i, vector<string> s):Dezinfectant(n, i, s)
    {}
    DezinfectantBacterii() = default;
    double getEficienta() const override;
};
double DezinfectantBacterii::getEficienta() const
{
    return nrSpecii / 1000000000;
}

class DezinfectantVirusuri : virtual public Dezinfectant
{
public:
    DezinfectantVirusuri(long int n, vector<string> i, vector<string> s) :Dezinfectant(n, i, s)
    {}
    DezinfectantVirusuri() = default;
    double getEficienta() const override;
};
double DezinfectantVirusuri::getEficienta() const
{
    return nrSpecii / 100000000;
}

class DezinfectantFungi : virtual public Dezinfectant
{
public:
    DezinfectantFungi(long int n, vector<string> i, vector<string> s) :Dezinfectant(n, i, s)
    {}
    DezinfectantFungi() = default;
    double getEficienta() const override;
};
double DezinfectantFungi::getEficienta() const
{
    return nrSpecii / (1.5 * 1000000);
}

class DezinfectantTotal : public DezinfectantBacterii, public DezinfectantVirusuri, public DezinfectantFungi
{
    double getEficienta() const override;
};
double DezinfectantTotal::getEficienta() const
{
    return 100;//nu scria in cerinta asa ca am pus 100 si am crescut pretul :)
}

class Achizitie
{
    unsigned total=0;
    unsigned int zi, luna, an;
    string nume;
    vector<Masca*> masti;
    vector<Dezinfectant*> dezinfectante;
public:
    Achizitie(unsigned, unsigned, unsigned, string);
    unsigned getLuna()
    {
        return luna;
    }
    unsigned getTotal()
    {
        return total;
    }

    friend void operator +=(Achizitie a, Masca &m)
    {
        a.masti.push_back(&m);
        a.total = a.total + m.getPrice();
    }
    friend void operator +=(Achizitie a, Dezinfectant &d)
    {
        a.dezinfectante.push_back(&d);
        a.total = a.total + d.getPrice();
    }
};
Achizitie::Achizitie(unsigned z, unsigned l, unsigned a, string n) :zi(z), luna(l), an(a), nume(n)
{
}

int main()
{
    
    MascaChirurgicala mc2("ffp2", "verde brotăcel", 55);
    //MascaChirurgicala mc1;
    DezinfectantBacterii d(100000000, vector<string>({ "sulfati","parfumuri" }), vector<string>({"lemn","sticla","ceramica"}) );
    //cin >> mc1;
    //cout << mc2 << mc1;
    vector <Dezinfectant*> stocDezinfectant;
    vector <Masca*> stocMasti;
    vector <Achizitie*> Achizitii;
    Achizitie* a1 = new Achizitie(26, 5, 2020, "Gucci");
    *a1 += mc2;
    *a1 += d;
    stocDezinfectant.push_back(&d);
    stocMasti.push_back(&mc2);
    Achizitii.push_back(a1);

    DezinfectantBacterii dtest(0, vector<string>({ "" }), vector<string>({ "" }));
    unsigned minprice = 10000;
    for (auto i : stocDezinfectant)
        if (i->getPrice() < minprice) 
            minprice = i->getPrice();
    cout << minprice << endl;

    unsigned luna=1;
    //cin >> luna;
    unsigned venitluna = 0;
    for (auto i : Achizitii)
        if (i->getLuna() == luna)
            venitluna = venitluna + i->getTotal();
    cout << venitluna << endl;

    unsigned venitmastimodel = 0;
    for (auto i : stocMasti)
        if (i->getLoggo())
            venitmastimodel = venitmastimodel + i->getPrice();
    cout << venitmastimodel;
    return 0;
}
