import zeroae.rocksdb.c.cache as cache


def test_fixture(rocksdb_cache_lru):
    assert rocksdb_cache_lru is not None


def test_set_capacity(rocksdb_cache_lru):
    cache.set_capacity(rocksdb_cache_lru, 2048)


def test_get_usage(rocksdb_cache_lru):
    usage = cache.get_usage(rocksdb_cache_lru)
    assert usage == 0


def test_get_pinned_usage(rocksdb_cache_lru):
    usage = cache.get_usage(rocksdb_cache_lru)
    assert usage == 0
