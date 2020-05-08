from zeroae.rocksdb.c import comparator


def test_fixture(rocksdb_comparator_f):
    assert rocksdb_comparator_f is not None


def test_name(rocksdb_comparator_mock):
    assert comparator.test_name_cb(rocksdb_comparator_mock) == rocksdb_comparator_mock.name()


def test_comparator(rocksdb_comparator_mock):
    assert comparator.test_compare_cb(rocksdb_comparator_mock, "a", "b") == rocksdb_comparator_mock.compare("a", "b")
