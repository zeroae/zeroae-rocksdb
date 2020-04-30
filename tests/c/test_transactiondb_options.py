from zeroae.rocksdb.c import transactiondb_options


def test_create():
    rv = transactiondb_options.create()
    assert rv is not None
    transactiondb_options.destroy(rv)


def test_set_max_num_locks(rocksdb_transactiondb_options):
    transactiondb_options.set_max_num_locks(rocksdb_transactiondb_options, 10)


def test_set_num_stripes(rocksdb_transactiondb_options):
    transactiondb_options.set_num_stripes(rocksdb_transactiondb_options, 10)


def test_set_transaction_lock_timeout(rocksdb_transactiondb_options):
    transactiondb_options.set_transaction_lock_timeout(rocksdb_transactiondb_options, 10)


def test_set_default_lock_timeout(rocksdb_transactiondb_options):
    transactiondb_options.set_default_lock_timeout(rocksdb_transactiondb_options, 10)
