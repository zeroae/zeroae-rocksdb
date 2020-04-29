import pytest
from zeroae.rocksdb.c import options


@pytest.fixture
def rocksdb_options():
    rv = options.create()
    yield rv
    options.destroy(rv)
