import pytest

from zeroae.rocksdb.c import sstfilewriter


def test_fixture(rocksdb_sstfilewriter):
    assert rocksdb_sstfilewriter is not None

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

