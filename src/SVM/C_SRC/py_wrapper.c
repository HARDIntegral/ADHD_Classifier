#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include <gsl_vector.h>

#include "opt_main.h"

PyObject* __opt(PyObject* self, PyObject* args) {
    PyObject* elements;
    int rbf;    // 1 if RBF kernel is used 0 for my kernel
	if (!PyArg_ParseTuple(args, "Oi", &elements, &rbf))
		return NULL;

	return __get_w_b(elements, rbf);
}

PyObject* __test(PyObject* self, PyObject* args) {
	PyObject* elements;
	if (!PyArg_ParseTuple(args, "O", &elements))
		return NULL;
	return __test_t(elements);
}

static PyMethodDef methods[] = {
	{"opt", __opt, METH_VARARGS, ""},
	{"test", __test, METH_VARARGS, ""},
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