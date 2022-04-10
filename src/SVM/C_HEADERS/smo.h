#ifndef __SMO_H__
#define __SMO_H__

#include "common.h"
#include "gsl_vector.h"

gsl_vector* compute_alphas(input_data_t* input);

#endif  /* __SMO_H__ */