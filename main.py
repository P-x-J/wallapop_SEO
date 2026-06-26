import sys
import time

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("https://wallapop.com/app/catalog/published")

time.sleep(4)

wait = WebDriverWait(driver, 10)

# click "Reject all"
reject_btn = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//button[contains(.,'Reject all')]"))
)
reject_btn.click()


time.sleep(40)

driver.quit()