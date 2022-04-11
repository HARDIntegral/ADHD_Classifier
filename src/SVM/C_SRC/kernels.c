#include "kernels.h"

// Prototypes
static double dot_prod(gsl_vector* u, gsl_vector* v);
static double magnitude(gsl_vector* u);

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

static double magnitude(gsl_vector* u) {
    double result = 0;
    for (size_t i=0; i<u->size; i++)
        result += pow(gsl_vector_get(u, i), 2);
    return sqrt(result);
}