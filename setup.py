from setuptools import setup, find_packages

setup(
    name='compress_pickle',
    url='https://github.com/sorig/compress_pickle',
    version='0.1',
    description='Wrapper around pickle, gzip, and tarfile allowing easy handling of compressed pickle files',
    author='Esben Sørig',
    author_email='esben@sorig.eu',
    license='BSD3',
    packages=find_packages('.', exclude=["*tests*", "*.develop"])
)
