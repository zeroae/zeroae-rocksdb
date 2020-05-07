%include "c.i"
ROCKSDB_MODULE_HEADER(sstfilewriter)

// Deprecated upstream (at C++ API level)
%ignore rocksdb_sstfilewriter_create_with_comparator;
%ignore rocksdb_sstfilewriter_add;

%newobject create;
%delobject destroy;

%cstring_input_binary(const char* key, size_t keylen);
%cstring_input_binary(const char* val, size_t vallen);
%apply (uint64_t *OUTPUT) { uint64_t* file_size }

ROCKSDB_MODULE_FOOTER()
