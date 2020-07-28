#!/usr/bin/env python
# -*- coding: utf-8 -*-

# adopted from Kenneth Reitz
# https://github.com/kennethreitz/setup.py
# released under MIT license
# (https://github.com/kennethreitz/setup.py/blob/master/LICENSE)

# Note: To use the 'upload' functionality of this file, you must:
#   $ pip install twine

import io
import os


from setuptools import find_packages, setup

# Package meta-data.
about = {}
with open("src/twinlet/__about__.py") as fp:
    exec(fp.read(), about)

VERSION = about['__version__']

REQUIRED = [
    'torch',
    'torchvision',
]

dev_deps = []

test_deps = [
    'pytest',
    'pytest-coverage',
]

doc_deps = [
    'sphinx',
]

# this is here so that the .travis.yml script can install
# dependencies just for the tests by running
# pip install .[tests]
EXTRAS = {
    'tests': test_deps,
    'dev': dev_deps,
    'doc': doc_deps,
}


PACKAGE_DATA = {}

# The rest you shouldn't have to touch too much :)
# ------------------------------------------------
# Except, perhaps the License and Trove Classifiers!
# If you do change the License, remember to change the Trove Classifier for that!

here = os.path.abspath(os.path.dirname(__file__))


DESCRIPTION = 'PyTorch implementation of siamese and triplet networks for learning embeddings'
# Import the README and use it as the long-description.
# Note: this will only work if 'README.md' is present in your MANIFEST.in file!
try:
    with io.open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
        long_description = '\n' + f.read()
except FileNotFoundError:
    long_description = DESCRIPTION


# Where the magic happens:
setup(
    name='twinlet',
    version=about['__version__'],
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Adam Bielski',
    packages=find_packages(where="src", exclude=('tests',)),
    package_dir={"": "src"},
    entry_points={},
    install_requires=REQUIRED,
    extras_require=EXTRAS,
    package_data=PACKAGE_DATA,
    include_package_data=True,
)
