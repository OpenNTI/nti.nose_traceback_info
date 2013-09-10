#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""


$Id$
"""

from __future__ import print_function, unicode_literals, absolute_import, division
__docformat__ = "restructuredtext en"

logger = __import__('logging').getLogger(__name__)

#disable: accessing protected members, too many methods
#pylint: disable=W0212,R0904


import sys
from unittest import TestCase

from nti.nose_traceback_info import NoseTracebackInfoPlugin

class TestNoseTracebackInfoPlugin(TestCase):

	def _throws(self, tbi, kind):
		__traceback_info__ = tbi
		raise kind()

	def setUp(self):
		self.plugin = NoseTracebackInfoPlugin()

	def test_format_failure(self):
		exc_info = None
		try:
			self._throws('abc', ValueError)
			self.fail("Must raise")
		except ValueError as v:
			exc_info = sys.exc_info()
			t, formatted, _ = self.plugin.formatFailure(None, exc_info)
			self.assertEqual( t, type(v) )
			lines = formatted.split('\n')
			self.assertEqual( lines[-2].strip(), 'ValueError' )
			self.assertEqual( lines[-3].strip(), '- __traceback_info__: abc' )
