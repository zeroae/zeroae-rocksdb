import pytest

from zeroae.rocksdb.c import db, livefiles


def test_fixture(rocksdb_db):
    assert rocksdb_db is not None


@pytest.mark.xfail
def test_open_with_ttl():
    assert False


@pytest.mark.xfail
def test_open_for_read_only():
    assert False


@pytest.mark.xfail
def test_open_as_secondary():
    assert False


def test_checkpoint_object_create(rocksdb_db):
    cp = db.checkpoint_object_create(rocksdb_db)
    assert cp is not None
    from zeroae.rocksdb.c import checkpoint_object
    checkpoint_object.destroy(cp)


@pytest.mark.xfail
def test_open_column_families():
    assert False


@pytest.mark.xfail
def test_open_for_read_only_column_families():
    assert False


@pytest.mark.xfail
def test_open_as_secondary_column_families():
    assert False


@pytest.mark.xfail
def test_list_column_families():
    assert False


@pytest.mark.xfail
def test_list_column_families_destroy():
    assert False


@pytest.mark.xfail
def test_create_column_family():
    assert False


@pytest.mark.xfail
def test_drop_column_family():
    assert False


@pytest.mark.xfail
def test_column_family_handle_destroy():
    assert False


def test_put(rocksdb_db, rocksdb_writeoptions):
    err = db.put(rocksdb_db, rocksdb_writeoptions, "key", "value")
    assert err is None


@pytest.mark.xfail
def test_put_cf():
    assert False


def test_delete(rocksdb_db, rocksdb_writeoptions):
    err = db.delete(rocksdb_db, rocksdb_writeoptions, "key")
    assert err is None
    err = db.put(rocksdb_db, rocksdb_writeoptions, "key", "value")
    assert err is None
    err = db.delete(rocksdb_db, rocksdb_writeoptions, "key")
    assert err is None


@pytest.mark.xfail
def test_delete_cf():
    assert False


@pytest.mark.xfail
def test_delete_range_cf():
    assert False


@pytest.mark.xfail
def test_merge():
    assert False


@pytest.mark.xfail
def test_merge_cf():
    assert False


@pytest.mark.xfail
def test_write():
    assert False


def test_get_exists(rocksdb_db, rocksdb_readoptions, rocksdb_writeoptions):
    val = db.get(rocksdb_db, rocksdb_readoptions, "dne")
    assert val is None

    db.put(rocksdb_db, rocksdb_writeoptions, "key", "value")
    val = db.get(rocksdb_db, rocksdb_readoptions, "key")
    assert val == "value"


@pytest.mark.xfail
def test_get_cf():
    assert False


@pytest.mark.xfail
def test_multi_get():
    assert False


@pytest.mark.xfail
def test_multi_get_cf():
    assert False


@pytest.mark.xfail
def test_create_iterator():
    assert False


@pytest.mark.xfail
def test_get_updates_since():
    assert False


@pytest.mark.xfail
def test_create_iterator_cf():
    assert False


@pytest.mark.xfail
def test_create_iterators():
    assert False


@pytest.mark.xfail
def test_create_snapshot():
    assert False


@pytest.mark.xfail
def test_release_snapshot():
    assert False


@pytest.mark.xfail
def test_property_value():
    assert False


@pytest.mark.xfail
def test_property_int():
    assert False


@pytest.mark.xfail
def test_property_int_cf():
    assert False


@pytest.mark.xfail
def test_property_value_cf():
    assert False


@pytest.mark.xfail
def test_approximate_sizes():
    assert False


@pytest.mark.xfail
def test_approximate_sizes_cf():
    assert False


@pytest.mark.xfail
def test_compact_range():
    assert False


@pytest.mark.xfail
def test_compact_range_cf():
    assert False


@pytest.mark.xfail
def test_compact_range_opt():
    assert False


@pytest.mark.xfail
def test_compact_range_cf_opt():
    assert False


@pytest.mark.xfail
def test_delete_file():
    assert False


def test_livefiles(rocksdb_db):
    rv = db.livefiles(rocksdb_db)
    assert rv is not None
    livefiles.destroy(rv)


@pytest.mark.xfail
def test_flush():
    assert False


@pytest.mark.xfail
def test_flush_cf():
    assert False


@pytest.mark.xfail
def test_disable_file_deletions():
    assert False


@pytest.mark.xfail
def test_enable_file_deletions():
    assert False


@pytest.mark.xfail
def test_destroy_db():
    assert False


@pytest.mark.xfail
def test_repair_db():
    assert False


@pytest.mark.xfail
def test_get_latest_sequence_number():
    assert False


@pytest.mark.xfail
def test_write_writebatch_wi():
    assert False


@pytest.mark.xfail
def test_set_options():
    assert False


@pytest.mark.xfail
def test_set_options_cf():
    assert False


@pytest.mark.xfail
def test_ingest_external_file():
    assert False


@pytest.mark.xfail
def test_ingest_external_file_cf():
    assert False


@pytest.mark.xfail
def test_try_catch_up_with_primary():
    assert False


@pytest.mark.xfail
def test_delete_file_in_range():
    assert False


@pytest.mark.xfail
def test_delete_file_in_range_cf():
    assert False


@pytest.mark.xfail
def test_free():
    assert False


@pytest.mark.xfail
def test_get_pinned():
    assert False


@pytest.mark.xfail
def test_get_pinned_cf():
    assert False
