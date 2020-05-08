import pytest

from zeroae.rocksdb.c import sstfilewriter as sstfw


def test_fixture(rocksdb_sstfilewriter):
    assert rocksdb_sstfilewriter is not None


@pytest.fixture
def sstfw_f(rocksdb_sstfilewriter, rocksdb_sstfilewriter_file):
    sstfw.open(rocksdb_sstfilewriter, rocksdb_sstfilewriter_file)
    yield rocksdb_sstfilewriter
    sstfw.finish(rocksdb_sstfilewriter)


def test_put(sstfw_f):
    sstfw.put(sstfw_f, "key0", "val")
    sstfw.put(sstfw_f, "key1", "val")


@pytest.mark.skip
def test_merge(sstfw_f):
    assert False


def test_delete(sstfw_f):
    sstfw.put(sstfw_f, "key0", "val")
    sstfw.delete(sstfw_f, "key1")


def test_file_size(rocksdb_sstfilewriter, rocksdb_sstfilewriter_file):
    assert sstfw.file_size(rocksdb_sstfilewriter) == 0

    sstfw.open(rocksdb_sstfilewriter, rocksdb_sstfilewriter_file)
    sstfw.put(rocksdb_sstfilewriter, "key", "val")
    sstfw.finish(rocksdb_sstfilewriter)

    assert sstfw.file_size(rocksdb_sstfilewriter) == pytest.approx(821, 8)
