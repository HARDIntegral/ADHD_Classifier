#include "kernels.h"
#include "common.h"

double k_rbf(gsl_vector* u, gsl_vector* v) {
    double sigma = 0.1; // just a generic small value for sigma
    gsl_vector* tmp = gsl_vector_alloc(u->size);
    gsl_vector_memcpy(tmp, u);
    gsl_vector_sub(tmp, v);
    double result = exp(-0.5*pow(magnitude(tmp),2)/pow(sigma,2));
    gsl_vector_free(tmp);
    return result;
}
/* 
Custom Kernel:
    This essentially is just a polynomial kernel with
    degree 3 that has masked the elements that correspond
    to EEG channels that do not source readings from the 
    frontal lobe
*/
double k_custom(gsl_vector* u, gsl_vector* v) {
    gsl_vector* _u = gsl_vector_alloc(u->size);
    gsl_vector* _v = gsl_vector_alloc(v->size);
    gsl_vector_memcpy(_u, u);
    gsl_vector_memcpy(_v, v);

    for (size_t i=0; i<u->size; i++) {
        if ((i<4 || i==10 || i==11 || i==16)) {
            gsl_vector_set(u, i, 0);
            gsl_vector_set(v, i, 0);
        }
    }
    double u_v = dot_prod(_u, _v);
    return pow(1 + u_v, 3);  
}
