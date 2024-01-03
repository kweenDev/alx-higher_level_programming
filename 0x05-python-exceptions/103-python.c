#define PY_SSIZE_T_CLEAN
#include <Python.h>

/**
* print_python_list - Print information about Python lists
* @p: PyObject pointer to a Python object
*/
void print_python_list(PyObject *p)
{
	Py_ssize_t i, size;

	printf("[*] Python list info\n");
	size = PyList_Size(p);
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

	for (i = 0; i < size; i++)
	{
		printf("Element %ld: ", i);
		PyObject_Print(PyList_GetItem(p, i), stdout, Py_PRINT_RAW);
		printf("\n");
	}
}

/**
* print_python_bytes - Print information about Python bytes
* @p: PyObject pointer to a Python object
*/
void print_python_bytes(PyObject *p)
{
	Py_ssize_t size, i;
	char *str;

	printf("[.] bytes object info\n");

	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	size = PyBytes_Size(p);
	printf("  size: %ld\n", size);

	str = PyBytes_AsString(p);

	printf("  trying string: %s\n", str);

	printf("  first %ld bytes: ", size < 10 ? size + 1 : 10);

	for (i = 0; i < size && i < 10; i++)
	{
		printf("%02x", (unsigned char)str[i]);
		if (i < size - 1 && i < 9)
			printf(" ");
	}
	printf("\n");
}

/**
* print_python_float - Print information about Python floats
* @p: PyObject pointer to a Python object
*/
void print_python_float(PyObject *p)
{
	double value;

	printf("[.] float object info\n");

	if (!PyFloat_Check(p))
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}

	value = ((PyFloatObject *)p)->ob_fval;

	printf("  value: %f\n", value);
}
