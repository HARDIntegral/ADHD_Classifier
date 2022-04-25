#ifndef __KERNELS_H__
#define __KERNELS_H__

#include <math.h>
#include "gsl_vector.h"

double k_rbf(gsl_vector* u, gsl_vector* v);
double k_custom(gsl_vector* u, gsl_vector* v);

#endif  /* __KERNELS_H__ */