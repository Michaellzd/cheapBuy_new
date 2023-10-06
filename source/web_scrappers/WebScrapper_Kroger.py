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


class WebScrapper_Kroger:
    """
    Main class used to scrape results from Kroger

    ...

    Attributes
    ----------
    description : str
        description of the product

    Methods
    -------
    run:
        Threaded method to execute subclasses
    get_driver:
        Returns Chrome Driver
    get_url_kroger:
        Returns kroger URL
    scrap_kroger:
        Returns Scraped result
    """

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
            results = self.scrap_kroger()
            # Condition to check whether results are avialable or not
            if len(results) == 0:
                print('kroger_results empty')
                self.result = {}
            else:
                item = results[0]
                # Find teh atag containing our required item
                atag = item.h3.a
                # Extract description from the atag
                self.result['description'] = atag.text.strip()

                # Get the URL for the page and shorten it
                self.result['url'] = 'https://www.kroger.com'+atag.get('href')
                self.result['url'] = shorten_url(self.result['url']) # short url is not applied currently

                # Find the span containging price of the item
                price_parent = item.find('div', 'flex justify-between items-center mb-8')
                # Find the price of the item
                # kroger using unique method to record price among all sites above...
                self.result['price'] = price_parent.find('data value').text
                # Assign the site as kroger to result
                self.result['site'] = 'kroger'

        except Exception as e:
            print('kroger_results exception', e)
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

    def get_url_kroger(self):
        """ 
        Returns kroger URL of search box
        """
        try:
            # Prepare URL for given description
            template = 'https://www.kroger.com/search?query={}&searchType=default_search&fulfillment=all'
            search_term = self.description.replace(' ', '+')
            template = template.format(search_term)
        except:
            template = ''
        return template

    def scrap_kroger(self):
        """ 
        Returns Scraped result
        """
        results = []
        try:
            # Call the function to get URL
            url = self.get_url_kroger()
            self.driver.get(url)
            # Use BeautifulSoup to scrap the webpage
            soup = BeautifulSoup(self.driver.page_source, 'html.parser')
            results = soup.find_all(
                'div', {"class": "kds-Card ProductCard"})
        except:
            results = []
        return results
