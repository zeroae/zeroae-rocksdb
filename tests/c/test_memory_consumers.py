import pytest

from zeroae.rocksdb.c import memory_consumers


def test_fixture(rocksdb_memory_consumers):
    assert rocksdb_memory_consumers is not None


@pytest.mark.xfail
def test_add_db(rocksdb_memory_consumers):
    assert False


def test_add_cache(rocksdb_memory_consumers, rocksdb_cache_lru):
    memory_consumers.add_cache(rocksdb_memory_consumers, rocksdb_cache_lru)
