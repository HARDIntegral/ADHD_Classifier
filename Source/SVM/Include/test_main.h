#ifndef __TEST_MAIN_H__
#define __TEST_MAIN_H__

#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include <stdlib.h>
#include <math.h>
#include <gsl_vector.h>
#include "common.h"
#include "svm_main.h"
#include "kernels.h"

// returns predictions and true values
PyObject* __test_t(PyObject* training, PyObject* testing, PyObject* alphas, double b, int rbf);

#endif  /* __TEST_MAIN_H__ */