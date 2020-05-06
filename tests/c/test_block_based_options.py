import pytest

from zeroae.rocksdb.c import block_based_options as bbto_mod


@pytest.fixture(params=[0,1])
def uchar_f(request):
    return request.param


@pytest.fixture()
def bbto_f(rocksdb_block_based_table_options):
    yield rocksdb_block_based_table_options


def test_fixture(bbto_f):
    assert bbto_f is not None


def test_set_block_size(bbto_f):
    bbto_mod.set_block_size(bbto_f, 10)


def test_set_block_size_deviation(bbto_f):
    bbto_mod.set_block_size_deviation(bbto_f, 1)


def test_set_block_restart_interval(bbto_f):
    bbto_mod.set_block_restart_interval(bbto_f, 1)


def test_set_index_block_restart_interval(bbto_f):
    bbto_mod.set_index_block_restart_interval(bbto_f, 1)


def test_set_metadata_block_size(bbto_f):
    bbto_mod.set_metadata_block_size(bbto_f, 1024)


def test_set_partition_filters(bbto_f, uchar_f):
    bbto_mod.set_partition_filters(bbto_f, uchar_f)


def test_set_use_delta_encoding(bbto_f, uchar_f):
    bbto_mod.set_use_delta_encoding(bbto_f, uchar_f)


@pytest.mark.xfail
def test_set_filter_policy(bbto_f):
    assert False


def test_set_no_block_cache(bbto_f, uchar_f):
    bbto_mod.set_no_block_cache(bbto_f, uchar_f)


def test_set_block_cache(bbto_f, rocksdb_cache_lru):
    bbto_mod.set_block_cache(bbto_f, rocksdb_cache_lru)


def test_set_block_cache_compressed(bbto_f, rocksdb_cache_lru):
    bbto_mod.set_block_cache_compressed(bbto_f, rocksdb_cache_lru)


def test_set_whole_key_filtering(bbto_f, uchar_f):
    bbto_mod.set_whole_key_filtering(bbto_f, uchar_f)


@pytest.mark.xfail
def test_set_format_version(bbto_f):
    assert False


@pytest.mark.xfail
def test_set_index_type(bbto_f):
    # TODO: Need enum
    assert False


@pytest.mark.xfail
def test_set_data_block_index_type(bbto_f):
    # TODO: Need enum
    assert False


def test_set_data_block_hash_ratio(bbto_f):
    bbto_mod.set_data_block_hash_ratio(bbto_f, .5)


def test_set_hash_index_allow_collision(bbto_f, uchar_f):
    bbto_mod.set_hash_index_allow_collision(bbto_f, uchar_f)


def test_set_cache_index_and_filter_blocks(bbto_f, uchar_f):
    bbto_mod.set_cache_index_and_filter_blocks(bbto_f, uchar_f)


def test_set_cache_index_and_filter_blocks_with_high_priority(bbto_f, uchar_f):
    bbto_mod.set_cache_index_and_filter_blocks_with_high_priority(bbto_f, uchar_f)


def test_set_pin_l0_filter_and_index_blocks_in_cache(bbto_f, uchar_f):
    bbto_mod.set_pin_l0_filter_and_index_blocks_in_cache(bbto_f, uchar_f)


def test_set_pin_top_level_index_and_filter(bbto_f, uchar_f):
    bbto_mod.set_pin_top_level_index_and_filter(bbto_f, uchar_f)
