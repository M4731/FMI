#include <iostream>
#include <map>
#include <string>
#include <set>
#include <fstream>
using namespace std;

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

	bool isFinalState(set<int>);
	set<int> deltaStar(set<int>, string);
};

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
	if ( w.length() == 1 )
	{
		return qq;
	}

	return deltaStar(qq, w.substr(1, w.length() - 1));
}

istream& operator >> (istream& f, LNFA& M)
{
	int noOfStates;
	f >> noOfStates;
	for (int i = 0; i < noOfStates; ++i)
	{
		int q;
		f >> q;
		M.Q.insert(q);
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

int main()
{
	LNFA M;

	ifstream fin("dfa.txt");
	fin >> M;
	fin.close();

	set<int> lastStates = M.deltaStar( M.getInitialState(), "ab");

	for( auto i:lastStates ) cout<<i<<" ";

	if (M.isFinalState(lastStates))
	{
		cout << "Cuvant acceptat";
	}
	else
	{
		cout << "Cuvant respins";
	}

	return 0;
}
