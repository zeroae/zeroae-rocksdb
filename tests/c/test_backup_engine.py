import pytest
from zeroae.rocksdb.c import db as rdb, backup_engine


@pytest.fixture
def db(rocksdb_db, rocksdb_writeoptions):
    for i in range(0, 10):
        rdb.put(rocksdb_db, rocksdb_writeoptions,
                f"key{i}", f"val{i}")
    yield rocksdb_db


@pytest.fixture
def be(rocksdb_backup_engine, db):
    backup_engine.create_new_backup(rocksdb_backup_engine, db)
    yield rocksdb_backup_engine


def test_fixture(rocksdb_backup_engine):
    assert rocksdb_backup_engine is not None


def test_create_new_backup(rocksdb_backup_engine, db):
    backup_engine.create_new_backup(rocksdb_backup_engine, db)


def test_create_new_backup_flush(rocksdb_backup_engine, db):
    backup_engine.create_new_backup_flush(rocksdb_backup_engine, db, 1)


def test_purge_old_backups(be):
    backup_engine.purge_old_backups(be, 1)


def test_verify_backup(be):
    backup_engine.verify_backup(be, 1)


def test_restore_db_from_latest_backup(be, rocksdb_db_dir, rocksdb_restore_options, rocksdb_options):
    backup_engine.restore_db_from_latest_backup(
        be, rocksdb_db_dir, rocksdb_db_dir, rocksdb_restore_options
    )
    restored_db = rdb.open(rocksdb_options, rocksdb_db_dir)
    rdb.close(restored_db)


def test_get_backup_info(rocksdb_backup_engine):
    backup_info = backup_engine.get_backup_info(rocksdb_backup_engine)
    assert backup_info is not None
