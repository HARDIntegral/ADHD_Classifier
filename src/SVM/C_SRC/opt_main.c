#include "opt_main.h"

// Prototypes
typedef struct _input_data {
    gsl_vector** x;
    bool* labels;
} input_data_t;

double rd();
input_data_t* process_input_data(PyObject* n_array, int* len);
PyObject* packup(gsl_vector* w, double width, double b);

// Main functions
PyObject* __get_w_b_width(PyObject* elements, int rbf) {
    // unpack list to be a set of vectors
    int len;
    input_data_t* x = process_input_data(elements, &len);

    //  guess a w vector and b
    gsl_vector* w = gsl_vector_alloc(2);
    for (int i=0; i<2; i++)
        gsl_vector_set(w, i, rd());
    double b = rd();   

    double width = 5.0;     // just a dummy width value

    // pack w vector, b, and width back into a python tuple
    return packup(w, width, b);
}

// Helper functions
double rd() {
    time_t t;
    srand((unsigned int)time(&t));
    uint64_t r53 = ((uint64_t)(rand()) << 21) ^ (rand() >> 2);
    return (double)r53 / 9007199254740991.0; // 2^53 - 1
}

input_data_t* process_input_data(PyObject* list, int* len) {
    Py_ssize_t list_len = PyList_Size(list);
    input_data_t* input = (input_data_t*)malloc(sizeof(input_data_t));
    input->x = (gsl_vector**)malloc(sizeof(gsl_vector)*list_len);
    bool* labels = (bool*)malloc(sizeof(bool)*list_len);
    for (Py_ssize_t i=0; i<list_len; i++) {
        PyObject* data_tup = PyObject_GetAttrString(PyList_GetItem(list, i), "features");
        input->x[i] = gsl_vector_alloc(2);
        gsl_vector_set(input->x[i], 0, PyFloat_AsDouble(PyTuple_GetItem(data_tup, 0)));
        gsl_vector_set(input->x[i], 1, PyFloat_AsDouble(PyTuple_GetItem(data_tup, 1)));
        PyObject* is_adhd = PyObject_GetAttrString(PyList_GetItem(list, i), "is_ADHD");
        labels[i] = PyBool_Check(is_adhd);
    }
    return input;
}

PyObject* packup(gsl_vector* w, double width, double b) {
    PyObject* return_tup = PyTuple_New(3);
    PyTuple_SetItem(return_tup, 1, PyFloat_FromDouble(width));
    PyTuple_SetItem(return_tup, 2, PyFloat_FromDouble(b));

    PyObject* w_list = PyList_New(2);
    PyList_SetItem(w_list, 0, PyFloat_FromDouble(gsl_vector_get(w, 0)));
    PyList_SetItem(w_list, 1, PyFloat_FromDouble(gsl_vector_get(w, 1)));
    PyTuple_SetItem(return_tup, 0, w_list);

    return return_tup;
}