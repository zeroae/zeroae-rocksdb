%include "c.i"
%rocksdb_module(directors="1") comparator;
%rocksdb_strip_and_keep_only(comparator);

// Typemaps
%cstring_director_input_binary(const char* a, size_t alen);
%cstring_director_input_binary(const char* b, size_t blen);

// Include the Comparator Class
%rename("%s") Comparator;
%rename("%s") Comparator::~Comparator;
%rename("%s") Comparator::compare;
%rename("%s") Comparator::name;

// Director class
%feature("director") Comparator;
%inline %{
struct Comparator {
  virtual ~Comparator() {}
  virtual const char* name() = 0;
  virtual int compare(const char* a, size_t alen, const char* b, size_t blen) = 0;
};
%}

%{
  // TODO: I think these functions are redundant...
  static void destructor_cb(void* self) {
    delete static_cast<Comparator*>(self);
  }
  static const char* name_cb(void* self) {
    return static_cast<Comparator*>(self)->name();
  }
  static int compare_cb(void* self, const char* a, size_t alen, const char* b, size_t blen) {
    return static_cast<Comparator*>(self)->compare(a, alen, b, blen);
  }
%}

// Override the create function
%ignore "rocksdb_comparator_create";
%rename("create") wrap_rocksdb_comparator_create;
%inline %{
  rocksdb_comparator_t* wrap_rocksdb_comparator_create(Comparator* comparator) {
    return rocksdb_comparator_create(comparator,
        &destructor_cb, &compare_cb, &name_cb
    );
  }
%}

// Constructor/Destructor
%newobject create;
%delobject destroy;

%inline %{
  const char* rocksdb_comparator_test_name_cb(Comparator* comparator) {
    return name_cb(comparator);
  }
  const int rocksdb_comparator_test_compare_cb(Comparator* comparator,
    const char* a, size_t alen, const char* b, size_t blen) {
    return compare_cb(comparator, a, alen, b, blen);
  }
%}

ROCKSDB_MODULE_FOOTER()
