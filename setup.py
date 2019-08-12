from setuptools import setup, find_packages
from os.path import join, dirname

NAME = 'fake_usrag_bor'
VERSION = __import__('fake_usrag_bor').__version__
AUTHOR = 'oskarmenrus'
AUTHOR_EMAIL = 'oskarmenrus@gmail.com'
URL = 'https://github.com/oskarmenrus'
KEYWORDS = [
    'user', 'agent', 'user agent', 'useragent',
    'fake', 'fake useragent', 'fake user agent',
]


def description():
    return open(join(dirname(__file__), 'README.md')).read()


setup(
    name=NAME,
    version=VERSION,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    url=URL,
    description='Simple package with fake user agents for your requests.',
    long_description=description(),
    long_description_content_type='text/markdown',
    packages=find_packages(),
    install_requires=[],  # Requires for project
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    keywords=KEYWORDS,
)
