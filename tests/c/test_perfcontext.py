from zeroae.rocksdb.c import perfcontext


def test_create():
    rv = perfcontext.create()
    assert rv is not None
    perfcontext.destroy(rv)


def test_reset(rocksdb_perfcontext):
    perfcontext.reset(rocksdb_perfcontext)


def test_report(rocksdb_perfcontext):
    result = perfcontext.report(rocksdb_perfcontext, 0)
    assert result is not None
    result = perfcontext.report(rocksdb_perfcontext, 1)
    assert result is not None


def test_metric(rocksdb_perfcontext):
    val = perfcontext.metric(rocksdb_perfcontext, 0)
    assert val == 0
