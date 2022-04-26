#ifndef __KERNELS_H__
#define __KERNELS_H__

#include <stdio.h>
#include <math.h>
#include "gsl_vector.h"

typedef enum _kernel_type {
    RBF,
    M_RBF,
    M_POLY,
    M_LIN_SPLINE
} kernel_type;

double k_rbf(gsl_vector* u, gsl_vector* v);
double k_m_rbf(gsl_vector* u, gsl_vector* v);
double k_m_poly_3(gsl_vector* u, gsl_vector* v);
double k_m_rbf_poly_3_3(gsl_vector* u, gsl_vector* v);

#endif  /* __KERNELS_H__ */