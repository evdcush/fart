import io
import os
import re

from setuptools import find_packages
from setuptools import setup


def read(filename):
    filename = os.path.join(os.path.dirname(__file__), filename)
    text_type = type(u"")
    with io.open(filename, mode="r", encoding='utf-8') as fd:
        return re.sub(text_type(r':[a-z]+:`~?(.*?)`'), text_type(r'``\1``'), fd.read())


setup(
    name="fart",
    version="0.1.3",
    url="https://github.com/evdcush/fart",
    license='BSD-3-Clause',

    author="Evan Cushing",
    author_email="evdcush@protonmail.com",

    description="FARt all over your documentation",
    long_description=read("README.rst"),

    packages=find_packages(exclude=('tests',)),

    install_requires=['pyperclip'],

    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    entry_points={
        "console_scripts": [
            "fart=fart.fart:main",
        ]
    }
)
