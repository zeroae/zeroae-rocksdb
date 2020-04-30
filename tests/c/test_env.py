from zeroae.rocksdb.c import env


def test_create_destroy_default():
    rv = env.create_default()
    assert rv is not None
    env.destroy(rv)


def test_create_destroy_mem():
    rv = env.create_mem()
    assert rv is not None
    env.destroy(rv)


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
