%include "c.i"
ROCKSDB_MODULE_HEADER(iter, "zeroae.rocksdb.c")

%apply (const char *STRING, size_t LENGTH) { (const char* k, size_t klen) }

%delobject destroy;

ROCKSDB_MODULE_FOOTER()
