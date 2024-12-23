from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException
from selenium.webdriver.common.action_chains import ActionChains

import logging
import time
from utili import SS_logs


class Menu:
    def __init__(self, driver):
        self.driver = driver

    def click_on_parent_and_child(self, parent_name, child_name):
        try:
        
            # Wait for sidebar menu to be present
            sidebar_menu = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, 'sidebar-wrapper')))
            logging.info("Sidebar menu located")
            # Find all dropdown items in the sidebar menu
            dropdown_items = sidebar_menu.find_elements(By.XPATH, './/li[contains(@class, "dropdown")]')
            logging.info(f"Found {len(dropdown_items)+1} dropdown items in the sidebar menu")
            # Iterate through each dropdown item and check if the current dropdown item contains the specified parent name
            for dropdown_item in dropdown_items:
                if parent_name in dropdown_item.text:
                    dropdown_item.click()
                    time.sleep(3)
                    logging.info(f"Clicked on {dropdown_item.text}")
                    SS_logs.log_and_screenshot(self.driver, "Clicked on parent", "SpecificMenuItems")
                    # Find all child items in the dropdown menu
                    child_items = dropdown_item.find_elements(By.XPATH, './/ul/li/a')
                    # Iterate through each child item and check if the current child item contains the specified child name
                    for child_item in child_items:
                        if child_name in child_item.text:
                            child_item.click()
                            logging.info(f"Clicked on {child_item.text}")
                            time.sleep(5)   
                            SS_logs.log_and_screenshot(self.driver, "Child item clicked", "SpecificMenuItems")
                            return
            logging.error(f"Could not find or click on {child_name}")
        except (TimeoutException, StaleElementReferenceException) as e:
            logging.error(f"Exception occurred: {e}")
