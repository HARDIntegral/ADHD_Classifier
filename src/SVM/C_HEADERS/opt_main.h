#ifndef __OPT_MAIN_H__
#define __OPT_MAIN_H__

#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include "ndarrayobject.h"

// returns vector normal to hyperplane and margin width
PyObject* __get_w_width(PyArrayObject* elements, int rbf);

#endif  /* __OPT_MAIN_H__ */