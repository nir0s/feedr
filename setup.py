from setuptools import setup
# from setuptools import find_packages
from setuptools.command.test import test as TestCommand
import sys
import re
import os
import codecs

here = os.path.abspath(os.path.dirname(__file__))


def read(*parts):
    # intentionally *not* adding an encoding option to open
    return codecs.open(os.path.join(here, *parts), 'r').read()


def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        print('VERSION: ', version_match.group(1))
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


class Tox(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        #import here, cause outside the eggs aren't loaded
        import tox
        errcode = tox.cmdline(self.test_args)
        sys.exit(errcode)

setup(
    name='feeder',
    version=find_version('feeder', '__init__.py'),
    url='https://github.com/nir0s/feeder',
    download_url='https://github.com/nir0s/feeder/tarball/0.1',
    author='nir0s',
    author_email='nir36g@gmail.com',
    license='LICENSE',
    platforms='All',
    description='Data Feeder using different transports',
    long_description=read('README.rst'),
    packages=['feeder'],
    entry_points={
        'console_scripts': [
            'mouth = feeder.cli:main',
        ]
    },
    install_requires=[
        "docopt==.0.6.1",
        "pika==0.9.13",
        "fake-factory>=0.4.0",
        "infi.docopt_completion==0.2.1",
        "prettytable==0.7.2",
        "elasticsearch==1.1.1",
        "LogentriesLogger==0.2.1",
        "pymongo==2.7.1",
        "influxdb==0.1.12",
    ],
    tests_require=['nose', 'tox'],
    cmdclass={'test': Tox},
    classifiers=[
        'Programming Language :: Python',
        'Development Status :: 3 - Alpha',
        'Natural Language :: English',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: POSIX :: Linux',
        'Operating System :: Microsoft',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Testing',
        'Topic :: System :: Logging',
    ],
)
