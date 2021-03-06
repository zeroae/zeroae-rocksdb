import pytest

from zeroae.rocksdb.c import options


def test_fixture(rocksdb_options):
    assert rocksdb_options is not None


def test_set_block_based_table_factory(rocksdb_options, rocksdb_block_based_table_options):
    options.set_block_based_table_factory(rocksdb_options, rocksdb_block_based_table_options)


def test_set_cuckoo_table_factory(rocksdb_options, rocksdb_cuckoo_table_options):
    options.set_cuckoo_table_factory(rocksdb_options, rocksdb_cuckoo_table_options)


def test_increase_parallelism(rocksdb_options):
    options.increase_parallelism(rocksdb_options, 2)


def test_optimize_for_point_lookup(rocksdb_options):
    options.optimize_for_point_lookup(rocksdb_options, 10)


@pytest.mark.xfail
def test_optimize_level_style_compaction():
    assert False


@pytest.mark.xfail
def test_optimize_universal_style_compaction():
    assert False


@pytest.mark.xfail
def test_set_allow_ingest_behind():
    assert False


@pytest.mark.xfail
def test_set_compaction_filter():
    assert False


def test_set_compaction_filter_factory(rocksdb_options, rocksdb_compactionfilterfactory_f):
    options.set_compaction_filter_factory(rocksdb_options, rocksdb_compactionfilterfactory_f)


def test_compaction_readahead_size(rocksdb_options):
    options.compaction_readahead_size(rocksdb_options, 1024)


def test_set_comparator(rocksdb_options, rocksdb_comparator_f):
    options.set_comparator(rocksdb_options, rocksdb_comparator_f)


@pytest.mark.xfail
def test_set_merge_operator():
    assert False


@pytest.mark.xfail
def test_set_uint64add_merge_operator():
    assert False


@pytest.mark.xfail
def test_set_compression_per_level():
    assert False


def test_set_create_if_missing(rocksdb_options):
    options.set_create_if_missing(rocksdb_options, 1)


@pytest.mark.xfail
def test_set_create_missing_column_families():
    assert False


def test_set_error_if_exists(rocksdb_options):
    options.set_error_if_exists(rocksdb_options, 1)


@pytest.mark.xfail
def test_set_paranoid_checks(rocksdb_options):
    assert False


def test_set_db_paths(rocksdb_options, rocksdb_dbpath):
    # TODO: Convert typemap to a list of dbpaths
    options.set_db_paths(rocksdb_options, (rocksdb_dbpath, rocksdb_dbpath), 2)


def test_set_env(rocksdb_options, rocksdb_env):
    options.set_env(rocksdb_options, rocksdb_env)


@pytest.mark.xfail
def test_set_info_log():
    assert False


@pytest.mark.xfail
def test_set_info_log_level():
    assert False


@pytest.mark.xfail
def test_set_write_buffer_size():
    assert False


@pytest.mark.xfail
def test_set_db_write_buffer_size():
    assert False


@pytest.mark.xfail
def test_set_max_open_files():
    assert False


@pytest.mark.xfail
def test_set_max_file_opening_threads():
    assert False


@pytest.mark.xfail
def test_set_max_total_wal_size():
    assert False


@pytest.mark.xfail
def test_set_compression_options():
    assert False


@pytest.mark.xfail
def test_set_prefix_extractor():
    assert False


@pytest.mark.xfail
def test_set_num_levels():
    assert False


@pytest.mark.xfail
def test_set_level0_file_num_compaction_trigger():
    assert False


@pytest.mark.xfail
def test_set_level0_slowdown_writes_trigger():
    assert False


@pytest.mark.xfail
def test_set_level0_stop_writes_trigger():
    assert False


@pytest.mark.xfail
def test_set_max_mem_compaction_level():
    assert False


@pytest.mark.xfail
def test_set_target_file_size_base():
    assert False


@pytest.mark.xfail
def test_set_target_file_size_multiplier():
    assert False


@pytest.mark.xfail
def test_set_max_bytes_for_level_base():
    assert False


@pytest.mark.xfail
def test_set_level_compaction_dynamic_level_bytes():
    assert False


@pytest.mark.xfail
def test_set_max_bytes_for_level_multiplier():
    assert False


@pytest.mark.xfail
def test_set_max_bytes_for_level_multiplier_additional():
    assert False


@pytest.mark.xfail
def test_enable_statistics(rocksdb_options):
    options.enable_statistics(rocksdb_options)


@pytest.mark.xfail
def test_set_skip_stats_update_on_db_open():
    assert False


@pytest.mark.xfail
def test_set_skip_checking_sst_file_sizes_on_db_open():
    assert False


def test_statistics_get_string(rocksdb_options):
    rv = options.statistics_get_string(rocksdb_options)
    assert rv is None
    options.enable_statistics(rocksdb_options)
    rv = options.statistics_get_string(rocksdb_options)
    assert rv is not None


@pytest.mark.xfail
def test_set_max_write_buffer_number():
    assert False


@pytest.mark.xfail
def test_set_min_write_buffer_number_to_merge():
    assert False


@pytest.mark.xfail
def test_set_max_write_buffer_number_to_maintain():
    assert False


@pytest.mark.xfail
def test_set_max_write_buffer_size_to_maintain():
    assert False


@pytest.mark.xfail
def test_set_enable_pipelined_write():
    assert False


@pytest.mark.xfail
def test_set_unordered_write():
    assert False


@pytest.mark.xfail
def test_set_max_subcompactions():
    assert False


@pytest.mark.xfail
def test_set_max_background_jobs():
    assert False


@pytest.mark.xfail
def test_set_max_background_compactions():
    assert False


@pytest.mark.xfail
def test_set_base_background_compactions():
    assert False


@pytest.mark.xfail
def test_set_max_background_flushes():
    assert False


@pytest.mark.xfail
def test_set_max_log_file_size():
    assert False


@pytest.mark.xfail
def test_set_log_file_time_to_roll():
    assert False


@pytest.mark.xfail
def test_set_keep_log_file_num():
    assert False


@pytest.mark.xfail
def test_set_recycle_log_file_num():
    assert False


@pytest.mark.xfail
def test_set_soft_rate_limit():
    assert False


@pytest.mark.xfail
def test_set_hard_rate_limit():
    assert False


@pytest.mark.xfail
def test_set_soft_pending_compaction_bytes_limit():
    assert False


@pytest.mark.xfail
def test_set_hard_pending_compaction_bytes_limit():
    assert False


@pytest.mark.xfail
def test_set_rate_limit_delay_max_milliseconds():
    assert False


@pytest.mark.xfail
def test_set_max_manifest_file_size():
    assert False


@pytest.mark.xfail
def test_set_table_cache_numshardbits():
    assert False


@pytest.mark.xfail
def test_set_table_cache_remove_scan_count_limit():
    assert False


@pytest.mark.xfail
def test_set_arena_block_size():
    assert False


@pytest.mark.xfail
def test_set_use_fsync():
    assert False


@pytest.mark.xfail
def test_set_db_log_dir():
    assert False


@pytest.mark.xfail
def test_set_wal_dir():
    assert False


@pytest.mark.xfail
def test_set_wal_ttl_seconds():
    assert False


@pytest.mark.xfail
def test_set_wal_size_limit_mb():
    assert False


@pytest.mark.xfail
def test_set_manifest_preallocation_size():
    assert False


@pytest.mark.xfail
def test_set_purge_redundant_kvs_while_flush():
    assert False


@pytest.mark.xfail
def test_set_allow_mmap_reads():
    assert False


@pytest.mark.xfail
def test_set_allow_mmap_writes():
    assert False


@pytest.mark.xfail
def test_set_use_direct_reads():
    assert False


@pytest.mark.xfail
def test_set_use_direct_io_for_flush_and_compaction():
    assert False


@pytest.mark.xfail
def test_set_is_fd_close_on_exec():
    assert False


@pytest.mark.xfail
def test_set_skip_log_error_on_recovery():
    assert False


@pytest.mark.xfail
def test_set_stats_dump_period_sec():
    assert False


@pytest.mark.xfail
def test_set_advise_random_on_open():
    assert False


@pytest.mark.xfail
def test_set_access_hint_on_compaction_start():
    assert False


@pytest.mark.xfail
def test_set_use_adaptive_mutex():
    assert False


@pytest.mark.xfail
def test_set_bytes_per_sync():
    assert False


@pytest.mark.xfail
def test_set_wal_bytes_per_sync():
    assert False


@pytest.mark.xfail
def test_set_writable_file_max_buffer_size():
    assert False


@pytest.mark.xfail
def test_set_allow_concurrent_memtable_write():
    assert False


@pytest.mark.xfail
def test_set_enable_write_thread_adaptive_yield():
    assert False


@pytest.mark.xfail
def test_set_max_sequential_skip_in_iterations():
    assert False


@pytest.mark.xfail
def test_set_disable_auto_compactions():
    assert False


@pytest.mark.xfail
def test_set_optimize_filters_for_hits():
    assert False


@pytest.mark.xfail
def test_set_delete_obsolete_files_period_micros():
    assert False


@pytest.mark.xfail
def test_prepare_for_bulk_load():
    assert False


@pytest.mark.xfail
def test_set_memtable_vector_rep():
    assert False


@pytest.mark.xfail
def test_set_memtable_prefix_bloom_size_ratio():
    assert False


@pytest.mark.xfail
def test_set_max_compaction_bytes():
    assert False


@pytest.mark.xfail
def test_set_hash_skip_list_rep():
    assert False


@pytest.mark.xfail
def test_set_hash_link_list_rep():
    assert False


@pytest.mark.xfail
def test_set_plain_table_factory():
    assert False


@pytest.mark.xfail
def test_set_min_level_to_compress():
    assert False


@pytest.mark.xfail
def test_set_memtable_huge_page_size():
    assert False


@pytest.mark.xfail
def test_set_max_successive_merges():
    assert False


@pytest.mark.xfail
def test_set_bloom_locality():
    assert False


@pytest.mark.xfail
def test_set_inplace_update_support():
    assert False


@pytest.mark.xfail
def test_set_inplace_update_num_locks():
    assert False


@pytest.mark.xfail
def test_set_report_bg_io_stats():
    assert False


@pytest.mark.xfail
def test_set_wal_recovery_mode():
    assert False


@pytest.mark.xfail
def test_set_compression():
    assert False


@pytest.mark.xfail
def test_set_compaction_style():
    assert False


def test_set_universal_compaction_options(rocksdb_options, rocksdb_universal_compaction_options):
    options.set_universal_compaction_options(rocksdb_options, rocksdb_universal_compaction_options)


def test_set_fifo_compaction_options(rocksdb_options, rocksdb_fifo_compaction_options):
    options.set_fifo_compaction_options(rocksdb_options, rocksdb_fifo_compaction_options)


def test_set_ratelimiter(rocksdb_options, rocksdb_ratelimiter):
    options.set_ratelimiter(rocksdb_options, rocksdb_ratelimiter)


@pytest.mark.xfail
def test_set_atomic_flush(rocksdb_options):
    assert False


def test_set_row_cache(rocksdb_options, rocksdb_cache_lru):
    options.set_row_cache(rocksdb_options, rocksdb_cache_lru)


@pytest.mark.xfail
def test_get_options_from_string():
    assert False
