import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.md')) as f:
    README = f.read()

requires = [
    'gces>=0.0.9a0',
]

tests_require = [
    'pytest',
    'pytest-cov',
    'pytest-mock',
    'pytest-capturelog>=0.7',
]

setup(
    name='gces_subsfm',
    version='0.0.1a0',
    description='GCES Subscriber Framework',
    long_description=README,
    long_description_content_type='text/markdown',
    classifiers=[
        'Programming Language :: Python',
        'Framework :: GCES',
    ],
    author='Daniel Debonzi',
    author_email='debonzi@gmail.com',
    url='',
    keywords='pubsub gces google',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    extras_require={
        'testing': tests_require,
    },
    install_requires=requires,
    entry_points = {
        'console_scripts': [
            'gces-subsfm = gces_subsfm:main'
        ]
    }
)
