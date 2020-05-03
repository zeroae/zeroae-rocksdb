from zeroae.rocksdb.c import transactiondb_options


def test_fixture(rocksdb_transactiondb_options):
    assert transactiondb_options is not None


def test_set_max_num_locks(rocksdb_transactiondb_options):
    transactiondb_options.set_max_num_locks(rocksdb_transactiondb_options, 10)


def test_set_num_stripes(rocksdb_transactiondb_options):
    transactiondb_options.set_num_stripes(rocksdb_transactiondb_options, 10)


def test_set_transaction_lock_timeout(rocksdb_transactiondb_options):
    transactiondb_options.set_transaction_lock_timeout(rocksdb_transactiondb_options, 10)


def test_set_default_lock_timeout(rocksdb_transactiondb_options):
    transactiondb_options.set_default_lock_timeout(rocksdb_transactiondb_options, 10)
