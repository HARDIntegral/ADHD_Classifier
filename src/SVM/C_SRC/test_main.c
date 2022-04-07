#include "test_main.h"

// Prototypes
gsl_vector* unpack_w(PyObject* w);
double unpack_b(PyObject* b);

// Main functions
PyObject* __test_t(PyObject* elements, PyObject* w, PyObject* b) {
    gsl_vector* _w = unpack_w(w);
    double _b = unpack_b(b);
}

// Helper functions
gsl_vector* unpack_w(PyObject* w) {

}

double unpack_b(PyObject* b) {

}