%include "c.i"
ROCKSDB_MODULE_HEADER(writebatch_wi)

// Typemaps
%apply (const char *STRING, size_t LENGTH) {
    (const char* key, size_t klen),
    (const char* key, size_t keylen),
    (const char* val, size_t vlen),
    (const char* blob, size_t len)
}

// Does not exist upstream
%ignore rocksdb_writebatch_wi_create_from;

// The following are not yet supported upstream
%ignore rocksdb_writebatch_wi_delete_range;
%ignore rocksdb_writebatch_wi_delete_range_cf;
%ignore rocksdb_writebatch_wi_delete_rangev;
%ignore rocksdb_writebatch_wi_delete_rangev_cf;


%newobject create;
%delobject destroy;

%newobject create_iterator_with_base;
%newobject create_iterator_with_base_cf;


ROCKSDB_MODULE_FOOTER()
