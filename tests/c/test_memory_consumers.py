import pytest

from zeroae.rocksdb.c import memory_consumers


def test_create():
    rv = memory_consumers.create()
    assert rv is not None
    memory_consumers.destroy(rv)


@pytest.mark.xfail
def test_add_db(rocksdb_memory_consumers):
    assert False


def test_add_cache(rocksdb_memory_consumers, rocksdb_cache_lru):
    memory_consumers.add_cache(rocksdb_memory_consumers, rocksdb_cache_lru)
