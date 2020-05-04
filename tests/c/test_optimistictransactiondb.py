import pytest

from zeroae.rocksdb.c import optimistictransactiondb, transaction


def test_fixture(rocksdb_otxdb):
    assert rocksdb_otxdb is not None


@pytest.mark.xfail()
def test_open_column_families():
    assert False


def test_base_db(rocksdb_otxdb):
    base_db = optimistictransactiondb.get_base_db(rocksdb_otxdb)
    assert base_db is not None
    optimistictransactiondb.close_base_db(base_db)


def test_begin_transaction(rocksdb_otxdb, rocksdb_writeoptions, rocksdb_otxn_options):
    txn = optimistictransactiondb.begin_transaction(rocksdb_otxdb, rocksdb_writeoptions, rocksdb_otxn_options, None)
    assert txn is not None
    transaction.destroy(txn)

