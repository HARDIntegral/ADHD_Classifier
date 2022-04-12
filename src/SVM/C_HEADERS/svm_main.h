#ifndef __SVM_MAIN_H__
#define __SVM_MAIN_H__

#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include <stdlib.h>
#include <gsl_vector.h>
#include <gsl_multimin.h>

// returns vector normal to hyperplane and margin width
PyObject* __get_w_b(PyObject* elements, int rbf, double C);

#endif  /* __SVM_MAIN_H__ */