%include "c.i"
ROCKSDB_MODULE_HEADER(livefiles, package="zeroae.rocksdb.c")

// Constructor/Destructor for rocksdb_options_t
%delobject destroy;

// malloc()-ed return values
%newobject statistics_get_string;

ROCKSDB_MODULE_FOOTER()
