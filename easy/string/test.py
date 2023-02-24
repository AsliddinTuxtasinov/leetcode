import unittest
from easy_1221 import balancedStringSplit
from easy_1832 import checkIfPangram
from easy_2325 import decodeMessage


class TestStringProblemSolves(unittest.TestCase):
    
    def test_balancedStringSplit_1221(self):
        self.assertEqual(
            first=balancedStringSplit(s="RLRRLLRLRL"), 
            second=4, 
            msg="Should be 4"
        )

    def test_checkIfPangram_1832(self):
        self.assertEqual(
            first=checkIfPangram(sentence="thequickbrownfoxjumpsoverthelazydog"),
            second=True,
            msg="Should be: True"
        )

    def test_decodeMessage_2325(self):
        self.assertEqual(
            first=decodeMessage(
                key = "the quick brown fox jumps over the lazy dog",
                message = "vkbs bs t suepuv"
            ),

            second="this is a secret",
            msg="Should be: this is a secret"
        )


if __name__ == '__main__':
    unittest.main()

