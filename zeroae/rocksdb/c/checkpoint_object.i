%include "c.i"
ROCKSDB_MODULE_HEADER(checkpoint_object)

ROCKSDB_IGNORE_FUNCTION(checkpoint_object_create)
ROCKSDB_INCLUDE_FUNCTION(checkpoint_create)

%delobject destroy;

ROCKSDB_MODULE_FOOTER()
