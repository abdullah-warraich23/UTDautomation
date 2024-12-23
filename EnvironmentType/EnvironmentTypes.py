from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

from utili import SS_logs
from MenuItems.UpdatedSpecificMenuItems import Menu
from utili import webdriverOptions, Helpers, SS_logs
from utili.Helpers import get_editor_input, scroll_to_view
import logging
import time


class Environment_Type:
    def __init__(self, driver):
        self.driver = driver
        self.menu = Menu(driver)

    # Webpage functions
    def AddEnvType(self, types_name):

        self.menu.click_on_parent_and_child("Environment Type", "Environment Types")

        WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.ID, "gridContainer")))

        add_button=self.driver.find_element(By.CLASS_NAME, "dx-datagrid-addrow-button")
        logging.info("add button located")
        add_button.click()
        SS_logs.log_and_screenshot(self.driver, "Add button clicked", "Environment Type")

        WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.CLASS_NAME, "dx-field-item-content")))
        logging.info("input field found")

        get_editor_input(self.driver, "typeName").send_keys(types_name)
        WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".dx-scrollable-content > div:nth-child(1) > table:nth-child(1) > tbody:nth-child(2) > tr")))

        SS_logs.log_and_screenshot(self.driver, "type input field located and filled", "Environment Type")



        WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.CLASS_NAME, "dx-button-content")))

        save_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@aria-label='Save']"))
        )
        save_button.click()
        logging.info("Click on save button successfully")
        SS_logs.log_and_screenshot(self.driver, "New type saved", "Environment Type")



    def EditStudy(self, study_name, updated_study_name):
        try:
            self.menu.click_on_parent_and_child("Environment Type", "Environment Types")

            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "gridContainer")))
            logging.info("Grid container located")

            WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".dx-scrollable-content > div:nth-child(1) > table:nth-child(1) > tbody:nth-child(2) > tr")))
            rows = self.driver.find_elements(By.CSS_SELECTOR, ".dx-scrollable-content > div:nth-child(1) > table:nth-child(1) > tbody:nth-child(2) > tr")
            logging.info("Rows located")
            SS_logs.log_and_screenshot(self.driver, "rows located", "Environment Type")

            # Iterating through each row to find the matching study name
            for row in rows:
                type_name_element = row.find_element(By.CSS_SELECTOR, "td:nth-child(1)")
                logging.info(f"Type Name column value: {type_name_element.text}")

                # Once iterated checking if the current row's type name matches the study name
                if type_name_element.text == study_name:
                    scroll_to_view(self.driver, type_name_element)
                    logging.info("Scrolled to view")
                    time.sleep(2)

                    SS_logs.log_and_screenshot(self.driver, "scrolled to view", "Environment Type")

                    ActionChains(self.driver).move_to_element(row).perform()

                    edit_button = row.find_element(By.CSS_SELECTOR, "td:nth-child(4) > a[title='Edit']")
                    logging.info("button located")
                    self.driver.execute_script("arguments[0].click();", edit_button)
                    logging.info(f"Edit button for '{study_name}' clicked")
                    SS_logs.log_and_screenshot(self.driver, "edit button clicked", "Environment Type")

                    # Waiting for the input field to be present and clear it
                    WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "dx-texteditor-input-container")))
                    edit_field = get_editor_input(self.driver, "typeName")
                    edit_field.send_keys(f" changed to {updated_study_name}")
                    logging.info("field filled with updated name")
                    SS_logs.log_and_screenshot(self.driver, "fields edited", "Environment Type")
                    time.sleep(2)

                    save_button = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@aria-label='Save']")))
                    save_button.click()
                    logging.info("Save button clicked")
                    break
            else:
                logging.info("Study name not found in the grid")
                SS_logs.log_and_screenshot(self.driver, "no study name found", "Environment Type")
        except Exception as e:
            logging.error(f"An error occurred: {e}")


    def DeleteStudy(self, study_name):
        try:
            self.menu.click_on_parent_and_child("Environment Type", "Environment Types")

            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "gridContainer")))
            logging.info("Grid container located")

            WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".dx-scrollable-content > div:nth-child(1) > table:nth-child(1) > tbody:nth-child(2) > tr")))
            rows = self.driver.find_elements(By.CSS_SELECTOR, ".dx-scrollable-content > div:nth-child(1) > table:nth-child(1) > tbody:nth-child(2) > tr")
            logging.info("Rows located")

            SS_logs.log_and_screenshot(self.driver, "rows located", "Environment Type")

            # Iterating through each row to find the matching study name
            for row in rows:
                type_name_element = row.find_element(By.CSS_SELECTOR, "td:nth-child(1)")
                logging.info(f"Type Name column value: {type_name_element.text}")

                # Once iterated checking if the current row's type name matches the study name
                if type_name_element.text == study_name:
                    scroll_to_view(self, type_name_element)
                    logging.info("Scrolled to view")
                    time.sleep(2)
                    SS_logs.log_and_screenshot(self.driver, "scrolled to view", "Environment Type")

                    ActionChains(self.driver).move_to_element(row).perform()

                    delete_button = row.find_element(By.CSS_SELECTOR, "td:nth-child(4) > a[title='Delete']")
                    logging.info("Delete button located")
                    self.driver.execute_script("arguments[0].click();", delete_button)
                    logging.info(f"Delete button for '{study_name}' clicked")
                    SS_logs.log_and_screenshot(self.driver, "delete button located and clicked", "Environment Type")

                    WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "dx-popup-normal")))
                    confirm_delete = self.driver.find_element(By.CSS_SELECTOR, "div.dx-popup-normal .dx-button:nth-child(1)")
                    logging.info("Confirm delete('YES') button located")
                    SS_logs.log_and_screenshot(self.driver, "delete confirmation", "Environment Type")

                    ActionChains(self.driver).move_to_element(confirm_delete).perform()
                    confirm_delete.click()
                    logging.info(f"{study_name} deleted successfully")
                    SS_logs.log_and_screenshot(self.driver, "deleted successfully", "Environment Type")
                    break
            else:
                logging.info("Study name not found in the grid")
                SS_logs.log_and_screenshot(self.driver, "no study name found", "Environment Type")
        except Exception as e:
            logging.error(f"An error occurred: {e}")

    def SetDefaults(self, study_name):
        try:
            self.menu.click_on_parent_and_child("Environment Type", "Environment Types")

            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "gridContainer")))
            logging.info("Grid container located")

            WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".dx-scrollable-content > div:nth-child(1) > table:nth-child(1) > tbody:nth-child(2) > tr")))
            rows = self.driver.find_elements(By.CSS_SELECTOR, ".dx-scrollable-content > div:nth-child(1) > table:nth-child(1) > tbody:nth-child(2) > tr")
            SS_logs.log_and_screenshot(self.driver, "Rows located", "Environment Type")

            # Iterating through each row to find the matching study name
            for row in rows:
                type_name_element = row.find_element(By.CSS_SELECTOR, "td:nth-child(1)")
                logging.info(f"Type Name column value: {type_name_element.text}")

                # Once iterated checking if the current row's type name matches the study name
                if type_name_element.text == study_name:
                    logging.info("name matched")
                    scroll_to_view(self.driver, type_name_element)
                    time.sleep(2)
                    SS_logs.log_and_screenshot(self.driver, "Scrolled to view", "Environment Type")

                    ActionChains(self.driver).move_to_element(row).perform()

                    set_default_button = row.find_element(By.CSS_SELECTOR, "td:nth-child(4) > a[title='Set Defaults']")
                    self.driver.execute_script("arguments[0].click();", set_default_button ) 
                    WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "sampleListMap")))
                    
                    SS_logs.log_and_screenshot(self.driver, f"Set Default button for '{study_name}' clicked", "Environment Type")
                    break
                else:
                    logging.info("Study name not found in the grid")
        except Exception as e:
            logging.error(f"An error occurred: {e}")
            SS_logs.log_and_screenshot(self.driver, "study name not found", "Environment Type")