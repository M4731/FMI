#ifndef fraction_hpp
#define fraction_hpp

#include <iostream>

class Fraction {
    int numitor, numarator; // n/m
    void simplify ();
public:
    Fraction (int n = 0, int = 1);
    Fraction operator+ (const Fraction&) const;
    Fraction operator- (const Fraction&) const;
    Fraction operator* (const Fraction&) const;
    Fraction operator/ (const Fraction&) const;
    bool operator== (const Fraction&) const;

    friend std::ostream& operator << (std::ostream&, const Fraction&);
    friend std::istream& operator >> (std::istream&, Fraction&);
    friend Fraction operator* (const int&, const Fraction&);
};

#endif
