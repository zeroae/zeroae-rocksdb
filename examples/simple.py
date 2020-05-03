#!/usr/bin/env python
import os
from zeroae.rocksdb import c as crocksdb

DBPath = "/tmp/rocksdb_simple_example"

# Optimize RocksDB
options = crocksdb.options.create()
crocksdb.options.set_create_if_missing(options, 1)

# Open the database
db = crocksdb.open(options, DBPath)

# Put key-value
writeoptions = crocksdb.writeoptions.create()
crocksdb.put(db, writeoptions, "key", "value")
crocksdb.writeoptions.destroy(writeoptions)


# Read the value back
readoptions = crocksdb.readoptions.create()
rv = crocksdb.get(db, readoptions, "key")
assert rv == "value"
crocksdb.readoptions.destroy(readoptions)

# Cleanup
crocksdb.options.destroy(options)
crocksdb.close(db)
