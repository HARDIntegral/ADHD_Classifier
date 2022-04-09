#ifndef __CV_OPT_H__
#define __CV_OPT_H__

#include <gsl/gsl_vector.h>
extern "C" {
#include "common.h"
}

extern "C" gsl_vector* compute_alphas(input_data_t* input);

#endif  /* __CV_OPT_H__ */