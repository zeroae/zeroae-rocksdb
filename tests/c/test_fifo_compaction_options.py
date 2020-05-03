import pytest

import zeroae.rocksdb.c.fifo_compaction_options as fco


def test_fixture(rocksdb_fifo_compaction_options):
    assert rocksdb_fifo_compaction_options is not None


def test_set_max_table_files_size(rocksdb_fifo_compaction_options):
    fco.set_max_table_files_size(rocksdb_fifo_compaction_options, 1024)

    with pytest.raises(OverflowError):
        fco.set_max_table_files_size(rocksdb_fifo_compaction_options, -1)

