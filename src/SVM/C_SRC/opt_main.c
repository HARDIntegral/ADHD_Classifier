#include "opt_main.h"

// Prototypes
double rd();
gsl_vector* ltov(PyObject* n_array, int* len);

// Main functions
PyObject* __get_w_b_width(PyObject* elements, int rbf) {
    // unpack list to be a set of vectors
    int len;
    gsl_vector* x = ltov(elements, &len);

    //  guess a w vector
    gsl_vector* w = gsl_vector_alloc(2);
    for (int i=0; i<2; i++)
        gsl_vector_set(w, i, rd());

    return PyList_New(0);   // just a dummy return value
}

// Helper functions
double rd() {
    time_t t;
    srand((unsigned int)time(&t));
    uint64_t r53 = ((uint64_t)(rand()) << 21) ^ (rand() >> 2);
    return (double)r53 / 9007199254740991.0; // 2^53 - 1
}

gsl_vector* ltov(PyObject* list, int* len) {
    gsl_vector* x = (gsl_vector*)malloc(sizeof(gsl_vector)* PyList_Size(list));

    return x;
}