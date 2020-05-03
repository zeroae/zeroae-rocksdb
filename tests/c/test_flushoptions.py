from zeroae.rocksdb.c import flushoptions


def test_fixture(rocksdb_flushoptions):
    assert rocksdb_flushoptions is not None


def test_set_wait(rocksdb_flushoptions):
    flushoptions.set_wait(rocksdb_flushoptions, 0)
    flushoptions.set_wait(rocksdb_flushoptions, 1)
