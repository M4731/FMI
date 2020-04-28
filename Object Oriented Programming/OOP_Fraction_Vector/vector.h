#ifndef vector_hpp
#define vector_hpp

#include "fraction.h"

class Vector {
    Fraction *array;
    unsigned size, max_size;
public:
    Vector(unsigned = 0);
    ~Vector();

    void push (const Fraction &);
    Fraction pop ();
    bool contains (const Fraction&) const;

    Fraction& operator[](const unsigned);
    friend std::istream& operator >> (std::istream&, Vector&);
//    Vector& operator= (const Vector&);
};

#endif
