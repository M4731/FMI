#include "Nod.h"


int v[100000001];

void Nod::setInfo(int i)
{
    info = i;
}

int Nod::getInfo()
{
    return info;
}

void Nod::setNext(Nod* w)
{
    next=w;
}

Nod* Nod::getNext()
{
    return next;
}

Nod::Nod(int i, Nod* w)
{
    info = i;
    next = w;
}

Nod::Nod()
{
    info = 0;
    next = 0;
}

Nod::~Nod()
{
   cout<<"nod distrus"<<endl;
}

