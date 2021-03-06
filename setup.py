#!/usr/bin/env python

import sys,time,urllib.request,urllib.parse,urllib.error,traceback,glob,os,os.path

from distutils.core import setup #, Extension, Command
#from distutils.command.install_data import install_data


scripts = [c for c in glob.glob("ocropus-*") if "." not in c and "~" not in c]

setup(
    name = 'ocropy',
    version = 'v0.2',
    author = "Thomas Breuel",
    description = "The OCRopy RNN-based Text Line Recognizer",
    packages = ["ocrolib"],
    data_files= [('share/ocropus', ["models/en-default.pyrnn.gz"])],
    scripts = scripts,
    )
