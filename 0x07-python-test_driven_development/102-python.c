#define PY_SSIZE_T_CLEAN
#include <Python.h>

/**
 * print_python_string - Prints information about Python strings
 * @p: PyObject string
 */
void print_python_string(PyObject *p) {
	if (PyUnicode_Check(p))
	{
		Py_ssize_t length;
		wchar_t *wstr;

		length = PyUnicode_GET_LENGTH(p);
		wstr = PyUnicode_AsWideCharString(p, &length);

		printf("[.] string object info\n");
		printf("  type: ");
		if (PyUnicode_IS_COMPACT_ASCII(p))
			printf("compact ascii\n");
		else
			printf("compact unicode object\n");

		printf("  length: %ld\n", length);
		printf("  value: %s\n", PyUnicode_AsUTF8(p));

		PyMem_Free(wstr);
	}
	else
	{
		printf("[.] string object info\n");
		printf("  [ERROR] Invalid String Object\n");
	}
}
