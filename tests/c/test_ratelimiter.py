from zeroae.rocksdb.c import ratelimiter


def test_create_destroy():
    rl = ratelimiter.create(1, 1, 1)
    assert rl is not None
    ratelimiter.destroy(rl)


