#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

requirements = [ ]

test_requirements = ['pytest>=3', ]

setup(
    author="Jean Dos Santos",
    author_email='jeandsantos88@gmail.com',
    python_requires='>=3.9',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.9',
    ],
    description="",
    install_requires=requirements,
    license="MIT license",
    long_description="",
    include_package_data=True,
    keywords='my_test_package',
    name='my_test_package',
    packages=find_packages(include=['my_test_package']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/jeandsantos/unit-tests-with-travis-ci',
    version='0.0.1',
    zip_safe=False,
)
