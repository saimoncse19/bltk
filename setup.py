from setuptools import setup, find_namespace_packages

setup(
  name='bltk',
  packages=find_namespace_packages(include=['bltk.*']),
  include_package_data=True,
  version='0.1',
  license='MIT',
  description='A lightweight but robust toolkit for Bengali Natural Language Processing.',
  maintainer="Saimon Hossain",
  maintainer_email="saimoncse19@gmail.com",
  author='Saimon Hossain',
  author_email='saimoncse19@gmail.com',
  url='https://github.com/saimoncse19/bltk',
  download_url='https://github.com/saimoncse19/bltk/archive/v0.1.tar.gz',
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
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    "Operating System :: OS Independent",
  ],
  python_requires='>=3.6',
)
