﻿# To run pyprocgame under Snow Leopard when libs are compiled 32-bit: export VERSIONER_PYTHON_PREFER_32_BIT=yes

# From: http://superjared.com/entry/anatomy-python-c-module/
from distutils.core import setup, Extension
import os
import sys
import platform

extra_compile_args = ['-O0', '-g']
extra_compile_args.append('-Wno-write-strings')  # fix "warning: deprecated conversion from string constant to 'char*'"
extra_link_args = []

# To use the ARCH flag simply:
#   ARCH=x86_64 python setup.py build
if 'ARCH' in os.environ:
    extra_compile_args += ['-arch', os.environ['ARCH']]
    extra_link_args += ['-arch', os.environ['ARCH']]

if os.name == 'nt':
    # Windows
    libraries = ['pinproc', 'ftd2xx']
else:
    if platform.system() == "Linux":
        # Linux
        libraries = ['usb', 'ftdi', 'pinproc']
    else:
        # OS X
        libraries = ['usb', 'ftdi1', 'pinproc']

module1 = Extension("pinproc",
                    include_dirs=['../libpinproc/include'],
                    libraries=libraries,
                    library_dirs=['/usr/local/lib', '../libpinproc/bin'],
                    extra_compile_args=extra_compile_args,
                    extra_link_args=extra_link_args,
                    sources=['pypinproc.cpp', 'dmdutil.cpp', 'dmd.c'])

setup(name="pinproc",
      version="2.1",
      ext_modules=[module1])
