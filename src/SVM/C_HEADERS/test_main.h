#ifndef __TEST_MAIN_H__
#define __TEST_MAIN_H__

#define PY_SSIZE_T_CLEAN
#include <python3.10/Python.h>
#include <stdlib.h>
#include <gsl/gsl_vector.h>

// returns predictions and true values
PyObject* __test_t(PyObject* elements, PyObject* w, PyObject* b);

#endif  /* __TEST_MAIN_H__ */