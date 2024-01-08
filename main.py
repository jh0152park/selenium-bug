import os
import time
import requests
import datetime

import urllib.request
from bs4 import BeautifulSoup
from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.common.exceptions import TimeoutException

from webdriver_manager.chrome import ChromeDriverManager

import features
from miner import Miner


PRODUCT_LIST = Miner().get_product_list()
STARTED_AT = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

os.mkdir(STARTED_AT)
os.chdir(os.path.join(os.getcwd(), STARTED_AT))

ROOT_FOLDER = os.getcwd()

chrome_options = Options()
chrome_options.add_argument(features.SELENIUM_SECRET_MODE)
chrome_options.add_argument(features.SELENIUM_NO_SANDBOX)
chrome_options.add_argument(features.SELENIUM_DISABLE_SHARED_MEMORY)
chrome_options.add_argument(features.SELENIUM_USER_AGENT)
chrome_options.add_experimental_option(features.SELENIUM_DETACH, True)
chrome_options.add_experimental_option(
    features.SELENIUM_EXCLUDE_SWITCH, [features.SELENIUM_ENABLE_LOGGING]
)


driver = webdriver.Chrome(
    options=chrome_options, service=ChromeService(ChromeDriverManager().install())
)

# driver = webdriver.Chrome(options=chrome_options)

for product in PRODUCT_LIST:
    try:
        driver.get(product["url"])

        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, features.MAIN_LOGO_XPATH))
        )

        soup = BeautifulSoup(driver.page_source, "lxml")
        images = soup.find_all("img", attrs={"class": "detail-gallery-img"})

        if len(images) > 0:
            os.mkdir(product["name"])
            os.chdir(product["name"])

            for index, image in enumerate(images):
                try:
                    image_url = image["src"]
                    urllib.request.urlretrieve(
                        image_url,
                        os.path.join(
                            os.getcwd() + "\\" + f"{product['name']}_{index+1}.jpg"
                        ),
                    )
                except Exception as err:
                    print(f"Occurred some error while image downloading: {err}")
                    print(f"source: {image}")
            os.chdir("..")

    except Exception as err:
        print(err)


driver.quit()
