import unittest

import LookAndSay


class TestLookAndSay(unittest.TestCase):
    def setUp(self):
        pass

    def test_LastTestInput(self):
        self.assertEqual('312211', LookAndSay.translate(str(111221)))
