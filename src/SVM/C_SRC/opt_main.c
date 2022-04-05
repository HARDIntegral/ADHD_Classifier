#include "opt_main.h"

// Prototypes
typedef struct _input_data {
    gsl_vector** x;
    int x_size;
    int* y;
    int use_rbf;
} input_data_t;
typedef struct _w_b {
    gsl_vector* w;
    double b;
} w_b;

gsl_vector* compute_alphas(input_data_t* input);
w_b* compute_w_b(gsl_vector* alphas, input_data_t* input);
input_data_t* process_input_data(PyObject* n_array, int rbf);
PyObject* packup(gsl_vector* w, double b);

double k_rbf(gsl_vector* u, gsl_vector* v);
double k_custom(gsl_vector* u, gsl_vector* v);

double rd();
double dot_prod(gsl_vector* u, gsl_vector* v);
double magnitude(gsl_vector* u);

double lagrangian(gsl_vector* alphas, void* params);

// Main functions
PyObject* __get_w_b(PyObject* elements, int rbf) {
    input_data_t* input = process_input_data(elements, rbf);
    gsl_vector* alphas = compute_alphas(input);
    w_b* outputs = compute_w_b(alphas, input);
    return packup(outputs->w, outputs->b);
}

gsl_vector* compute_alphas(input_data_t* input) {
    // set a dummy variable for now

    //TODO: Add the optimization functionality please
    const gsl_multimin_fminimizer_type *T = gsl_multimin_fminimizer_nmsimplex2;
    gsl_multimin_fminimizer *s = NULL;
    gsl_multimin_function min_lagrange;

    size_t iter = 0;
    int status;
    double size;

    gsl_vector* alphas = gsl_vector_alloc(input->x_size);
    gsl_vector* ss = gsl_vector_alloc(input->x_size);
    gsl_vector_set_all(alphas, rd());
    gsl_vector_set_all(ss, 1);

    min_lagrange.n = 2;
    min_lagrange.f = &lagrangian;
    min_lagrange.params = (void*)input;

    s = gsl_multimin_fminimizer_alloc(T, 2);
    gsl_multimin_fminimizer_set(s, &min_lagrange, alphas, ss);

    return alphas;
}

w_b* compute_w_b(gsl_vector* alphas, input_data_t* input) {
    w_b* output = (w_b*)malloc(sizeof(w_b));
    output->w = gsl_vector_alloc(2);
    gsl_vector_set_zero(output->w);
    output->b = 0;
    for (int i=0; i<alphas->size; i++) {
        // safe to manipulate x vectors directly since they will not be used anymore
        gsl_vector_scale(input->x[i], gsl_vector_get(alphas, i) * input->y[i]);
        gsl_vector_add(output->w, input->x[i]); 
        output->b += gsl_vector_get(alphas, i) * input->y[i];
    }
    return output;
}

input_data_t* process_input_data(PyObject* list, int rbf) {
    Py_ssize_t list_len = PyList_Size(list);
    input_data_t* input = (input_data_t*)malloc(sizeof(input_data_t));
    input->x = (gsl_vector**)malloc(sizeof(gsl_vector)*list_len);
    input->y = (int*)malloc(sizeof(int)*list_len);
    for (Py_ssize_t i=0; i<list_len; i++) {
        PyObject* data_tup = PyObject_GetAttrString(PyList_GetItem(list, i), "features");
        input->x[i] = gsl_vector_alloc(2);
        gsl_vector_set(input->x[i], 0, PyFloat_AsDouble(PyTuple_GetItem(data_tup, 0)));
        gsl_vector_set(input->x[i], 1, PyFloat_AsDouble(PyTuple_GetItem(data_tup, 1)));
        PyObject* is_adhd = PyObject_GetAttrString(PyList_GetItem(list, i), "is_ADHD");
        input->y[i] = PyBool_Check(is_adhd) ? 1 : -1;
    }
    input->x_size = (int)list_len;
    input->use_rbf = rbf;
    return input;
}

PyObject* packup(gsl_vector* w, double b) {
    PyObject* return_tup = PyTuple_New(2);
    PyTuple_SetItem(return_tup, 1, PyFloat_FromDouble(b));
    PyObject* w_list = PyList_New(2);
    PyList_SetItem(w_list, 0, PyFloat_FromDouble(gsl_vector_get(w, 0)));
    PyList_SetItem(w_list, 1, PyFloat_FromDouble(gsl_vector_get(w, 1)));
    PyTuple_SetItem(return_tup, 0, w_list);
    return return_tup;
}

// Kernels
double k_rbf(gsl_vector* u, gsl_vector* v) {
    double sigma = 0.1; // just a generic small value for sigma
    gsl_vector* tmp = gsl_vector_alloc(u->size);
    gsl_vector_memcpy(tmp, u);
    gsl_vector_sub(tmp, v);
    double result = exp(-0.5*pow(magnitude(tmp),2)/pow(sigma,2));
    gsl_vector_free(tmp);
    return result;
}

double k_custom(gsl_vector* u, gsl_vector* v) {
    return dot_prod(u, v);  // dummy return value
}

// Helper functions
double rd() {
    time_t t;
    srand((unsigned int)time(&t));
    uint64_t r53 = ((uint64_t)(rand()) << 21) ^ (rand() >> 2);
    return (double)r53 / 9007199254740991.0; // 2^53 - 1
}

double dot_prod(gsl_vector* u, gsl_vector* v) {
    gsl_vector* tmp = gsl_block_alloc(u->size);
    gsl_vector_set_all(tmp, 1);
    gsl_vector_mul(tmp, u);
    gsl_vector_mul(tmp, v);
    double result = 0;
    for (int i=0; i<tmp->size; i++)
        result += gsl_vector_get(tmp, i);
    return result;
}

double magnitude(gsl_vector* u) {
    double result = 0;
    for (int i=0; i<u->size; i++)
        result += pow(gsl_vector_get(u, i), 2);
    return sqrt(result);
}

double lagrangian(gsl_vector* alphas, void* params) {
    input_data_t* input = (input_data_t*)params;
    double result = 0;
    for (int i=0; i<alphas->size; i++) {
        for (int j=0; j<alphas->size; j++) {
            double computed_k = input->use_rbf ? k_rbf(input->x[i], input->x[j]) : k_custom(input->x[i], input->x[j]);
            result += 0.5 * computed_k * gsl_vector_get(alphas, i) * gsl_vector_get(alphas, j) * input->y[i] * input->y[j];
        }
        result -= gsl_vector_get(alphas, i);
    }
    return result;
}