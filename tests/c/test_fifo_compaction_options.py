import zeroae.rocksdb.c.fifo_compaction_options as fco


def test_create_destroy():
    opt = fco.create()
    assert opt is not None
    fco.destroy(opt)


def test_set_max_table_files_size(rocksdb_fifo_compaction_options):
    fco.set_max_table_files_size(rocksdb_fifo_compaction_options, 1024)

