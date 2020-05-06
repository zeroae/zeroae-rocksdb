%include "c.i"
ROCKSDB_MODULE_HEADER(sstfilewriter, package="zeroae.rocksdb.c")

%newobject create;
%newobject create_with_comparator;
%delobject destroy;

%cstring_input_binary(const char* key, size_t keylen);
%cstring_input_binary(const char* val, size_t vallen);
%apply (uint64_t *OUTPUT) { uint64_t* file_size }

ROCKSDB_MODULE_FOOTER()
