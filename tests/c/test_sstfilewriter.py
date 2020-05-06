import pytest

from zeroae.rocksdb.c import sstfilewriter as sstfw

@pytest.fixture
def sstfw_f(rocksdb_sstfilewriter, rocksdb_sstfilewriter_file):
    sstfw.open(rocksdb_sstfilewriter, rocksdb_sstfilewriter_file)
    yield rocksdb_sstfilewriter
    sstfw.finish(rocksdb_sstfilewriter)


def test_fixture(rocksdb_sstfilewriter):
    assert sstfw_f is not None


@pytest.mark.xfail
def test_create_with_comparator(rocksdb_envoptions, rocksdb_options):
    assert False


def test_add(sstfw_f):
    sstfw.add(sstfw_f, "key0", "val")
    sstfw.add(sstfw_f, "key1", "val")


def test_put(sstfw_f):
    sstfw.put(sstfw_f, "key", "val")


@pytest.mark.skip
def test_merge(sstfw_f):
    assert False


def test_delete(sstfw_f):
    sstfw.add(sstfw_f, "key0", "val")
    sstfw.delete(sstfw_f, "key1")


def test_file_size(rocksdb_sstfilewriter, rocksdb_sstfilewriter_file):
    assert sstfw.file_size(rocksdb_sstfilewriter) == 0

    sstfw.open(rocksdb_sstfilewriter, rocksdb_sstfilewriter_file)
    sstfw.add(rocksdb_sstfilewriter, "key", "val")
    sstfw.finish(rocksdb_sstfilewriter)

    assert sstfw.file_size(rocksdb_sstfilewriter) == pytest.approx(821, 8)
