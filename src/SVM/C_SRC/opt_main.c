#include "opt_main.h"

// Prototypes
double rd();
gsl_vector* natov(PyArrayObject* n_array, int* len);

// Main functions
PyObject* __get_w_width(PyArrayObject* elements, int rbf) {
    // unpack NumPy list and convert an array of vectors
    int len;
    gsl_vector* x = natov(elements, &len);

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

gsl_vector* natov(PyArrayObject* n_array, int* len) {
    PyObject* t_elements = (PyObject*)PyArray_DATA(n_array);
    printf("In C, %d\n", PyFloat_AsDouble(PyTuple_GetItem(t_elements, 0)));
}