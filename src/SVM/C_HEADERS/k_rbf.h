#ifndef __K_RBF_H__
#define __K_RBF_H__

#include <stdlib.h>
#include <gsl_vector.h>

double k_rbf(gsl_vector* u, gsl_vector* v);

#endif  /* __K_RBF_H__ */