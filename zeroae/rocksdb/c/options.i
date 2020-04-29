%module(package="zeroae.rocksdb.c") options
%{
#define SWIG_FILE_WITH_INIT
#include <rocksdb/c.h>
%}

%include "stdint.i"

// Ignore all functions that dont' start with rocksdb_options_
%rename("$ignore", notregexmatch$name="^rocksdb_options_") "";

// Strip rocksdb_options_ from function names
%rename("%(strip:[rocksdb_options_])s", regexmatch$name="^rocksdb_options_") "";

// Constructor/Destructor for rocksdb_options_t
%newobject create;
%delobject destroy;

// malloc()-ed return values
%newobject statistics_get_string;

%include <rocksdb/c.h>

