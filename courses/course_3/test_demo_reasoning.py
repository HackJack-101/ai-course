import unittest


from courses.course_3.demo_reasoning import chain_of_thought


class TestChainOfThought(unittest.TestCase):
    def test_chain_of_thought_phi4(self):
        result = chain_of_thought(
            question="What is the result of 2+3*9+10^2 ?", model="phi4-mini"
        )

        print(result)
        self.assertEqual(result.answer, 129.0)

    def test_chain_of_thought_mistral(self):
        result = chain_of_thought(
            question="What is the result of 2+3*9+10^2 ?", model="mistral:latest"
        )

        print(result)
        self.assertEqual(result.answer, 129.0)


if __name__ == "__main__":
    unittest.main()
