
from setuptools import setup

setup(
    name='aquacropeto',
    version='0.2.0',
    description=(
        'Library for estimating reference and potential evapotranspiration.'
    ),
    long_description=open('README.rst').read(),
    author='Tom Kelly',
    author_email='REMOVETHIS@gmail.com',
    license='BSD 3-Clause',
    url='None',
    packages=['aquacropeto'],
    package_data={'': ['*.rst', '*.txt']},
    test_suite='tests',
    classifiers=[
        'Programming Language :: Python',
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        'Programming Language :: Python :: Implementation :: PyPy',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Intended Audience :: Science/Research',
        'Development Status :: 3 - Alpha',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Atmospheric Science',
    ],
)
