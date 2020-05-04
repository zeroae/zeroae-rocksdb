%include "c.i"
ROCKSDB_MODULE_HEADER(pinnableslice, package="zeroae.rocksdb.c")

%delobject destroy;

%cstring_output_allocate_size_keep_null(const char **rv, size_t* rvlen,);
%wrap_rv(value, (rocksdb_pinnableslice_t* t, const char** rv, size_t* rvlen),
         rocksdb_pinnableslice_value, (t, rvlen))

ROCKSDB_MODULE_FOOTER()
