import pytest

from zeroae.rocksdb.c import sstfilewriter


@pytest.skip(reason="GH-64")
def test_create_destroy(rocksdb_envoptions, rocksdb_options):
    rv = sstfilewriter.create(rocksdb_envoptions, rocksdb_options)
    assert rv is not None
    sstfilewriter.destroy(rv)


@pytest.mark.xfail
def test_create_with_comparator(rocksdb_envoptions, rocksdb_options):
    assert False


@pytest.mark.xfail
def test_open():
    assert False


@pytest.mark.xfail
def test_add():
    assert False


@pytest.mark.xfail
def test_put():
    assert False


@pytest.mark.xfail
def test_merge():
    assert False


@pytest.mark.xfail
def test_delete():
    assert False


@pytest.mark.xfail
def test_finish():
    assert False


@pytest.mark.xfail
def test_file_size():
    assert False

