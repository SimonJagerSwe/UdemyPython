########## EXERCISE: TEST ##########
import unittest
import exercise_test

class TestGame(unittest.TestCase):
    def test_input(self):
        answer = 5
        guess = 5
        result = exercise_test.run_guess(answer, guess)
        self.assertTrue(result)

    def test_input_wrong_guess(self):
        result = exercise_test.run_guess(5, 0)
        self.assertFalse(result)

    def test_input_wrong_number(self):
        result = exercise_test.run_guess(5, 11)
        self.assertFalse(result)

    def test_input_string(self):
        result = exercise_test.run_guess(5, '11')
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()