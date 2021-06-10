#include <Python.h>
//mozliwe sygnatury funkcji stanowiącej "interfejs" pomiędzy pythonem i C
//static PyObject *mod_met(PyObject *self){
//static PyObject *mod_met(PyObject *self, PyObject *args, PyObject *kw){
static PyObject *mod_met(PyObject *self, PyObject *args){
	int a, b;
	PyObject *c = NULL;
	PyObject *d = NULL;
	if(!PyArg_ParseTuple(args, "ii|OO", &a, &b, &c, &d)){ //jezeli do stringa wstawi sie | to po sa parametry opcjonalne; O od Object
		return NULL;	//zwracane w przypadku bledu; interpreter zglasza wyjatek wywolania funkcji
	}
	int s = a + b;
  if (c) 
  {
    s += PyLong_AsLong(c);
  }
  
	if(d){
		int r=PyList_Size(d);
		for(int i = 0; i < r; i++){
			s += PyLong_AsLong(PyList_GetItem(d, i));
		}
	}
	//Py_RETURN_NONE; //jesli nic nie zwraca
	return Py_BuildValue("i", s);
}

static PyObject *mod_met3(PyObject *self, PyObject *args){
  PyObject *dict = NULL;
  if(!PyArg_ParseTuple(args, "O", &dict))
  {
    return NULL;
  }

  PyObject *key, *value;
  Py_ssize_t pos = 0;

  PyObject *new_dict = PyDict_New();
  int counter = 0;
  while (PyDict_Next(dict, &pos, &key, &value))
  {
    long a = PyLong_AsLong(key);
    long b = PyLong_AsLong(value);
    while( a != b)
    {
      if(a > b)
      {
        a = a - b;
      }
      else
      {
        b = b - a;
      }
    }
    PyDict_SetItem(new_dict, PyLong_FromLong(counter), PyLong_FromLong(a));
    counter++;
  }
  return Py_BuildValue("O", new_dict);
}


//tablica metod
static PyMethodDef mod_metody[]={
	{"met", (PyCFunction)mod_met, METH_VARARGS, "Funkcja ..."}, 
	//nazwa funkcja stosowana w Pythonie, adres funkcji , j.w. lub METH_KEYWORDS lub METH_NOARGS, lancuch dokumentacyjny
  {"met3", (PyCFunction)mod_met3, METH_VARARGS, "Funkcja ..."},
	{NULL, NULL, 0, NULL}	//wartownik
};


static struct PyModuleDef modmodule = {
        PyModuleDef_HEAD_INIT,
        "mod",
        NULL,
        -1,
        mod_metody
};

//funkcja inicjalizujaca
PyMODINIT_FUNC PyInit_mod(void){
        return PyModule_Create(&modmodule);
}
