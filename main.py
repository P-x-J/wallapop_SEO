import sys
import time

from selenium import webdriver
from selenium.webdriver.firefox.service import Service

service = Service(executable_path="/geckodriver-v0.37.0-linux-aarch64/geckodriver")
driver = webdriver.Chrome(service=service)

driver = webdriver.Firefox(service=service)

driver.get("https://google.com")

time.sleep(10)

driver.quit()