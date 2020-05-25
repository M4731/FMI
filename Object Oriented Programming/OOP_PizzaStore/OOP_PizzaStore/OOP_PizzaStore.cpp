#include <iostream>
#include <vector>
#include <string>

class Pizza {
protected:
    unsigned diametru;
    bool blat;
    double pret;
    std::string pizzaId;

    unsigned nrFelii;
    static int nrComanda;

public:
    Pizza(unsigned, bool, double);
    unsigned getDiametru();
    void setDiametru(unsigned);
    bool getBlat();
    void setBlat(bool);
    double getPret();
    void setPret(double);
    std::string getPizzaId();

    virtual void feliere() = 0;
    virtual std::string getExtra() const = 0;

    friend std::ostream& operator<<(std::ostream& out, const Pizza& p)
    {
        out << "diametru: " << p.diametru << std::endl;
        if (p.blat)
            out << "blat pufos" << std::endl;
        else
            out << "blat subtire" << std::endl;
        out << "pret: " << p.pret << std::endl;
        out << p.getExtra() << std::endl;
        out << std::endl;
        return out;
    }
};
int Pizza::nrComanda = 0;
Pizza::Pizza(unsigned d, bool b, double p) :diametru(d), blat(b), pret(p)
{
    this->pizzaId = std::to_string(nrComanda);
    nrComanda++;
}
unsigned Pizza::getDiametru()
{
    return this->diametru;
}
void Pizza::setDiametru(unsigned d)
{
    this->diametru = d;
}
bool Pizza::getBlat()
{
    return this->blat;
}
void Pizza::setBlat(bool b)
{
    this->blat = b;
}
double Pizza::getPret()
{
    return this->pret;
}
void Pizza::setPret(double p)
{
    this->pret = p;
}
std::string Pizza::getPizzaId()
{
    return pizzaId;
}

class Diavola final :public Pizza
{
public:
    Diavola(unsigned, bool, double);
    void feliere() override;
    std::string getExtra() const override;
};
Diavola::Diavola(unsigned d, bool b, double p) :Pizza(d, b, p)
{
    this->pizzaId = "D" + this->pizzaId;
}
void Diavola::feliere()
{
    if (this->diametru > 20)
        this->nrFelii = 8;
    else
        this->nrFelii = 4;
}
std::string Diavola::getExtra() const
{
    return "<Pizza Diavola>";
}

class Nevada :virtual public Pizza
{
public:
    Nevada(unsigned, bool, double);
    void feliere() override;
    std::string getExtra() const  override;
};
Nevada::Nevada(unsigned d, bool b, double p) :Pizza(d, b, p)
{
    this->pizzaId = "N" + this->pizzaId;
}
void Nevada::feliere()
{
    if (this->diametru > 20)
        this->nrFelii = 10;
    else
        this->nrFelii = 5;
}
std::string Nevada::getExtra() const
{
    return "<Pizza Nevada>";
}

class Pineapple :virtual public Pizza
{
public:
    Pineapple(unsigned, bool, double);
    void feliere() override;
    std::string getExtra() const override;
};
Pineapple::Pineapple(unsigned d, bool b, double p) :Pizza(d, b, p)
{
    this->pizzaId = "P" + this->pizzaId;
}
void Pineapple::feliere()
{
    if (this->diametru > 20)
        this->nrFelii = 12;
    else
        this->nrFelii = 6;
}
std::string Pineapple::getExtra() const
{
    return "<Pizza Pineapple>";
}

class PC final :public Pineapple, public Nevada
{
public:
    PC(unsigned, bool, double);
    void feliere() override;
    std::string getExtra() const override;
};
PC::PC(unsigned d, bool b, double p) :Nevada(d, b, p), Pineapple(d, b, p), Pizza(d, b, p)
{
    this->pizzaId = "PC" + (this->pizzaId.substr(2));
}
void PC::feliere()
{
    if (this->diametru > 20)
        this->nrFelii = 14;
    else
        this->nrFelii = 7;
}
std::string PC::getExtra() const
{
    return "<Pizza Casei*maresmecherie>";
}

class App
{
    static App* instanta;
    std::vector<Pizza*> vectorDePizza;
    App() {};
public:
    static App* getApp();
    void insert(Pizza*);
    void pop(std::string);

    friend std::ostream& operator<<(std::ostream& out, const App& p)
    {
        for (auto i : p.vectorDePizza)
            out << *i;
        return out;
    }
};

App* App::instanta;

App* App::getApp()
{
    if (!instanta)
    {
        instanta = new App();
    }
    return instanta;
}
void App::insert(Pizza* p)
{
    vectorDePizza.push_back(p);
}
void App::pop(std::string s)
{
    for (auto i : vectorDePizza)
    {
        if (i->getPizzaId() == s)
        {
            unsigned j = 0;
            while (j < vectorDePizza.size() && i != vectorDePizza[j])
                j++;
            for (unsigned y = j; y < vectorDePizza.size() - 1; y++)
                vectorDePizza[j] = vectorDePizza[j + 1];
            vectorDePizza.pop_back();
        }
    }
}


int main()
{
    Nevada NEG(32, 0, 40);
    //std::cout<<NEGGER;
    App::getApp()->insert(&NEG);
    PC GER(32, 1, 45);
    //std::cout<<gay;
    App::getApp()->insert(&GER);
    //App::getApp()->pop(gay.getPizzaId());
    std::cout << *App::getApp();
    return 0;
}