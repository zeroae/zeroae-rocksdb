%include "c.i"
ROCKSDB_MODULE_HEADER(filterpolicy)

%newobject create;
%newobject create_bloom;
%newobject create_bloom_full;
%delobject destroy;

ROCKSDB_MODULE_FOOTER()
