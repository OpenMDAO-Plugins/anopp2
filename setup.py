#
# This file is autogenerated during plugin quickstart and overwritten during
# plugin makedist. DO NOT CHANGE IT if you plan to use plugin makedist to update 
# the distribution.
#

from setuptools import setup, find_packages

kwargs = {'author': '',
 'author_email': '',
 'classifiers': ['Intended Audience :: Science/Research',
                 'Topic :: Scientific/Engineering'],
 'description': '',
 'download_url': '',
 'entry_points': '[openmdao.anopp2]\nanopp2.anopp2.anopp2=anopp2.anopp2:anopp2',
 'include_package_data': True,
 'install_requires': ['openmdao.main'],
 'keywords': ['openmdao'],
 'license': '',
 'maintainer': '',
 'maintainer_email': '',
 'name': 'Anopp2',
 'package_data': {'anopp2': []},
 'package_dir': {'': 'src'},
 'packages': ['anopp2','anopp2.test'],
 'url': '',
 'version': '0.1',
 'zip_safe': False}


setup(**kwargs)
