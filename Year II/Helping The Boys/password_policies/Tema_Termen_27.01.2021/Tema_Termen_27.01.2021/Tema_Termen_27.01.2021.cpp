#include <iostream>
#include <string>
#include <fstream>
#include <vector>
using namespace std;

ifstream f("date.in");


class Policy
{
protected:
    bool isChecked;
public:
    void virtual check(string const& s) = 0;
    bool getCheck() const
    {
        return isChecked;
    }
};


class LengthPolicy : public Policy
{
private:
    unsigned short minLength;
    unsigned short maxLength;

public:
    LengthPolicy(unsigned short minim)
    {
        minLength = minim;
        maxLength = 255;
    }
    LengthPolicy(unsigned short minim, unsigned short maxim)
    {
        minLength = minim;
        maxLength = maxim;
    }
    void check(string const& s)
    {
        if (s.size() >= minLength && s.size() <= maxLength)
        {
            this->isChecked = true;
        }
        else
        {
            this->isChecked = false;
        }
    }


};


class ClassPolicy : public Policy
{
private:
    unsigned short minClassCount;

public:
    ClassPolicy(unsigned short minim)
    {
        minClassCount = minim;
    }
    void check(string const& s)
    {
        unsigned a = 0;
        unsigned b = 0;
        unsigned c = 0;
        unsigned d = 0;
        unsigned count = 0;
        for (unsigned i = 0; i < s.size(); i++)
        {
            if (isdigit(s[i]))
            {
                a++; 
            }
            else if (isupper(s[i]))
            {
                b++;
            }
            else if (islower(s[i]))
            {
                c++;
            }
            else
            {
                d++;
            }
        }

        if (a) count++;
        if (b) count++;
        if (c) count++;
        if (d) count++;

        if (count >= minClassCount)
        {
            this->isChecked = true;
        }
        else
        {
            this->isChecked = false;
        }
    }

};


class IncludePolicy : public Policy
{
private:
    char characterType;

public:
    IncludePolicy(char caracter)
    {
        characterType = caracter;
    }
    void check(string const& s)
    {
        for (unsigned i = 0; i < s.size(); i++)
        {
            if (isdigit(s[i]) && isdigit(characterType))
            {
                this->isChecked = true;
                return;
            }
            else if (isupper(s[i]) && isupper(characterType))
            {
                this->isChecked = true;
                return;
            }
            else if (islower(s[i]) && islower(characterType))
            {
                this->isChecked = true;
                return;
            }
            else if (!isalnum(s[i]) && !isalnum(characterType))
            {
                this->isChecked = true;
                return;
            }

        }
        this->isChecked = false;
    }
};


class NotIncludePolicy : public Policy
{
private:
    char characterType;

public:
    NotIncludePolicy(char caracter)
    {
        characterType = caracter;
    }
    void check(string const& s)
    {
        for (unsigned i = 0; i < s.size(); i++)
        {
            if (isdigit(s[i]) && isdigit(characterType))
            {
                this->isChecked = false;
                return;
            }
            else if (isupper(s[i]) && isupper(characterType))
            {
                this->isChecked = false;
                return;
            }
            else if (islower(s[i]) && islower(characterType))
            {
                this->isChecked = false;
                return;
            }
            else if (!isalnum(s[i]) && !isalnum(characterType))
            {
                this->isChecked = false;
                return;
            }

        }
        this->isChecked = true;
    }
};


class RepetitionPolicy : public Policy
{
private:
    unsigned short maxCount;

public:
    RepetitionPolicy(unsigned short maxim)
    {
        maxCount = maxim;
    }
    void check(string const& s)
    {
        unsigned count = 0;
        unsigned local = 1;
        for (unsigned i = 1; i < s.size(); i++)
        {
            char car = s[i];
            if (s[i] == s[i - 1])
            {
                local++;
                if (local > count)
                {
                    count = local;
                }
            }
            else
            {
                local = 1;
            }
        }
        if (count > maxCount)
        {
            this->isChecked = false;
        }
        else
        {
            this->isChecked = true;
        }
    }
};


class ConsecutivePolicy : public Policy
{
private:
    unsigned short maxCount;

public:
    ConsecutivePolicy(unsigned short maxim)
    {
        maxCount = maxim;
    }
    void check(string const& s)
    {
        unsigned count = 0;
        unsigned local = 1;
        for (unsigned i = 1; i < s.size(); i++)
        {
            char car = s[i];
            /*cout << s[i] << " " << s[i - 1] << endl;*/
            if (s[i] == s[i - 1] + 1)
            {
                local++;
                /*cout << local<<endl;*/
                if (local > count)
                {
                    count = local;
                }
            }
            else
            {
                local = 1;
            }
        }
        /*cout << count << " " << maxCount << endl;*/
        if (count > maxCount)
        {
            this->isChecked = false;
        }
        else
        {
            this->isChecked = true;
        }
    }
};


string checkPassword(string parola, vector<Policy*> conditions)
{
    bool ok = true;
    for (auto i : conditions)
    {
        i->check(parola);
        ok = (ok && i->getCheck());
        /*cout << i->getCheck();*/
    }
    if (ok)
    {
        return "OK";
    }
    else
    {
        return "NOK";
    }
}


int main()
{
    vector<Policy*> policies;
    unsigned n;
    string a;
    bool amcititstring = false;
    f >> n;
    for (unsigned i = 0; i < n; i++)
    {
        if (!amcititstring)
        {
            f >> a;
        }
        else
        {
            amcititstring = false;
        }
        if (a == "length")
        {
            int b;
            f >> b;

            string c;
            f >> c;
            int in;

            try
            {
                in = stoi(c);
            }
            catch (exception E)
            {
                amcititstring = true;
                /*cout << "exceptie" << endl;*/
                a = c;
            }

            if (!amcititstring)
            {
                Policy* politica = new LengthPolicy(b, in);
                policies.push_back(politica);
            }
            else
            {
                Policy* politica = new LengthPolicy(b);
                policies.push_back(politica);
            }
        }
        else 
        {
            if (a == "class")
            {
                unsigned citire;
                f >> citire;
                Policy* politica = new ClassPolicy(citire);
                policies.push_back(politica);
            }
            else if (a == "include")
            {
                char citire;
                f >> citire;
                Policy* politica = new IncludePolicy(citire);
                policies.push_back(politica);
            }
            else if (a == "ninclude")
            {
                char citire;
                f >> citire;
                Policy* politica = new NotIncludePolicy(citire);
                policies.push_back(politica);
            }
            else if (a == "repetition")
            {
                unsigned citire;
                f >> citire;
                Policy* politica = new RepetitionPolicy(citire);
                policies.push_back(politica);
            }
            else if (a == "consecutive")
            {
                unsigned citire;
                f >> citire;
                Policy* politica = new ConsecutivePolicy(citire);
                policies.push_back(politica);
            }
        }
    }

    string cit;
    while (f>>cit)
    {
        cout << checkPassword(cit, policies) << endl;
    }
}
