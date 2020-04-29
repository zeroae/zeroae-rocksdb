%include "c.i"
 ROCKSDB_MODULE_HEADER(options, package="zeroae.rocksdb.c")

// Constructor/Destructor for rocksdb_options_t
%newobject create;
%delobject destroy;

// malloc()-ed return values
%newobject statistics_get_string;

%include <rocksdb/c.h>
