#include "Python.h"
#include <dystopia.h>
#include <stdlib.h>
#include <stdbool.h>
#include <stdint.h>

static PyObject *
put(PyObject *self,PyObject *args){
    const char *dbname;
    const char *stext;
    const int *kid;
    int ecode;
    bool result;
    TCIDB *idb;
    if (!PyArg_ParseTuple(args, "sis", &dbname, &kid, &stext))
        return NULL;
    /* create the object */
    idb = tcidbnew();
    /* open the database */
    if(!tcidbopen(idb, dbname, IDBOCREAT | IDBOWRITER)){
        ecode = tcidbecode(idb);
        fprintf(stderr, "open error: %s\n", tcidberrmsg(ecode));
    }
    result = tcidbput(idb,(int64_t)kid,stext);
    /* close the database */
    if(!tcidbclose(idb)){
        ecode = tcidbecode(idb);
        fprintf(stderr, "close error: %s\n", tcidberrmsg(ecode));
    }
    /* delete the object */
    tcidbdel(idb);
    return Py_BuildValue("b",result);
}

static PyObject *
search(PyObject *self, PyObject *args){
    const char *stext;
    const char *dbname;
    TCIDB *idb;
    int ecode, rnum, i;
    uint64_t *result;
    char *text;
    PyObject* pList;
    
    if (!PyArg_ParseTuple(args, "ss", &dbname, &stext))
        return NULL;

    /* create the object */
    idb = tcidbnew();

    /* open the database */
    if(!tcidbopen(idb, dbname, IDBOREADER | IDBONOLCK)){
        ecode = tcidbecode(idb);
        fprintf(stderr, "open error: %s\n", tcidberrmsg(ecode));
    }
    /* search records */
    result = tcidbsearch2(idb, stext, &rnum);
    pList = PyList_New(rnum);
    if(result){
        for(i = 0; i < rnum; i++){
            // printf("r[i]:%lld\n",result[i]);
            PyList_SetItem(pList, i, Py_BuildValue("i", (int)result[i]));
        }
        tcfree(result);
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
  {"put", put, METH_VARARGS},
  {NULL, NULL},
};

void initpykhufu(){
    PyObject* m;
    m = Py_InitModule("pykhufu", methods);
}
