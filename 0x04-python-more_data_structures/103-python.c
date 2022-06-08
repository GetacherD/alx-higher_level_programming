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
    printf("  trying string: %s\n",by->ob_sval);
    printf("  first %d bytes: ", 10 >= size?size:10);
    for (i = 0; i < 9 && i < size - 1; i++)
    {
      printf("%x ", by->ob_sval[i]);
    }
    printf("%x\n", by->ob_sval[i]);
  }
}
void print_python_list(PyObject *p)
{

  int size ,alloc, i = 0;
  PyObject **objects = ((PyListObject *)p)->ob_item;
  PyObject *ob;
  size = PyList_Size(p);
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
  
/*


  s = b"Hello"
  lib.print_python_bytes(s);
  [.] bytes object info
  size: 5
  trying string: Hello
  first 6 bytes: 48 65 6c 6c 6f 00*/
