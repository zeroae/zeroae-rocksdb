from zeroae.rocksdb.c import flushoptions


def test_create():
    fopt = flushoptions.create()
    assert fopt is not None
    flushoptions.destroy(fopt)


def test_set_wait(rocksdb_flushoptions):
    flushoptions.set_wait(rocksdb_flushoptions, 0)
    flushoptions.set_wait(rocksdb_flushoptions, 1)
