#ifndef _LIST_H_
#define _LIST_H_

#include <iostream>
#include "node.h"
#include <stdexcept>
using namespace std;

template <typename T>
class List
{
    Node<T> *start, *last;
    unsigned size;

    void cleanup ();
public:
    List ();
    List (const unsigned&, const T&);
    List (const List<T>&);
    ~List();
    void push (const T&);
    void pop (const T&);
    T operator[] (const unsigned&) const;
    List<T>& operator= (const List<T>&);

    template <typename U>
    friend ostream& operator<<(ostream&, const List<U>&);

    template <typename U>
    friend istream& operator>>(istream&, List<U>&);
};


template <typename T>
List<T>::List() : start(NULL), last(NULL), size(0) { }

template <typename T>
void List<T>::cleanup () {
    Node<T>* actual=start;
    Node<T>* past=start;
    while(past)
    {
        actual=actual->next;
        delete past;
        past=actual;
    }
    start = last = NULL;
    size = 0;
}

template <typename T>
List<T>::~List() {
    this->cleanup();
}

template <typename T>
void List<T>::push(const T& val)
{
    if (start == NULL)
    {
        start = new Node<T>(val);
        last = start;
    }
    else
    {
        Node<T>* p = new Node<T>(val);
        last->next = p;
        last = last->next;
    }
    size++;
}


template <typename T>
T List<T>::operator[] (const unsigned& i) const {
    if (i >= size) {
        throw out_of_range("Invlid index");
    }

    Node<T> *p = start;
    unsigned j = 0;

    while (p) {
        if (i == j) {
            return p->info;
        }
        j++;
        p = p->next;
    }
}

template<typename T>
List<T>::List (const unsigned& s, const T& x) : List() {
    for (int i = 0; i < s; i++) {
        this->push(x);
    }
}

template<typename T>
List<T>::List (const List<T>& l) : List() {
    if (l.size == 0) {
        return;
    }
    for (int i = 0; i < l.size; i++) {
        this->push(l[i]);
    }
}

template <typename T>
List<T>& List<T>::operator= (const List<T>& l) {
    if (&l == this) {
        return *this;
    }
    this->cleanup();

    if (l.size == 0) {
        return *this;
    }

    for (int i = 0; i < l.size; i++) {
        this->push(l[i]);
    }
}

template <typename T>
void List<T>::pop(const T& x) {
    Node<T> *p = start, *q = NULL;

    while (p) {
        if (p->info == x) {
            if (q) {
                q->next = p->next;
            } else {
                start = start->next;
            }
            if (p->next == NULL) {
                last = q;
                last->next = NULL;
            }
            delete p;
            size--;
            return;
        }
        q = p;
        p = p->next;
    }
}

template <typename U>
ostream& operator<<(ostream& out, const List<U>& l) {
    Node<U> *p;

    while (p) {
        out << p->info << " ";
    }

    return out;
}

template <typename U>
istream& operator>>(istream& in, List<U>& l) {
    unsigned s;
    in >> s;
    l.cleanup();

    for (int i = 0; i < s; i++) {
        U x;
        in >> x;
        l.push(x);
    }

    return in;
}




#endif // _LIST_H_
