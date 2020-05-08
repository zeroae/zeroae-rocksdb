%{
#define SWIG_FILE_WITH_INIT
#include <rocksdb/c.h>

// TODO: This makes the interface non-reentrant
char* ERRMSG = NULL;
%}

%include "typemaps.i"
%include "stdint.i"
%include "cstring.i"
%include "exception.i"

/*
 * Convert errptr to an exception
 */
%typemap(in,noblock=1,numinputs=0) char** errptr {
  $1 = &ERRMSG;
}
%typemap(freearg,match="in") char** errptr "";
%typemap(argout,noblock=1) char** errptr {
  if (*$1) {
    SWIG_exception(SWIG_RuntimeError, *$1);
  }
}

/*
 * %cstring_director_input_binary(TYPEMAP, SIZE)
 *
 * This macro extends the %cstring_input_binary macro
 * with a typemap for `directorin`
 */
%define %cstring_director_input_binary(TYPEMAP, SIZE)
%cstring_input_binary(TYPEMAP, SIZE);
%typemap(directorin, noblock=1, numinputs=0, fragment="SWIG_FromCharPtrAndSize") (TYPEMAP, SIZE) {
    $input = SWIG_FromCharPtrAndSize($1, $2);
}
%enddef

/*
 * %cstring_output_allocate_keep_null(TYPEMAP, RELEASE)
 *
 * This macro replaces the argout typemap of %cstring_output_allocate
 * so it appends the return value even if it is NULL.
 */
%define %cstring_output_allocate_keep_null(TYPEMAP, RELEASE)
%cstring_output_allocate(TYPEMAP, RELEASE);
%typemap(argout,noblock=1,fragment="SWIG_FromCharPtr") TYPEMAP {
  %append_output(SWIG_FromCharPtr(*$1));
  if (*$1) {
      RELEASE;
  }
}
%enddef

/*
 * %cstring_output_allocate_size_keep_null(TYPEMAP, SIZE, RELEASE)
 *
 * This macro replaces the argout typemap of %cstring_output_allocate_size
 * so it appends the return value even if it is NULL.
 */
%define %cstring_output_allocate_size_keep_null(TYPEMAP, SIZE, RELEASE)
%cstring_output_allocate_size(TYPEMAP, SIZE, RELEASE);
%typemap(argout,noblock=1,fragment="SWIG_FromCharPtrAndSize")(TYPEMAP,SIZE) {
  %append_output(SWIG_FromCharPtrAndSize(*$1,*$2));
  if (*$1) {
    RELEASE;
  }
}
%enddef

/**
 * Wrap functions that return char* rv, size_t* rvlen
 */
%define %wrap_rv(NEW, NEW_SIG, OLD, OLD_ARGS)
%ignore OLD;
%rename(NEW) wrap_##OLD;
%inline %{
  void wrap_##OLD NEW_SIG {
    *rv = OLD OLD_ARGS;
  }
%}
%enddef

/**
 * %rocksdb_module(...)
 *
 * This macro creates a SWIG module with the package="zeroae.rocksdb.c", ...)
 */
%define %rocksdb_module(...)
%module(package="zeroae.rocksdb.c", ## __VA_ARGS__)
%enddef

/*
 * %rocksdb_strip_and_keep_only(PREFIX)
 *
 * This macro ignores all items that do not start with
 * rocksdb_$PREFIX, and strips rocksdb_$PREFIX from symbols
 */
%define %rocksdb_strip_and_keep_only(PREFIX)
%rename("$ignore", notregexmatch$name="^rocksdb_" #PREFIX "_") "";
%rename("%(strip:[rocksdb_" #PREFIX "_])s", regexmatch$name="^rocksdb_" #PREFIX "_") ""
%enddef

/**
 * This macro selects only the rocksdb functions that start
 * with the name_prefix (after having rocksdb_) removed.
 *
 *  - Ignore all functions that dont' start with rocksdb_ ## name_prefix _
 *  - Strip rocksdb_ ## name_prefix _ from function names
 */
%define ROCKSDB_MODULE_HEADER(name_prefix)
%module(package="zeroae.rocksdb.c") name_prefix;
%rocksdb_strip_and_keep_only(name_prefix);
%cstring_output_allocate_size_keep_null(char** rv, size_t* rvlen, rocksdb_free($1));
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
%define ROCKSDB_MODULE(name_prefix)
ROCKSDB_MODULE_HEADER(name_prefix)

// Constructor/Destructor for rocksdb_block_based_table_options_t
%newobject create;
%delobject destroy;

ROCKSDB_MODULE_FOOTER()
%enddef
