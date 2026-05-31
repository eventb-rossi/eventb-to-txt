# Copyright (c) 2018 Ilya Shchepetkov
# Use of this source code is governed by the MIT license that can be
# found in the LICENSE file.

import re

import setuptools


def read_version():
    with open("eventb_to_txt/__init__.py", encoding="utf8") as f:
        match = re.search(r'^__version__ = "([^"]+)"', f.read(), re.M)
    if not match:
        raise RuntimeError("Unable to find __version__ in eventb_to_txt/__init__.py")
    return match.group(1)


setuptools.setup(
    name="eventb-to-txt",
    version=read_version(),
    author="Ilya Shchepetkov",
    author_email="ilya.shchepetkov@gmail.com",
    license="MIT",
    description="Event-B to txt converter",
    long_description=open("README.md", encoding="utf8").read(),
    long_description_content_type="text/markdown",
    python_requires=">=3.9",
    url="https://github.com/eventb-rossi/eventb-to-txt",
    packages=["eventb_to_txt"],
    entry_points={
        "console_scripts": [
            "eventb-to-txt=eventb_to_txt.__main__:main",
        ],
    },
    classifiers=(
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Programming Language :: Python :: 3.14",
        "Programming Language :: Python :: Implementation :: CPython",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
    ),
)
