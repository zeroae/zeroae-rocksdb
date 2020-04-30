#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_namespace_packages, Extension
import os

with open("README.rst") as readme_file:
    readme = readme_file.read()

i_files = [
    "backup_engine",
    "backup_engine_info",
    "block_based_options",
    "cache",
    "compactionfiltercontext",
    "compactoptions",
    "cuckoo_options",
    "dbpath",
    "env",
    "envoptions",
    "fifo_compaction_options",
    "flushoptions",
    "options",
    "ratelimiter",
    "readoptions",
    "restore_options",
    "universal_compaction_options",
    "writeoptions",
]
ext_modules = [Extension(f"zeroae.rocksdb.c._{i_file}",
                      libraries=["rocksdb"],
                      sources=[f"zeroae/rocksdb/c/{i_file}.i"],
                      swig_opts=["-py3",
                                 f"-I{os.environ['CONDA_PREFIX']}/include"]
                      )
                for i_file in i_files
                ]

# The requirements section should be kept in sync with the environment.yml file
requirements = [
    # fmt: off
    # fmt: on
]

setup_requirements = [
    # fmt: off
    "pytest-runner",
    "setuptools_scm",
    "wheel",
    # fmt: on
]

test_requirements = [
    # fmt: off
    "pytest>=3",
    "pytest-cov",
    # fmt: on
]

conda_rosetta_stone = {
    # fmt: off
    "pypa-requirement": "conda-dependency"
    # fmt: on
}

setup_kwargs = dict(
    author="Patrick Sodré",
    author_email="psodre@gmail.com",
    use_scm_version={"write_to": "zeroae/rocksdb/_version.py"},
    python_requires=">=3.6",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    description="ZeroAE's RocksDB Python bindings",
    install_requires=requirements,
    license="Apache",
    long_description=readme,
    long_description_content_type="text/x-rst",
    include_package_data=True,
    keywords="rocksdb zeroae",
    name="zeroae-rocksdb",
    packages=find_namespace_packages(include=["zeroae.*"]),
    setup_requires=setup_requirements,
    test_suite="tests",
    tests_require=test_requirements,
    extras_require={
        # fmt: off
        "test": test_requirements
        # fmt: on
    },
    url="https://github.com/zeroae/zeroae-rocksdb",
    zip_safe=False,
    ext_modules=ext_modules,
)

if "CONDA_BUILD_STATE" in os.environ:
    try:
        from setuptools_scm import get_version

        setup_kwargs["version"] = get_version(**setup_kwargs["use_scm_version"])
        del setup_kwargs["use_scm_version"]
    except ModuleNotFoundError:
        print(
            "Error: zeroae-rocksdb requires that setuptools_scm be installed with conda-build!"  # noqa: E501
        )
        raise
    setup_kwargs["conda_rosetta_stone"] = conda_rosetta_stone

setup(**setup_kwargs)
