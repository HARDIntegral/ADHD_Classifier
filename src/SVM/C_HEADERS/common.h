#ifndef __COMMON_H__
#define __COMMON_H__

#include "gsl_vector.h"
typedef struct _input_data {
    gsl_vector** x;
    int x_size;
    int* y;
    int use_rbf;
    int C;
} input_data_t;

#endif  /* __COMMON_H__ */