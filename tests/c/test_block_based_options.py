import pytest

from zeroae.rocksdb.c import block_based_options as bbto


def test_fixture(rocksdb_block_based_table_options):
    assert rocksdb_block_based_table_options is not None


def test_set_block_size(rocksdb_block_based_table_options):
    bbto.set_block_size(rocksdb_block_based_table_options, 10)


def test_set_block_size_deviation(rocksdb_block_based_table_options):
    bbto.set_block_size_deviation(rocksdb_block_based_table_options, 1)


@pytest.mark.xfail
def test_set_block_restart_interval(rocksdb_block_based_table_options):
    assert False


@pytest.mark.xfail
def test_set_index_block_restart_interval(rocksdb_block_based_table_options):
    assert False


@pytest.mark.xfail
def test_set_metadata_block_size(rocksdb_block_based_table_options):
    assert False


@pytest.mark.xfail
def test_set_partition_filters(rocksdb_block_based_table_options):
    assert False


@pytest.mark.xfail
def test_set_use_delta_encoding(rocksdb_block_based_table_options):
    assert False


@pytest.mark.xfail
def test_set_filter_policy(rocksdb_block_based_table_options):
    assert False


@pytest.mark.xfail
def test_set_no_block_cache(rocksdb_block_based_table_options):
    assert False


def test_set_block_cache(rocksdb_block_based_table_options, rocksdb_cache_lru):
    bbto.set_block_cache(rocksdb_block_based_table_options, rocksdb_cache_lru)


@pytest.mark.xfail
def test_set_block_cache_compressed(rocksdb_block_based_table_options):
    assert False


@pytest.mark.xfail
def test_set_whole_key_filtering(rocksdb_block_based_table_options):
    assert False


@pytest.mark.xfail
def test_set_format_version(rocksdb_block_based_table_options):
    assert False


@pytest.mark.xfail
def test_set_index_type(rocksdb_block_based_table_options):
    # TODO: Need enum
    assert False


@pytest.mark.xfail
def test_set_data_block_index_type(rocksdb_block_based_table_options):
    # TODO: Need enum
    assert False


@pytest.mark.xfail
def test_set_data_block_hash_ratio(rocksdb_block_based_table_options):
    assert False


@pytest.mark.xfail
def test_set_hash_index_allow_collision(rocksdb_block_based_table_options):
    assert False


@pytest.mark.xfail
def test_set_cache_index_and_filter_blocks(rocksdb_block_based_table_options):
    assert False


@pytest.mark.xfail
def test_set_cache_index_and_filter_blocks_with_high_priority(rocksdb_block_based_table_options):
    assert False


@pytest.mark.xfail
def test_set_pin_l0_filter_and_index_blocks_in_cache(rocksdb_block_based_table_options):
    assert False


@pytest.mark.xfail
def test_set_pin_top_level_index_and_filter(rocksdb_block_based_table_options):
    assert False
