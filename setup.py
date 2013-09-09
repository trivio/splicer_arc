import os.path
from setuptools import setup

HERE = os.path.abspath(os.path.dirname(__file__))

README_PATH = os.path.join(HERE, 'README.md')
try:
    README = open(README_PATH).read()
except IOError:
    README = ''


setup(
  name='splicer_arc_file',

  version='0.0.1',
  description='ARC File support for splicer',
  long_description=README,
  author='Scott Robertson',
  author_email='scott@triv.io',
  url='http://github.com/trivio/splicer_arc_file',
  classifiers=[
      "Programming Language :: Python",
      "License :: OSI Approved :: MIT License",
      "Operating System :: OS Independent",
      "Development Status :: 3 - Alpha",
      "Intended Audience :: Developers",
      "Topic :: Software Development",
  ],

  py_modules = ['splicer_arc'],

  install_requires = [
    'splicer',
    'warc'
  ],
 
  setup_requires=[
    'nose>=1.3.0',
    'coverage'
  ]
)
