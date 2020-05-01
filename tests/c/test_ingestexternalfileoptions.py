from zeroae.rocksdb.c import ingestexternalfileoptions


def test_create():
    rv = ingestexternalfileoptions.create()
    assert rv is not None
    ingestexternalfileoptions.destroy(rv)


def test_set_move_files(rocksdb_ingestexternalfileoptions):
    ingestexternalfileoptions.set_move_files(rocksdb_ingestexternalfileoptions, 0)
    ingestexternalfileoptions.set_move_files(rocksdb_ingestexternalfileoptions, 1)


def test_set_snapshot_consistency(rocksdb_ingestexternalfileoptions):
    ingestexternalfileoptions.set_snapshot_consistency(rocksdb_ingestexternalfileoptions, 0)
    ingestexternalfileoptions.set_snapshot_consistency(rocksdb_ingestexternalfileoptions, 1)


def test_set_allow_global_seqno(rocksdb_ingestexternalfileoptions):
    ingestexternalfileoptions.set_allow_global_seqno(rocksdb_ingestexternalfileoptions, 0)
    ingestexternalfileoptions.set_allow_global_seqno(rocksdb_ingestexternalfileoptions, 1)


def test_set_allow_blocking_flush(rocksdb_ingestexternalfileoptions):
    ingestexternalfileoptions.set_allow_blocking_flush(rocksdb_ingestexternalfileoptions, 0)
    ingestexternalfileoptions.set_allow_blocking_flush(rocksdb_ingestexternalfileoptions, 1)


def test_set_ingest_behind(rocksdb_ingestexternalfileoptions):
    ingestexternalfileoptions.set_ingest_behind(rocksdb_ingestexternalfileoptions, 0)
    ingestexternalfileoptions.set_ingest_behind(rocksdb_ingestexternalfileoptions, 1)
