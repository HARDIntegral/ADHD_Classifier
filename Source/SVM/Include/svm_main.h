#ifndef __SVM_MAIN_H__
#define __SVM_MAIN_H__

#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include <stdlib.h>
#include <gsl_vector.h>
#include <gsl_multimin.h>
#include "common.h"
#include "smo.h"
#include "kernels.h"

// returns vector normal to hyperplane and margin width
PyObject* __get_w_b(PyObject* elements, int k_type, double C);
input_data_t* process_input_data(PyObject* n_array, int k_type, double C);

#endif  /* __SVM_MAIN_H__ */