import unittest

from detect_characters_in_text import detect_character_by_ai, Character


class TestDetectCharactersByAIE2E(unittest.TestCase):
    def test_detect_character_by_ai_e2e(self):
        sample_text = """
        John Doe is a 35-year-old detective. You can reach him at 555-1234.
        His partner, Jane Smith, is 28 years old. Her phone number is 555-5678.
        """

        result = detect_character_by_ai(sample_text)

        self.assertIsInstance(result, list)

        sorted_result = sorted(
            result, key=lambda _character: _character.age, reverse=True
        )

        self.assertEqual(len(sorted_result), 2)
        self.assertEqual(sorted_result[0].first_name, "John")
        self.assertEqual(sorted_result[0].last_name, "Doe")
        self.assertEqual(sorted_result[0].age, 35)
        self.assertEqual(sorted_result[0].phone_number, "555-1234")

        self.assertEqual(sorted_result[1].first_name, "Jane")
        self.assertEqual(sorted_result[1].last_name, "Smith")
        self.assertEqual(sorted_result[1].age, 28)
        self.assertEqual(sorted_result[1].phone_number, "555-5678")

    def test_detect_character_by_ai_no_characters(self):
        sample_text = "This is a simple expression without any character information."

        result = detect_character_by_ai(sample_text)

        self.assertIsInstance(result, list)

        for character in result:
            self.assertIsInstance(character, Character)


if __name__ == "__main__":
    unittest.main()
