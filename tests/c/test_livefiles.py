import pytest

from zeroae.rocksdb.c import db as rdb
import zeroae.rocksdb.c.livefiles as rlf


@pytest.fixture()
def db(rocksdb_db, rocksdb_writeoptions, rocksdb_flushoptions):
    rv = rocksdb_db
    opt = rocksdb_writeoptions
    rdb.put(rv, opt, "aaa", "value")
    rdb.put(rv, opt, "mmm", "value")
    rdb.put(rv, opt, "zzz", "value")
    rdb.flush(rv, rocksdb_flushoptions)
    yield rv


@pytest.fixture()
def lf(db):
    rv = rdb.livefiles(db)
    yield rv
    rlf.destroy(rv)


def test_fixture(lf):
    assert lf is not None


def test_count(lf):
    assert rlf.count(lf) == 1


def test_smallestkey(lf):
    assert rlf.smallestkey(lf, 0) == "aaa"


def test_largestkey(lf):
    assert rlf.largestkey(lf, 0) == "zzz"


def test_name(lf):
    assert rlf.name(lf, 0) == "/000007.sst"


def test_level(lf):
    assert rlf.level(lf, 0) == 0


def test_size(lf):
    assert rlf.size(lf, 0) == pytest.approx(830, 8)


def test_entries(lf):
    assert rlf.entries(lf, 0) == 3


def test_deletions(lf, db, rocksdb_writeoptions, rocksdb_flushoptions):
    assert rlf.deletions(lf, 0) == 0

    # Actually delete something...
    rdb.delete(db, rocksdb_writeoptions, "aaa")
    rdb.flush(db, rocksdb_flushoptions)

    lf = rdb.livefiles(db)
    assert rlf.count(lf) == 2
    assert rlf.deletions(lf, 0) == 1
    rlf.destroy(lf)

