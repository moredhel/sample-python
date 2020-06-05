"""
sample tests
"""

import unittest
import pkg.util


class MyTest(unittest.TestCase):
    """
    Sample Test cases
    """
    def test_exists(self):
        """
        sample test case
        """
        self.assertEqual(pkg.util.HELLO, 'world')

    def test_ping(self):
        """
        sample ping
        """
        self.assertEqual(pkg.util.ping(), 'pong')
