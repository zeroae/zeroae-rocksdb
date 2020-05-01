%include "c.i"
ROCKSDB_MODULE_HEADER(writebatch_wi, "zeroae.rocksdb.c")


%newobject create;
%ignore create_from; // This function does not exist in the .so
%delobject destroy;

%newobject create_iterator_with_base;
%newobject create_iterator_with_base_cf;

// The following are not yet supported upstream
%ignore delete_range;
%ignore delete_range_cf;
%ignore delete_rangev;
%ignore delete_rangev_cf;

ROCKSDB_MODULE_FOOTER()
