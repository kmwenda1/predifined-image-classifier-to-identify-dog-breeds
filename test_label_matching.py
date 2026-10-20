#!/usr/bin/env python3

import unittest

from calculates_results_stats import calculates_results_stats
from label_matching import is_label_match


class TestLabelMatching(unittest.TestCase):
    def test_cat_matches_synonym_list(self):
        self.assertTrue(is_label_match("cat", "tabby, tabby cat, cat"))

    def test_cat_does_not_match_catamount(self):
        self.assertFalse(is_label_match("cat", "lynx, catamount"))

    def test_dog_matches_synonym_list(self):
        self.assertTrue(
            is_label_match(
                "dog",
                "german shepherd, german shepherd dog, german police dog, alsatian",
            )
        )

    def test_dog_does_not_match_redbone(self):
        self.assertFalse(is_label_match("dog", "redbone"))

    def test_chair_matches_folding_chair(self):
        self.assertTrue(is_label_match("chair", "folding chair"))

    def test_boston_terrier_matches(self):
        self.assertTrue(is_label_match("boston terrier", "boston bull, boston terrier"))

    def test_empty_truth_is_false(self):
        self.assertFalse(is_label_match("", "tabby, tabby cat, cat"))


class TestCalculateResultsStats(unittest.TestCase):
    def test_no_dog_images_sets_dog_percentages_to_zero(self):
        results_dic = {
            "chair_01.jpg": ["chair", "folding chair", 1, 0, 0],
        }
        stats = calculates_results_stats(results_dic)
        self.assertEqual(stats["pct_correct_dogs"], 0.0)
        self.assertEqual(stats["pct_correct_breed"], 0.0)


if __name__ == "__main__":
    unittest.main()
