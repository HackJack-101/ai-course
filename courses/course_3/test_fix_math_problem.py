import unittest


from courses.course_3.response import solve_algebra, apply_calculations


class TestFixMathProblem(unittest.TestCase):
    def test_solve_algebra(self):
        result = solve_algebra("2+3*9+10^2")

        print(result)
        self.assertEqual(apply_calculations(result.answer), 129)


if __name__ == "__main__":
    unittest.main()
