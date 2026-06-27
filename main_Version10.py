import sys
import time
import pyautogui

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from user_login_input import login
from items_list_input import prompt_items_list
from add_remove_dot_utils import append_dot
from add_remove_dot_utils import remove_trailing_dot

driver = webdriver.Chrome()
driver.get("https://es.wallapop.com/app/catalog/published")

wait = WebDriverWait(driver, 10)
# Let user login to the catalog
login()
items_list_link = prompt_items_list()

while True:
    for item_link in items_list_link:
        driver.get(item_link)
        time.sleep(10)

        # Close any overlays
        driver.execute_script("document.querySelectorAll('[inert]').forEach(el => el.remove());")
        time.sleep(1)

        # Wait for the button to be present
        edit_button = wait.until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/main/div/div[2]/div/aside/section/div[3]/div/div/walla-button[1]"))
        )
        time.sleep(5)
        edit_button.click()
        
        # Scroll and click
        driver.execute_script("""
            arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});
            arguments[0].click();
        """, edit_button)
        time.sleep(7)

        # Added a dot to the description
        description = wait.until(EC.presence_of_element_located((By.ID, "description")))
        append_dot(driver, description)

        # Find and click save button
        save_button = wait.until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/main/div/div[2]/div/aside/section/div[3]/div/div/walla-button[2]"))
        )
        driver.execute_script("""
            arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});
            arguments[0].click();
        """, save_button)
        time.sleep(5)

    for item_link in items_list_link:
        driver.get(item_link)
        time.sleep(10)

        # Close any overlays
        driver.execute_script("document.querySelectorAll('[inert]').forEach(el => el.remove());")
        time.sleep(1)

        # Enter editor mode
        edit_button = wait.until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/main/div/div[2]/div/aside/section/div[3]/div/div/walla-button[1]"))
        )
        driver.execute_script("""
            arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});
            arguments[0].click();
        """, edit_button)
        time.sleep(7)

        # Added a dot to the description
        description = wait.until(EC.presence_of_element_located((By.ID, "description")))
        append_dot(driver, description)
        
        # Find and click save button
        save_button = wait.until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/main/div/div[2]/div/aside/section/div[3]/div/div/walla-button[2]"))
        )
        driver.execute_script("""
            arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});
            arguments[0].click();
        """, save_button)
        time.sleep(5)

time.sleep(10)
driver.quit()