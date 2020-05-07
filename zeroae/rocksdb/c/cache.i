%include "c.i"
ROCKSDB_MODULE_HEADER(cache)

%newobject create_lru;
%delobject destroy;

ROCKSDB_MODULE_FOOTER()
