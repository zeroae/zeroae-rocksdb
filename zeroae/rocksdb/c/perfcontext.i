%include "c.i"
ROCKSDB_MODULE_HEADER(perfcontext)

ROCKSDB_INCLUDE_FUNCTION(set_perf_level)

%newobject create;
%delobject destroy;

%newobject report;

ROCKSDB_MODULE_FOOTER()
