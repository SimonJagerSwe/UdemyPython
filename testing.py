########## TESTING ##########
import unittest
import test_main

class TestMain(unittest.TestCase):
    def test_do_stuff(self):
        test_param = 10
        result = test_main.do_stuff(test_param)
        self.assertEqual(result, 15)

unittest.main()