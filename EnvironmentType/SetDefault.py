'''
in this file i want to create automations for study type default page. this includes:
* dropdown menu selections for two fields
* file uploading from local
* and study section configuration

this file will be called in the EnvironmentTypes.py -> SetDefaults()
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select

from utili import SS_logs
from utili import webdriverOptions, secretCode, Helpers
from utili.Helpers import get_editor_input, filter_elements_by_text, scroll_to_view
from EnvironmentType.EnvironmentTypes import Environment_Type 
import logging
import time
#import robot
#from robot import Robot
from pywinauto import Application


class StudyTypeDefaults:
    def __init__(self, driver):
        self.driver = driver


    def SetStudyTypeDefaults(self,  study_name, sample_list, config, path, button_text):
        env_type = Environment_Type(self.driver)        
        env_type.SetDefaults(study_name)
        
        try:
            ##SAMPLE MAPPING SELECTION
            sample_list_dropdown = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "sampleListMap")))
            logging.info("sample mapping list field detected")
            
            sample_list_dropdown.click() 
            logging.info("Sample List Mappings located and clicked on")
            time.sleep(2) #wait for the options to load

            # Wait for options to load
            WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#sampleListMap option")))            
            SS_logs.log_and_screenshot(self.driver, "Sample mapping list field located and clicked", "Environment Type")
            
            # Select the desired option by study name
            select_sample_list = Select(self.driver.find_element(By.ID, "sampleListMap"))

             # Ensure scrolling to the desired option
            select_sample_list.select_by_visible_text(sample_list)
            logging.info(f"Selected '{sample_list}' from Sample List dropdown")
            SS_logs.log_and_screenshot(self.driver, "Sample mapping from list is selected", "Environment Type")
        
        except Exception as e:
            logging.error(f"An error occurred during Sample mapping list selection from dropdown: {e}")
            return  # Exit if sample list selection fails
    

        try:
            ##CONFIGURATIONS SELECTION

            config_dropdown = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "configVersion")))
            logging.info("Configurations field detected")
            
            config_dropdown.click() 
            logging.info("Configurations located and clicked on")
            
            # Wait for options to load
            WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#configVersion option")))            
            time.sleep(2) # Additional wait for stability
            SS_logs.log_and_screenshot(self.driver, "Configurations field located and clicked", "Environment Type")
            
            # Interact with the dropdown
            configVersion_select = Select(self.driver.find_element(By.ID, "configVersion"))

            # Select the desired option by visible text
            configVersion_select.select_by_visible_text(config)
            logging.info(f"Selected '{config}' from Configurations dropdown")
            SS_logs.log_and_screenshot(self.driver, "Configuration from list is selected", "Environment Type")
        
        except Exception as e:
            logging.error(f"An error occurred during configurations selection from dropdown: {e}")
            return  # Exit if configuration selection fails
    
        
         # FILE UPLOAD
        try:


            #upload_button = WebDriverWait(self.driver, 10).until(
            #    EC.presence_of_element_located((By.CLASS_NAME, "dx-fileuploader-button"))
            #)
            #logging.info("File upload button located")
            
            # Upload the file using send_keys
            #upload_button.click()
            #time.sleep(3)  # Wait for the upload window to open
            #SS_logs.log_and_screenshot(self.driver, "Upload button located and clicked", "Environment Type")
            
            # Send the file path to the file input element
            
            logging.info(f"File uploaded: {path}")

           # # Use Robot to input the file path
           # rob.type_string(path)
           # rob.press_key('enter')
           # time.sleep(5)
        
            # Use pywinauto to interact with the file dialog
            
            #app = Application(backend='uia').connect(title_re='.*Open.*')
            #dialog = app.window(title_re='.*Open.*')
            #dialog.set_focus()
            #dialog.Edit.type_keys(path)
            #dialog.Button.click()  # Click the 'Open' button
            #time.sleep(5)  # Wait for the file to be uploaded
            
            file_input = self.driver.find_element(By.CLASS_NAME,"dx-fileuploader-input")
            file_input.send_keys(path)

            logging.info(f"File uploaded: {path}")
            
            SS_logs.log_and_screenshot(self.driver, "file path entered and selected", "Environment Type")


            # Wait for the envTables to load
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "envTables"))
            )
            
            logging.info("envTables area loaded")
            SS_logs.log_and_screenshot(self.driver, "Generic Sections loaded", "Environment Type")
            

            # Find all options within the envTables section
            env_options = self.driver.find_elements(By.CSS_SELECTOR, "#envTables .col-sm-4")
            logging.info(f"Found {len(env_options)} options in the envTables section")

            # Iterate through the options and log their text
            for option in env_options:
                option_text = option.text
                logging.info(f"Option found: {option_text}")

                if button_text:
                    try:
                        # Locate the button within the option
                        button = self.driver.find_element(By.XPATH, f"//button[contains(@onclick, 'configureSection(&quot;'{button_text}'&quot;)')]")
                        button.click()
                        
                        SS_logs.log_and_screenshot(self.driver, f"Setup for '{button_text}' clicked", "Environment Type")
                        logging.info(f"Clicked '{button_text}' button for option '{option_text}'")
                    except Exception as e:
                        logging.error(f"Button '{button_text}' not found or clickable in option '{option_text}': {e}")
                        SS_logs.log_and_screenshot(self.driver, f"Setup button for '{button_text}' not found", "Environment Type")


        except Exception as e:
            logging.error(f"An error occurred during file upload and option extraction: {e}")