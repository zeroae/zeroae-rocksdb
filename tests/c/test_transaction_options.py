from zeroae.rocksdb.c import transaction_options


def test_fixture(rocksdb_transaction_options):
    assert rocksdb_transaction_options is not None


def test_set_set_snapshot(rocksdb_transaction_options):
    transaction_options.set_set_snapshot(rocksdb_transaction_options, 0)
    transaction_options.set_set_snapshot(rocksdb_transaction_options, 1)


def test_set_deadlock_detect(rocksdb_transaction_options):
    transaction_options.set_deadlock_detect(rocksdb_transaction_options, 0)
    transaction_options.set_deadlock_detect(rocksdb_transaction_options, 1)


def test_set_lock_timeout(rocksdb_transaction_options):
    transaction_options.set_lock_timeout(rocksdb_transaction_options, 0)
    transaction_options.set_lock_timeout(rocksdb_transaction_options, 10)


def test_set_expiration(rocksdb_transaction_options):
    transaction_options.set_expiration(rocksdb_transaction_options, 10)


def test_set_deadlock_detect_depth(rocksdb_transaction_options):
    transaction_options.set_deadlock_detect_depth(rocksdb_transaction_options, 10)


def test_set_max_write_batch_size(rocksdb_transaction_options):
    transaction_options.set_max_write_batch_size(rocksdb_transaction_options, 1024)
