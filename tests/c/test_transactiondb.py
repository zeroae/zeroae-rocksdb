import pytest

from zeroae.rocksdb.c import transactiondb, transaction, iter


def test_fixture(rocksdb_txn_db):
    assert rocksdb_txn_db is not None


@pytest.mark.xfail
def test_open_column_families():
    assert False


def test_begin_transaction(rocksdb_txn_db, rocksdb_writeoptions, rocksdb_transaction_options):
    txn = transactiondb.begin_transaction(rocksdb_txn_db, rocksdb_writeoptions, rocksdb_transaction_options, None)
    assert txn is not None
    transaction.destroy(txn)

