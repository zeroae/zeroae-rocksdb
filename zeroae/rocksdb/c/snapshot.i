%include "c.i"
%module(package="zeroae.rocksdb.c") snapshot;
%ignore "";
%rename("destroy") "rocksdb_free";
%delobject destroy;
ROCKSDB_MODULE_FOOTER()
