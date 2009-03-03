#include <dystopia.h>
#include <stdlib.h>
#include <stdbool.h>
#include <stdint.h>

int main (int argc, char const *argv[]){
    TCIDB *idb;
    int ecode, rnum, i;
    uint64_t *result;
    char *text;

    idb = tcidbnew();
    
    if(!tcidbopen(idb, "khufu", IDBOWRITER | IDBOCREAT)){
        ecode = tcidbecode(idb);
        fprintf(stderr, "open error: %s\n", tcidberrmsg(ecode));
    }
    
    /* search records */
    result = tcidbsearch2(idb, "严旭", &rnum);
    if(result){
        for(i = 0; i < rnum; i++){
            text = tcidbget(idb, result[i]);
            if(text){
                printf("%d\t%s\n", (int)result[i], text);
                free(text);
            }
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

    tcidbdel(idb);

    return 0;
}
