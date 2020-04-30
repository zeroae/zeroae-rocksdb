from zeroae.rocksdb.c import optimistictransaction_options


def test_create():
    rv = optimistictransaction_options.create()
    assert rv is not None
    optimistictransaction_options.destroy(rv)


def test_set_set_snapshot(rocksdb_optimistictransaction_options):
    optimistictransaction_options.set_set_snapshot(rocksdb_optimistictransaction_options, 0)
    optimistictransaction_options.set_set_snapshot(rocksdb_optimistictransaction_options, 1)
