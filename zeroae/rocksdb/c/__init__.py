import os
from importlib import import_module

from .db import *

# get all modules
_, _, filenames = next(os.walk(__path__[0]), (None, None, []))
py_files = [filename.replace(".py", "")
            for filename in filenames
            if filename.endswith(".py")]
py_files.remove("__init__")
py_files.remove("db")

for module in py_files:
    import_module(f".{module}", "zeroae.rocksdb.c")

del os, import_module


