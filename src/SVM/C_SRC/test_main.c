#include "test_main.h"

// Prototypes
static double classify(gsl_vector* _u, gsl_vector* alphas, double b, input_data_t* input);

static gsl_vector* unpack_alphas(PyObject* a);
static gsl_vector* unwrap_u(PyObject* _u);

// Main functions
PyObject* __test_t(PyObject* training, PyObject* testing, PyObject* alphas, double b, int rbf) {
    PyObject* return_tup = PyTuple_New(2);
    gsl_vector* _a = unpack_alphas(alphas);
    PyObject* pred_values = PyList_New(PyList_Size(testing));
    PyObject* true_values = PyList_New(PyList_Size(testing));
    input_data_t* input = process_input_data(training, rbf, 0);
    for (Py_ssize_t i=0; i<PyList_Size(testing); i++) {
        PyObject* curr_e = PyList_GetItem(testing, i);
        PyList_SetItem(
            pred_values, i, 
            PyFloat_FromDouble(classify(unwrap_u(PyObject_GetAttrString(curr_e, "features")), _a, b, input))
        );
        PyList_SetItem(
            true_values, i, 
            _PyLong_AsInt(PyObject_GetAttrString(curr_e, "is_ADHD")) == 1 ? PyLong_FromLong(1) : PyLong_FromLong(0)
        );
    }
    PyTuple_SetItem(return_tup, 0, pred_values);
    PyTuple_SetItem(return_tup, 1, true_values);
    return return_tup;
}

static double classify(gsl_vector* _u, gsl_vector* _a, double b, input_data_t* input) {
    double result = 0;
    if (input->use_rbf) {
        for (int i=0; i<input->x_size; i++)
            result += gsl_vector_get(_a, i) * input->y[i] * k_rbf(input->x[i], _u);
    } else {
        for (int i=0; i<input->x_size; i++)
            result += gsl_vector_get(_a, i) * input->y[i] * k_custom(input->x[i], _u);
    }
    return result + b;
}

// Helper functions
static gsl_vector* unpack_alphas(PyObject* a) {
    gsl_vector* result = gsl_vector_alloc((int)PyList_Size(a));
    for (size_t i=0; i<result->size; i++)
        gsl_vector_set(result, i, PyFloat_AsDouble(PyList_GetItem(a, i)));
    return result;
}

static gsl_vector* unwrap_u(PyObject* _u) {
    gsl_vector* u = gsl_vector_alloc((int)PyList_Size(_u));
    for (size_t i=0; i<u->size; i++)
        gsl_vector_set(u, i, PyFloat_AsDouble(PyList_GetItem(_u, i)));
    return u;
}