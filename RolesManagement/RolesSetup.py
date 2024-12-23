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
from MenuItems import UpdatedSpecificMenuItems
import utili
from utili import webdriverOptions


UpdatedSpecificMenuItems.click_on_parent_and_child(webdriverOptions.driver, 'Roles Management', 'Roles Setup')

# Helper Functions
def scroll_to_view(driver, element):
    driver.execute_script("arguments[0].scrollIntoView();", element)
    time.sleep(1)

def selectRole(driver, selectedRole, permissions, state):
    select_element= WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'roles')))
    select_element.click()

    WebDriverWait(driver,10).until(EC.visibility_of_all_elements_located((By.TAG_NAME, 'option')))
    SS_logs.log_and_screenshot(driver, "clicked on roles dropdown", "RolesSetup")
    
    select = Select(select_element)
    select.select_by_visible_text(selectedRole)
    time.sleep(1)
    SS_logs.log_and_screenshot(driver, f"'{selectedRole}'' selected", "RolesSetup")

    WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.ID, "mappingList")))
    logging.info("Mapping list in view")
    for module, action in permissions:
        try:
            
            row = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, f"//p[text()='{module}']/ancestor::tr[.//p[text()='{action}']]")))
            scroll_to_view(driver, row)
            logging.info(f"Row found for module '{module}' and action '{action}'")


            # Find the checkbox in the row
            checkbox = row.find_element(By.CLASS_NAME, 'canAccess')
            logging.info("Switch located")

            # Always toggle the switch to 'on'
            if state == 'on' and not checkbox.is_selected():
                driver.execute_script("arguments[0].click();", checkbox)
                time.sleep(1)

            # If the desired state is 'off', toggle the switch again
            if state == 'off':
                driver.execute_script("arguments[0].click();", checkbox)
                time.sleep(1)

        except Exception as e:
            print(f"An error occurred while processing permission '{module}', '{action}': {e}")

    save_button = driver.find_element(By.CSS_SELECTOR, "button.btn")
    logging.info("save button located")
    scroll_to_view(driver, save_button)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn")))
    save_button.click()
    time.sleep(2)
    SS_logs.log_and_screenshot(driver, f"{selectedRole} role updated successfully", "RolesSetup")

### issue with the save button and the process, need to correct it