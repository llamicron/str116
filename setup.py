from setuptools import setup, find_packages
from codecs import open
from os import path

dependencies = []

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='str116',
    version='0.0.1',
    description='A driver for the str116 relay board',
    long_description=long_description,
    url='https://github.com/llamicron/str116',
    author='llamicron',
    author_email='llamicron@gmail.com',
    keywords='str116 relay raspberry pi brewing controller board',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    install_requires=dependencies,
    extras_require={
        'dev': [],
        'test': [],
    },
    # To provide executable scripts, use entry points in preference to the
    # "scripts" keyword. Entry points provide cross-platform support and allow
    # `pip` to create the appropriate form of executable for the target
    # platform.
    #
    # For example, the following would provide a command called `sample` which
    # executes the function `main` from this package when invoked:
    # entry_points={
    #     'console_scripts': [
    #         'str116=str116:demo', # Maybe have an interactive CLI?
    #     ],
    # },
)
