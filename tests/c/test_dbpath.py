from zeroae.rocksdb.c import dbpath


def test_fixture(rocksdb_dbpath):
    assert rocksdb_dbpath is not None
