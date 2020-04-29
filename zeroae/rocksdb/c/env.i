%include "c.i"
ROCKSDB_MODULE_HEADER(env, package="zeroae.rocksdb.c")

%rename("create_default") "rocksdb_create_default_env";
%rename("create_mem") "rocksdb_create_mem_env";

%newobject create_default;
%newobject create_mem;
%delobject destroy;

ROCKSDB_MODULE_FOOTER()
