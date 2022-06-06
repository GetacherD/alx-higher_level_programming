#include <Python.h>
#include <object.h>
#include <listobject.h>
#include <stdio.h>
/**
* print_python_list_info - prints python list info
* @p: python List Object
*/
void print_python_list_info(PyObject *p)
{
	int i;
	PyObject *elem;

	printf("[*] Size of the Python List = %d\n", (int) Py_SIZE(p));
	printf("[*] Allocated = %d\n", (int)((PyListObject *)p)->allocated);
	for (i = 0; i < Py_SIZE(p); i++)
	{
		printf("Element %d: ", i);
		elem = PyList_GetItem(p, i);
		printf("%s\n", Py_TYPE(elem)->tp_name);
	}
}
