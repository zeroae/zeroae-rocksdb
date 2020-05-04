import pytest

from zeroae.rocksdb.c import approximate_memory_usage, memory_consumers


@pytest.fixture
def db_consumer(rocksdb_db, rocksdb_memory_consumers):
    memory_consumers.add_db(rocksdb_memory_consumers, rocksdb_db)
    yield rocksdb_memory_consumers


@pytest.fixture
def amu(db_consumer):
    rv = approximate_memory_usage.create(db_consumer)
    yield rv
    approximate_memory_usage.destroy(rv)


def test_fixture(amu):
    assert amu is not None


def test_get_mem_table_total(amu):
    total = approximate_memory_usage.get_mem_table_total(amu)
    assert total == pytest.approx(704, 704/10)


def test_get_mem_table_unflushed(amu):
    unflushed = approximate_memory_usage.get_mem_table_unflushed(amu)
    assert unflushed == pytest.approx(704, 704/10)


def test_get_mem_table_readers_total(amu):
    readers = approximate_memory_usage.get_mem_table_readers_total(amu)
    assert readers == 0


def test_get_cache_total(amu):
    cache = approximate_memory_usage.get_cache_total(amu)
    assert cache == 0
