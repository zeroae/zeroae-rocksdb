from zeroae.rocksdb.c import db
from zeroae.rocksdb.c import checkpoint_object


def test_checkpoint_create(rocksdb_db, tmp_path_factory):
    cp = db.checkpoint_object_create(rocksdb_db)

    cp_dir = str(tmp_path_factory.mktemp("checkpoint", numbered=True) / "cp")
    checkpoint_object.checkpoint_create(cp, cp_dir, 1)

    checkpoint_object.destroy(cp)
