#include <iostream>
#include "fraction.h"
#include "vector.h"
#include <cassert>
#include <exception>

using namespace std;

void fractionTests () {
    assert(Fraction(1, 2) == Fraction(3, 6));
    assert(Fraction(1,2) + Fraction(3, 2) == Fraction(4,2));
    assert(Fraction(1,2) + Fraction(1, 3) == Fraction(5,6));
}

void vectorTests () {
    Vector v;
    v.push(Fraction(1,3));
    v.push(Fraction(2,3));
    v.push(Fraction(3,4));

    assert(v[0] == Fraction(1,3));
    assert(v[1] == Fraction(2,3));
    assert(v[2] == Fraction(3,4));

    try {
        v[5];
        assert(false);
    } catch(...) {
        assert(true);
    }
}


int main () {

    fractionTests();
    vectorTests();

    cout << "Testele au trecut" << endl;

    return 0;
}
