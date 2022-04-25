#ifndef __SMO_H__
#define __SMO_H__

#include <stdlib.h>
#include <stdint.h>
#include <time.h>
#include "common.h"
#include "gsl_vector.h"

typedef struct opt_output_t {
    gsl_vector* alphas;
    double b;
} opt_output;

opt_output* compute_alphas(input_data_t* input, double tol, int max_passes);

#endif  /* __SMO_H__ */