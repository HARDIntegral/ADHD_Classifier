#include "kernels.h"
#include "common.h"

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
    double u_v = dot_prod(u, v);
    return pow(u_v, 2);  
}