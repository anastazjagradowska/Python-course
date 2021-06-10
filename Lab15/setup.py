from distutils.core import setup, Extension
setup(name='mod', version='1.0', ext_modules=[Extension('mod', sources=['mod.c'])])
