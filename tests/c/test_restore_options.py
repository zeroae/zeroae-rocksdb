from zeroae.rocksdb.c import restore_options


def test_fixture(rocksdb_restore_options):
    assert rocksdb_restore_options is not None


def test_set_keep_log_files(rocksdb_restore_options):
    restore_options.set_keep_log_files(rocksdb_restore_options, 1)
