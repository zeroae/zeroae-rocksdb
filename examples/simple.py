#!/usr/bin/env python
import os
from zeroae.rocksdb import c as crocksdb

DBPath = "/tmp/rocksdb_simple_example"

# Optimize RocksDB
options = crocksdb.options.create()
crocksdb.options.set_create_if_missing(options, 1)

# Open the database
db, err = crocksdb.open(options, DBPath)
assert err is None

# Put key-value
writeoptions = crocksdb.writeoptions.create()
err = crocksdb.put(db, writeoptions, "key", "value")
assert err is None
crocksdb.writeoptions.destroy(writeoptions)


# Read the value back
readoptions = crocksdb.readoptions.create()
rv, err = crocksdb.get(db, readoptions, "key")
assert err is None
assert rv == "value"
crocksdb.readoptions.destroy(readoptions)

# Cleanup
crocksdb.options.destroy(options)
crocksdb.close(db)
