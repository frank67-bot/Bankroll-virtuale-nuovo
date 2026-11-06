import unittest
from src.bankroll import analyze

class TestBankroll(unittest.TestCase):
    def test_value(self):
        result = analyze({'1': 2.2, 'X': 3.3, '2': 3.6}, {'1': .5, 'X': .28, '2': .22})
        self.assertAlmostEqual(result['1']['roi_atteso'], .1)
        self.assertAlmostEqual(sum(x['mercato_senza_margine'] for x in result.values()), 1)

    def test_bad_probabilities(self):
        with self.assertRaises(ValueError):
            analyze({'1': 2, 'X': 3, '2': 4}, {'1': .5, 'X': .5, '2': .5})
