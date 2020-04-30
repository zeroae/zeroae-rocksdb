from zeroae.rocksdb.c import restore_options


def test_create_destroy():
    opt = restore_options.create()
    assert opt is not None
    restore_options.destroy(opt)


def test_set_keep_log_files(rocksdb_restore_options):
    restore_options.set_keep_log_files(rocksdb_restore_options, 1)
