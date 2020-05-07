%include "c.i"
ROCKSDB_MODULE_HEADER(iter)

%delobject destroy;

%cstring_input_binary(const char* k, size_t klen);

%cstring_output_allocate_size_keep_null(const char **rv, size_t* rvlen, );
%wrap_rv(key,
         (rocksdb_iterator_t* t, const char** rv, size_t* rvlen),
         rocksdb_iter_key, (t, rvlen))
%wrap_rv(value,
         (rocksdb_iterator_t* t, const char** rv, size_t* rvlen),
         rocksdb_iter_value, (t, rvlen))

ROCKSDB_MODULE_FOOTER()
