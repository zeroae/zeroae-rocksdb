import zeroae.rocksdb.c.cache as cache


def test_create_destroy_lru():
    c = cache.create_lru(1024)
    assert c is not None
    cache.destroy(c)


def test_set_capacity(rocksdb_cache_lru):
    cache.set_capacity(rocksdb_cache_lru, 2048)


def test_get_usage(rocksdb_cache_lru):
    usage = cache.get_usage(rocksdb_cache_lru)
    assert usage == 0


def test_get_pinned_usage(rocksdb_cache_lru):
    usage = cache.get_usage(rocksdb_cache_lru)
    assert usage == 0
