#!/usr/bin/python

from setuptools import setup

setup(
    name="toothbrush",
    version="0.0.2",
    description="Receive BLE packets from Oral-B toothbrushC",
    url="https://github.com/molobrakos/toothbrush",
    license="",
    author="Erik",
    author_email="error.errorsson@gmail.com",
    scripts=["toothbrush"],
    py_modules=["toothbrush"],
    packages=[],
    install_requires=list(open("requirements.txt").read().strip().split("\n")),
    extras_require={"console": ["docopt"]},
)
