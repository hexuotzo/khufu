#include "Python.h"
#include <dystopia.h>
#include <stdlib.h>
#include <stdbool.h>
#include <stdint.h>

static PyObject *
search(PyObject *self, PyObject *args)
{
    const char *stext;
    TCIDB *idb;
    int ecode, rnum, i;
    uint64_t *result;
    char *text;
    PyObject* pList;
    
    if (!PyArg_ParseTuple(args, "s", &stext))
        return NULL;

    /* create the object */
    idb = tcidbnew();

    /* open the database */
    if(!tcidbopen(idb, "/home/yanxu/khufu/khufu", IDBOWRITER | IDBOCREAT)){
        ecode = tcidbecode(idb);
        fprintf(stderr, "open error: %s\n", tcidberrmsg(ecode));
    }
    /* search records */
    result = tcidbsearch2(idb, stext, &rnum);
    pList = PyList_New(rnum);
    if(result){
        for(i = 0; i < rnum; i++){
            PyList_SetItem(pList, i, Py_BuildValue("i", result[i]));
         //  text = tcidbget(idb, result[i]);
         //  if(text){
         //    printf("%d\t%s\n", (int)result[i], text);
         //    free(text);
        }
        free(result);
    } else {
        ecode = tcidbecode(idb);
        fprintf(stderr, "search error: %s\n", tcidberrmsg(ecode));
    }
    
    /* close the database */
    if(!tcidbclose(idb)){
        ecode = tcidbecode(idb);
        fprintf(stderr, "close error: %s\n", tcidberrmsg(ecode));
    }

    /* delete the object */
    tcidbdel(idb);

    return Py_BuildValue("O",pList);
}

PyMethodDef methods[] = {
  {"search", search, METH_VARARGS},
  {NULL, NULL},
};

void initpykhufu(){
    PyObject* m;
    m = Py_InitModule("pykhufu", methods);
}
