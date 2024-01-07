import os
import time
import requests

import urllib.request
from bs4 import BeautifulSoup
from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService

from webdriver_manager.chrome import ChromeDriverManager

from miner import Miner


PRODUCT_LIST = Miner().get_product_list()

chrome_options = Options()
chrome_options.add_argument('incognito')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument(
    "user-agent=Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko")
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options, service=ChromeService(
    ChromeDriverManager().install()))

for product in [PRODUCT_LIST[0]]:
    driver.get(product["url"])
    WebDriverWait(driver, 20).until(EC.presence_of_element_located(
        (By.XPATH, '//*[@id="hd_0_container_0"]/div[1]/div[2]/div/div[1]/div[1]')))

    soup = BeautifulSoup(driver.page_source, "lxml")

    images = soup.find_all("img", attrs={"class": "detail-gallery-img"})
    for index, image in enumerate(images):
        image_url = image["src"]
        urllib.request.urlretrieve(image_url, os.path.join(
            os.getcwd() + "\\" + f"{product['name']}_{index+1}.jpg"))


driver.close()
