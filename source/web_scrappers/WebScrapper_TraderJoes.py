"""
Copyright (c) 2021 Anshul Patel
This code is licensed under MIT license (see LICENSE.MD for details)

@author: cheapBuy
"""
import sys

from bs4 import BeautifulSoup
from selenium import webdriver
from source.utils.url_shortener import shorten_url
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

# Set working directory path
sys.path.append('../')

class WebScrapper_TraderJoes:

    def __init__(self, description):
        """
        Parameters
        ----------
        description : str
            description of the product
        """
        # Initialize class variables
        self.description = description
        self.result = {}

    def run(self):
        """ 
        Returns final result
        """
        self.driver = self.get_driver()
        try:
            # Get results from scrapping function
            results = self.scrap_traderjoes()
            # Condition to check whether results are avialable or not
            if len(results) == 0:
                print('TraderJoes_results empty')
                self.result = {}
            else:
                item = results[0]
                # Find teh atag containing our required item
                atag = item.h2.a
                # Extract description from the atag
                self.result['description'] = atag.text.strip()
                # Get the URL for the page and shorten it
                self.result['url'] = 'https://www.traderjoes.com/home'+atag.get('href')
                self.result['url'] = shorten_url(self.result['url']) # short url is not applied currently
                # Find the span containging price of the item
                price_parent = item.find('span', 'a-price')
                # Find the price of the item
                self.result['price'] = price_parent.find(
                    'span', 'ProductPrice_productPrice__price__3-50j').text
                # Assign the site as traderjoes to result
                self.result['site'] = 'traderjoes'
        except Exception as e:
            print('TraderJoes_results exception', e)
            self.result = {}
        return self.result

    def get_driver(self):
        """ 
        Returns Chrome Driver
        """
        # Prepare driver for scrapping

        options = webdriver.FirefoxOptions()
        options.headless = True
        driver_path = "D:\\510\\1\\geckodriver-v0.33.0-win64\\geckodriver.exe"
        driver = webdriver.Firefox(options=options, executable_path=driver_path)
        return driver

    def get_url_traderjoes(self):
        """ 
        Returns amazon URL of search box
        """
        try:
            # Prepare URL for given description
            template = 'https://www.traderjoes.com/home'+'/search?q={}&global=yes'
            
            search_term = self.description.replace(' ', '+')
            template = template.format(search_term)
        except:
            template = ''
        return template

    def scrap_traderjoes(self):
        """ 
        Returns Scraped result
        """
        results = []
        try:
            # Call the function to get URL
            url = self.get_url_traderjoes()
            self.driver.get(url)
            # Use BeautifulSoup to scrap the webpage
            soup = BeautifulSoup(self.driver.page_source, 'html.parser')
            results = soup.find_all(
                'div', {'data-component-type': 's-search-result'})
        except:
            results = []
        return results
