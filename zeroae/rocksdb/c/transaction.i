%include "c.i"
ROCKSDB_MODULE_HEADER(transaction, "zeroae.rocksdb.c")

%rename("$ignore", regexmatch$name="^rocksdb_transaction_options_") "";

// Typemaps
%cstring_output_allocate_size_keep_null(char **rv, size_t* rvlen, rocksdb_free(*$1));
%cstring_input_binary(const char* key, size_t klen);
%cstring_input_binary(const char* val, size_t vlen);

// Constructor/Destructors
%delobject destroy;

// should be freed with rocksdb_free
%newobject get_snapshot;

%newobject create_iterator;
%newobject create_iterator_cf;

// Wrap functions with return values
%wrap_rv(get, (rocksdb_transaction_t* txn, const rocksdb_readoptions_t* options,
               const char* key, size_t klen,
               char** rv, size_t* rvlen,
               char** errptr),
         rocksdb_transaction_get, (txn, options, key, klen, rvlen, errptr))
%wrap_rv(get_cf, (rocksdb_transaction_t* txn, const rocksdb_readoptions_t* options,
                  rocksdb_column_family_handle_t* column_family,
                  const char* key, size_t klen,
                  char** rv, size_t* rvlen,
                  char** errptr),
         rocksdb_transaction_get_cf, (txn, options, column_family, key, klen, rvlen, errptr))
ROCKSDB_MODULE_FOOTER()
