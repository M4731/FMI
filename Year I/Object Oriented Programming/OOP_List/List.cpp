#include "List.h"



int v[100000001];

List::List(int x)
{
    size=1;
    Nod* t=new Nod(x,0);
    start =  end = t;
}

List::List(int x, int y)
{
    size=1;
    Nod* t=new Nod(y,0);
    start =  end = t;
    for(int i=1; i<x; i++){
        Nod* t = new Nod(x,0);
        end -> setNext(t);
        end =  t;
        size++;
    }
}

void List::insert(int x)
{
    size++;
    Nod* t = new Nod(x,0);
    end -> setNext(t);
    end =  t;
}

void List::insertAt(int x, int i)
{
    if (i>=size){
        insert(x);
        return;
    }
    if (i==0){
        Nod* t = new Nod(x,start);
        size++;
        start = t;
        return;
    }
    Nod* s = start;
    for( int j = 1; j<i; j++){
        s = s->getNext();
    }
    Nod* t =  new Nod(x,s->getNext());
    s->setNext(t);size++;
}

void List::afisare()
{
    Nod* s = start;
    while(s!=0){
        cout<<s->getInfo()<<" ";
        s=s->getNext();
    }
    cout<<endl;
}
int List::get(int i)
{
     if(i>=size || i< 0) return 2147483647;
    Nod* s = start;
    for( int j = 0; j<i; j++){
        s = s->getNext();
    }
    return s->getInfo();
}

void List::remove(int i)
{
   if (i==0){
        size--;
        start = start->getNext();
        return;
    }
    Nod* s = start;
    for( int j = 1; j<i; j++){
        s = s->getNext();
    }
    s->setNext(s->getNext()->getNext());size--;
}

int List::length()
{
    return size;
}

List::~List()
{
    Nod* s = start;
    Nod* t=s->getNext();
    while(s!=0){
        delete(s);
        s=t;
        t=s->getNext();
    }
}

List List::reverse()
{
    List l(start->getInfo());
    Nod* s = start->getNext();
    while(s!=0){
       // cout<<"1"<<" ";
        l.insertAt(s->getInfo(),0);
        s=s->getNext();
    }
    return l;
}

void List::removeFirst()
{
    remove(0);
}

void List::removeLast()
{
    remove(size-1);
}

bool List::hasDuplicates()
{
    Nod* s = start;
    while(s!=0){
        v[s->getInfo()]++;
        s=s->getNext();
    }
    int k=0;
    for(int q=0;q<=100000001;q++)
        if(v[q]>1)k=1;
    if (k==1)return true;
    else return false;
}

bool List::hasX(int x)
{
    Nod* s = start;
    while(s!=0){
        v[s->getInfo()]++;
        s=s->getNext();
    }
    int k=0;
    for(int q=0;q<=100000001;q++)
        if(v[x]>0)k=1;
    if (k==1)return true;
    else return false;
}

bool List::isEmpty()
{
    Nod* s = start;
    while(s!=0){
        v[s->getInfo()]++;
        s=s->getNext();
    }
    int k=0;
    for(int q=0;q<=100000001;q++)
        if(v[q]>0)k=1;
    if (k==0)return true;
    else return false;
}

void f(List * l,int x)
{
   l->afisare();
   l->insert(x);
   cout<<endl;
}
