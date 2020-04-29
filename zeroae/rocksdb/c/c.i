%define ROCKSDB_MODULE(name_prefix, ...)
%module(## __VA_ARGS__) name_prefix
%{
#define SWIG_FILE_WITH_INIT
#include <rocksdb/c.h>
%}

%include "stdint.i"
// Ignore all functions that dont' start with rocksdb_block_based_table_options_
%rename("$ignore", notregexmatch$name="^rocksdb_" #name_prefix "_") "";

// Strip rocksdb_options_ from function names
%rename("%(strip:[rocksdb_" #name_prefix "_])s", regexmatch$name="^rocksdb_" #name_prefix "_") "";

// Constructor/Destructor for rocksdb_block_based_table_options_t
%newobject create;
%delobject destroy;

%include <rocksdb/c.h>
%enddef
