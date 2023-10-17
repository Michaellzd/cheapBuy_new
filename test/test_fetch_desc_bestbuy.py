"""
To check if
fetch_desc_bestbuy in FetchDescription
works properly
"""

import unittest
from source.web_scrappers.FetchDescription import FetchDescription
import sys
sys.path.append('./')

class TestFetchDescriptionBestBuy(unittest.TestCase):

    def test_fetch_description_bestbuy(self):
        link = "https://www.bestbuy.com/site/dyson-outsize-total-clean-cordless-vacuum-nickel-red/6451332.p?skuId=6451332"
        fd = FetchDescription(link)
        self.assertEqual(fd.fetch_desc_bestbuy(), "dyson outsize total clean cordless vacuum nickel red")

if __name__ == '__main__':
    unittest.main()
