#include <Python.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);

/**
 * print_python_list - function
 * that prints some basic info about Python lists
 * @p: pyobject list
 */
void print_python_list(PyObject *p)
{
        int size, n, i;
	const char *type;
        PyListObject *list = (PyListObject *)p;
	PyVarObject *var = (PyVarObject *)p;

        size = var->ob_size;
        n = list->allocated;

	printf("[*] Python list info\n");
        printf("[*] Size of the Python List = %d\n", size);
        printf("[*] Allocated = %d\n", n);

        for (i = 0; i < size; i++)
        {
		type = list->ob_item[i]->ob_type->tp_name;
                printf("Element %d: ", type);
                if (strcmp(type, "bytes") == 0)
			print_python_bytes(list->ob_item[i]);
        }
}

/**
 * print_python_bytes - functions that print
 * some basic info about Python lists and Python bytes objects
 * @p: pyobject list
 */
void print_python_bytes(PyObject *p)
{
	unsigned char i, s;
	PyBytesObject *bytes = (PyBytesObject *)p;

	printf("[.] bytes object info\n");
	if (strcmp(p->ob_type->tp_name, "bytes") != 0)
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	printf("  size: %d\n", ((PyVarObject *)p)->ob_size);
	printf("  trying string: %s\n", bytes->ob_sval);

	if (((PyVarObject *)p)->ob_size > 10)
		s = 10;
	else
		s = ((PyVarObject *)p)->ob_size + 1;
	printf("  first %d bytes: ", s);
	for (i = 0; i < s; i++)
	{
		printf("%02hhx", bytes->ob_sval[i]);
		if (i == (s - 1))
			printf("\n");
		else
			printf(" ");
	}
}

