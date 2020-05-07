%include "c.i"
ROCKSDB_MODULE_HEADER(readoptions)

// Constructor/Destructor for rocksdb_readoptions
%newobject create;
%delobject destroy;

// Key input
%apply (const char *STRING, size_t LENGTH) { (const char* key, size_t keylen) };

// Function was deprecated
%ignore rocksdb_readoptions_set_managed;

ROCKSDB_MODULE_FOOTER()
