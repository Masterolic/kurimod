import unittest

from kurimod.types.identifier import Identifier


class IdentifierTests(unittest.TestCase):
    def test_empty_pattern_matches_any_identifier(self):
        self.assertTrue(Identifier().matches(Identifier(chat_id=123, message_id=9)))

    def test_matching_scalar_values(self):
        pattern = Identifier(chat_id=123, message_id=9)
        self.assertTrue(pattern.matches(Identifier(chat_id=123, message_id=9)))

    def test_non_matching_scalar_values(self):
        pattern = Identifier(chat_id=123)
        self.assertFalse(pattern.matches(Identifier(chat_id=456)))

    def test_pattern_list_matches_intersecting_update_list(self):
        pattern = Identifier(chat_id=[123, 456])
        self.assertTrue(pattern.matches(Identifier(chat_id=[456, 789])))

    def test_pattern_list_rejects_non_intersecting_update_list(self):
        pattern = Identifier(chat_id=[123, 456])
        self.assertFalse(pattern.matches(Identifier(chat_id=[789, 987])))

    def test_pattern_list_matches_scalar_update(self):
        pattern = Identifier(chat_id=[123, 456])
        self.assertTrue(pattern.matches(Identifier(chat_id=456)))

    def test_scalar_pattern_matches_list_update(self):
        pattern = Identifier(chat_id=456)
        self.assertTrue(pattern.matches(Identifier(chat_id=[123, 456])))

    def test_none_pattern_fields_are_ignored(self):
        pattern = Identifier(chat_id=123)
        self.assertTrue(
            pattern.matches(
                Identifier(chat_id=123, message_id=99, from_user_id=456)
            )
        )

    def test_count_populated(self):
        identifier = Identifier(chat_id=123, message_id=9)
        self.assertEqual(identifier.count_populated(), 2)
        self.assertEqual(Identifier().count_populated(), 0)


if __name__ == "__main__":
    unittest.main()
