#include <Python.h>

void print_python_bytes(PyObject *p)
{
  int size, i;
  PyBytesObject *by = (PyBytesObject *)p;
  int is_valid;
  is_valid = PyBytes_Check(p);
  size = ((PyVarObject *)p)->ob_size;
  printf("[.] bytes object info\n");
  if (!is_valid)
  {
    printf("  [ERROR] Invalid Bytes Object\n");
  }
  else
  {
    printf("  size: %d\n", size);
    printf("  trying string: %s\n", by->ob_sval);
    printf("  first %d bytes: ", 10 >= size ? size : 10);
    for (i = 0; i < 9 && i < size - 1; i++)
    {
      printf("%02hhx ", by->ob_sval[i]);
    }
    printf("%02hhx\n",  by->ob_sval[i]);
  }
}
void print_python_list(PyObject *p)
{

  int size, alloc, i = 0;
  PyObject **objects;
  PyObject *ob;
  /*is_valid = PyList_Check(p);
  if (is_valid)
  {*/
  size = PyList_Size(p);
  printf("IS IT HERE\n");
  
       
  objects = ((PyListObject *)p)->ob_item;
  alloc = ((PyListObject *)p)->allocated;
  printf("[*] Python list info\n");
  printf("[*] Size of the Python List = %d\n", size);
  printf("[*] Allocated = %d\n", alloc);
  for (i = 0; i < size ; i++)
    {
      printf("Element %d: ", i);
      ob = objects[i];
      printf("%s\n", (ob->ob_type)->tp_name);
    }
    

}
