from zeroae.rocksdb.c import writeoptions


def test_create_destroy():
    wopt = writeoptions.create()
    assert wopt is not None
    writeoptions.destroy(wopt)


def test_set_sync(rocksdb_writeoptions):
    writeoptions.set_sync(rocksdb_writeoptions, 0)
    writeoptions.set_sync(rocksdb_writeoptions, 1)


def test_disable_wal(rocksdb_writeoptions):
    writeoptions.disable_WAL(rocksdb_writeoptions, 1)


def test_set_ignore_missing_column_families(rocksdb_writeoptions):
    writeoptions.set_ignore_missing_column_families(rocksdb_writeoptions, 0)
    writeoptions.set_ignore_missing_column_families(rocksdb_writeoptions, 1)


def test_set_no_slowdown(rocksdb_writeoptions):
    writeoptions.set_no_slowdown(rocksdb_writeoptions, 0)
    writeoptions.set_no_slowdown(rocksdb_writeoptions, 1)


def test_set_low_pri(rocksdb_writeoptions):
    writeoptions.set_low_pri(rocksdb_writeoptions, 0)
    writeoptions.set_low_pri(rocksdb_writeoptions, 1)


def test_set_memtable_insert_hint_per_batch(rocksdb_writeoptions):
    writeoptions.set_memtable_insert_hint_per_batch(rocksdb_writeoptions, 0)
    writeoptions.set_memtable_insert_hint_per_batch(rocksdb_writeoptions, 1)
