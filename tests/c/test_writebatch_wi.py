import pytest

from zeroae.rocksdb.c import writebatch_wi


def test_create():
    rv = writebatch_wi.create(1024, 0)
    assert rv is not None
    writebatch_wi.destroy(rv)


@pytest.mark.xfail
def test_get_from_batch(rocksdb_writebatch_wi):
    assert False


@pytest.mark.xfail
def test_get_from_batch_cf(rocksdb_writebatch_wi):
    assert False


@pytest.mark.xfail
def test_get_from_batch_and_db(rocksdb_writebatch_wi):
    assert False


@pytest.mark.xfail
def test_get_from_batch_and_db_cf(rocksdb_writebatch_wi):
    assert False


@pytest.mark.xfail
def test_create_iterator_with_base(rocksdb_writebatch_wi):
    assert False


@pytest.mark.xfail
def test_create_iterator_with_base_cf(rocksdb_writebatch_wi):
    assert False
