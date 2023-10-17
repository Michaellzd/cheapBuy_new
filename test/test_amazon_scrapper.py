import unittest
from source.web_scrappers.WebScrapper_Amazon import WebScrapper_Amazon
import sys
sys.path.append('../')

class TestWebScrapperAmazon(unittest.TestCase):

    def test_amazon_scrapper(self):
        description = 'Brita 35503 Standard Replacement Filters'
        t = WebScrapper_Amazon(description)
        self.assertIsNotNone(t.result)

if __name__ == '__main__':
    unittest.main()
