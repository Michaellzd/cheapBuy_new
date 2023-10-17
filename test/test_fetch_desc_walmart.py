# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 23:52:22 2021

@author: Rohan Shah
"""

import unittest
from source.web_scrappers.FetchDescription import FetchDescription
import sys
sys.path.append('../')

class TestFetchDescriptionWalmart(unittest.TestCase):

    def test_fetch_description_walmart(self):
        link = "https://www.walmart.com/ip/Brita-Longlast-Water-Filter-Replacement-Reduces-Lead-2-Count/128876038"
        fd = FetchDescription(link)
        self.assertEqual(fd.fetch_desc_walmart(), "Brita Longlast Water Filter Replacement Reduces Lead 2 Count")

if __name__ == '__main__':
    unittest.main()
