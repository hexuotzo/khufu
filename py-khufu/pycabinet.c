#include "Python.h"
#include <tctdb.h>
#include <stdlib.h>
#include <stdbool.h>
#include <stdint.h>

static PyObject *
get(PyObject *self,PyObject *args){
    TCTDB *tdb;
    int ecode;
    const char *name;

    const char *dbname;
    const char *key;
    if (!PyArg_ParseTuple(args, "ss", &dbname, &key))
        return NULL;

    tdb = tctdbnew();
    if(!tctdbopen(tdb, dbname, TDBONOLCK | TDBOREADER)){
        ecode = tctdbecode(tdb);
        fprintf(stderr, "open error: %s\n", tctdberrmsg(ecode));
    }
    name = tctdbget3(tdb,key);
    if(!tctdbclose(tdb)){
        ecode = tctdbecode(tdb);
        fprintf(stderr, "close error: %s\n", tctdberrmsg(ecode));
    }
    tctdbdel(tdb);
    return Py_BuildValue("s",name);
}


static PyObject *
search(PyObject *self, PyObject *args){
    TCTDB *tdb;
    int ecode, i, rsiz;
    const char *rbuf, *name;
    TCMAP *cols;
    TDBQRY *qry;
    TCLIST *res;

    const char *dbname;
    const char *sfield;
    const char *stext;
    const int *max;
    PyObject* pDict = PyDict_New();
    PyObject* pList = PyList_New(0);

    if (!PyArg_ParseTuple(args, "sssi", &dbname, &sfield, &stext,&max))
        return NULL;

    tdb = tctdbnew();
    
    if(!tctdbopen(tdb, dbname, TDBONOLCK | TDBOREADER)){
        ecode = tctdbecode(tdb);
        fprintf(stderr, "open error: %s\n", tctdberrmsg(ecode));
    }
    qry = tctdbqrynew(tdb);
    tctdbqryaddcond(qry, sfield, TDBQCSTREQ, stext);
    tctdbqrysetlimit(qry, max, 0);
    res = tctdbqrysearch(qry);
    for(i = 0; i < tclistnum(res); i++){
        rbuf = tclistval(res, i, &rsiz);
        cols = tctdbget(tdb, rbuf, rsiz);
        if(cols){
          // printf("%s", rbuf);
          tcmapiterinit(cols);
          PyDict_SetItemString(pDict, "kid", Py_BuildValue("s",rbuf));
          while((name = tcmapiternext2(cols)) != NULL){
              // printf("%s",tcmapget2(cols, name));
              PyDict_SetItemString(pDict, name, Py_BuildValue("s", tcmapget2(cols, name)));
              // printf("\t%s\t%s", name, tcmapget2(cols, name));
          }
          PyList_Append(pList,pDict);
          pDict = PyDict_New();
          // printf("\n");
          tcmapdel(cols);
        }
    }
    tclistdel(res);
    tctdbqrydel(qry);

    if(!tctdbclose(tdb)){
        ecode = tctdbecode(tdb);
        fprintf(stderr, "close error: %s\n", tctdberrmsg(ecode));
    }

    tctdbdel(tdb);

    return Py_BuildValue("O",pList);
}

PyMethodDef methods[] = {
  {"search", search, METH_VARARGS},
  {"get", get, METH_VARARGS},
  {NULL, NULL},
};

void initpycabinet(){
    PyObject* m;
    m = Py_InitModule("pycabinet", methods);
}
