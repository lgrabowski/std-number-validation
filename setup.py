from setuptools import setup, find_packages

install_requires = [
    'six'
]

tests_require = [
    'mock',
    'pytest',
    ]

setup_requires=[
   'pytest-runner'
]

setup(
    name='std_number_validation',
    version=open('Changelog').readline().strip().split()[-1],
    license=open('LICENSE').read().strip(),
    author='Luigi',
    author_email='luigi@lgrabowski.pl',
    url='http://lgrabowski.pl',
    description='standard numbers and codes validation',
    long_description=open('README.md').read().strip(),
    packages=find_packages(),
    install_requires=install_requires,
    tests_require=tests_require,
    setup_requires=setup_requires,
    test_suite='tests',
)


