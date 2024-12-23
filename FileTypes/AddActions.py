from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

from utili import SS_logs
from MenuItems import UpdatedSpecificMenuItems
from utili import webdriverOptions, secretCode
import logging
import time


# Helper functions
def get_editor_input(driver,input_key):
    inputs = driver.find_elements(By.CLASS_NAME,"dx-texteditor-input")
    for input in inputs:
        if input.get_attribute('id').startswith("dx_dx-") and input.get_attribute('id').endswith("_"+input_key):
            return input
    return None

def filter_elements_by_tags(elements, tags):
    filtered_elements = []
    for element in elements:
        if element.tag_name in tags:
            filtered_elements.append(element)
    return filtered_elements

def filter_elements_by_text(elements, text):
    filtered_elements = []
    for element in elements:
        if element.text == text:
            filtered_elements.append(element)
    return filtered_elements

def scroll_to_view(driver, element):
    driver.execute_script("arguments[0].scrollIntoView(false);", element)
    return None

# There is an issue with this function it opens all previously called instences prior to opening the last one
UpdatedSpecificMenuItems.click_on_parent_and_child(webdriverOptions.driver, 'File Types', 'Add Action')

def addActions(driver):

    WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID, "gridContainer")))
    
    add_button=driver.find_element(By.CSS_SELECTOR, "div.dx-button[aria-label='Add new action']")
    logging.info("add button located")
    add_button.click()
    SS_logs.log_and_screenshot(driver, "Add button clicked", "Environment Type")