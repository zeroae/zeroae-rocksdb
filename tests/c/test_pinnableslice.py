import pytest

from zeroae.rocksdb.c import db as rdb
from zeroae.rocksdb.c import pinnableslice


@pytest.fixture
def db(rocksdb_db, rocksdb_writeoptions):
    rdb.put(rocksdb_db, rocksdb_writeoptions, "key", "value")
    yield rocksdb_db


@pytest.fixture
def slice(db, rocksdb_readoptions):
    rv = rdb.get_pinned(db, rocksdb_readoptions, "key")
    yield rv
    pinnableslice.destroy(rv)


def test_fixture(slice):
    assert slice is not None


def test_value(slice):
    rv = pinnableslice.value(slice)
    assert rv == "value"
