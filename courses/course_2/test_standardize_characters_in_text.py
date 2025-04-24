import unittest

from courses.course_2.data import get_sample_text
from standardize_characters_in_text import standardize_character_by_ai


class TestStandardizeCharactersByAIE2E(unittest.TestCase):
    def test_standardize_character_by_ai_e2e(self):
        result = standardize_character_by_ai(get_sample_text())

        self.assertIsInstance(result, list)

        sorted_result = sorted(
            result, key=lambda _character: _character.age, reverse=True
        )

        self.assertEqual(len(sorted_result), 4)

        self.assertEqual(sorted_result[0].first_name, "Pierre")
        self.assertEqual(sorted_result[0].last_name, "Dupont")
        self.assertEqual(sorted_result[0].age, 45)
        self.assertEqual(sorted_result[0].phone_number, "+339991234")
        self.assertEqual(sorted_result[0].country_code, "FRA")

        self.assertEqual(sorted_result[1].first_name, "John")
        self.assertEqual(sorted_result[1].last_name, "Smith")
        self.assertEqual(sorted_result[1].age, 40)
        self.assertEqual(sorted_result[1].phone_number, "+15559876")
        self.assertEqual(sorted_result[1].country_code, "USA")

        self.assertEqual(sorted_result[2].first_name, "Emily")
        self.assertEqual(sorted_result[2].last_name, "Thomas")
        self.assertEqual(sorted_result[2].age, 32)
        self.assertEqual(sorted_result[2].country_code, "USA")
        self.assertEqual(sorted_result[2].phone_number, "+15556543")

        self.assertEqual(sorted_result[3].first_name, "Sato")
        self.assertEqual(sorted_result[3].last_name, "Hiroshi")
        self.assertEqual(sorted_result[3].age, 28)
        self.assertEqual(sorted_result[3].phone_number, "+815559870")
        self.assertEqual(sorted_result[3].country_code, "JPN")


if __name__ == "__main__":
    unittest.main()
