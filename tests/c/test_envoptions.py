from zeroae.rocksdb.c import envoptions


def test_create():
    opt = envoptions.create()
    assert opt is not None
    envoptions.destroy(opt)
