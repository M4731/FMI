#include "fraction.h"

int cmmdc (int a, int b) {
    int r;

    while (b != 0) {
        r = a % b;
        a = b;
        b = r;
    }

    return a;
}

int cmmc (int a, int b) {
    return (a * b) / cmmdc(a, b);
}

void Fraction::simplify () {
    int c = cmmdc(numarator, numitor);
    if (c == 0) {
        return;
    }
    numarator /= c;
    numitor /= c;
}


Fraction::Fraction(int n, int m) : numarator(n), numitor(m) {
    simplify();
}

Fraction Fraction::operator+(const Fraction& f) const {
    int m = cmmc(numitor, f.numitor);
    int n = numarator * (m / numitor) + f.numarator * (m / f.numitor);

    Fraction result(n, m);

    return result;
}

Fraction Fraction::operator-(const Fraction& f) const {
    int m = cmmc(numitor, f.numitor);
    int n = numarator * (m / numitor) - f.numarator * (m / f.numitor);

    Fraction result(n, m);

    return result;
}

Fraction Fraction::operator*(const Fraction& f) const {
    int m = numitor * f.numitor;
    int n = numarator * f.numarator;

    Fraction result(n, m);

    return result;
}

Fraction Fraction::operator/ (const Fraction& f) const {
    Fraction aux (f.numitor, f.numarator);
    return *this * aux;
}

std::ostream& operator << (std::ostream& out, const Fraction& f) {
    out << f.numarator << "/" << f.numitor;
    return out;
}

std::istream& operator >> (std::istream& in, Fraction& f) {
    in >> f.numarator >> f.numitor;
    f.simplify();
    return in;
}

Fraction operator* (const int& i, const Fraction& f) {
    Fraction result (i * f.numarator, i * f.numitor);
    return result;
}

bool Fraction::operator==(const Fraction & f) const {
    // v2
    // float f1 = (float) numarator/ (float) numitor;
    // float f2 = (float) f.numarator/ (float) f.numitor;
    // if (f1 == f2)
    // v3
    // if (numitor * f.numarator === numarator * f.numitor)
    if (f.numitor == numitor && numarator == f.numarator) {
        return true;
    }
    return false;
}
