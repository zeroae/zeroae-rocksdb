import pytest

from zeroae.rocksdb.c import transactiondb, transaction, iter, snapshot


@pytest.fixture()
def txn_db_f(rocksdb_txn_db):
    yield rocksdb_txn_db

@pytest.fixture()
def txn_db_mod_f():
    yield transactiondb

@pytest.fixture()
def txn_f(txn_db_mod_f, txn_db_f, rocksdb_writeoptions, rocksdb_transaction_options):
    txn_db_mod_f.put(txn_db_f, rocksdb_writeoptions, "key-pre-txn", "value")

    txn = txn_db_mod_f.begin_transaction(txn_db_f, rocksdb_writeoptions, rocksdb_transaction_options, None)
    yield txn
    transaction.destroy(txn)


def test_fixture(txn_f):
    assert txn_f is not None


def test_get(txn_f, rocksdb_readoptions):
    v = transaction.get(txn_f, rocksdb_readoptions, "key-pre-txn")
    assert v == "value"
    assert transaction.get(txn_f, rocksdb_readoptions, "dne") is None


@pytest.mark.xfail
def test_get_cf():
    assert False


@pytest.mark.skip(reason="ERRPTR Resetting")
def test_get_for_update(txn_db_mod_f, txn_db_f, txn_f, rocksdb_readoptions, rocksdb_writeoptions):
    v = transaction.get_for_update(txn_f, rocksdb_readoptions, "key-pre-txn", 1)
    assert v == "value"

    with pytest.raises(RuntimeError):
        txn_db_mod_f.put(txn_db_f, rocksdb_writeoptions, "key-pre-txn", "value0")
        transaction.commit(txn_f)


@pytest.mark.xfail
def test_get_for_update_cf():
    assert False


def test_commit(txn_db_mod_f, txn_db_f, txn_f, rocksdb_readoptions):
    transaction.put(txn_f, "key", "committed")
    transaction.delete(txn_f, "key-pre-txn")
    transaction.commit(txn_f)

    assert txn_db_mod_f.get(txn_db_f, rocksdb_readoptions, "key") == "committed"


def test_rollback(txn_f, rocksdb_readoptions):
    transaction.put(txn_f, "A", "a")
    transaction.rollback(txn_f)

    assert transaction.get(txn_f, rocksdb_readoptions, "A") is None


def test_savepoint(txn_f, rocksdb_readoptions):
    transaction.put(txn_f, "A", "a")
    transaction.set_savepoint(txn_f)
    transaction.put(txn_f, "B", "b")
    transaction.rollback_to_savepoint(txn_f)

    assert transaction.get(txn_f, rocksdb_readoptions, "A") == "a"
    assert transaction.get(txn_f, rocksdb_readoptions, "B") is None


def test_get_snapshot(txn_db_mod_f, txn_db_f, txn_f, rocksdb_writeoptions, rocksdb_readoptions):
    # https://github.com/facebook/rocksdb/wiki/Transactions#setting-a-snapshot
    snap = transaction.get_snapshot(txn_f)

    txn_db_mod_f.put(txn_db_f, rocksdb_writeoptions, "key1", "value0")

    with pytest.raises(RuntimeError):
        transaction.put(txn_f, "key1", "value1")
        transaction.commit(txn_f)

    assert txn_db_mod_f.get(txn_db_f, rocksdb_readoptions, "key1") == "value0"
    snapshot.destroy(snap)


def test_put(txn_f, rocksdb_readoptions):
    transaction.put(txn_f, "key", "value")
    v = transaction.get(txn_f, rocksdb_readoptions, "key")
    assert v == "value"


@pytest.mark.xfail
def test_put_cf():
    assert False


@pytest.mark.xfail
def test_merge():
    assert False


@pytest.mark.xfail
def test_merge_cf():
    assert False


def test_delete(txn_f, rocksdb_readoptions):
    transaction.delete(txn_f, "key-pre-txn")
    v = transaction.get(txn_f, rocksdb_readoptions, "key-pre-txn")
    assert v is None


@pytest.mark.xfail
def test_delete_cf():
    assert False


def test_create_iterator(txn_f, rocksdb_readoptions):
    it = transaction.create_iterator(txn_f, rocksdb_readoptions)
    assert it is not None
    iter.destroy(it)


@pytest.mark.xfail
def test_create_iterator_cf():
    assert False
