#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""


$Id$
"""

from __future__ import print_function, unicode_literals, absolute_import, division
__docformat__ = "restructuredtext en"


import nose.plugins

class NoseTracebackInfoPlugin(nose.plugins.Plugin):

	name = 'nose_traceback_info'
	score = 1000
	enabled = True # Enabled by default

	def configure(self, options, conf ):
		# Force the logcapture plugin, enabled by default,
		# to use the zope exception formatter.
		import zope.exceptions.log
		import logging
		logging.Formatter = zope.exceptions.log.Formatter

	# Also present failure cases formatted the same way
	def formatError(self, test, exc_info):
		t, v, tb = exc_info
		from zope.exceptions.exceptionformatter import format_exception
		# Despite what the docs say, you do not return the test.
		# see logcapture and failuredetail.
		# Omitting filenames makes things shorter
		# and generally more readable, but when the last part of the traceback
		# is in initializing a module, then the filename is the only discriminator

		# Note that we are joining with a byte string, not a unicode string. Under
		# python2, tracebacks are byte strings and mixing unicode at this level may
		# result in UnicodeDecodeError
		formatted_tb = b''.join(format_exception(t, v, tb, with_filenames=False))
		if b'Module None' in formatted_tb:
			formatted_tb = b''.join(format_exception(t, v, tb, with_filenames=True))
		return (t, formatted_tb, None)

	def formatFailure(self, test, exc_info):
		return self.formatError( test, exc_info)
