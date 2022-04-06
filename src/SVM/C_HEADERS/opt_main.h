#ifndef __OPT_MAIN_H__
#define __OPT_MAIN_H__

#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include <stdlib.h>
#include <gsl_vector.h>
#include <gsl_multimin.h>

// returns vector normal to hyperplane and margin width
PyObject* __get_w_b(PyObject* elements, int rbf);
// returns predictions and true values
PyObject* __test_t(PyObject* elements);

#endif  /* __OPT_MAIN_H__ */