#include "svm_main.h"
#include "common.h"
#include "smo.h"
#include "kernels.h"

// Prototypes
typedef struct _w_b {
    gsl_vector* w;
    double b;
} w_b;

static w_b* compute_w_b(gsl_vector* alphas, input_data_t* input);
static input_data_t* process_input_data(PyObject* n_array, int rbf, int C);
static PyObject* packup(gsl_vector* w, double b);

double f_lagrangian(const gsl_vector* alphas, void* params);
void df_lagrangian(const gsl_vector* alphas, void* params, gsl_vector* df);
void fdf_lagrangian(const gsl_vector* alphas, void* params, double* f, gsl_vector* df); 

// Main functions
PyObject* __get_w_b(PyObject* elements, int rbf, int C) {
    input_data_t* input = process_input_data(elements, rbf, C);
    gsl_vector* alphas = compute_alphas(input);
    w_b* outputs = compute_w_b(alphas, input);
    return packup(outputs->w, outputs->b);
}

static w_b* compute_w_b(gsl_vector* alphas, input_data_t* input) {
    w_b* output = (w_b*)malloc(sizeof(w_b));
    output->w = gsl_vector_alloc(input->x[0]->size);
    gsl_vector_set_zero(output->w);
    output->b = 0;
    for (size_t i=0; i<alphas->size; i++) {
        // safe to manipulate x vectors directly since they will not be used anymore
        gsl_vector_scale(input->x[i], gsl_vector_get(alphas, i) * input->y[i]);
        gsl_vector_add(output->w, input->x[i]); 
        output->b += gsl_vector_get(alphas, i) * input->y[i];
    }
    return output;
}

static input_data_t* process_input_data(PyObject* list, int rbf, int C) {
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
        input->y[i] = PyBool_Check(is_adhd) ? 1 : -1;
    }
    input->x_size = (int)list_len;
    input->use_rbf = rbf;
    input->C = C;
    return input;
}

static PyObject* packup(gsl_vector* w, double b) {
    PyObject* return_tup = PyTuple_New(2);
    PyTuple_SetItem(return_tup, 1, PyFloat_FromDouble(b));
    PyObject* w_list = PyList_New((int)w->size);
    for (size_t i=0; i<w->size; i++)
        PyList_SetItem(w_list, i, PyFloat_FromDouble(gsl_vector_get(w, i)));
    PyTuple_SetItem(return_tup, 0, w_list);
    return return_tup;
}

// Helper functions
double f_lagrangian(const gsl_vector* alphas, void* params) {
    input_data_t* input = (input_data_t*)params;
    double result = 0;
    for (size_t i=0; i<alphas->size; i++) {
        for (size_t j=0; j<alphas->size; j++) {
            double computed_k = input->use_rbf ? k_rbf(input->x[i], input->x[j]) : k_custom(input->x[i], input->x[j]);
            result += 0.5 * computed_k * gsl_vector_get(alphas, i) * gsl_vector_get(alphas, j) * input->y[i] * input->y[j];
        }
        result -= gsl_vector_get(alphas, i);
    }
    return result;
}

void df_lagrangian(const gsl_vector* alphas, void* params, gsl_vector* df) {
    input_data_t* input = (input_data_t*)params;
    for (size_t i=0; i<alphas->size; i++) {
        double grad_element = 0;
        for (size_t j=0; j<alphas->size; j++) {
            double computed_k = input->use_rbf ? k_rbf(input->x[i], input->x[j]) : k_custom(input->x[i], input->x[j]);
            grad_element += 0.5 * computed_k * input->y[i] * input->y[j] - 1;
        }
        gsl_vector_set(df, i, grad_element);
    }
}

void fdf_lagrangian(const gsl_vector* alphas, void* params, double* f, gsl_vector* df) {
    *f = f_lagrangian(alphas, params);
    df_lagrangian(alphas, params, df);
}