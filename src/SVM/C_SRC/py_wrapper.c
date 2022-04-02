#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include "ndarrayobject.h"

#include "opt_main.h"

PyObject* __opt(PyObject* self, PyObject* args) {
    PyArrayObject* p_cases;
    PyArrayObject* n_cases;
    PyArrayObject* p_zetas;
    PyArrayObject* n_zetas;
    int C;
    int rbf;    // 1 if RBF kernel is used 0 for my kernel
	if (!PyArg_ParseTuple(args, "OOOOi", &p_cases, &n_cases, &p_zetas, &n_zetas, &C, &rbf))
		return NULL;

	return __get_w_width(p_cases, n_cases, p_zetas, n_zetas, C, rbf);
}

static PyMethodDef methods[] = {
	{"opt", __opt, METH_VARARGS, ""},
	{NULL, NULL, 0, NULL}
};

static struct PyModuleDef c_opt = {
	PyModuleDef_HEAD_INIT,
	"C OPT",
	"C interop to optimize a custom implementation of an SVM",
	-1,
	methods
};

PyMODINIT_FUNC PyInit_c_opt() {
	return PyModule_Create(&c_opt);
}