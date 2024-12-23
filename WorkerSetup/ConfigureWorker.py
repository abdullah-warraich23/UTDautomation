'''
In this file we are to create automations for Configure Worker page functions, which includes:
* Create worker configuration
* Delete worker configuration
this file will be called in the main.py
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

from utili import SS_logs
from MenuItems.UpdatedSpecificMenuItems import Menu
from utili import webdriverOptions, secretCode
import logging
import time

class ConfigureWorkersclass:
    def __init__(self, driver):
        self.driver = driver
        self.menu = Menu(driver)

    # Helper functions
    def get_editor_input(self, input_key):
        inputs = self.driver.find_elements(By.CLASS_NAME,"dx-texteditor-input")
        for input in inputs:
            if input.get_attribute('id').startswith("dx_dx-") and input.get_attribute('id').endswith("_"+input_key):
                return input
        return None

    def scroll_to_view(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView(false);", element)
        return None

    # Webpage functions
    def CreateworkerConfig(self, configName, allowedFileType):
        
        self.menu.click_on_parent_and_child("Worker Setup", "Configure Worker")
       
        create_worker_config = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//div[@aria-label="Create Worker Configuration"]')))
        create_worker_config.click()
        logging.info("create worker configuration clicked successfully")

        config_name=WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "input.form-control[name='ConfigurationName']")))
        config_name.send_keys(configName)
        SS_logs.log_and_screenshot(self.driver, "enter config name", "Configure Worker")

        publisher_access_key= WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "accesskey")))
        publisher_access_key.send_keys(secretCode.pub_access_key)
        SS_logs.log_and_screenshot(self.driver, "enter Publisher Access Key", "Configure Worker")

        publisher_secret_key= WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "clientSecret")))
        publisher_secret_key.send_keys(secretCode.pub_secret_key)
        SS_logs.log_and_screenshot(self.driver, "enter Publisher Secret Key", "Configure Worker")

        Queue_Url= WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "queUrl")))
        Queue_Url.send_keys(secretCode.queue_url)
        SS_logs.log_and_screenshot(self.driver, "enter Queue URL", "Configure Worker")

        Allowed_files= WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "input.form-control[name='AllowedFileTypes']")))
        Allowed_files.send_keys(allowedFileType)
        SS_logs.log_and_screenshot(self.driver, "enter File type", "Configure Worker")

        test_que= self.driver.find_element(By.CSS_SELECTOR, "#saverfsForm > button.btn.btn-warning.float-right.mr-md-2")
        test_que.click()

        Save_Worker_Config=self.driver.find_element(By.CSS_SELECTOR, "#saverfsForm > button.btn.btn-icon.icon-left.btn-success.float-right")
        if toast_success := WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'dx-toast-success'))
        ):
            SS_logs.log_and_screenshot(self.driver, "test success message", "Configure Worker")
            print("Success Toast Message is: ", toast_success.text)
            Save_Worker_Config.click()  
        else:
            SS_logs.log_and_screenshot(self.driver, "test failure message", "Configure Worker")        
            print("Error Toast. something went wrong check again and test")



    def delete_row(self, config_name, allowed_file_types):
        
        self.menu.click_on_parent_and_child("Worker Setup", "Configure Worker")

        WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#WcGridContainer > div > div.dx-datagrid-rowsview.dx-datagrid-nowrap.dx-last-row-border.dx-scrollable.dx-visibility-change-handler.dx-scrollable-both.dx-scrollable-simulated.dx-fixed-columns")))

        rows = self.driver.find_elements(By.CSS_SELECTOR, ".dx-scrollable-content > div > table > tbody > tr")
        print("Number of rows found: ", len(rows))
        logging.info("rows located")

        for row in rows:

            name = row.find_element(By.XPATH, './/td[1]').text
            logging.info("Name: "+ name)
            
            file_types = row.find_element(By.XPATH, './/td[2]').text
            logging.info("File types: "+ file_types)


            if name == config_name and file_types == allowed_file_types:
            
                logging.info("Match found. Clicking delete button.")

                delete_button = row.find_element(By.CLASS_NAME, 'dx-link.dx-icon-trash.dx-link-icon')
                logging.info(f"located delete button for {name} with file type {file_types}")
                self.driver.execute_script("arguments[0].click();", delete_button)
                SS_logs.log_and_screenshot(self.driver, "delete button clicked successfully", "Configure Worker")

                logging.info("\n Enter audit message")
                WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, 'studyProps')))

                WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, 'description')))
                action = ActionChains(self.driver)
                cells = self.driver.find_element(By.ID,"description").click()

                logging.info("Entering audit message")
                action.send_keys("automated test message").perform()

                time.sleep(1)
                SS_logs.log_and_screenshot(self.driver, "audit message", "Configure Worker")



                cells = self.driver.find_element(By.CLASS_NAME,"btn-success")
                cells.click()
                logging.info("Saving audit message")

                time.sleep(2)
                logging.info("Save button clicked successfully")
                SS_logs.log_and_screenshot(self.driver, "save audit message", "Configure Worker")
                break
            else:
                print(f"file name: {config_name} with allowed file type: {allowed_file_types} NOT FOUND!")