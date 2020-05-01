%include "c.i"
ROCKSDB_MODULE_HEADER(transactiondb, "zeroae.rocksdb.c")

%rename("$ignore", regexmatch$name="^rocksdb_transactiondb_options_") "";

%newobject open;
%newobject open_column_families;
%delobject close;

%newobject create_snapshot;
%newobject create_column_family;

%rename("begin_transaction") "rocksdb_transaction_begin";
%newobject begin_transaction;

ROCKSDB_MODULE_FOOTER()
