'''One-line description of package

'''
from setuptools import setup
from os import path

try:
    import pypandoc
    long_description = pypandoc.convert('README.md', 'rst')
    long_description = long_description.replace("\r","") # Do not forget this line
except:
    print("Pandoc not found. Long_description conversion failure.")

    # pandoc is not installed, fallback to using raw contents
    with open('README.md') as f:
        long_description = f.read()

from waterconnect import __version__

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

WHITESPACE_SEP_KEYWORDS = ''

CLASSIFIERS = [
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.2",
    "Programming Language :: Python :: 3.3",
    "Programming Language :: Python :: 3.4",
    "Programming Language :: Python :: 3.5",
    "Programming Language :: Python :: 3.6",
    "Topic :: Scientific/Engineering",
    ]


setup(name='waterconnect',
      version=__version__,
      description=__doc__,
      long_description=long_description,
      url="https://github.com/kinverarity1/waterconnect",
      author="Kent Inverarity",
      author_email="kinverarity@hotmail.com",
      license="MIT",
      classifiers=CLASSIFIERS,
      keywords=WHITESPACE_SEP_KEYWORDS,
      packages=['waterconnect', ],
      install_requires=requirements,
      entry_points={
          'console_scripts': [
              # 'script_executable_name = waterconnect.module:function',
          ],
      }
      )
