# glowprom
# Copyright (C) 2020 Andrew Wilkinson
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import os

import setuptools

try:
    from glowprom import __version__
except ImportError:
    import re

    with open('glowprom.egg-info/PKG-INFO') as f:
        __version__ = re.search("^Version: (.*)$", f.read(), re.MULTILINE).group(1)

with open("README.md", "r") as fh:
    long_description = fh.read()

with open('requirements.txt' if os.path.exists('requirements.txt') else 'glowprom.egg-info/requires.txt') as f:
    requirements = f.read().splitlines()

setuptools.setup(
    name="glowprom", # Replace with your own username
    version=__version__,
    author="Andrew Wilkinson",
    author_email="andrewjwilkinson@gmail.com",
    description="Receives gas and electric meter data from https://glowmarkt.com/ and exposes it to Prometheus.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/andrewjw/glowprom",
    packages=setuptools.find_packages(),
    scripts=["bin/glowprom"],
    classifiers=[
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.9',
    install_requires=requirements,
)
