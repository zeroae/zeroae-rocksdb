%include "c.i"
ROCKSDB_MODULE_HEADER(transactiondb)

%rename("$ignore", regexmatch$name="^rocksdb_transactiondb_options_") "";

// Typemaps
%cstring_output_allocate_size_keep_null(char **rv, size_t* rvlen, rocksdb_free(*$1));
%cstring_input_binary(const char* key, size_t keylen);
%cstring_input_binary(const char* key, size_t klen);
%cstring_input_binary(const char* val, size_t vlen);
%cstring_input_binary(const char* val, size_t vallen);

%newobject open;
%newobject open_column_families;
%delobject close;

%newobject create_snapshot;
%newobject create_column_family;

%rename("begin_transaction") "rocksdb_transaction_begin";
%newobject begin_transaction;

// Wrap functions with return values
%wrap_rv(get, (rocksdb_transactiondb_t* txn_db, const rocksdb_readoptions_t* options,
               const char* key, size_t keylen,
               char** rv, size_t* rvlen,
               char** errptr),
         rocksdb_transactiondb_get, (txn_db, options, key, keylen, rvlen, errptr))
%wrap_rv(get_cf, (rocksdb_transactiondb_t* db, const rocksdb_readoptions_t* options,
                  rocksdb_column_family_handle_t* column_family,
                  const char* key, size_t keylen,
                  char** rv, size_t* rvlen,
                  char** errptr),
         rocksdb_transactiondb_get_cf, (db, options, column_family, key, keylen, rvlen, errptr))
ROCKSDB_MODULE_FOOTER()
