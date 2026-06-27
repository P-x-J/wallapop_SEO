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

def add_dot_loop(items_list_link: list, wait, driver):
    for item_link in items_list_link:
        driver.get(item_link)
        time.sleep(10)

        # Close any overlays
        driver.execute_script("document.querySelectorAll('[inert]').forEach(el => el.remove());")
        time.sleep(1)

        print("looking for element")
        # Wait for the button to be present
        edit_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/main/div/div[2]/div/aside/section/div[3]/div/div/walla-button[1]"))
        )

        time.sleep(5)
        print("Scrolling")
        driver.execute_script("""
            arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});
            """, edit_button)
        time.sleep(2)


        print("Clicking")
        edit_button.click()
        time.sleep(7)

        # Added a dot to the description
        print("Looking for description...")
        description = wait.until(EC.presence_of_element_located((By.ID, "description")))
        time.sleep(2)

        print("Adding dot...")
        append_dot(driver, description)
        time.sleep(1)

        # Find and click save button
        print("Looking for save button...")
        save_button = wait.until(
            EC.presence_of_element_located((By.XPATH, "/html/body/tsl-root/tsl-private/div/div[2]/div/tsl-edit/section/div/tsl-edit-product/form/tsl-footer-actions/div/div[2]/walla-button"))
        )
        print("Scrolling")
        driver.execute_script("""
            arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'})
        """, save_button)
        time.sleep(2)

        print("Clicking")
        save_button.click()
        time.sleep(5)
