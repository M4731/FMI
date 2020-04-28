#include<iostream>
#include "List.h"
#include "Nod.h"

using namespace std;

int v[100000001];

int main()
{
    List ll(1);
    ll.remove(0);
    if(ll.isEmpty()==true)cout<<"true empty"<<endl;
    else cout<<"false empty"<<endl;
    int oo;cin>>oo;
    List l(1,4);
    f(&l,213);
    if(l.hasDuplicates()==true)cout<<"true"<<endl;
    else cout<<"false"<<endl;
    l.afisare();
    f(&l,213);
    f(&l,213);
    f(&l,213);
    f(&l,213);
    cout<<l.get(2)<<endl;
    l.insert(1);
    l.afisare();
    cout<<endl;
    l.insertAt(214314124,0);
    l.insertAt(5,2);
    l.remove(2);
    cout<<l.get(7)<<" "<<l.length()<<endl;
    l.afisare();
    l.removeFirst();l.removeLast();
    l.afisare();
    if(l.isEmpty()==true)cout<<"true empty"<<endl;
    else cout<<"false empty"<<endl;
    if(l.hasX(oo)==true)cout<<"are "<<oo<<endl;
    else cout<<"n are"<<oo<<endl;
    if(l.hasDuplicates()==true)cout<<"true"<<endl;
    else cout<<"false"<<endl;
    l.reverse().afisare();cout<<endl;
//   Nod t(12,0);
//    cout << t.getInfo()<<" "<< t.getNext() << endl;
    return 0;
}
