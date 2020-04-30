%include "c.i"
ROCKSDB_MODULE_HEADER(perfcontext, "zeroae.rocksdb.c")

%newobject create;
%delobject destroy;

%newobject report;

ROCKSDB_MODULE_FOOTER()
