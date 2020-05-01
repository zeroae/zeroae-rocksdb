%include "c.i"
ROCKSDB_MODULE_HEADER(sstfilewriter, package="zeroae.rocksdb.c")

%newobject create;
%newobject create_with_comparator;
%delobject destroy;

%apply (const char *STRING, size_t LENGTH) {
    (const char* key, size_t keylen),
    (const char* val, size_t vallen)
}

ROCKSDB_MODULE_FOOTER()
