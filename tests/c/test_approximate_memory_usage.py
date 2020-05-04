import pytest

from zeroae.rocksdb.c import approximate_memory_usage, memory_consumers


@pytest.fixture
def db_consumer(rocksdb_memory_consumers, rocksdb_db):
    memory_consumers.add_db(rocksdb_memory_consumers, rocksdb_db)
    yield rocksdb_memory_consumers


@pytest.fixture
def lru_consumer(rocksdb_memory_consumers, rocksdb_cache_lru):
    memory_consumers.add_cache(rocksdb_memory_consumers, rocksdb_cache_lru)
    yield rocksdb_memory_consumers


@pytest.fixture(params=["db", "lru"])
def consumers(request, db_consumer, lru_consumer):
    if "db" == request.param:
        yield db_consumer
    if "lru" == request.param:
        yield lru_consumer


@pytest.fixture
def amu(consumers):
    rv = approximate_memory_usage.create(consumers)
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
