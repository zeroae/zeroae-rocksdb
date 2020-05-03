import zeroae.rocksdb.c.universal_compaction_options as uco


def test_fixture(rocksdb_universal_compaction_options):
    assert rocksdb_universal_compaction_options is not None


def test_set_size_ratio(rocksdb_universal_compaction_options):
    uco.set_size_ratio(rocksdb_universal_compaction_options, 1)


def test_set_min_merge_width(rocksdb_universal_compaction_options):
    uco.set_min_merge_width(rocksdb_universal_compaction_options, 1)


def test_set_max_merge_width(rocksdb_universal_compaction_options):
    uco.set_max_merge_width(rocksdb_universal_compaction_options, 10)


def test_set_max_size_amplification_percent(rocksdb_universal_compaction_options):
    uco.set_max_size_amplification_percent(rocksdb_universal_compaction_options, 10)


def test_set_compression_size_percent(rocksdb_universal_compaction_options):
    uco.set_compression_size_percent(rocksdb_universal_compaction_options, 10)


def test_set_stop_style(rocksdb_universal_compaction_options):
    uco.set_stop_style(rocksdb_universal_compaction_options, 0)

