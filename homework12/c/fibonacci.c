#include <Python.h>

static PyObject* fibonacci(PyObject* self, PyObject* args) {
    long long n;

    if(!PyArg_ParseTuple(args, "L", &n)) {
        return NULL;
    }

    if (n <= 2) {
        PyObject *first = PyLong_FromLong(1);
        Py_INCREF(first);
        return first;
    }

    PyObject *first = PyLong_FromLong(1);
    PyObject *second = PyLong_FromLong(1);
    PyObject *next = PyLong_FromLong(2);

    for (long long c = 2; c < n; c++) {
        next = PyNumber_Add(first, second);
        first = second;
        second = next;
    }

    Py_INCREF(next);
    return Py_BuildValue("O", next);
};

static PyMethodDef methods[] = {
    { "fibonacci", fibonacci, METH_VARARGS, "Returns n-th Fibonacci number" },
    { NULL, NULL, 0, NULL }
};

static struct PyModuleDef module = {
    PyModuleDef_HEAD_INIT,
    "fibonacci",
    "Fibonacci module",
    -1,
    methods
};

PyMODINIT_FUNC PyInit_fibonacci(void) {
    return PyModule_Create(&module);
};
