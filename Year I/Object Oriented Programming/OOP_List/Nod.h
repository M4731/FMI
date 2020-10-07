#ifndef NOD_H
#define NOD_H
#include "List.h"


class Nod
{
    int info;
    Nod * next;

public:
    void setInfo(int i);
    int getInfo();
    void setNext(Nod* w);
    Nod* getNext();
    Nod(int, Nod*);
    Nod();
    ~Nod();
};

#endif
