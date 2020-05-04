import pytest

from zeroae.rocksdb.c import backup_engine as rbe, backup_engine_info

from .test_backup_engine import be


@pytest.fixture()
def be_info(be):
    rv = rbe.get_backup_info(be)
    yield rv
    backup_engine_info.destroy(rv)


def test_count(be_info):
    rv = backup_engine_info.count(be_info)
    assert rv == 1


def test_timestamp(be_info):
    rv = backup_engine_info.timestamp(be_info, 0)
    assert rv > 0


def test_backup_id(be_info):
    rv = backup_engine_info.backup_id(be_info, 0)
    assert rv == 1


def test_size(be_info):
    rv = backup_engine_info.size(be_info, 0)
    assert rv == pytest.approx(5657, 5657/10)


def test_number_files(be_info):
    rv = backup_engine_info.number_files(be_info, 0)
    assert rv == 4
