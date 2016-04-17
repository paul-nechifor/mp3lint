from setuptools import setup, find_packages

setup(
    name='mp3lint',
    version='0.0.0',
    author='Paul Nechifor',
    author_email='paul@nechifor.net',
    description='A linter for my MP3 collection.',
    packages=find_packages(),
    long_description=open('README.rst').read(),
    entry_points={'console_scripts': ['mp3lint=mp3lint:entry_point']},
    install_requires=['six==1.10.0'],
    license='ISC',
    url='http://github.com/paul-nechifor/mp3lint',
)
