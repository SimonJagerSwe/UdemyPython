########## TESTING ##########
import unittest
import test_main


class TestMain(unittest.TestCase):
    def test_do_stuff(self):
        test_param = 10
        result = test_main.do_stuff(test_param)
        self.assertEqual(result, 15)

    def test_do_stuff2(self):
            test_param = 'asdadwea'
            result = test_main.do_stuff(test_param)
            self.assertIsInstance(result, ValueError)

    def test_do_stuff3(self):
         test_param = None
         result = test_main.do_stuff(test_param)
         self.assertEqual(result, 'Please enter number')

    def test_do_stuff4(self):
         test_param = ''
         result = test_main.do_stuff(test_param)
         self.assertEqual(result, 'Please enter number')
        
if __name__ == '__main__':
    unittest.main()