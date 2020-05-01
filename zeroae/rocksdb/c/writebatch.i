%include "c.i"
ROCKSDB_MODULE_HEADER(writebatch, "zeroae.rocksdb.c")
%rename("$ignore", regexmatch$name="^rocksdb_writebatch_wi_") "";

// Typemaps
%apply (const char *STRING, size_t LENGTH) { (const char* rep, size_t size) }
%apply (const char *STRING, size_t LENGTH) { (const char* key, size_t klen) }
%apply (const char *STRING, size_t LENGTH) { (const char* key, size_t keylen) }
%apply (const char *STRING, size_t LENGTH) { (const char* val, size_t vlen) }
%apply (const char *STRING, size_t LENGTH) { (const char* blob, size_t len) }

%apply (const char *STRING, size_t LENGTH) { (const char* start_key, size_t start_key_len) }
%apply (const char *STRING, size_t LENGTH) { (const char* end_key, size_t end_key_len) }

%newobject create;
%delobject destroy;

ROCKSDB_MODULE_FOOTER()
