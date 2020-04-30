import pytest
from zeroae.rocksdb.c import (
    block_based_options, cuckoo_options, options, ratelimiter,
    universal_compaction_options, fifo_compaction_options, cache, env, dbpath, flushoptions, restore_options,
    compactoptions, writeoptions, readoptions, memory_consumers, perfcontext
)


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
def rocksdb_compactoptions():
    rv = compactoptions.create()
    yield rv
    compactoptions.destroy(rv)


@pytest.fixture
def rocksdb_cuckoo_table_options():
    rv = cuckoo_options.create()
    yield rv
    cuckoo_options.destroy(rv)


@pytest.fixture
def rocksdb_dbpath(tmp_path):
    db = dbpath.create(str(tmp_path), 10)
    assert db is not None
    dbpath.destroy(db)


@pytest.fixture(params=[env.create_default,
                        env.create_mem])
def rocksdb_env(request):
    rv = request.param()
    yield rv
    env.destroy(rv)


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
def rocksdb_memory_consumers():
    rv = memory_consumers.create()
    yield rv
    memory_consumers.destroy(rv)


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


@pytest.fixture
def rocksdb_universal_compaction_options():
    rv = universal_compaction_options.create()
    yield rv
    universal_compaction_options.destroy(rv)


@pytest.fixture
def rocksdb_writeoptions():
    rv = writeoptions.create()
    yield rv
    writeoptions.destroy(rv)
