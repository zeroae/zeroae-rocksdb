%include "c.i"
%module("zeroae.rocksdb.c") snapshot;
%ignore "";
%rename("destroy") "rocksdb_free";
%delobject destroy;
ROCKSDB_MODULE_FOOTER()
