import unittest
from poker import PokerHand, Result, sort_cards_values, is_royal_flush, is_straight, is_flush, is_n_kind, is_two_pair

class TestPokerFunctions(unittest.TestCase):
    def test_sort_cards_values(self):
        hand = ["7C", "8S", "9H", "TH", "JH"]
        self.assertEqual(sort_cards_values(hand), [11, 10, 9, 8, 7])
    
    def test_is_royal_flush(self):
        hand = ["JC", "KC", "TC", "QC", "AC"]
        ranks = sort_cards_values(hand)
        self.assertTrue(is_royal_flush(ranks, hand))

    def test_is_straight(self):
        hand = ["2C", "3H", "4C", "5H", "6C"]
        self.assertTrue(is_straight(sort_cards_values(hand)))

    def test_is_flush(self):
        hand = ["2C", "8C", "4C", "TC", "6C"]
        self.assertTrue(is_flush(hand))


class TestPokerHand(unittest.TestCase):
    def tests(self):
        self.assertTrue(PokerHand("TC TH 5C 5H KH").compare_with(PokerHand("9C 9H 5C 5H AC")) == Result.WIN)
        self.assertTrue(PokerHand("TS TD KC JC 7C").compare_with(PokerHand("JS JC AS KC TD")) == Result.LOSS)
        self.assertTrue(PokerHand("7H 7C QC JS TS").compare_with(PokerHand("7D 7C JS TS 6D")) == Result.WIN)
        self.assertTrue(PokerHand("5S 5D 8C 7S 6H").compare_with(PokerHand("7D 7S 5S 5D JS")) == Result.LOSS)
        self.assertTrue(PokerHand("AS AD KD 7C 3D").compare_with(PokerHand("AD AH KD 7C 4S")) == Result.LOSS)
        self.assertTrue(PokerHand("TS JS QS KS AS").compare_with(PokerHand("AC AH AS AS KS")) == Result.WIN)
        self.assertTrue(PokerHand("TS JS QS KS AS").compare_with(PokerHand("TC JS QC KS AC")) == Result.WIN)
        self.assertTrue(PokerHand("TS JS QS KS AS").compare_with(PokerHand("QH QS QC AS 8H")) == Result.WIN)
        self.assertTrue(PokerHand("AC AH AS AS KS").compare_with(PokerHand("TC JS QC KS AC")) == Result.WIN)
        self.assertTrue(PokerHand("AC AH AS AS KS").compare_with(PokerHand("QH QS QC AS 8H")) == Result.WIN)
        self.assertTrue(PokerHand("TC JS QC KS AC").compare_with(PokerHand("QH QS QC AS 8H")) == Result.WIN)
        self.assertTrue(PokerHand("7H 8H 9H TH JH").compare_with(PokerHand("JH JC JS JD TH")) == Result.WIN)
        self.assertTrue(PokerHand("7H 8H 9H TH JH").compare_with(PokerHand("4H 5H 9H TH JH")) == Result.WIN)
        self.assertTrue(PokerHand("7H 8H 9H TH JH").compare_with(PokerHand("7C 8S 9H TH JH")) == Result.WIN)
        self.assertTrue(PokerHand("7H 8H 9H TH JH").compare_with(PokerHand("TS TH TD JH JD")) == Result.WIN)
        self.assertTrue(PokerHand("7H 8H 9H TH JH").compare_with(PokerHand("JH JD TH TC 4C")) == Result.WIN)
        self.assertTrue(PokerHand("JH JC JS JD TH").compare_with(PokerHand("4H 5H 9H TH JH")) == Result.WIN)
        self.assertTrue(PokerHand("JH JC JS JD TH").compare_with(PokerHand("7C 8S 9H TH JH")) == Result.WIN)
        self.assertTrue(PokerHand("JH JC JS JD TH").compare_with(PokerHand("TS TH TD JH JD")) == Result.WIN)
        self.assertTrue(PokerHand("JH JC JS JD TH").compare_with(PokerHand("JH JD TH TC 4C")) == Result.WIN)
        self.assertTrue(PokerHand("4H 5H 9H TH JH").compare_with(PokerHand("7C 8S 9H TH JH")) == Result.WIN)
        self.assertTrue(PokerHand("4H 5H 9H TH JH").compare_with(PokerHand("TS TH TD JH JD")) == Result.LOSS)
        self.assertTrue(PokerHand("4H 5H 9H TH JH").compare_with(PokerHand("JH JD TH TC 4C")) == Result.WIN)
        self.assertTrue(PokerHand("7C 8S 9H TH JH").compare_with(PokerHand("TS TH TD JH JD")) == Result.LOSS)
        self.assertTrue(PokerHand("7C 8S 9H TH JH").compare_with(PokerHand("JH JD TH TC 4C")) == Result.WIN)
        self.assertTrue(PokerHand("TS TH TD JH JD").compare_with(PokerHand("JH JD TH TC 4C")) == Result.WIN)

if __name__ == "__main__":
    unittest.main()