from zeroae.rocksdb.c import  cuckoo_options


def test_fixture(rocksdb_cuckoo_table_options):
    assert rocksdb_cuckoo_table_options is not None


def test_set_hash_ratio(rocksdb_cuckoo_table_options):
    cuckoo_options.set_hash_ratio(rocksdb_cuckoo_table_options, 1)


def test_set_max_search_depth(rocksdb_cuckoo_table_options):
    cuckoo_options.set_max_search_depth(rocksdb_cuckoo_table_options, 10)


def test_set_cuckoo_block_size(rocksdb_cuckoo_table_options):
    cuckoo_options.set_cuckoo_block_size(rocksdb_cuckoo_table_options, 1024)


def test_set_identity_as_first_hash(rocksdb_cuckoo_table_options):
    cuckoo_options.set_identity_as_first_hash(rocksdb_cuckoo_table_options, 1)


def test_set_use_module_hash(rocksdb_cuckoo_table_options):
    cuckoo_options.set_use_module_hash(rocksdb_cuckoo_table_options, 0)
