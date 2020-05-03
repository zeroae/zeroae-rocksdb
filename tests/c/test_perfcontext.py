import pytest

from zeroae.rocksdb.c import perfcontext


def test_fixture(rocksdb_perfcontext):
    assert rocksdb_perfcontext is not None


def test_reset(rocksdb_perfcontext):
    perfcontext.reset(rocksdb_perfcontext)


def test_report(rocksdb_perfcontext):
    result = perfcontext.report(rocksdb_perfcontext, 0)
    assert result is not None
    result = perfcontext.report(rocksdb_perfcontext, 1)
    assert result is not None


@pytest.mark.xfail(reason="swig:enums")
def test_metric(rocksdb_perfcontext):
    val = perfcontext.metric(rocksdb_perfcontext, 0)
    assert val == 0
    assert False


@pytest.mark.xfail(reason="swig:enums")
def test_set_perf_level():
    perfcontext.set_perf_level(0)
    assert False
