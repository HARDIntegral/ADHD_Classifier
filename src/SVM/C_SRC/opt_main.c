#include <stdlib.h>
#include <gsl_vector.h>
#include "opt_main.h"

// Prototypes
double rd();

// Main functions
PyObject* __get_w_width(PyArrayObject* elements, int rbf) {
    //  guess a w vector
    gsl_vector* w = gsl_vector_alloc(2);
    for (int i=0; i<2; i++)
        gsl_vector_set(w, i, rd());
    
    return PyTuple_Pack(2, 1.0, 1.0);   // just a dummy return value
}

// Helper functions
double rd() {
    time_t t;
    srand((unsigned int)time(&t));
    uint64_t r53 = ((uint64_t)(rand()) << 21) ^ (rand() >> 2);
    return (double)r53 / 9007199254740991.0; // 2^53 - 1
}