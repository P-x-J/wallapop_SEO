import sys
import time

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from user_login_input import login

driver = webdriver.Chrome()
driver.get("https://wallapop.com/app/catalog/published")

#Let user login to the catalog
login()

time.sleep(10)

driver.quit()