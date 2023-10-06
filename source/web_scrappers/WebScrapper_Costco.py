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

sys.path.append('../')


class WebScrapper_Costco:
    """
    Main class used to scrape results from Costco

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
    get_url_costco:
        Returns costco URL
    scrap_costco:
        Returns Scraped result
    """

    def __init__(self, description):
        """
        Parameters
        ----------
        description : str
            description of the product
        """
        if description:
            if len(description) < 5:
                self.description = description
            else:
                self.description = ' '.join(description.split()[:5])
        self.result = {}

    def run(self):
        """ 
        Returns final result
        """
        self.driver = self.get_driver()
        self.result = {}
        try:
            results = self.scrap_costco()
            if len(results) == 0:
                print('Costco_results empty')
                self.result = {}
            else:
                item = results[0]
                atag = item.find("span", {"class": "description"}).find('a')
                self.result['description'] = atag.text
                self.result['url'] = atag.get('href')
                self.result['url'] = shorten_url(self.result['url']) # short url is not applied currently
                self.result['price'] = item.find(
                    "div", {"class": "price"}).text.strip()
                self.result['site'] = 'costco'
        except Exception as e:
            print('Costco_results exception', e)
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

    def get_url_costco(self):
        """ 
        Returns costco URL of search box
        """
        template = "https://www.costco.com"+"/CatalogSearch?dept=All&keyword={}"
        search_term = self.description.replace(' ', '+')
        return template.format(search_term)

    def scrap_costco(self):
        """ 
        Returns Scraped result
        """
        url = self.get_url_costco()
        self.driver.get(url)
        soup = BeautifulSoup(self.driver.page_source, "html.parser")
        results = soup.find_all('div', {'class': 'product-list grid'})
        return results
