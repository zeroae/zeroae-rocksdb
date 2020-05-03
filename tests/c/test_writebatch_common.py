import pytest

from zeroae.rocksdb.c import writebatch_wi, writebatch


@pytest.fixture(params=[writebatch_wi, writebatch])
def writebatch_impl(request):
    return request.param


@pytest.fixture
def writebatch_obj(writebatch_impl):
    if writebatch_impl == writebatch_wi:
        return writebatch_impl.create(1024, 0)
    if writebatch_impl == writebatch:
        return writebatch_impl.create()


def test_fixture(writebatch_obj):
    assert writebatch_obj is not None


def test_clear(writebatch_obj, writebatch_impl):
    writebatch_impl.put(writebatch_obj, "key", "value")
    writebatch_impl.clear(writebatch_obj)
    count = writebatch_impl.count(writebatch_obj)
    assert count == 0


def test_count(writebatch_obj, writebatch_impl):
    count = writebatch_impl.count(writebatch_obj)
    assert count == 0

    writebatch_impl.put(writebatch_obj, "key", "value")
    count = writebatch_impl.count(writebatch_obj)
    assert count == 1


def test_put(writebatch_obj, writebatch_impl):
    writebatch_impl.put(writebatch_obj, "key", "value")


@pytest.mark.xfail
def test_put_cf(writebatch_obj, writebatch_impl):
    assert False


@pytest.mark.xfail
def test_putv(writebatch_obj, writebatch_impl):
    assert False


@pytest.mark.xfail
def test_putv_cf(writebatch_obj, writebatch_impl):
    assert False


def test_merge(writebatch_obj, writebatch_impl):
    writebatch_impl.merge(writebatch_obj, "key", "val")


@pytest.mark.xfail
def test_merge_cf(writebatch_obj, writebatch_impl):
    assert False


@pytest.mark.xfail
def test_mergev(writebatch_obj, writebatch_impl):
    assert False


@pytest.mark.xfail
def test_mergev_cf(writebatch_obj, writebatch_impl):
    assert False


def test_delete(writebatch_obj, writebatch_impl):
    writebatch_impl.merge(writebatch_obj, "key", "val")


@pytest.mark.xfail
def test_delete_cf(writebatch_obj, writebatch_impl):
    assert False


@pytest.mark.xfail
def test_deletev(writebatch_obj, writebatch_impl):
    assert False


@pytest.mark.xfail
def test_deletev_cf(writebatch_obj, writebatch_impl):
    assert False


def test_put_log_data(writebatch_obj, writebatch_impl):
    writebatch_impl.put_log_data(writebatch_obj, "this is a blob")


@pytest.mark.xfail
def test_iterate(writebatch_obj, writebatch_impl):
    assert False


@pytest.mark.xfail
def test_data(writebatch_obj, writebatch_impl):
    assert False


def test_set_save_point(writebatch_obj, writebatch_impl):
    writebatch_impl.set_save_point(writebatch_obj)


@pytest.mark.xfail
def test_rollback_to_save_point(writebatch_obj, writebatch_impl):
    assert False


