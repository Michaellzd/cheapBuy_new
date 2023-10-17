"""
Copyright (c) 2021 Anshul Patel
This code is licensed under MIT license (see LICENSE.MD for details)

@author: cheapBuy
"""

import unittest
from source.web_scrappers.WebScrapper_Costco import WebScrapper_Costco
import sys
sys.path.append('../')

class TestWebScrapperCostco(unittest.TestCase):

    def test_costco_scrapper(self):
        description = 'brita replacement filters%2c 10 pack'
        t = WebScrapper_Costco(description)
        self.assertIsNotNone(t.result)

if __name__ == '__main__':
    unittest.main()
