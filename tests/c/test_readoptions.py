import pytest

from zeroae.rocksdb.c import readoptions


def test_create():
    rv = readoptions.create()
    assert rv is not None
    readoptions.destroy(rv)


def test_set_verify_checksums(rocksdb_readoptions):
    readoptions.set_verify_checksums(rocksdb_readoptions, 0)
    readoptions.set_verify_checksums(rocksdb_readoptions, 1)


def test_set_fill_cache(rocksdb_readoptions):
    readoptions.set_fill_cache(rocksdb_readoptions, 0)
    readoptions.set_fill_cache(rocksdb_readoptions, 1)


@pytest.mark.xfail
def test_set_snapshot(rocksdb_readoptions):
    assert False


def test_set_iterate_upper_bound(rocksdb_readoptions):
    readoptions.set_iterate_upper_bound(rocksdb_readoptions, "zzz")


def test_set_iterate_lower_bound(rocksdb_readoptions):
    readoptions.set_iterate_lower_bound(rocksdb_readoptions, "aaa")


def test_set_read_tier(rocksdb_readoptions):
    readoptions.set_read_tier(rocksdb_readoptions, 10)


def test_set_tailing(rocksdb_readoptions):
    readoptions.set_tailing(rocksdb_readoptions, 0)
    readoptions.set_tailing(rocksdb_readoptions, 1)


def test_set_managed(rocksdb_readoptions):
    readoptions.set_managed(rocksdb_readoptions, 0)


def test_set_readahead_size(rocksdb_readoptions):
    readoptions.set_readahead_size(rocksdb_readoptions, 1024)


def test_set_prefix_same_as_start(rocksdb_readoptions):
    readoptions.set_prefix_same_as_start(rocksdb_readoptions, 0)
    readoptions.set_prefix_same_as_start(rocksdb_readoptions, 1)


def test_set_pin_data(rocksdb_readoptions):
    readoptions.set_pin_data(rocksdb_readoptions, 0)
    readoptions.set_pin_data(rocksdb_readoptions, 1)


def test_set_total_order_seek(rocksdb_readoptions):
    readoptions.set_total_order_seek(rocksdb_readoptions, 0)
    readoptions.set_total_order_seek(rocksdb_readoptions, 1)


def test_set_max_skippable_internal_keys(rocksdb_readoptions):
    readoptions.set_max_skippable_internal_keys(rocksdb_readoptions, 0)
    readoptions.set_max_skippable_internal_keys(rocksdb_readoptions, 1024)


def test_set_background_purge_on_iterator_cleanup(rocksdb_readoptions):
    readoptions.set_background_purge_on_iterator_cleanup(rocksdb_readoptions, 0)
    readoptions.set_background_purge_on_iterator_cleanup(rocksdb_readoptions, 1)


def test_set_ignore_range_deletions(rocksdb_readoptions):
    readoptions.set_ignore_range_deletions(rocksdb_readoptions, 0)
    readoptions.set_ignore_range_deletions(rocksdb_readoptions, 1)
