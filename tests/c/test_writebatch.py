import pytest

from zeroae.rocksdb.c import writebatch, writebatch_wi


def test_create_destroy():
    rv = writebatch.create()
    assert rv is not None
    writebatch.destroy(rv)


def test_create_from():
    rv = writebatch.create_from("hello")
    assert rv is not None
    writebatch.destroy(rv)


def test_delete_range(rocksdb_writebatch):
    writebatch.delete_range(rocksdb_writebatch, "aaa", "zzz")


@pytest.mark.xfail
def test_delete_range_cf(rocksdb_writebatch):
    assert False


@pytest.mark.xfail
def test_delete_rangev(rocksdb_writebatch):
    assert False


@pytest.mark.xfail
def test_delete_rangev_cf(rocksdb_writebatch):
    assert False


@pytest.mark.xfail
def test_pop_save_point(rocksdb_writebatch):
    assert False
