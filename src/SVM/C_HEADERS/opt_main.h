#ifndef __OPT_MAIN_H__
#define __OPT_MAIN_H__

#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include <stdlib.h>
#include <stdint.h>
#include <gsl_vector.h>

// returns vector normal to hyperplane and margin width
PyObject* __get_w_b_width(PyObject* elements, int rbf);

#endif  /* __OPT_MAIN_H__ */