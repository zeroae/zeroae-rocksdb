from zeroae.rocksdb.c import block_based_options as bbto


def test_create_destroy():
    opt = bbto.create()
    assert opt is not None
    bbto.destroy(opt)


def test_set_block_size(rocksdb_block_based_table_options):
    bbto.set_block_size(rocksdb_block_based_table_options, 10)


def test_set_block_size_deviation():
    assert False


def test_set_block_restart_interval():
    assert False


def test_set_index_block_restart_interval():
    assert False


def test_set_metadata_block_size():
    assert False


def test_set_partition_filters():
    assert False


def test_set_use_delta_encoding():
    assert False


def test_set_filter_policy():
    assert False


def test_set_no_block_cache():
    assert False


def test_set_block_cache():
    assert False


def test_set_block_cache_compressed():
    assert False


def test_set_whole_key_filtering():
    assert False


def test_set_format_version():
    assert False


def test_set_index_type():
    assert False


def test_set_data_block_index_type():
    assert False


def test_set_data_block_hash_ratio():
    assert False


def test_set_hash_index_allow_collision():
    assert False


def test_set_cache_index_and_filter_blocks():
    assert False


def test_set_cache_index_and_filter_blocks_with_high_priority():
    assert False


def test_set_pin_l0_filter_and_index_blocks_in_cache():
    assert False


def test_set_pin_top_level_index_and_filter():
    assert False
