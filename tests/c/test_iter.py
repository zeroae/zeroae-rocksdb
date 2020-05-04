import pytest

from zeroae.rocksdb.c import db
from zeroae.rocksdb.c import iter as rdb_iter


@pytest.fixture()
def local_db(rocksdb_db, rocksdb_writeoptions):
    for i in range(0, 10):
        db.put(rocksdb_db, rocksdb_writeoptions, f"k{i}", f"v{i}")
    yield rocksdb_db


@pytest.fixture
def forward_iterator(local_db, rocksdb_readoptions):
    rv = db.create_iterator(local_db, rocksdb_readoptions)
    rdb_iter.seek_to_first(rv)
    yield rv
    rdb_iter.destroy(rv)


@pytest.fixture
def backward_iterator(local_db, rocksdb_readoptions):
    rv = db.create_iterator(local_db, rocksdb_readoptions)
    rdb_iter.seek_to_last(rv)
    yield rv
    rdb_iter.destroy(rv)


def test_fixture(forward_iterator, backward_iterator):
    assert forward_iterator is not None
    assert backward_iterator is not None


def test_use_case(forward_iterator):
    def items(it, start_key, end_key):
        rdb_iter.seek(it, start_key)
        key, val = rdb_iter.key(it), rdb_iter.value(it)
        rdb_iter.get_error(it)
        while rdb_iter.valid(it) == 1 and key < end_key:
            yield key, val
            rdb_iter.next(it)
            key, val = rdb_iter.key(it), rdb_iter.value(it)
            rdb_iter.get_error(it)

    kv = {k: v for k, v in items(forward_iterator, "k2", "k8" ) }

    assert "k1" not in kv
    assert "k2" in kv
    assert "k8" not in kv


def test_key(forward_iterator, backward_iterator):
    assert rdb_iter.key(forward_iterator) == "k0"
    assert rdb_iter.key(backward_iterator) == "k9"


def test_value(forward_iterator, backward_iterator):
    assert rdb_iter.value(forward_iterator) == "v0"
    assert rdb_iter.value(backward_iterator) == "v9"


def test_valid(forward_iterator, backward_iterator):
    assert rdb_iter.valid(forward_iterator) == 1
    rdb_iter.seek_to_last(forward_iterator)
    rdb_iter.next(forward_iterator)
    assert rdb_iter.valid(forward_iterator) == 0

    assert rdb_iter.valid(backward_iterator) == 1
    rdb_iter.seek_to_first(backward_iterator)
    rdb_iter.prev(backward_iterator)
    assert rdb_iter.valid(backward_iterator) == 0


def test_seek(forward_iterator):
    rdb_iter.seek(forward_iterator, "k5")
    assert rdb_iter.key(forward_iterator) == "k5"


def test_seek_for_prev(backward_iterator):
    rdb_iter.seek_for_prev(backward_iterator, "k5")
    assert rdb_iter.key(backward_iterator) == "k5"


def test_next(forward_iterator):
    rdb_iter.next(forward_iterator)


def test_prev(backward_iterator):
    rdb_iter.prev(backward_iterator)


def test_get_error(forward_iterator, backward_iterator):
    assert rdb_iter.get_error(forward_iterator) is None
    rdb_iter.seek_to_last(forward_iterator)
    rdb_iter.next(forward_iterator)
    assert rdb_iter.get_error(forward_iterator) is None

