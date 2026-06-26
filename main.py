import sys
import time

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from user_login_input import login
from items_list_input import prompt_items_list
from add_remove_dot_utils import append_dot
from add_remove_dot_utils import remove_trailing_dot

driver = webdriver.Chrome()
driver.get("https://wallapop.com/app/catalog/published")

wait = WebDriverWait(driver, 10)
#Let user login to the catalog
login()
items_list_link = prompt_items_list()

for item_link in items_list_link:
    driver.get(item_link)
    time.sleep(10)

    # Enter editor mode
    edit_button = driver.find_element(By.CLASS_NAME, "walla-button__button walla-button__button--full-width walla-button__button--medium walla-button__button--primary")
    edit_button.click()
    time.sleep(7)

    # Added a dot to the description
    description = wait.until(EC.presence_of_element_located((By.ID, "description")))
    append_dot(driver, description)

    refresh_button = driver.find_element(By.CLASS_NAME, "walla-button__button walla-button__button--full-width walla-button__button--medium walla-button__button--primary")
    time.sleep(5)


for item_link in items_list_link:
    driver.get(item_link)
    time.sleep(10)

    # Enter editor mode
    edit_button = driver.find_element(By.CLASS_NAME, "walla-button__button walla-button__button--full-width walla-button__button--medium walla-button__button--primary")
    edit_button.click()
    time.sleep(7)

    # Added a dot to the description
    description = wait.until(EC.presence_of_element_located((By.ID, "description")))
    append_dot(driver, description)
    refresh_button = driver.find_element(By.CLASS_NAME, "walla-button__button walla-button__button--full-width walla-button__button--medium walla-button__button--primary")
    time.sleep(5)





time.sleep(10)

driver.quit()