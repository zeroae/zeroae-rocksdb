#!/usr/bin/env python
import os
from zeroae.rocksdb import c as crocksdb
from zeroae.rocksdb.c import options
from zeroae.rocksdb.c.comparator import Comparator

SSTFilePath = "/tmp/test.sst"


# Use a Python Comparator
class ReverseComparator(Comparator):
    def __init__(self):
        super().__init__()

    def compare(self, a, b):
        return 1 if a < b else 0 if a == b else -1

    def name(self):
        return "ReverseComparator"


my_comp = ReverseComparator()
assert crocksdb.comparator.test_name_cb(my_comp) == my_comp.name()
assert crocksdb.comparator.test_compare_cb(my_comp, "key0", "key1") == my_comp.compare("key0", "key1")

# Python Callback Comparator
comp = crocksdb.comparator.create(my_comp.__disown__())

# SST Options
io_opts = crocksdb.options.create()
crocksdb.options.set_create_if_missing(io_opts, 1)
crocksdb.options.set_comparator(io_opts, comp)

env_opts = crocksdb.envoptions.create()

# Create and Open the SST File
sst = crocksdb.sstfilewriter.create(env_opts, io_opts)
crocksdb.sstfilewriter.open(sst, SSTFilePath)

# Write some keys...
crocksdb.sstfilewriter.put(sst, "key2", "a")
crocksdb.sstfilewriter.put(sst, "key1", "b")
crocksdb.sstfilewriter.put(sst, "key0", "c")

# Write the actual file
crocksdb.sstfilewriter.finish(sst)
crocksdb.sstfilewriter.destroy(sst)
