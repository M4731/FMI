#include <iostream>
#include <map>
#include <string>
#include <set>
#include <fstream>

using namespace std;

/*
Am pus comentarii la tot ce am adaugat pentru a face transformarea.
Restul codului (care nu are comentarii) este copy-paste din tema I.
*/


class DFA
{
	set<int> Q, F;
	set<char> Sigma;
	int q0;
	map<pair<int, char>, int> delta;

public:
	DFA() { this->q0 = 0; }
	DFA(set<int> Q, set<char> Sigma, map<pair<int, char>, int> delta, int q0, set<int> F)
	{
		this->Q = Q;
		this->Sigma = Sigma;
		this->delta = delta;
		this->q0 = q0;
		this->F = F;
	}

	set<int> getQ() const { return this->Q; }
	set<int> getF() const { return this->F; }
	set<char> getSigma() const { return this->Sigma; }
	int getInitialState() const { return this->q0; }
	map<pair<int, char>, int> getDelta() const { return this->delta; }

	bool isFinalState(int);
	int deltaStar(int, string);

	friend ostream& operator<< (ostream&, const DFA&);                   //creem o metoda prieten noua pentru supraincarcarea operatorului de afisare
};

class NFA
{
	set<int> Q, F;
	set<char> Sigma;
	set<int> q0;
	map<pair<int, char>, set<int> > delta;

public:
	NFA() {  }
	NFA(set<int> Q, set<char> Sigma, map<pair<int, char>, set<int> > delta, set<int> q0, set<int> F)
	{
		this->Q = Q;
		this->Sigma = Sigma;
		this->delta = delta;
		this->q0 = q0;
		this->F = F;
	}

	set<int> getQ() const { return this->Q; }
	set<int> getF() const { return this->F; }
	set<char> getSigma() const { return this->Sigma; }
	set<int> getInitialState() const { return this->q0; }
	map<pair<int, char>, set<int> > getDelta() const { return this->delta; }

	friend istream& operator >> (istream&, NFA&);

	bool isFinalState(set<int>);
	set<int> deltaStar(set<int>, string);

	DFA toDFA();                                                         //creem metoda noua pentru transformare
};

bool NFA::isFinalState(set<int> q)
{
    for ( auto i:q )
	    if ( F.find(i) != F.end() ) return true;
    return false;
}

set<int> NFA::deltaStar(set<int> q, string w)
{
    set<int> qq;
    for ( auto i:q )
       for ( auto j:delta[{i,w[0]}] )
          qq.insert(j);
	if ( w.length() == 1 )
	{
		return qq;
	}

	return deltaStar(qq, w.substr(1, w.length() - 1));
}

bool DFA::isFinalState(int q)
{
	return F.find(q) != F.end();
}

int DFA::deltaStar(int q, string w)
{
	if (w.length() == 1)
	{
		return delta[{q, (char)w[0]}];
	}

	int new_q = delta[{q, (char)w[0]}];
	return deltaStar(new_q, w.substr(1, w.length() - 1));
}

istream& operator >> (istream& f, NFA& M)
{
	int noOfStates;
	f >> noOfStates;
	for (int i = 0; i < noOfStates; ++i)
	{
		M.Q.insert(i);
	}

	int noOfLetters;
	f >> noOfLetters;
	for (int i = 0; i < noOfLetters; ++i)
	{
		char ch;
		f >> ch;
		M.Sigma.insert(ch);
	}

	int noOfTransitions;
	f >> noOfTransitions;
	for (int i = 0; i < noOfTransitions; ++i)
	{
		int s, d;
		char ch;
		f >> s >> ch >> d;
		M.delta[{s, ch}].insert( d );
	}

	int a;
	f >> a;
	M.q0.insert(a);

	int noOfFinalStates;
	f >> noOfFinalStates;
	for (int i = 0; i < noOfFinalStates; ++i)
	{
		int q;
		f >> q;
		M.F.insert(q);
	}

	return f;
}


ostream& operator << (ostream& out, const DFA& D)
{
    out<<D.q0<<endl;                                                     //afisam DFA-ul cu chestii de poo :D
    for ( auto i:D.delta ){
        out<<i.first.first<<" "<<i.first.second<<" "<<i.second;
    out<<endl;
    }
    for ( auto i:D.F )
        out<<i<<" ";
    out<<endl;
}

DFA NFA::toDFA()
{
    auto alfabet = this -> Sigma;                                        //copiem alfabetul
    map < set<int>, int > x;                                             //creem un map
    map < int, set<int> > y;                                             //map invers
    set<int> newQ;                                                       //Q nou
    int q;
    for ( auto i:q0 ) q = i;                                             //q e nodul initial
    newQ.insert(q);                                                      //bag nodul initial in multimea noua de stari
    x[newQ] = q;
    y[q] = newQ;
    set<int> f;
    if( isFinalState(newQ) ) f.insert(q);                                //f e multumea noua de stari finale
    map<pair<int, char>, int> newDelta;                                  //delta nou
    for ( int i=q; i<q+newQ.size(); i++ ){                               //mergem prin toate starile noi
        for ( auto c:alfabet )                                           //fiecare litera din alfabet
        {
            auto v = this->deltaStar( y[i],string({c}) );                //starile multiple ale nodurilor reprezentate de nodul nou prin deltaStar cu litera respectiva
            if (v.size()>0 ){                                            //cat timp primim cel putin un nod
                if ( x.find(v)==x.end() ){                               //daca nu e deja in multimea existenta de noduri noi atunci il facem nod nou
                    x[v] = q+newQ.size();
                    y[q+newQ.size()] = v;
                    if ( isFinalState(v) )
                        f.insert(q+newQ.size());
                    newQ.insert(q+newQ.size());
                }
                newDelta[{i,c}] = x[v];                                   //inseram drumul in newDelta
            }
        }
    }

    DFA D(newQ, alfabet, newDelta, q, f);                                 //creem si returnam un DFA nou
    return  D;
}


int main()
{
	NFA M;
	ifstream fin("dfa.txt");
	fin >> M;
	fin.close();

	DFA D = M.toDFA();
    cout << D;

	return 0;
}
