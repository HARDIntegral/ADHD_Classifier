#ifndef __SMO_H__
#define __SMO_H__

#include <gsl_vector.h>

typedef struct _input_data {
    gsl_vector** x;
    int x_size;
    int* y;
    int use_rbf;
} input_data_t;

gsl_vector* compute_alphas(input_data_t* input);

#endif  /* __SMO_H__ */