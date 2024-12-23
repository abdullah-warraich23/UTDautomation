from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

import time
import logging

from Login import Auth_con
from utili import SS_logs

# Helper Functions
def scroll_to_view(driver, element):
    y = element.location['y']
    delta = 100
    driver.execute_script(f'window.scrollTo(0, {y - delta})')
    time.sleep(1)

def filter_elements_by_text(elements, text):
    filtered_elements = []
    for element in elements:
        if element.text == text:
            filtered_elements.append(element)
    return filtered_elements



# Test Functions

def save_options(driver, current_audit_type):
    action = ActionChains(driver)

    save_button = driver.find_element(By.CSS_SELECTOR, ".btn")
   
    ##esig only
    save_button.click()

    
    WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CLASS_NAME, "modal-body")))
    time.sleep(1)
    SS_logs.log_and_screenshot(driver, "Audit reason modal", "BuildAuditSchema")
    
    logging.info("selecting and populating audit reason field")
    audit_reason = driver.find_element(By.ID, "auditReason")
    logging.info("Audit reason input field found")
    audit_reason.send_keys("automated audit message")
    SS_logs.log_and_screenshot(driver, "entered audit reason", "BuildAuditSchema")
    
    otp = Auth_con.TOTP()
    logging.info("selecting and populating 2FA field")
    two_fa = driver.find_element(By.ID, "password")
    two_fa.send_keys(otp)
    SS_logs.log_and_screenshot(driver, f"entered 2FA code {otp}", "BuildAuditSchema")
    
    save_audit_button = driver.find_element(By.XPATH, '//*[@id="audit-footer"]/button[2]')
    save_attribute = save_audit_button.get_attribute("onclick")    
    
    if save_attribute ==  "checkPasswordSubmitAudit()":
        save_audit_button.click()
        SS_logs.log_and_screenshot(driver, "Entry saved successfully", "BuildAuditSchema")
        time.sleep(3)
    else:
        logging.error("No 'Save Audit' button found.")
        SS_logs.log_and_screenshot(driver, "Not saved", "BuildAuditSchema")

#    if current_audit_type == "Active":
#        # Perform actions for Active state
#
#        logging.info("\nClicking save button")
#
#        time.sleep(1)
#        scroll_to_view(driver, save_button)
#        save_button.click()
#
#        logging.info("\n Enter audit message")
#        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'studyProps')))
#
#        cells = driver.find_element(By.ID,"description")
#        cells.click()
#        time.sleep(1) 
#        logging.info("Entering audit message")
#        action.send_keys("automated test message").perform()
#        time.sleep(1)
#        SS_logs.log_and_screenshot(driver, "audit message", "BuildAuditSchema")
#
#        cells = driver.find_element(By.CLASS_NAME,"btn-success")
#        cells.click()
#        logging.info("Saving audit message")
#        time.sleep(2)
#        logging.info("Save button clicked successfully")
#        SS_logs.log_and_screenshot(driver, "save audit message", "BuildAuditSchema")
#
#    elif current_audit_type == "Passive":
#        # Perform actions for Passive state
#        save_button.click()
#        time.sleep(2)
#        logging.info("Save button clicked successfully")
#        SS_logs.log_and_screenshot(driver, "Saved successfully", "BuildAuditSchema")
#
#    elif current_audit_type == "Esig":
#        save_button.click()
#
#        audit_info_modal = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CLASS_NAME, "modal-body")))
#        time.sleep(1)
#        SS_logs.log_and_screenshot(driver, "Audit reason modal", "BuildAuditSchema")
#
#        logging.info("selecting and populating audit reason field")
#        audit_reason = driver.find_element(By.ID, "auditReason")
#        logging.info("Audit reason input field found")
#        audit_reason.send_keys("automated audit message")
#        SS_logs.log_and_screenshot(driver, "entered audit reason", "BuildAuditSchema")
#
#        otp = Auth_con.TOTP()
#
#        logging.info("selecting and populating 2FA field")
#        two_fa = driver.find_element(By.ID, "password")
#        two_fa.send_keys(otp)
#        SS_logs.log_and_screenshot(driver, f"entered 2FA code {otp}", "BuildAuditSchema")
#
#        SS_logs.log_and_screenshot(driver, "Clicking Save Audit button", "BuildAuditSchema")
#        save_audit_button = driver.find_element(By.XPATH, '//*[@id="audit-footer"]/button[2]')
#        save_attribute = save_audit_button.get_attribute("onclick")    
#
#        if save_attribute ==  "checkPasswordSubmitAudit()":
#            save_audit_button.click()
#            SS_logs.log_and_screenshot(driver, "Entry saved successfully", "BuildAuditSchema")
#            time.sleep(3)
#        else:
#            logging.error("No 'Save Audit' button found.")
#            SS_logs.log_and_screenshot(driver, "Not saved", "BuildAuditSchema")
#
#    elif current_audit_type == "None":
#        # Perform actions for None state (e.g., directly save options)
#        save_button.click()
#        time.sleep(2)
#        logging.info("Save button clicked successfully")
#        SS_logs.log_and_screenshot(driver, "Saved successfully", "BuildAuditSchema")
#    else:
#        logging.error("Invalid expected_audit_type")
#        SS_logs.log_and_screenshot(driver, "Invalid expected_audit_type", "Test Failed")

def select_audit_type(driver, controller_name, action_name, expected_audit_type):
    try:
        # Find all rows
        rows =WebDriverWait(driver,10).until(EC.presence_of_all_elements_located((By.CLASS_NAME,"row")))
        logging.info("row found")

 
        for row in rows:
            # Find elements within the row
            controller_elements = row.find_elements(By.CLASS_NAME, "controllerName")
            action_elements = row.find_elements(By.CLASS_NAME, "actionName")
            time.sleep(1)
            audit_type_elements = row.find_elements(By.CLASS_NAME, "auditType")
            print("length of audit type elements\n", len(audit_type_elements))

            # Extract text from elements
            controller_texts = [element.text for element in controller_elements]
            action_texts = [element.text for element in action_elements]
            logging.info(f"text extracted from controller and actions: {controller_texts} and {action_texts}")

            # Check if the row matches the specified controller and action
            for i in range(len(controller_texts)):
                if controller_texts[i] == controller_name and action_texts[i] == action_name:
                    
                    # Scroll to the controller element
                    scroll_to_view(driver, controller_elements[i])
                    logging.info(f"scrolled to view") 
                    print(i)
                    # Click on the audit type dropdown
                    if audit_type_elements[i]:
                        print("desired index = ", i)

                        audit_type_elements[i].click()
                        time.sleep(2)

                        #scroll_to_view(driver, audit_type_elements[i])
                        #time.sleep(1)

                        scroll_to_view(driver, controller_elements[i])
                        print(i)


                        # registering CURRENT ATTRIBUTE
                        selected_option = Select(audit_type_elements[i]).first_selected_option
                        current_audit_type = selected_option.text
                        logging.info(f"current audit type: {current_audit_type}")

                        # Find the option with the expected audit type and click on it
                        option_elements = audit_type_elements[i].find_elements(By.TAG_NAME, "option")
                        print("checking if options are populated\n", len(option_elements))
                        for option in option_elements:
                            if option.text == expected_audit_type:
                                option.click()
                                time.sleep(1)
                                logging.info(f"audit type: {option.text} selected")
                                break

                    time.sleep(2)
                    SS_logs.log_and_screenshot(driver, f"Selected {expected_audit_type} for {controller_name} - {action_name}", "BuildAuditSchema")
                    
                    save_options(driver, current_audit_type)
                    return True

        # If no matching row is found
        logging.error(f"Row not found for Controller: {controller_name}, Action: {action_name}")
        SS_logs.log_and_screenshot(driver, f"Row not found for Controller: {controller_name}, Action: {action_name}", "Test Failed")
        return False

    except Exception as e:
        logging.error(f"An error occurred: {e}")
        SS_logs.log_and_screenshot(driver, f"An error occurred: {e}", "Test Failed")
        return False