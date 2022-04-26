#include "svm_main.h"

// Prototypes
typedef struct _w_b {
    gsl_vector* w;
    double b;
} w_b;

static w_b* compute_w_b(gsl_vector* alphas, input_data_t* input);
static PyObject* packup(opt_output* opt);

// Main functions
PyObject* __get_w_b(PyObject* elements, int k_type , double C) {
    input_data_t* input = process_input_data(elements, k_type, C);
    opt_output* opt = compute_alphas(input, 1e-1, 3);
    return packup(opt);
}

input_data_t* process_input_data(PyObject* list, int k_type, double C) {
    Py_ssize_t list_len = PyList_Size(list);
    input_data_t* input = (input_data_t*)malloc(sizeof(input_data_t));
    input->x = (gsl_vector**)malloc(sizeof(gsl_vector)*list_len);
    input->y = (int*)malloc(sizeof(int)*list_len);
    for (Py_ssize_t i=0; i<list_len; i++) {
        PyObject* data_list = PyObject_GetAttrString(PyList_GetItem(list, i), "features");
        input->x[i] = gsl_vector_alloc((int)PyList_Size(data_list));
        for (Py_ssize_t j=0; j<PyList_Size(data_list); j++)
            gsl_vector_set(input->x[i], j, PyFloat_AsDouble(PyList_GetItem(data_list, j)));
        PyObject* is_adhd = PyObject_GetAttrString(PyList_GetItem(list, i), "is_ADHD");
        input->y[i] = PyObject_IsTrue(is_adhd) ? 1 : -1;
    }
    input->x_size = (int)list_len;
    input->k_type = k_type;
    input->C = C;
    return input;
}

static PyObject* packup(opt_output* opt) {
    PyObject* return_tup = PyTuple_New(2);
    PyTuple_SetItem(return_tup, 1, PyFloat_FromDouble(opt->b));
    PyObject* alpha_list = PyList_New((int)opt->alphas->size);
    for (size_t i=0; i<opt->alphas->size; i++) 
        PyList_SetItem(alpha_list, i, PyFloat_FromDouble(gsl_vector_get(opt->alphas, i))); 
    PyTuple_SetItem(return_tup, 0, alpha_list);
    return return_tup;
}