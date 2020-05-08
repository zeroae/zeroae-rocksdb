import pytest
from zeroae.rocksdb.c import *


@pytest.fixture()
def rocksdb_backend_engine_dir(tmp_path_factory):
    return str(tmp_path_factory.mktemp("db-backup", numbered=True))


@pytest.fixture()
def rocksdb_backup_engine(rocksdb_options, rocksdb_backend_engine_dir):
    options.set_create_if_missing(rocksdb_options, 1)
    rv = backup_engine.open(rocksdb_options, rocksdb_backend_engine_dir)
    yield rv
    backup_engine.close(rv)


@pytest.fixture
def rocksdb_block_based_table_options():
    rv = block_based_options.create()
    yield rv
    block_based_options.destroy(rv)


@pytest.fixture
def rocksdb_cache_lru():
    rv = cache.create_lru(1024)
    yield rv
    cache.destroy(rv)


@pytest.fixture
def rocksdb_compactionfilterfactory_mock():
    from zeroae.rocksdb.c.compactionfilterfactory import CompactionFilterFactory

    class MyCompactionFilterFactory(CompactionFilterFactory):
        def __init__(self):
            super().__init__()

        def name(self):
            return "MyCompactionFilterFactory"

        def create_compaction_filter(self, context):
            return None

    return MyCompactionFilterFactory()


@pytest.fixture
def rocksdb_compactionfilterfactory_f(rocksdb_compactionfilterfactory_mock):
    rv = compactionfilterfactory.create(rocksdb_compactionfilterfactory_mock.__disown__())
    yield rv
    compactionfilterfactory.destroy(rv)


@pytest.fixture
def rocksdb_compactoptions():
    rv = compactoptions.create()
    yield rv
    compactoptions.destroy(rv)


@pytest.fixture()
def rocksdb_comparator_mock():
    from zeroae.rocksdb.c.comparator import Comparator

    class MyComparator(Comparator):
        def __init__(self):
            super().__init__()

        def compare(self, a, b):
            print(f"compare {a} with {b}")
            return -1 if a < b else 0 if a == b else 1

        def name(self):
            return "MyComparator"

    return MyComparator()


@pytest.fixture()
def rocksdb_comparator_f(rocksdb_comparator_mock):
    rv = comparator.create(rocksdb_comparator_mock.__disown__())
    yield rv
    comparator.destroy(rv)


@pytest.fixture
def rocksdb_cuckoo_table_options():
    rv = cuckoo_options.create()
    yield rv
    cuckoo_options.destroy(rv)


@pytest.fixture()
def rocksdb_db_dir(tmp_path_factory):
    return str(tmp_path_factory.mktemp("db", numbered=1))


@pytest.fixture()
def rocksdb_db(rocksdb_options, rocksdb_db_dir):
    options.set_create_if_missing(rocksdb_options, 1)
    rv = db.open(rocksdb_options, rocksdb_db_dir)
    yield rv
    db.close(rv)


@pytest.fixture
def rocksdb_dbpath(tmp_path):
    rv = dbpath.create(str(tmp_path), 10)
    yield rv
    dbpath.destroy(rv)


@pytest.fixture(params=[env.create_default,
                        env.create_mem])
def rocksdb_env(request):
    rv = request.param()
    yield rv
    env.destroy(rv)


@pytest.fixture
def rocksdb_envoptions():
    rv = envoptions.create()
    yield rv
    envoptions.destroy(rv)


@pytest.fixture
def rocksdb_fifo_compaction_options():
    rv = fifo_compaction_options.create()
    yield rv
    fifo_compaction_options.destroy(rv)


@pytest.fixture
def rocksdb_flushoptions():
    rv = flushoptions.create()
    yield rv
    flushoptions.destroy(rv)


@pytest.fixture
def rocksdb_ingestexternalfileoptions():
    rv = ingestexternalfileoptions.create()
    yield rv
    ingestexternalfileoptions.destroy(rv)


@pytest.fixture
def rocksdb_memory_consumers():
    rv = memory_consumers.create()
    yield rv
    memory_consumers.destroy(rv)


@pytest.fixture
def rocksdb_otxn_options():
    rv = optimistictransaction_options.create()
    yield rv
    optimistictransaction_options.destroy(rv)


@pytest.fixture()
def rocksdb_otxn_db_dir(tmp_path_factory):
    return str(tmp_path_factory.mktemp("otxdb", numbered=1))


@pytest.fixture()
def rocksdb_otxn_db(rocksdb_options, rocksdb_otxn_db_dir):
    options.set_create_if_missing(rocksdb_options, 1)
    rv = optimistictransactiondb.open(rocksdb_options, rocksdb_otxn_db_dir)
    yield rv
    optimistictransactiondb.close(rv)


@pytest.fixture
def rocksdb_options():
    rv = options.create()
    yield rv
    options.destroy(rv)


@pytest.fixture
def rocksdb_perfcontext():
    rv = perfcontext.create()
    yield rv
    perfcontext.destroy(rv)


@pytest.fixture
def rocksdb_ratelimiter():
    rv = ratelimiter.create(1024, 1000, 1)
    yield rv
    ratelimiter.destroy(rv)


@pytest.fixture
def rocksdb_readoptions():
    rv = readoptions.create()
    yield rv
    readoptions.destroy(rv)


@pytest.fixture
def rocksdb_restore_options():
    rv = restore_options.create()
    yield rv
    restore_options.destroy(rv)


@pytest.fixture()
def rocksdb_sstfilewriter_file(tmp_path_factory):
    return str(tmp_path_factory.mktemp("sstfw", numbered=1)/"file.sst")


@pytest.fixture(params=["default", "py_comp"])
def rocksdb_sstfilewriter(request, rocksdb_envoptions, rocksdb_options, rocksdb_comparator_f):
    if request.param == "py_comp":
        options.set_comparator(rocksdb_options, rocksdb_comparator_f)
    rv = sstfilewriter.create(rocksdb_envoptions, rocksdb_options)
    yield rv
    sstfilewriter.destroy(rv)


@pytest.fixture
def rocksdb_transaction_options():
    rv = transaction_options.create()
    yield rv
    transaction_options.destroy(rv)


@pytest.fixture()
def rocksdb_txn_db_dir(tmp_path_factory):
    return str(tmp_path_factory.mktemp("txdb", numbered=1))


@pytest.fixture()
def rocksdb_txn_db(rocksdb_options, rocksdb_transactiondb_options, rocksdb_txn_db_dir):
    options.set_create_if_missing(rocksdb_options, 1)
    rv = transactiondb.open(rocksdb_options, rocksdb_transactiondb_options, rocksdb_txn_db_dir)
    yield rv
    transactiondb.close(rv)


@pytest.fixture
def rocksdb_transactiondb_options():
    rv = transactiondb_options.create()
    yield rv
    transactiondb_options.destroy(rv)


@pytest.fixture
def rocksdb_universal_compaction_options():
    rv = universal_compaction_options.create()
    yield rv
    universal_compaction_options.destroy(rv)


@pytest.fixture
def rocksdb_writebatch():
    rv = writebatch.create()
    yield rv
    writebatch.destroy(rv)


@pytest.fixture
def rocksdb_writebatch_wi():
    rv = writebatch_wi.create(1024, 0)
    yield rv
    writebatch_wi.destroy(rv)


@pytest.fixture
def rocksdb_writeoptions():
    rv = writeoptions.create()
    yield rv
    writeoptions.destroy(rv)
