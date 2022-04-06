#include "k_custom.h"

double k_custom(gsl_vector* u, gsl_vector* v) {
    return dot_prod(u, v);  // dummy return value
}