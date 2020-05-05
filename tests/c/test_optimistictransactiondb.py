import pytest

from zeroae.rocksdb.c import optimistictransactiondb, transaction


def test_fixture(rocksdb_otxn_db):
    assert rocksdb_otxn_db is not None


@pytest.mark.xfail()
def test_open_column_families():
    assert False


def test_base_db(rocksdb_otxn_db):
    base_db = optimistictransactiondb.get_base_db(rocksdb_otxn_db)
    assert base_db is not None
    optimistictransactiondb.close_base_db(base_db)


def test_begin_transaction(rocksdb_otxn_db, rocksdb_writeoptions, rocksdb_otxn_options):
    txn = optimistictransactiondb.begin_transaction(rocksdb_otxn_db, rocksdb_writeoptions, rocksdb_otxn_options, None)
    assert txn is not None
    transaction.destroy(txn)

