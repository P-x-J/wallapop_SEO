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
from adding_dot_loop import add_dot_loop
from removing_dot_loop import removing_dot_loop
from prompt_time_intervals import time_interval_verification

driver = webdriver.Chrome()
driver.get("https://es.wallapop.com/app/catalog/published")

wait = WebDriverWait(driver, 10)
# Let user login to the catalog
login()
items_list_link = prompt_items_list()
time_interval = time_interval_verification()

while True:
    print("STARTING ADDING DOT LOOPS")
    add_dot_loop(items_list_link, wait, driver)
    print("START REMOVING DOT LOOPS")
    removing_dot_loop(items_list_link, wait, driver)
    print(f"Waiting {time_interval} minutes")
    time.sleep(int(time_interval*60))
