#include "vector.h"
#include <exception>

Vector::Vector(unsigned s) : max_size(s), size(0) {
    if (s == 0) {
        array = nullptr;
    } else {
        array = new Fraction[max_size];
    }
}

Vector::~Vector () {
    if (array != nullptr) {
        delete [] array;
    }
    max_size = size = 0;
}


void Vector::push(const Fraction& f) {
    if (max_size == 0) {
        max_size = 5;
        array = new Fraction[max_size];
    } else if (size == max_size) {
        max_size += 5;
        Fraction *aux = new Fraction[max_size];
        for (unsigned i = 0; i < size; i++) {
            aux[i] = array[i];
        }
        delete [] array;
        array = aux;
    }
    array[size++] = f;
}

Fraction Vector::pop() {
    return array[--size];
}

bool Vector::contains(const Fraction& f) const {
    for (unsigned i = 0; i < size; i++) {
        if (array[i] == f) {
            return true;
        }
    }
    return false;
}

Fraction& Vector::operator[] (const unsigned i) {
    if (i >= size) {
        throw std::out_of_range("index gresit");
    }
    return array[i];
}

std::istream& operator >> (std::istream& in, Vector& v) {
    unsigned new_size;
    in >> new_size;

    if (new_size != v.max_size) {
        if (v.array != nullptr) {
            delete[] v.array;
        }
        v.array = new Fraction[new_size];
        v.size = v.max_size = new_size;
    }

    for (unsigned i = 0; i < v.size; i++) {
        in >> v[i];
    }

    return in;
}
