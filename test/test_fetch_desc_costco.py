# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 23:52:22 2021

@author: Rohan Shah
"""

import unittest
from source.web_scrappers.FetchDescription import FetchDescription
import sys
sys.path.append('../')

class TestFetchDescriptionCostco(unittest.TestCase):

    def test_fetch_description_costco(self):
        link = "https://www.costco.com/brita-replacement-filters%2c-10-pack.product.100131571.html"
        fd = FetchDescription(link)
        self.assertEqual(fd.fetch_desc_costco(), "brita replacement filters%2c 10 pack")

if __name__ == '__main__':
    unittest.main()
