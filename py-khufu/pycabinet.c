#include "Python.h"
#include <tcutil.h>
#include <tcadb.h>
#include <tcbdb.h>
#include <tctdb.h>
#include <tcrdb.h>
#include <stdlib.h>
#include <stdbool.h>
#include <stdint.h>

TCADB *openadb(const char *dbname){
    TCADB *adb = tcadbnew();
    if(!tcadbopen(adb, dbname)) {
        fprintf(stderr, "open error: %s\n", dbname);
    }
    return adb;
}
int closeadb(TCADB *adb){
    if(!tcadbclose(adb)){
        fprintf(stderr, "close error:");
        return 0;
    }
    tcadbdel(adb);
    return 1;
}

static PyObject *
create(PyObject *self,PyObject *args){
    const char *dbname;
    if (!PyArg_ParseTuple(args, "s", &dbname))
        return NULL;
    TCADB *adb = openadb(dbname);
    closeadb(adb);
    return Py_BuildValue("s",dbname);
}


static PyObject *
put(PyObject *self,PyObject *args){
    const char *dbname;
    const char *key;
    const char *value;
    if (!PyArg_ParseTuple(args, "sss", &dbname, &key, &value))
        return NULL;
    TCADB *adb = openadb(dbname);
    tcadbput2(adb, key, value);
    closeadb(adb);
    return Py_BuildValue("s",value);
}

static PyObject *
put3(PyObject *self,PyObject *args){
    const char *dbname;
    const char *key;
    const char *value;
    if (!PyArg_ParseTuple(args, "sss", &dbname, &key, &value))
        return NULL;
    TCADB *adb = openadb(dbname);
    tctdbput3(adb->tdb, key, value);
    closeadb(adb);
    return Py_BuildValue("s",value);
}

static PyObject *
put4(PyObject *self,PyObject *args){
    TCRDB *rdb;
    int ecode,pksiz;
    char pkbuf[256];
    const char *host;
    const int *port;
    const char *dbkey;
    PyObject *kv;
    TCMAP *cols;
    if (!PyArg_ParseTuple(args,"sisO",&host,&port,&dbkey,&kv))
        return NULL;
    rdb = tcrdbnew();
    if(!tcrdbopen(rdb, host, port)){
        ecode = tcrdbecode(rdb);
        fprintf(stderr, "open error: %s\n", tcrdberrmsg(ecode));
    }
    pksiz = sprintf(pkbuf, dbkey);
    cols = tcmapnew();
    PyObject *key, *value;
    int pos = 0;
    while (PyDict_Next(kv, &pos, &key, &value)) {
        tcmapput2(cols, PyString_AsString(key), PyString_AsString(value));
    }
    if(!tcrdbtblputkeep(rdb, pkbuf, pksiz, cols)){
        ecode = tcrdbecode(rdb);
        fprintf(stderr, "put error: %s\n", tcrdberrmsg(ecode));
    }
    tcmapdel(cols);
    if(!tcrdbclose(rdb)){
        ecode = tcrdbecode(rdb);
        fprintf(stderr, "close error: %s\n", tcrdberrmsg(ecode));
    }
    tcrdbdel(rdb);
    return Py_BuildValue("s","ok");
}

static PyObject *
get(PyObject *self,PyObject *args){
    char *value;
    const char *dbname;
    const char *key;
    if (!PyArg_ParseTuple(args, "ss", &dbname, &key))
        return NULL;
    TCADB *adb = openadb(dbname);
    if (adb->omode==ADBOTDB)
        value = tctdbget3(adb->tdb,key);
    else
        value = tcadbget2(adb, key);
    closeadb(adb);
    return Py_BuildValue("s",value);
}

static PyObject *
out(PyObject *self,PyObject *args){
    const char *dbname;
    const char *key;
    if (!PyArg_ParseTuple(args, "ss", &dbname, &key))
        return NULL;
    TCADB *adb = openadb(dbname);
    bool value = tcadbout2(adb, key);
    closeadb(adb);
    return Py_BuildValue("i",value);
}


static PyObject *
put2(PyObject *self,PyObject *args){
    const char *dbname;
    const char *key;
    const char *value;
    if (!PyArg_ParseTuple(args, "sss", &dbname, &key, &value))
        return NULL;
    TCADB *adb = openadb(dbname);
    tcbdbputdup2(adb->bdb, key, value);
    closeadb(adb);
    return Py_BuildValue("s",value);
}


static PyObject *
list2(PyObject *self,PyObject *args){
    const char *dbname;
    if (!PyArg_ParseTuple(args, "s", &dbname))
        return NULL;
    TCADB *adb = openadb(dbname);
    PyObject* pList = PyList_New(0);
    if(!tcadbiterinit(adb)){
        return NULL;
    }
    BDBCUR *cur = tcbdbcurnew(adb->bdb);
    TCXSTR *key = tcxstrnew();
    TCXSTR *val = tcxstrnew();
    if(!tcbdbcurfirst(cur) && tcbdbecode(adb->bdb) != TCENOREC){
        return NULL;
    }
    while(tcbdbcurrec(cur, key, val)){
        PyObject* pList1 = PyList_New(0);
        PyList_Append(pList1,Py_BuildValue("s",tcxstrptr(key)));
        PyList_Append(pList1,Py_BuildValue("s",tcxstrptr(val)));
        PyList_Append(pList,pList1);
        if(!tcbdbcurnext(cur) && tcbdbecode(adb->bdb) != TCENOREC){
            return NULL;
        }
    }
    tcxstrdel(val);
    tcxstrdel(key);
    tcbdbcurdel(cur);
    closeadb(adb);
    return Py_BuildValue("O",pList);
}


static PyObject *
list(PyObject *self,PyObject *args){
    const char *dbname;
    if (!PyArg_ParseTuple(args, "s", &dbname))
        return NULL;
    TCADB *adb = openadb(dbname);
    PyObject* pDict = PyDict_New();
    if(!tcadbiterinit(adb)){
        return NULL;
    }
    int ksiz;
    char *kbuf;
    while((kbuf = tcadbiternext(adb, &ksiz)) != NULL){
        int vsiz;
        char *vbuf = tcadbget(adb, kbuf, ksiz, &vsiz);
        PyDict_SetItemString(pDict,kbuf,Py_BuildValue("s",vbuf));
        tcfree(vbuf);
        tcfree(kbuf);
    }
    closeadb(adb);
    return Py_BuildValue("O",pDict);
}

static PyObject *
search(PyObject *self, PyObject *args){
    TCRDB *rdb;
    int ecode, i, rsiz;
    const char *rbuf, *name;
    TCMAP *cols;
    RDBQRY *qry;
    TCLIST *res;

    const char *host;
    const int *port;
    const char *sfield;
    const char *stext;
    const int *spage;
    const int *epage;
    const int *is_fulltext;
    PyObject* pDict = PyDict_New();
    PyObject* pList = PyList_New(0);

    if (!PyArg_ParseTuple(args,"sissiii",&host,&port,&sfield, \
                            &stext,&spage,&epage,&is_fulltext))
        return NULL;

    rdb = tcrdbnew();
    
    /* connect to the server */
    if(!tcrdbopen(rdb, host, port)){
        ecode = tcrdbecode(rdb);
        fprintf(stderr, "open error: %s\n", tcrdberrmsg(ecode));
    }
    qry = tcrdbqrynew(rdb);
    if(is_fulltext)
        tcrdbqryaddcond(qry, sfield, RDBQCFTSPH, stext);
    else
        tcrdbqryaddcond(qry, sfield, RDBQCSTREQ, stext);
    // tcrdbqryaddcond(qry, "savedate", TDBQOSTRDESC);
    tcrdbqrysetlimit(qry, spage, epage);
    res = tcrdbqrysearch(qry);
    for(i = 0; i < tclistnum(res); i++){
        rbuf = tclistval(res, i, &rsiz);
        cols = tcrdbtblget(rdb, rbuf, rsiz);
        if(cols){
          tcmapiterinit(cols);
          PyDict_SetItemString(pDict, "kid", Py_BuildValue("s",rbuf));
          while((name = tcmapiternext2(cols)) != NULL){
              PyDict_SetItemString(pDict, name, Py_BuildValue("s", tcmapget2(cols, name)));
          }
          PyList_Append(pList,pDict);
          pDict = PyDict_New();
          tcmapdel(cols);
        }
    }
    tclistdel(res);
    tcrdbqrydel(qry);

    if(!tcrdbclose(rdb)){
        ecode = tcrdbecode(rdb);
        fprintf(stderr, "close error: %s\n", tcrdberrmsg(ecode));
    }

    tcrdbdel(rdb);

    return Py_BuildValue("O",pList);
}

PyMethodDef methods[] = {
  {"create", create, METH_VARARGS},
  {"put", put, METH_VARARGS},
  {"put2", put2, METH_VARARGS},
  {"put3", put3, METH_VARARGS},
  {"put4", put4, METH_VARARGS},
  {"get", get, METH_VARARGS},
  {"out", out, METH_VARARGS},
  {"list", list, METH_VARARGS},
  {"list2", list2, METH_VARARGS},
  {"search", search, METH_VARARGS},
  // {"get2", get2, METH_VARARGS},
  {NULL, NULL},
};

void initpycabinet(){
    PyObject* m;
    m = Py_InitModule("pycabinet", methods);
}
