#ifndef __OPT_MAIN_H__
#define __OPT_MAIN_H__

#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include "ndarrayobject.h"

// returns vector normal to hyperplane and margin width
PyObject* __get_w_width(PyArrayObject* p_cases, PyArrayObject* n_cases, PyArrayObject* p_zetas, PyArrayObject* n_zetas, int C, int rbf);

#endif  /* __OPT_MAIN_H__ */