#include <python.h>

/**
 * print_python_list_info - function
 * that prints some basic info about Python lists
 * @p: pyobject list
 */
void print_python_list_info(PyObject *p)
{
	int size, n, i;
	PyObject *object;

	size = Py_SIZE(p);
	n = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", n);

	for (i = 0; i < size; i++)
	{
		printf("Element %d: ", i);
		object = PyList_GetItem(p, i);
		printf("%s\n", Py_TYPE(object)->tp_name);
	}
}
