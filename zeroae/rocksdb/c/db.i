%include "c.i"
%module(package="zeroae.rocksdb.c") db
%rename("%(strip:[rocksdb_])s", regexmatch$name="^rocksdb_") "";

//
// Ignore other modules
ROCKSDB_IGNORE_MODULE(approximate_memory_usage)
ROCKSDB_IGNORE_MODULE(backup_engine)
ROCKSDB_IGNORE_MODULE(block_based_options)
ROCKSDB_IGNORE_MODULE(cache)
ROCKSDB_IGNORE_MODULE(checkpoint_object)
ROCKSDB_INCLUDE_FUNCTION(checkpoint_object_create)
ROCKSDB_IGNORE_FUNCTION(checkpoint_create)
ROCKSDB_IGNORE_MODULE(compactionfilter)
ROCKSDB_IGNORE_MODULE(compactionfiltercontext)
ROCKSDB_IGNORE_MODULE(compactionfilterfactory)
ROCKSDB_IGNORE_MODULE(compactoptions)
ROCKSDB_IGNORE_MODULE(comparator)
ROCKSDB_IGNORE_MODULE(cuckoo_options)
ROCKSDB_IGNORE_MODULE(dbpath)
ROCKSDB_IGNORE_MODULE(env)
ROCKSDB_IGNORE_FUNCTION(create_default_env)
ROCKSDB_IGNORE_FUNCTION(create_mem_env)
ROCKSDB_IGNORE_MODULE(envoptions)
ROCKSDB_IGNORE_MODULE(fifo_compaction_options)
ROCKSDB_IGNORE_MODULE(filterpolicy)
ROCKSDB_IGNORE_MODULE(flushoptions)
ROCKSDB_IGNORE_MODULE(ingestexternalfileoptions)
ROCKSDB_IGNORE_MODULE(iter)
ROCKSDB_IGNORE_MODULE(livefiles)
ROCKSDB_IGNORE_MODULE(memory_consumers)
ROCKSDB_IGNORE_MODULE(mergeoperator)
ROCKSDB_IGNORE_MODULE(optimistictransaction_options)
ROCKSDB_IGNORE_MODULE(optimistictransaction)
ROCKSDB_IGNORE_MODULE(optimistictransactiondb)
ROCKSDB_IGNORE_MODULE(options)
ROCKSDB_IGNORE_FUNCTION(get_options_from_string)
ROCKSDB_IGNORE_MODULE(perfcontext)
ROCKSDB_IGNORE_FUNCTION(set_perf_level)
ROCKSDB_IGNORE_MODULE(pinnableslice)
ROCKSDB_IGNORE_MODULE(ratelimiter)
ROCKSDB_IGNORE_MODULE(readoptions)
ROCKSDB_IGNORE_MODULE(restore_options)
ROCKSDB_IGNORE_MODULE(slicetransform)
ROCKSDB_IGNORE_MODULE(sstfilewriter)
ROCKSDB_IGNORE_MODULE(transaction)
ROCKSDB_IGNORE_MODULE(transactiondb)
ROCKSDB_IGNORE_MODULE(universal_compaction_options)
ROCKSDB_IGNORE_MODULE(wal_iter)
ROCKSDB_IGNORE_MODULE(writebatch)
ROCKSDB_IGNORE_MODULE(writeoptions)

// Typemaps
%cstring_output_allocate_keep_null(char **errptr, rocksdb_free($1));
%cstring_output_allocate_size_keep_null(char** rv, size_t* rvlen, rocksdb_free($1));
%apply (const char *STRING, size_t LENGTH) {
    (const char* key, size_t keylen),
    (const char* val, size_t vallen),
    (const char* start_key, size_t start_key_len),
    (const char* limit_key, size_t limit_key_len)
}

// Memory Management
// rocksdb_t
%newobject open;
%newobject open_with_ttl;
%newobject open_for_read_only;
%newobject open_as_secondary;
%newobject open_column_families;
%newobject open_for_read_only_column_families;
%newobject open_as_secondary_column_families;
%delobject close;

// checkpoint_t
%newobject checkpoint_object_create;

// Column family
%newobject create_column_family;
%delobject column_family_handle_destroy;

// Iterator
%newobject create_iterator;
%newobject get_updates_since;
%newobject create_iterator_cf;

// snapshot
%newobject create_snapshot;

// global
%delobject free;


// Wrap functions with return values
%wrap_rv(get, (rocksdb_t* db, const rocksdb_readoptions_t* options, const char* key,
            size_t keylen, char** rv, size_t* rvlen, char** errptr),
      rocksdb_get, (db, options, key, keylen, rvlen, errptr))
%wrap_rv(get_cf, (rocksdb_t* db, const rocksdb_readoptions_t* options, rocksdb_column_family_handle_t* column_family,
                  const char* key, size_t keylen, char** rv, size_t* rvlen, char** errptr),
      rocksdb_get_cf, (db, options, column_family, key, keylen, rvlen, errptr))

ROCKSDB_MODULE_FOOTER()
