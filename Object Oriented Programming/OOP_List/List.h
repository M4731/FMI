#ifndef LIST_H
#define LIST_H

#include "Nod.h"
#include<iostream>

using namespace std;

class Nod;
class List
{
    Nod * start;
    Nod * end;
    unsigned int size;

public:
    List(int);
    List(int, int);
    void insert(int);
    void insertAt(int, int);
    void afisare();
    int get(int);
    void remove(int);
    int length();

    virtual ~List();

    List reverse();
    void removeFirst();
    void removeLast();
    bool hasDuplicates();
    bool hasX(int x);
    bool isEmpty();

    friend void f(List*, int);

};

#endif
