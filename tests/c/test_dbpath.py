from zeroae.rocksdb.c import dbpath


def test_create(tmp_path):
    db = dbpath.create(str(tmp_path), 10)
    assert db is not None
    dbpath.destroy(db)
