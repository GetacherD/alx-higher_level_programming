#include <Python.h>

void print_python_list_info(PyObject __attribute__((unused))*p)
{
  int i;
  PyObject *elem;

  printf("[*] Size of Python List = %d\n",(int) Py_SIZE(p));
  printf("[*] Allocated = %d\n", (int)((PyListObject *)p)->allocated);
  for (i = 0; i < Py_SIZE(p); i++)
    {
      printf("Element %d: ", i);
      elem = PyList_GetItem(p ,i);
      printf("%s\n", Py_TYPE(elem)->tp_name);
    }
 }
