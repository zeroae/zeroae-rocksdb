import pytest

from zeroae.rocksdb.c import db, transactiondb, iter, options, checkpoint_object, optimistictransactiondb


@pytest.fixture(params=["db", "txndb", "otxndb"])
def base_db_type(request):
    yield request.param


@pytest.fixture
def base_db_mod(base_db_type):
    if base_db_type in ["db", "otxndb"]:
        return db
    if base_db_type == "txndb":
        return transactiondb


@pytest.fixture()
def base_db_dir(tmp_path_factory):
    return str(tmp_path_factory.mktemp("basedb", numbered=1))


@pytest.fixture
def base_db(base_db_type, base_db_mod, rocksdb_options, rocksdb_transactiondb_options, base_db_dir):
    options.set_create_if_missing(rocksdb_options, 1)
    rv = None

    if base_db_type == "db":
        rv = base_db_mod.open(rocksdb_options, base_db_dir)
    elif base_db_type == "txndb":
        rv = base_db_mod.open(rocksdb_options, rocksdb_transactiondb_options, base_db_dir)
    elif base_db_type == "otxndb":
        otxn_db = optimistictransactiondb.open(rocksdb_options, base_db_dir)
        rv = optimistictransactiondb.get_base_db(otxn_db)
        yield rv
        optimistictransactiondb.close_base_db(rv)
        optimistictransactiondb.close(otxn_db)
        return

    yield rv

    base_db_mod.close(rv)


def test_fixture(base_db):
    assert base_db is not None


def test_get(base_db_mod, base_db, rocksdb_readoptions, rocksdb_writeoptions):
    val = base_db_mod.get(base_db, rocksdb_readoptions, "dne")
    assert val is None

    base_db_mod.put(base_db, rocksdb_writeoptions, "key", "value")
    val = base_db_mod.get(base_db, rocksdb_readoptions, "key")
    assert val == "value"


@pytest.mark.xfail
def test_get_cf():
    assert False


def test_put(base_db_mod, base_db, rocksdb_writeoptions):
    base_db_mod.put(base_db, rocksdb_writeoptions, "key", "value")


@pytest.mark.xfail
def test_put_cf():
    assert False


@pytest.mark.xfail
def test_write():
    assert False


@pytest.mark.xfail
def test_merge_negative(base_db_mod, base_db, rocksdb_writeoptions):
    # TODO: reenable this test and fix the errptr handling issue
    # This is raising an issue with the "errptr" handling down in *our* swig code.
    # base_db_mod.merge(base_db, rocksdb_writeoptions, "key", "1")
    assert False


@pytest.mark.xfail
def test_merge_cf():
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
def test_create_column_family():
    assert False


def test_create_iterator(base_db_mod, base_db, rocksdb_readoptions):
    i = base_db_mod.create_iterator(base_db, rocksdb_readoptions)
    assert i is not None
    iter.destroy(i)


@pytest.mark.xfail
def test_create_iterator_cf():
    assert False


def test_create_release_snapshot(base_db_mod, base_db):
    snap = base_db_mod.create_snapshot(base_db)
    assert snap is not None
    base_db_mod.release_snapshot(base_db, snap)


def test_checkpoint_object_create(base_db_mod, base_db):
    cp = base_db_mod.checkpoint_object_create(base_db)
    assert cp is not None
    checkpoint_object.destroy(cp)
