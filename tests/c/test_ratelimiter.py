from zeroae.rocksdb.c import ratelimiter


def test_fixture(rocksdb_ratelimiter):
    assert rocksdb_ratelimiter is not None


