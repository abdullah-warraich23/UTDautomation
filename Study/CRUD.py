from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select

import time
import logging

from Login import Auth_con
from utili import SS_logs

class crud_class:

    def __init__(self, driver):
        self.driver = driver
        self.action = ActionChains(driver)

    # Helper Functions
    def filter_elements_by_attribute(self, elements, attribute, value):
        return [element for element in elements if element.get_attribute(attribute) == value]

    def filter_elements_by_tags(self, elements, tags):
        return [element for element in elements if element.tag_name in tags]

    def filter_elements_by_text(self, elements, text):
        return [element for element in elements if element.text == text]

    def get_editor_input(self, input_key):
        inputs = self.driver.find_elements(By.CLASS_NAME, "dx-texteditor-input")
        for input in inputs:
            if input.get_attribute('id').startswith("dx_dx-") and input.get_attribute('id').endswith("_" + input_key):
                return input
        return None

    def scroll_to_view(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    # CRUD Operations
    def create_entry(self, study_name, study_number, tags, environment_type, user):
        try:
            logging.info("\n----1 Creating a new entry----")
            time.sleep(2)
            add_button = self.filter_elements_by_text('Add Study') 
            # self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div/main/div[3]/div/div/div[4]/div/div/div[3]/div[2]/div/div/div')
            add_button.click()
            logging.info("click on add button")
            SS_logs.log_and_screenshot(self.driver, "click add button", "CRUD-Create")

            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="gridContainer"]/div/div[6]/div[2]/table/tbody/tr[1]'))
            )

            logging.info("\n----2 Entering study name----")
            self.get_editor_input('studyName').send_keys(study_name)
            logging.info("input study name in study name field")
            SS_logs.log_and_screenshot(self.driver, "Study Name", "CRUD-Create")

            logging.info("\n----3 Entering study number----")
            self.get_editor_input('studyNumber').send_keys(study_number)
            logging.info("input study number in study number field")
            SS_logs.log_and_screenshot(self.driver, "Study Number", "CRUD-Create")

            logging.info("\n----4 Entering tag----")
            self.get_editor_input('tags').send_keys(tags)
            self.get_editor_input('tags').send_keys(Keys.RETURN)
            logging.info("input tag in tags field")
            SS_logs.log_and_screenshot(self.driver, "tag", "CRUD-Create")

            logging.info("\n----5 Selecting environment type----")
            self.get_editor_input('environmentType').click()
            cells = self.driver.find_elements(By.CLASS_NAME, "dx-list-item-content")
            self.filter_elements_by_text(cells, environment_type)[0].click()
            SS_logs.log_and_screenshot(self.driver, "env selected", "CRUD-Create")
            time.sleep(1)

            logging.info("\n----6 Selecting role----")
            self.get_editor_input('roles').click()
            time.sleep(1)
            cells = self.driver.find_elements(By.CLASS_NAME, "dx-data-row")
            self.filter_elements_by_text(cells, user)[0].click()
            time.sleep(1)
            self.action.send_keys(Keys.ESCAPE).perform()

            logging.info("clicked successfully")
            SS_logs.log_and_screenshot(self.driver, "role open popup", "CRUD-Create")

            logging.info("\n----7 Clicking save button----")
            time.sleep(1)
            save_button = self.filter_elements_by_text(self.driver.find_elements(By.CLASS_NAME, "dx-button-content"), "Save")[0]
            save_button.click()
            logging.info("Click on save button to add data and create a row")
            SS_logs.log_and_screenshot(self.driver, "save", "CRUD-Create")

            logging.info("\n----8 Enter audit----")
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, 'auditMessage')))
            time.sleep(1)
            cells = self.driver.find_elements(By.ID, "description")
            cells[0].click()
            self.action.send_keys("this is an automated test audit message").perform()
            time.sleep(1)
            logging.info("Entering audit message")
            SS_logs.log_and_screenshot(self.driver, "audit message", "CRUD-Create")
            cells = self.driver.find_elements(By.CLASS_NAME, "btn-success")
            cells[0].click()
            logging.info("Saving Audit")
            SS_logs.log_and_screenshot(self.driver, "save audit", "CRUD-Create")
        except Exception as e:
            SS_logs.log_and_screenshot(self.driver,"error creating", "CRUD-Create")

    def read_data(self):
        time.sleep(5)
        try:
            logging.info("Locating the table")
            SS_logs.log_and_screenshot(self.driver, "Locating the table", "CRUD-Read")
            table = self.driver.find_element(By.CSS_SELECTOR, '#gridContainer > div > div.dx-datagrid-rowsview.dx-datagrid-nowrap.dx-scrollable.dx-visibility-change-handler.dx-scrollable-both.dx-scrollable-simulated.dx-fixed-columns > div.dx-scrollable-wrapper > div > div.dx-scrollable-content > div > table')
            rows = table.find_elements(By.TAG_NAME, 'tr')
            table_data = [[cell.text for cell in row.find_elements(By.TAG_NAME, 'td')] for row in rows[1:]]

            for row in table_data:
                print(row)
                logging.info(row)

            SS_logs.log_and_screenshot(self.driver, "All data read successfully", "CRUD-Read")

        except Exception as e:
            logging.error(f"An error occurred while reading table data: {str(e)}")
            SS_logs.log_and_screenshot(self.driver, "read_table_error", "CRUD-Read")

    def update_entry(self, row_num, new_study_name=None, new_study_number=None, new_tags=None, new_environment_type=None, new_roles=None):
        logging.info("\n----1 Updating an entry ----")
        time.sleep(3)
        row_xpath = self.driver.find_element(By.XPATH, f'//*[@id="gridContainer"]/div/div[6]/div[2]/table/tbody/tr[{row_num}]')
        self.scroll_to_view(row_xpath)

        cell = row_xpath.find_element(By.XPATH, f'/html/body/div[1]/div/div/main/div[3]/div/div/div[6]/div[2]/table/tbody/tr[{row_num}]/td[2]/a[1]')
        edit_attribute = cell.get_attribute('title')

        if edit_attribute == 'Edit':
            cell.click()
            SS_logs.log_and_screenshot(self.driver, "edit button clicked", "CRUD-Update")
        else:
            logging.info("No 'Edit' button found.")
            SS_logs.log_and_screenshot(self.driver, "Edit notFound", "CRUD-Update")

        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, f'//*[@id="gridContainer"]/div/div[6]/div[2]/table/tbody/tr[{row_num}]/td')))

        if new_study_name:
            study_name_input = self.get_editor_input('studyName')
            self.scroll_to_view(study_name_input)
            study_name_input.clear()
            study_name_input.send_keys(new_study_name)
            SS_logs.log_and_screenshot(self.driver, "Updated Study Name", "CRUD-Update")

        if new_study_number:
            study_number_input = self.get_editor_input('studyNumber')
            self.scroll_to_view(study_number_input)
            study_number_input.clear()
            study_number_input.send_keys(new_study_number)
            SS_logs.log_and_screenshot(self.driver, "Updated Study Number", "CRUD-Update")

        if new_tags:
            tags_input = self.get_editor_input('tags')
            self.scroll_to_view(tags_input)
            tags_input.clear()
            tags_input.send_keys(new_tags)
            tags_input.send_keys(Keys.RETURN)
            SS_logs.log_and_screenshot(self.driver, "updated tag", "CRUD-Update")

        if new_environment_type:
            environment_type_input = self.get_editor_input('environmentType')
            self.scroll_to_view(environment_type_input)
            environment_type_input.click()
            cells = self.driver.find_elements(By.CLASS_NAME, "dx-list-item-content")
            dropdown_options = self.filter_elements_by_text(cells, new_environment_type)
            if dropdown_options:
                dropdown_options[0].click()
                SS_logs.log_and_screenshot(self.driver, "Updated environment selected by text", "CRUD-Update")

        if new_roles:
            get_roles = self.get_editor_input('roles')
            self.scroll_to_view(get_roles)
            get_roles.click()
            SS_logs.log_and_screenshot(self.driver, "roles field selected successfully", "CRUD-Update")
            cells = self.driver.find_elements(By.CLASS_NAME, "dx-data-row")
            self.filter_elements_by_text(cells, new_roles)[0].click()
            self.action.send_keys(Keys.ESCAPE).perform()
            SS_logs.log_and_screenshot(self.driver, "Updated role successfully", "CRUD-Update")

        save_button = self.filter_elements_by_text(self.driver.find_elements(By.CLASS_NAME, "dx-button-content"), "Save")[0]
        self.scroll_to_view(save_button)
        save_button.click()
        logging.info("clicking save button")
        SS_logs.log_and_screenshot(self.driver, "updated and saved", "CRUD-Update")

    def delete_entry(self, row_num):
        logging.info("\n----1 Deleting an entry ----")
        time.sleep(2)
        delete_button = self.driver.find_element(By.XPATH, f'/html/body/div[1]/div/div/main/div[3]/div/div/div[6]/div[2]/table/tbody/tr[{row_num}]/td[2]/a[2]')
        delete_attribute = delete_button.get_attribute('title')

        if delete_attribute == 'Delete':
            delete_button.click()
            SS_logs.log_and_screenshot(self.driver, "delete button clicked", "CRUD-Delete")
        else:
            logging.info("No 'Delete' button found.")
            SS_logs.log_and_screenshot(self.driver, "Delete button not found", "CRUD-Delete")

        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "dx-dialog-content")))

        delete_popup_button = self.filter_elements_by_text(self.driver.find_elements(By.CLASS_NAME, "dx-button-content"), "Delete")[0]
        self.scroll_to_view(delete_popup_button)
        delete_popup_button.click()

        logging.info("delete confirmed")
        SS_logs.log_and_screenshot(self.driver, "delete confirmation", "CRUD-Delete")

        logging.info("\n----2 Deletion confirmed ----")
