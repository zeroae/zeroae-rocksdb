%include "c.i"
ROCKSDB_MODULE_HEADER(cache, package="zeroae.rocksdb.c")

%newobject create_lru;
%delobject destroy;

ROCKSDB_MODULE_FOOTER()
