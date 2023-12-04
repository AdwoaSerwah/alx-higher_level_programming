#include <Python.h>

/**
 * print_python_string - Prints information about Python strings
 * @p: PyObject pointer to the Python string
 */
void print_python_string(PyObject *p)
{
	printf("[.] string object info\n");

	if (!PyUnicode_Check(p))
	{
		printf("  [ERROR] Invalid String Object\n");
		return;
	}

	Py_ssize_t length = PyUnicode_GET_LENGTH(p);

	printf("  type: compact ");
	if (PyUnicode_IS_ASCII(p))
		printf("ascii\n");
	else
		printf("unicode object\n");

	printf("  length: %ld\n", length);
	printf("  value: ");

	const char *utf8_str = PyUnicode_AsUTF8(p);

	if (utf8_str != NULL)
	{
		for (Py_ssize_t i = 0; i < length; ++i)
			printf("%c", utf8_str[i]);
	}
	else
	{
		printf("[ERROR] Failed to decode UTF-8\n");
	}

	printf("\n");
}
