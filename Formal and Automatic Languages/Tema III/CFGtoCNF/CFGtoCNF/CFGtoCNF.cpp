#include <iostream>
#include <map>
#include <set>
#include <queue>
using namespace std;

int main()
{
    auto CFG = map<string, set<string>>();
    auto CFGNodes = set<string>();
    CFGNodes.insert("S");
    CFGNodes.insert("A");
    CFGNodes.insert("B");
    CFGNodes.insert("C");
    CFGNodes.insert("D");
    CFGNodes.insert("F");
    CFG["S"].insert("aAB");
    CFG["S"].insert("BC");
    CFG["S"].insert("");
    CFG["S"].insert("B");
    CFG["A"].insert("AaB");
    CFG["A"].insert("DB");
    CFG["B"].insert("b");
    CFG["B"].insert("c");
    CFG["C"].insert("");
    CFG["C"].insert("ab");
    CFG["D"].insert("");
    CFG["F"].insert("a");

    for (auto i : CFGNodes)
    {
        CFG[i].erase("");
    }
    auto CNFNodes = set<string>();
    CNFNodes.insert("S");
    auto q = queue<string>();
    q.push("S");
    while (q.size() != 0)
    {
        auto actual = q.front();
        q.pop();
        for (auto prod : CFG[actual])
            for (auto caracter : prod)
                if (caracter >= 'A' && caracter <= 'Z' && CNFNodes.find(string({ caracter })) == CNFNodes.end())
                {
                    CNFNodes.insert(string({ caracter }));
                    q.push(string({ caracter }));
                }
    }

    for (auto i : CFG)
    {
        if (CFG[i.first].size() == 0)
        {
            CFG.erase(i.first);
            CNFNodes.erase(i.first);
        }
        else if (CNFNodes.find(i.first) == CNFNodes.end())
            CFG.erase(i.first);
    }

    bool ok = true;
    while (ok)
    {
        ok = false;
        for (auto i : set<string>(CNFNodes))
        {
            for (auto prod : set<string>(CFG[i]))
            {
                if (prod.size() == 1 && prod[0] <= 'Z' && prod[0] >= 'A')
                {
                    ok = true;
                    CFG[i].erase(prod);
                    for (auto prod2 : CFG[prod])
                    {
                        CFG[i].insert(prod2);
                    }
                }
                else
                {
                    string s = "";
                    for (auto j : prod)
                        if (j >= 'A' && j <= 'Z')
                        {
                            if (CNFNodes.find(string({ j })) != CNFNodes.end())
                                s = s + string({ j });
                            else ok = true;
                        }
                        else s = s + string({ j });
                    CFG[i].erase(prod);
                    CFG[i].insert(s);
                }
            }
        }
    }

    //buguri aici probabil :)
    for (auto i : CFG)
    {
        if (CFG[i.first].size() == 0)
            CFG.erase(i.first);
        else if (CNFNodes.find(i.first) == CNFNodes.end())
            CFG.erase(i.first);
    }

    auto t = map<string, string>();
    auto count = 0;

    for (auto i : map<string, set<string>>(CFG))
        for (auto b : set<string>(i.second))
        {
            if (b.size() < 2)
                continue;
            string s = "";
            for (auto caracter : b)
            {
                if (caracter <= 'z' && caracter >= 'a')
                {
                    if (t.find(string({ caracter })) == t.end())
                    {
                        t[string({ caracter })] = "X" + to_string(count);
                        CNFNodes.insert("X" + to_string(count));
                        CFG["X" + to_string(count)].insert(string({ caracter }));
                        count++;
                    }
                    s += t[string({ caracter })];
                }
                else
                    s += caracter;
            }
            CFG[i.first].erase(b);
            CFG[i.first].insert(s);
        }

    count = 0;

    for (auto i : map<string, set<string>>(CFG))
        for (auto b : set<string>(i.second))
        {
            auto s = b;
            int c = 0;
            for (int j = 0; j < b.size(); j++)
                if (b[j] <= 'Z' && b[j] >= 'A')
                    c++;
            while (c > 2)
            {

                bool cm = false;
                for (int j = 1; j < b.size(); j++)
                    if (b[j] <= 'Z' && b[j] >= 'A')
                    {
                        if (cm)
                        {
                            CFG["Y" + to_string(count)].insert(s.substr(0, j));
                            s = "Y" + to_string(count) + s.substr(j);
                            CNFNodes.insert("Y" + to_string(count));
                            count++;
                        }
                        else
                        {
                            cm = true;
                        }
                    }
                c--;
            }
            CFG[i.first].erase(b);
            CFG[i.first].insert(s);
        }

    for (auto node : CNFNodes)
        cout << node << endl;

    cout << endl;

    for (auto i : CFG)
    {
        cout << i.first + ":";
        for (auto j : CFG[i.first])
            cout << " " + j + " ";
        cout << endl;
    }
}