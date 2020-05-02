%{
#define SWIG_FILE_WITH_INIT
#include <rocksdb/c.h>
%}

%include "stdint.i"

/*
 * %cstring_output_allocate_keep_null(TYPEMAP, RELEASE)
 *
 * This macro is used to return Character data that was
 * allocated with new or malloc. NULLs are returned as
 * well.
 *
 *     %cstring_output_allocate_keep_null(Char **outx, free($1));
 *     void foo(Char **outx) {
 *         *outx = (Char *) malloc(512);
 *         sprintf(outx,"blah blah\n");
 *     }
 */

%define %cstring_output_allocate_keep_null(TYPEMAP, RELEASE)
%typemap(in, noblock=1, numinputs=0) TYPEMAP ($*1_ltype temp=NULL) {
    $1 = &temp;
}
%typemap(freearg,match="in") TYPEMAP "";
%typemap(argout,noblock=1,fragment="SWIG_FromCharPtr") TYPEMAP {
    %append_output(SWIG_FromCharPtr(*$1));
    if (*$1) {
        RELEASE;
    }
}
%enddef


/**
 * This macro selects only the rocksdb functions that start
 * with the name_prefix (after having rocksdb_) removed.
 */
%define ROCKSDB_MODULE_HEADER(name_prefix, ...)
%module(## __VA_ARGS__) name_prefix
// Ignore all functions that dont' start with rocksdb_ ## name_prefix _
%rename("$ignore", notregexmatch$name="^rocksdb_" #name_prefix "_") "";
// Strip rocksdb_ ## name_prefix _ from function names
%rename("%(strip:[rocksdb_" #name_prefix "_])s", regexmatch$name="^rocksdb_" #name_prefix "_") "";
// Typemaps
%cstring_output_allocate_keep_null(char **errptr, rocksdb_free($1));
%enddef

/**
 * This macro ignores all functions starting with the name_prefix
 */
%define ROCKSDB_IGNORE_MODULE(name_prefix)
%rename("$ignore", regexmatch$name="^rocksdb_" #name_prefix "_") "";
%enddef

/**
 * This includes the function name
 */
%define ROCKSDB_INCLUDE_FUNCTION(name)
%rename(#name) "rocksdb_" #name;
%enddef

/**
 * This excludes the function name
 */
%define ROCKSDB_IGNORE_FUNCTION(name)
%ignore "rocksdb_" #name;
%enddef

/**
 * This macro includes the rocksdb/c.h file for rendering.
 */
%define ROCKSDB_MODULE_FOOTER(...)
%include <rocksdb/c.h>
%enddef


/**
 * This macro creates a basic SWIG Module assuming the
 * dataype constructor, destructor are called "create", and "destroy"
 * after all the renaming
 */
%define ROCKSDB_MODULE(name_prefix, ...)
ROCKSDB_MODULE_HEADER(name_prefix, ## __VA_ARGS__)

// Constructor/Destructor for rocksdb_block_based_table_options_t
%newobject create;
%delobject destroy;

ROCKSDB_MODULE_FOOTER()
%enddef
