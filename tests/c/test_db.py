import pytest

from zeroae.rocksdb.c import db


@pytest.mark.xfail
def test_open(rocksdb_options, tmp_path):
    rv, err = db.open(rocksdb_options, str(tmp_path))
    assert rv is not None

    assert False


@pytest.mark.xfail
def test_open_with_ttl():
    assert False


@pytest.mark.xfail
def test_open_for_read_only():
    assert False


@pytest.mark.xfail
def test_open_as_secondary():
    assert False


@pytest.mark.xfail
def test_checkpoint_object_create():
    assert False


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


@pytest.mark.xfail
def test_close():
    assert False


@pytest.mark.xfail
def test_put():
    assert False


@pytest.mark.xfail
def test_put_cf():
    assert False


@pytest.mark.xfail
def test_delete():
    assert False


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


@pytest.mark.xfail
def test_get():
    assert False


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


@pytest.mark.xfail
def test_livefiles():
    assert False


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
