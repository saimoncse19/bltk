from setuptools import setup, find_namespace_packages
from os import path

with open(path.join(path.abspath(path.dirname(__file__)), 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
  name='bltk',
  packages=find_namespace_packages(include=['bltk.*']),
  include_package_data=True,
  version='1.2',
  license='MIT',
  description='A lightweight but robust toolkit for Bengali Natural Language Processing.',
  long_description=long_description,
  long_description_content_type='text/markdown',
  maintainer="Saimon Hossain",
  maintainer_email="saimoncse19@gmail.com",
  author='Saimon Hossain',
  author_email='saimoncse19@gmail.com',
  url='https://github.com/saimoncse19/bltk',
  download_url='https://github.com/saimoncse19/bltk/archive/v1.2.tar.gz',
  keywords=['pos-tagger', 'pos tagger', 'phrase chunker', 'phrase-chunker', 'stemmer',
            'bengali', 'natural language processing', 'Machine learning', 'NLP'],
  install_requires=[
      'sklearn >=0.0',
      'six >=1.13.0',
      'scipy >=1.4.1',
      'scikit-learn >=0.21.3',
      'numpy >=1.18.1',
      'nltk >=3.4.5',
      'joblib >=0.14.1',
      'certifi >=2019.11.28'


  ],
  classifiers=[
    "Development Status :: 5 - Production/Stable",
    "Intended Audience :: Developers",
    'Intended Audience :: Education',
    'Natural Language :: English',
    'Natural Language :: Bengali',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3 :: Only',
    "Operating System :: OS Independent",
  ],
  python_requires='>=3.6',
)
