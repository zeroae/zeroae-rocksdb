from zeroae.rocksdb.c import compactoptions


def test_fixture(rocksdb_compactoptions):
    assert rocksdb_compactoptions is not None


def test_set_exclusive_manual_compaction(rocksdb_compactoptions):
    compactoptions.set_exclusive_manual_compaction(rocksdb_compactoptions, 0)
    compactoptions.set_exclusive_manual_compaction(rocksdb_compactoptions, 1)


def test_set_bottommost_level_compaction(rocksdb_compactoptions):
    compactoptions.set_bottommost_level_compaction(rocksdb_compactoptions, 0)
    compactoptions.set_bottommost_level_compaction(rocksdb_compactoptions, 1)


def test_set_change_level(rocksdb_compactoptions):
    compactoptions.set_change_level(rocksdb_compactoptions, 0)
    compactoptions.set_change_level(rocksdb_compactoptions, 1)


def test_set_target_level(rocksdb_compactoptions):
    compactoptions.set_target_level(rocksdb_compactoptions, 0)
    compactoptions.set_target_level(rocksdb_compactoptions, 10)
