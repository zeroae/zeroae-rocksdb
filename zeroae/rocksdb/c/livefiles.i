%include "c.i"
ROCKSDB_MODULE_HEADER(livefiles)

%delobject destroy;

%cstring_output_allocate_size_keep_null(const char **rv, size_t* rvlen,);
%wrap_rv(smallestkey, (rocksdb_livefiles_t* t, int index, const char** rv, size_t* rvlen),
         rocksdb_livefiles_smallestkey, (t, index, rvlen))
%wrap_rv(largestkey, (rocksdb_livefiles_t* t, int index, const char** rv, size_t* rvlen),
          rocksdb_livefiles_largestkey, (t, index, rvlen))

ROCKSDB_MODULE_FOOTER()
