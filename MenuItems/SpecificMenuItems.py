from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
import time
import logging

from utili import SS_logs


def OpenDropdown(driver):
    # Find the menu dropdown element and click on it
    menu_dropdown = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/header/nav/div[2]/div/div")))
    menu_dropdown.click()
    # Find all the menu items
    menu_items = driver.find_elements(By.XPATH, '//*[@id="navbarCollapse"]/div/div/div')
    SS_logs.log_and_screenshot(driver, "Menu dropdown clicked", "Menu Items")
    return menu_items

# Helper function to click a menu item and capture a screenshot
def click_menu_item(driver, menu_item_xpath, item_name, folder_name):
    OpenDropdown(driver)
    menu_item = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, menu_item_xpath)))
    menu_item.click()
    time.sleep(1)
    SS_logs.log_and_screenshot(driver, f"{item_name} clicked", folder_name)

# Helper function to navigate to a specific menu item
def navigate_to_menu_item(driver, item_name):
    time.sleep(3)
    if item_name in options:
        url = options[item_name]
        click_menu_item(driver, url, item_name, "Menu Items")
    else:
        logging.warning(f"Menu item '{item_name}' not found in options.")

# Your options dictionary
options = {
    "Profile": "/html/body/header/nav/div[2]/div/div/div/a[1]",
    "Design Schema": "/html/body/header/nav/div[2]/div/div/div/a[2]",
    "Rdb Schema": "/html/body/header/nav/div[2]/div/div/div/a[3]",
    "Environment Types": "/html/body/header/nav/div[2]/div/div/div/a[4]",
    "Show Configuration": "/html/body/header/nav/div[2]/div/div/div/a[5]",
    "Show RFS Config": "/html/body/header/nav/div[2]/div/div/div/a[6]",
    "Okta Properties": "/html/body/header/nav/div[2]/div/div/div/a[7]",
    "Build Audit Schema": "/html/body/header/nav/div[2]/div/div/div/a[8]",
    "Audit Logs": "/html/body/header/nav/div[2]/div/div/div/a[9]",
    "Roles Setup": "/html/body/header/nav/div[2]/div/div/div/a[10]",
    "Roles Management": "/html/body/header/nav/div[2]/div/div/div/a[11]",
    "Users Management": "/html/body/header/nav/div[2]/div/div/div/a[12]",
    "Worker Configuration": "/html/body/header/nav/div[2]/div/div/div/a[13]",
    "Study Section": "/html/body/header/nav/div[2]/div/div/div/a[14]",
    "Add File Types": "/html/body/header/nav/div[2]/div/div/div/a[15]",
    "Add Work Flow Actions": "/html/body/header/nav/div[2]/div/div/div/a[16]",
    "Show Login Logs": "/html/body/header/nav/div[2]/div/div/div/a[17]",
    "Export Entities": "/html/body/header/nav/div[2]/div/div/div/a[18]",
    "Import Entities": "/html/body/header/nav/div[2]/div/div/div/a[19]",
    "On boarding Request": "/html/body/header/nav/div[2]/div/div/div/a[20]",
    "Two-Factor Authentication": "/html/body/header/nav/div[2]/div/div/div/a[21]",
    "Logout": "/html/body/header/nav/div[2]/div/div/div/a[22]"
}


