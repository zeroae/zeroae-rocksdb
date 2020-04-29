from zeroae.rocksdb.c import options


def test_create_destroy():
    opt = options.create()
    assert opt is not None
    options.destroy(opt)


def test_increase_parallelism(rocksdb_options):
    options.increase_parallelism(rocksdb_options, 2)


def test_optimize_for_point_lookup(rocksdb_options):
    options.optimize_for_point_lookup(rocksdb_options, 10)
