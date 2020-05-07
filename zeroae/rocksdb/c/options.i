%include "c.i"
ROCKSDB_MODULE_HEADER(options)

ROCKSDB_INCLUDE_FUNCTION(get_options_from_string)

// Constructor/Destructor for rocksdb_options_t
%newobject create;
%delobject destroy;

// malloc()-ed return values
%newobject statistics_get_string;

ROCKSDB_MODULE_FOOTER()
