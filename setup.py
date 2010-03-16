#!/usr/bin/env python

from ez_setup import use_setuptools
use_setuptools()

from setuptools import setup, find_packages
setup(
    name = "kibot-echo",
    version = "0.1",
    author = "Peter Teichman",
    author_email = "peter@teichman.org",
    url = "http://wiki.github.com/pteichman/kibot-echo/",
    description = "An example Kibot module.",
    packages = find_packages(),
    namespace_packages = ["kibot", "kibot.modules"],
    classifiers = [
        "Development Status :: 5 - Production/Stable",
        "Environment :: Plugins",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Topic :: Communications :: Chat :: Internet Relay Chat"
    ],
    entry_points = {
        "kibot.modules" : [
            "echo = kibot.modules.echo"
        ]
    }
)
