#include <iostream>
#include <map>
#include <string>
#include <set>
#include <fstream>

using namespace std;

/*
Am pus comentarii la tot ce am adaugat pentru a face transformarea.
Restul codului (care nu are comentarii) este copy-paste din tema I sau din prima problema de la tema II.
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

	friend ostream& operator<< (ostream&, const DFA&);
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

	DFA toDFA();
};

class LNFA
{
	set<int> Q, F;
	set<char> Sigma;
	set<int> q0;
	map<pair<int, char>, set<int> > delta;

public:
	LNFA() {  }
	LNFA(set<int> Q, set<char> Sigma, map<pair<int, char>, set<int> > delta, set<int> q0, set<int> F)
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

	friend istream& operator >> (istream&, LNFA&);

	set<int> lambdaStar(set<int>);

	bool isFinalState(set<int>);
	set<int> deltaStar(set<int>, string);

	DFA toDFA();                                                         //creem metoda noua pentru transformare din LNFA la NFA
};

set<int> LNFA::lambdaStar(set<int> q)
{
    set<int>qq;
    for ( auto i:q )
        qq.insert(i);
    for ( int i=0; i<Q.size(); ++i ){
        set<int> qqq = deltaStar(qq,"~");
        for ( auto j:qqq ) qq.insert(j);
    }

    return qq;
}

bool LNFA::isFinalState(set<int> q)
{
    for ( auto i:q )
	    if ( F.find(i) != F.end() ) return true;
    return false;
}

set<int> LNFA::deltaStar(set<int> q, string w)
{
    set<int> qq;
    for ( auto i:q )
       for ( auto j:delta[{i,w[0]}] )
          qq.insert(j);
	if (w.length() == 1 && w == "~")
	{
		return qq;
	}
	if (w.length() == 1)
    {
        return lambdaStar(qq);
    }

	return lambdaStar( deltaStar(qq, w.substr(1, w.length() - 1)) );
}

istream& operator >> (istream& f, LNFA& M)
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
    auto alfabet = this -> Sigma;
    map < set<int>, int > x;
    map < int, set<int> > y;
    set<int> newQ;
    int q;
    for ( auto i:q0 ) q = i;
    newQ.insert(q);
    x[newQ] = q;
    y[q] = newQ;
    set<int> f;
    if( isFinalState(newQ) ) f.insert(q);
    map<pair<int, char>, int> newDelta;
    for ( int i=q; i<q+newQ.size(); i++ ){
        for ( auto c:alfabet )
        {
            auto v = this->deltaStar( y[i],string({c}) );
            if (v.size()>0 ){
                if ( x.find(v)==x.end() ){
                    x[v] = q+newQ.size();
                    y[q+newQ.size()] = v;
                    if ( isFinalState(v) )
                        f.insert(q+newQ.size());
                    newQ.insert(q+newQ.size());
                }
                newDelta[{i,c}] = x[v];
            }
        }
    }

    DFA D(newQ, alfabet, newDelta, q, f);
    return  D;
}

DFA LNFA::toDFA()
{
    map<pair<int, char>, set<int> > newDelta;                                           //creem harta noua
    for ( char j:Sigma )                                                                //mergem prin toate literele
    {
        for ( auto i:Q ){                                                               //mergem prin toate starile
            set<int> aux;                                                               //setam un auxiliar
            aux.insert(i);
            set<int> lastStates = deltaStar( lambdaStar(aux), string({j}) );            //vedem unde duce nudul respectiv
            newDelta[{i,j}] = lastStates;                                               //setam delta-ul pentru nodul si caracterul respectiv
        }
    }
    NFA N( Q, Sigma, newDelta, lambdaStar(q0), F);
    return N.toDFA();                                                                   //transformam in DFA ajutandu-ne de subprogramul de la problema precedenta
}

int main()
{
	LNFA M;
	ifstream fin("nfa.txt");
	fin >> M;
	fin.close();

	DFA D = M.toDFA();
    cout << D;

	return 0;
}
