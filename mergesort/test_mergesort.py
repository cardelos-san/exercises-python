## Unit Test

import unittest
import mergesort as ms

class TestMergeSort(unittest.TestCase):

    def test_mergesort(self):
        arr = [1, 4, 5, 7]
        result = ms.mSort(arr)
        flag = False

        #Checking if list is sorted
        if(all(result[i] <= result[i+1] for i in range(len(result)-1))):
            flag = True

        self.assertTrue(flag)


if __name__ == '__main__':
    unittest.main()