%include "c.i"
ROCKSDB_MODULE_HEADER(writebatch, "zeroae.rocksdb.c")
%rename("$ignore", regexmatch$name="^rocksdb_writebatch_wi_") "";

// Typemaps
%apply (const char *STRING, size_t LENGTH) {
    (const char* rep, size_t size),
    (const char* key, size_t klen),
    (const char* key, size_t keylen),
    (const char* val, size_t vlen),
    (const char* blob, size_t len),
    (const char* start_key, size_t start_key_len),
    (const char* end_key, size_t end_key_len)
}

%newobject create;
%delobject destroy;

ROCKSDB_MODULE_FOOTER()
