#ifndef __SVM_MAIN_H__
#define __SVM_MAIN_H__

#define PY_SSIZE_T_CLEAN
#include <python3.10/Python.h>
#include <stdlib.h>
#include <gsl/gsl_vector.h>
#include <gsl/gsl_multimin.h>

// returns vector normal to hyperplane and margin width
PyObject* __get_w_b(PyObject* elements, int rbf);

#endif  /* __SVM_MAIN_H__ */