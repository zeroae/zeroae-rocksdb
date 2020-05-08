%include "c.i"
%rocksdb_module(directors="1") compactionfilterfactory;
%rocksdb_strip_and_keep_only(compactionfilterfactory);

// Include the CompactionFilterFactory Class
%rename("%s") CompactionFilterFactory;
%rename("%s") CompactionFilterFactory::~CompactionFilterFactory;
%rename("%s") CompactionFilterFactory::create_compaction_filter;
%rename("%s") CompactionFilterFactory::name;

// Director class
%feature("director") CompactionFilterFactory;
%inline %{
struct CompactionFilterFactory {
  virtual ~CompactionFilterFactory() {}
  virtual const char* name() = 0;
  virtual rocksdb_compactionfilter_t*
    create_compaction_filter(rocksdb_compactionfiltercontext_t* context) = 0;
};
%}

// Callbacks
%{
  // TODO: I think these are redundant
  static void destructor_cb(void* self) {
    delete static_cast<CompactionFilterFactory*>(self);
  }
  static const char* name_cb(void* self) {
    return static_cast<CompactionFilterFactory*>(self)->name();
  }
  static rocksdb_compactionfilter_t*
  create_compaction_filter_cb(void* self, rocksdb_compactionfiltercontext_t* context) {
    return static_cast<CompactionFilterFactory*>(self)->create_compaction_filter(context);
  }
%}

// Override the function
%ignore "rocksdb_compactionfilterfactory_create";
%rename("create") wrap_rocksdb_compactionfilterfactory_create;
%inline %{
  rocksdb_compactionfilterfactory_t*
  wrap_rocksdb_compactionfilterfactory_create(CompactionFilterFactory* factory) {
    return rocksdb_compactionfilterfactory_create(factory,
        &destructor_cb, &create_compaction_filter_cb, &name_cb
    );
  }
%}

// Constructor/Destructor
%newobject create;
%delobject destroy;

ROCKSDB_MODULE_FOOTER()
