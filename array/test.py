import unittest

from array.easy.easy_1920 import buildArray
from array.easy.easy_1929 import getConcatenation
from array.easy.easy_1470 import shuffle
from array.easy.easy_1480 import runningSum


class TestSum(unittest.TestCase):
    def test_buildArray_easy_1920(self):
        self.assertEqual(
            first=buildArray(nums=[5, 0, 1, 2, 3, 4]),
            second=[4, 5, 0, 1, 2, 3],
            msg="Should be [4, 5, 0, 1, 2, 3]",
        )

    def test_getConcatenation_easy_1929(self):
        self.assertEqual(
            first=getConcatenation(nums=[1, 2, 1]),
            second=[1, 2, 1, 1, 2, 1],
            msg="Should be [1, 2, 1, 1, 2, 1]",
        )

    def test_shuffle_easy_1970(self):
        self.assertEqual(
            first=shuffle(nums=[2, 5, 1, 3, 4, 7], n=3),
            second=[2, 3, 5, 4, 1, 7],
            msg="Should be [2, 3, 5, 4, 1, 7]",
        )

    def test_runningSum_easy_1480(self):
        self.assertEqual(
            first=runningSum(nums=[1, 2, 3, 4]),
            second=[1, 3, 6, 10],
            msg="Should be [1,3,6,10]",
        )


if __name__ == "__main__":
    unittest.main()
