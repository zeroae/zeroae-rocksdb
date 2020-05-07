%include "c.i"
ROCKSDB_MODULE_HEADER(backup_engine)

// backup_engine_info  is its own module
%rename("$ignore", regexmatch$name="^rocksdb_backup_engine_info_") "";

%newobject open;
%delobject close;

%newobject get_backup_info;

ROCKSDB_MODULE_FOOTER()
