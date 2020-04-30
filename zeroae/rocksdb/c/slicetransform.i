%include "c.i"
ROCKSDB_MODULE_HEADER(slicetransform, "zeroae.rocksdb.c")
%newobject create;
%newobject create_fixed_prefix;
%newobject create_noop;
%delobject destroy;
ROCKSDB_MODULE_FOOTER()
