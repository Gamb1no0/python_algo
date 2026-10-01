import unittest

from anagrams import group_anagrams


class TestGroupAnagrams(unittest.TestCase):
    def assert_groups_equal(self, actual, expected):
        # Порядок групп и слов не важен, но повторы должны сохраниться.
        self.assertEqual(
            sorted(tuple(sorted(group)) for group in actual),
            sorted(tuple(sorted(group)) for group in expected),
        )

    def test_example(self):
        words = ["eat", "tea", "tan", "ate", "nat", "bat"]
        expected = [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
        self.assert_groups_equal(group_anagrams(words), expected)

    def test_empty_list(self):
        self.assertEqual(group_anagrams([]), [])

    def test_single_word(self):
        self.assertEqual(group_anagrams(["hello"]), [["hello"]])

    def test_empty_words(self):
        self.assert_groups_equal(
            group_anagrams(["", "a", "", ""]), [["", "", ""], ["a"]]
        )

    def test_repeated_words(self):
        self.assert_groups_equal(
            group_anagrams(["eat", "eat", "tea", "bat", "bat"]),
            [["eat", "eat", "tea"], ["bat", "bat"]],
        )

    def test_no_anagrams(self):
        self.assert_groups_equal(
            group_anagrams(["a", "bb", "cat", "dog"]),
            [["a"], ["bb"], ["cat"], ["dog"]],
        )

    def test_all_in_one_group(self):
        self.assert_groups_equal(
            group_anagrams(["abc", "cba", "bac", "cab"]),
            [["abc", "cba", "bac", "cab"]],
        )

    def test_different_letter_counts(self):
        self.assert_groups_equal(
            group_anagrams(["abb", "aab", "bba", "aba", "ab"]),
            [["abb", "bba"], ["aab", "aba"], ["ab"]],
        )

    def test_unicode(self):
        self.assert_groups_equal(
            group_anagrams(["кот", "ток", "окт", "дом", "мод"]),
            [["кот", "ток", "окт"], ["дом", "мод"]],
        )

    def test_case_sensitive(self):
        self.assert_groups_equal(
            group_anagrams(["Eat", "tea", "atE", "Tea"]),
            [["Eat", "atE"], ["tea"], ["Tea"]],
        )

    def test_spaces_and_punctuation(self):
        self.assert_groups_equal(
            group_anagrams(["a!", "!a", "a ", " a", "a"]),
            [["a!", "!a"], ["a ", " a"], ["a"]],
        )

    def test_input_unchanged(self):
        words = ["tea", "bat", "eat", "tea"]
        original = words.copy()
        group_anagrams(words)
        self.assertEqual(words, original)

    def test_first_seen_order(self):
        self.assertEqual(
            group_anagrams(["tea", "tan", "eat", "bat", "nat", "ate"]),
            [["tea", "eat", "ate"], ["tan", "nat"], ["bat"]],
        )


if __name__ == "__main__":
    unittest.main()
