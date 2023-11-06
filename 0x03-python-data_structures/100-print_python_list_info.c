#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include "lists.h"

/**
 * print_python_list_info - Prints python list info
 * @p: Pointer
 *
 * Return: Nothing
 */
void print_python_list_info(PyObject *p)
{
	Py_ssize_t size, allocated, i;
	PyObject *elem;

	size = PyList_Size(p);
	allocated = ((PyListObject *)p)->allocated;
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", allocated);
	for (i = 0; i < size; i++)
	{
		elem = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(elem)->tp_name);
	}
}
