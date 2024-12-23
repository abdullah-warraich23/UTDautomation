import os, sys

sys.path.append(os.path.abspath(r"W:\Code\Automation\automation_StudyGen\Login"))
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import logging
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from utili import SS_logs
from utili import webdriverOptions, Helpers, SS_logs
from utili.Helpers import get_editor_input, scroll_to_view, filter_elements_by_text

class header_Class:

    def __init__(self, driver):
        self.driver = driver

    def logoUrl(self):
        try:
            # Verify that the header has Studygen available and clickable
            logging.info("2- Click on study gen logo to verify the URL")
            logo_url = self.driver.current_url
            SS_logs.log_and_screenshot(self.driver, " Click on study gen logo to verify the URL")

            expected_Hp_Url = "https://ewallet.goodlucklhr.pk/"
            if logo_url == expected_Hp_Url:
                SS_logs.log_and_screenshot(self.driver, f" URL to be verified- {logo_url}")
            else:
                SS_logs.log_and_screenshot(self.driver, f" URL is not the same as expected- {expected_Hp_Url}")
                raise AssertionError(f"expected URL:  {expected_Hp_Url}, \n\nActual URL:  {logo_url}")
        except Exception as e:
            logging.info("error occured while verifying header logo link")

    def verify_dropdown_links(self):
            try:
                # Find the sidebar element by link text
                sidebar_menu = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, 'sidebar-wrapper')))                

                # Find all the menu items
                menu_items = self.driver.find_elements(By.XPATH, '//*[@id="navbarCollapse"]/div/div/div')

                with open("dropdown_results.txt", "w") as f:
                    for item in menu_items:
                        option_text = item.text
                        SS_logs.log_and_screenshot(self.driver, f"Selecting an option from the dropdown: {option_text}")
                        item.click()

                        option_url = self.driver.current_url
                        SS_logs.log_and_screenshot(self.driver, f"Dropdown -> {option_text}")


                        if option_url:
                            logging.info("Option '{option_text}': {option_url}\n")
                            f.write(f"Option '{option_text}': {option_url}\n")
                            SS_logs.log_and_screenshot(self.driver, f"Option '{option_text}' URL: {option_url}")
                        else:
                            f.write(f"Option '{option_text}' does not have a URL\n")
                            SS_logs.log_and_screenshot(self.driver, f"Option '{option_text}' does not have a URL")

                        self.driver.back()
                        SS_logs.log_and_screenshot(self.driver, "Navigated back to the main page")

                print("Results written to dropdown_results.txt")

            except Exception as e:
                print(f"An error occurred: {str(e)}")