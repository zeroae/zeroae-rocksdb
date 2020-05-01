import pytest

from zeroae.rocksdb.c import writebatch_wi


def test_create():
    rv = writebatch_wi.create(1024, 0)
    assert rv is not None
    writebatch_wi.destroy(rv)


def test_clear(rocksdb_writebatch_wi):
    writebatch_wi.put(rocksdb_writebatch_wi, "key", "value")
    writebatch_wi.clear(rocksdb_writebatch_wi)
    count = writebatch_wi.count(rocksdb_writebatch_wi)
    assert count == 0

def test_count(rocksdb_writebatch_wi):
    count = writebatch_wi.count(rocksdb_writebatch_wi)
    assert count == 0

    writebatch_wi.put(rocksdb_writebatch_wi, "key", "value")
    count = writebatch_wi.count(rocksdb_writebatch_wi)
    assert count == 1


def test_put(rocksdb_writebatch_wi):
    writebatch_wi.put(rocksdb_writebatch_wi, "key", "value")


@pytest.mark.xfail
def test_put_cf(rocksdb_writebatch_wi):
    assert False


@pytest.mark.xfail
def test_putv(rocksdb_writebatch_wi):
    assert False


@pytest.mark.xfail
def test_putv_cf(rocksdb_writebatch_wi):
    assert False


def test_merge(rocksdb_writebatch_wi):
    writebatch_wi.merge(rocksdb_writebatch_wi, "key", "val")


@pytest.mark.xfail
def test_merge_cf(rocksdb_writebatch_wi):
    assert False


@pytest.mark.xfail
def test_mergev(rocksdb_writebatch_wi):
    assert False


@pytest.mark.xfail
def test_mergev_cf(rocksdb_writebatch_wi):
    assert False


def test_delete(rocksdb_writebatch_wi):
    writebatch_wi.merge(rocksdb_writebatch_wi, "key", "val")


@pytest.mark.xfail
def test_delete_cf(rocksdb_writebatch_wi):
    assert False


@pytest.mark.xfail
def test_deletev(rocksdb_writebatch_wi):
    assert False


@pytest.mark.xfail
def test_deletev_cf(rocksdb_writebatch_wi):
    assert False


def test_put_log_data(rocksdb_writebatch_wi):
    writebatch_wi.put_log_data(rocksdb_writebatch_wi, "this is a blob")


@pytest.mark.xfail
def test_iterate(rocksdb_writebatch_wi):
    assert False


@pytest.mark.xfail
def test_data(rocksdb_writebatch_wi):
    assert False


def test_set_save_point(rocksdb_writebatch_wi):
    writebatch_wi.set_save_point(rocksdb_writebatch_wi)


@pytest.mark.xfail
def test_rollback_to_save_point(rocksdb_writebatch_wi):
    assert False


@pytest.mark.xfail
def test_get_from_batch(rocksdb_writebatch_wi):
    assert False


@pytest.mark.xfail
def test_get_from_batch_cf(rocksdb_writebatch_wi):
    assert False


@pytest.mark.xfail
def test_get_from_batch_and_db(rocksdb_writebatch_wi):
    assert False


@pytest.mark.xfail
def test_get_from_batch_and_db_cf(rocksdb_writebatch_wi):
    assert False


@pytest.mark.xfail
def test_create_iterator_with_base(rocksdb_writebatch_wi):
    assert False


@pytest.mark.xfail
def test_create_iterator_with_base_cf(rocksdb_writebatch_wi):
    assert False
