%module(package="zeroae.rocksdb.c") block_based_table_options
%{
#define SWIG_FILE_WITH_INIT
#include <rocksdb/c.h>
%}

%include "stdint.i"
// Ignore all functions that dont' start with rocksdb_block_based_table_options_
%rename("$ignore", notregexmatch$name="^rocksdb_block_based_options_") "";

// Strip rocksdb_options_ from function names
%rename("%(strip:[rocksdb_block_based_options_])s", regexmatch$name="^rocksdb_block_based_options_") "";

// Constructor/Destructor for rocksdb_block_based_table_options_t
%newobject create;
%delobject destroy;

%include <rocksdb/c.h>
