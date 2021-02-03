# setup.py

from distutils.core import setup, Extension

expint_module = Extension('_expint', sources=['expint_wrap.cxx', 'expint.cpp', 'expint_asymp.cpp', 'expint_ei.cpp', 'expint_series.cpp'],extra_link_args=["-mmacosx-version-min=10.15"])

setup(name='expint', ext_modules=[expint_module], py_modules=["expint"])