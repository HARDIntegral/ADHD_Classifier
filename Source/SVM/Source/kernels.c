#include "kernels.h"
#include "common.h"

// Prototypes
gsl_vector** get_mask(gsl_vector* a, gsl_vector* b);
gsl_vector** kill_mask(gsl_vector** mask);

double k_rbf(gsl_vector* u, gsl_vector* v) {
    double sigma = 0.1; // just a generic small value for sigma
    gsl_vector* tmp = gsl_vector_alloc(u->size);
    gsl_vector_memcpy(tmp, u);
    gsl_vector_sub(tmp, v);
    double result = exp(-0.5*pow(magnitude(tmp),2)/pow(sigma,2));
    gsl_vector_free(tmp);
    return result;
}

double k_m_rbf(gsl_vector* u, gsl_vector* v) {
    gsl_vector** masks = get_mask(u, v);
    double k_result = k_rbf(masks[0], masks[1]);
    kill_mask(masks);
    return k_result; 
}

double k_m_poly_3(gsl_vector* u, gsl_vector* v) {
    gsl_vector** masks = get_mask(u, v);
    double u_v = dot_prod(masks[0], masks[1]);
    kill_mask(masks);
    return pow(1 + u_v, 3);  
}

double k_m_rbf_poly_3_3(gsl_vector* u, gsl_vector* v) {
    gsl_vector** masks = get_mask(u, v);
    double multiplier = pow(1+dot_prod(masks[0], masks[1]),3);
    gsl_vector_scale(masks[0],multiplier);
    gsl_vector_scale(masks[1],multiplier);
    double result = k_rbf(masks[0], masks[1]);
    kill_mask(masks);
    return result;
}

// Helper functions
gsl_vector** get_mask(gsl_vector* a, gsl_vector* b) {
    gsl_vector** result = (gsl_vector**)malloc(sizeof(gsl_vector*)*2);
    result[0] = gsl_vector_alloc(a->size);
    result[1] = gsl_vector_alloc(b->size);
    gsl_vector_memcpy(result[0], a);
    gsl_vector_memcpy(result[1], b);
    for (size_t i=0; i<a->size; i++) {
        if ((i<4 || i==10 || i==11 || i==16)) {
            gsl_vector_set(result[0], i, 0);
            gsl_vector_set(result[1], i, 0);
        }
    }
    return result;
}

gsl_vector** kill_mask(gsl_vector** mask) {
    gsl_vector_free(mask[0]);
    gsl_vector_free(mask[1]);
    free(mask);
}