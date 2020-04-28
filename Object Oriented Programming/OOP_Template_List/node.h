#ifndef _NODE_H
#define _NODE_H

template <typename T> class List;

template <typename T>
class Node {
    T info;
    Node<T>* next;
public:
    Node (const T&, Node<T>* = NULL);
    friend class List<T>;
};


template<typename T>
Node<T>::Node (const T& x, Node<T>* n) : info(x), next(n) { }

#endif // _NODE_H
