from zeroae.rocksdb.c import optimistictransaction_options


def test_fixture(rocksdb_optimistictransaction_options):
    assert rocksdb_optimistictransaction_options is not None


def test_set_set_snapshot(rocksdb_optimistictransaction_options):
    optimistictransaction_options.set_set_snapshot(rocksdb_optimistictransaction_options, 0)
    optimistictransaction_options.set_set_snapshot(rocksdb_optimistictransaction_options, 1)
