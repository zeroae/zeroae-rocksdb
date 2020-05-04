from zeroae.rocksdb.c import optimistictransaction_options


def test_fixture(rocksdb_otxn_options):
    assert rocksdb_otxn_options is not None


def test_set_set_snapshot(rocksdb_otxn_options):
    optimistictransaction_options.set_set_snapshot(rocksdb_otxn_options, 0)
    optimistictransaction_options.set_set_snapshot(rocksdb_otxn_options, 1)
