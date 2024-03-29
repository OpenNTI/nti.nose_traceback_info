#!/usr/bin/env python
import codecs
from setuptools import setup, find_packages

VERSION = '1.0.3.dev0'

entry_points = {
	"nose.plugins.0.10" : [
		"nosetracebackinfo = nti.nose_traceback_info:NoseTracebackInfoPlugin"
	],
}

setup(
	name = 'nti.nose_traceback_info',
	version = VERSION,
	author = 'Jason Madden',
	author_email = 'open-source@nextthought.com',
	description = ('Include __traceback_info__ in tracebacks printed by nose'),
	long_description = codecs.open('README.rst', encoding='utf-8').read() + '\n\n' + codecs.open('CHANGES.rst', encoding='utf-8').read(),
	license = 'Apache',
	keywords = 'nose exceptions zope',
	url = 'https://github.com/OpenNTI/nti.nose_traceback_info',
	classifiers = [
		'Development Status :: 5 - Production/Stable',
		'Intended Audience :: Developers',
		'License :: OSI Approved :: Apache Software License',
		'Natural Language :: English',
		'Operating System :: OS Independent',
		'Programming Language :: Python :: 2',
		'Programming Language :: Python :: 2.7',
		'Programming Language :: Python :: 3',
		'Programming Language :: Python :: 3.2',
		'Programming Language :: Python :: 3.3',
		'Programming Language :: Python :: 3.4',
		'Topic :: Software Development :: Testing',
		"Programming Language :: Python :: Implementation :: CPython",
		"Programming Language :: Python :: Implementation :: PyPy",
		'Framework :: Zope3'
		],
	packages=find_packages('src'),
	package_dir={'': 'src'},
	install_requires=[
		'setuptools',
		'nose >= 1.3.0',
		'zope.exceptions >= 4.0.6'
	],
	namespace_packages=['nti'],
	entry_points=entry_points
)
