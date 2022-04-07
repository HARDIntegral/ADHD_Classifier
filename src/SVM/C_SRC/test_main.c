#include "test_main.h"

// Prototypes
static gsl_vector* unwrap_u(PyObject* _u);
static long classify(gsl_vector* _u, gsl_vector* _w, double b);

static gsl_vector* unpack_w(PyObject* w);
static double unpack_b(PyObject* b);
static double dot_prod(gsl_vector* u, gsl_vector* v);

// Main functions
PyObject* __test_t(PyObject* elements, PyObject* w, PyObject* b) {
    PyObject* return_tup = PyTuple_New(2);
    gsl_vector* _w = unpack_w(w);
    double _b = unpack_b(b);
    PyObject* pred_values = PyList_New(PyList_Size(elements));
    PyObject* true_values = PyList_New(PyList_Size(elements));
    for (Py_ssize_t i=0; i<PyList_Size(elements); i++) {
        PyObject* curr_e = PyList_GetItem(elements, i);
        PyList_SetItem(pred_values, i, PyLong_FromLong(classify(unwrap_u(PyObject_GetAttrString(curr_e, "features")), _w, _b)));
        PyList_SetItem(true_values, i, _PyLong_AsInt(PyObject_GetAttrString(curr_e, "is_ADHD")) == 1 ? PyLong_FromLong(1) : PyLong_FromLong(0));
    }
    PyTuple_SetItem(return_tup, 0, pred_values);
    PyTuple_SetItem(return_tup, 1, true_values);
    return return_tup;
}

static gsl_vector* unwrap_u(PyObject* _u) {
    gsl_vector* u = gsl_vector_alloc((int)PyList_Size(_u));
    for (size_t i=0; i<u->size; i++)
        gsl_vector_set(u, i, PyFloat_AsDouble(PyList_GetItem(_u, i)));
    return u;
}

static long classify(gsl_vector* _u, gsl_vector* _w, double b) {
    gsl_vector* u = gsl_vector_alloc(_u->size);
    gsl_vector* w = gsl_vector_alloc(_w->size);
    gsl_vector_memcpy(u, _u);
    gsl_vector_memcpy(w, _w);
    long result = dot_prod(u, w) + b;
    printf("%ld\n", result);
    if (result>0) {return 1;} else {return 0;}
}

// Helper functions
static gsl_vector* unpack_w(PyObject* w) {
    gsl_vector* result = gsl_vector_alloc((int)PyList_Size(w));
    for (size_t i=0; i<result->size; i++)
        gsl_vector_set(result, i, PyFloat_AsDouble(PyList_GetItem(w, i)));
    return result;
}

static double unpack_b(PyObject* b) {
    return PyFloat_AsDouble(b);
}

static double dot_prod(gsl_vector* u, gsl_vector* v) {
    gsl_vector* tmp = gsl_vector_alloc(u->size);
    gsl_vector_set_all(tmp, 1);
    gsl_vector_mul(tmp, u);
    gsl_vector_mul(tmp, v);
    double result = 0;
    for (size_t i=0; i<tmp->size; i++)
        result += gsl_vector_get(tmp, i);
    return result;
}