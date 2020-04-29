import pytest
from zeroae.rocksdb.c import (
    block_based_options, cuckoo_options, options
)


@pytest.fixture
def rocksdb_block_based_table_options():
    rv = block_based_options.create()
    yield rv
    block_based_options.destroy(rv)


@pytest.fixture
def rocksdb_cuckoo_table_options():
    rv = cuckoo_options.create()
    yield rv
    cuckoo_options.destroy(rv)


@pytest.fixture
def rocksdb_options():
    rv = options.create()
    yield rv
    options.destroy(rv)
