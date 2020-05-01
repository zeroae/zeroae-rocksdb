%include "c.i"
ROCKSDB_MODULE_HEADER(transaction, "zeroae.rocksdb.c")

%delobject destroy;

// should be freed with rocksdb_free
%newobject get_snapshot;

%newobject create_iterator;
%newobject create_iterator_cf;

ROCKSDB_MODULE_FOOTER()
