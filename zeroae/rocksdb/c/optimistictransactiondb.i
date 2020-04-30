%include "c.i"
ROCKSDB_MODULE_HEADER(optimistictransactiondb, "zeroae.rocksdb.c")

%newobject open
%newobject open_column_families
%delobject close

// How is this supposed to be handled?
// http://swig.org/Doc4.0/Python.html#Python_nn30
%newobject get_base_dn
%newobject close_base_dn

ROCKSDB_MODULE_FOOTER()
