from zeroae.rocksdb.c import env


def test_fixture(rocksdb_env):
    assert rocksdb_env is not None


def test_set_background_threads(rocksdb_env):
    env.set_background_threads(rocksdb_env, 1)


def test_set_high_priority_background_threads(rocksdb_env):
    env.set_high_priority_background_threads(rocksdb_env, 2)


def test_join_all_threads(rocksdb_env):
    env.join_all_threads(rocksdb_env)


def test_lower_thread_pool_io_priority(rocksdb_env):
    env.lower_thread_pool_io_priority(rocksdb_env)


def test_lower_high_priority_thread_pool_io_priority(rocksdb_env):
    env.lower_high_priority_thread_pool_io_priority(rocksdb_env)


def test_lower_thread_pool_cpu_priority(rocksdb_env):
    env.lower_thread_pool_cpu_priority(rocksdb_env)


def test_lower_high_priority_thread_pool_cpu_priority(rocksdb_env):
    env.lower_high_priority_thread_pool_cpu_priority(rocksdb_env)
