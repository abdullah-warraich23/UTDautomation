from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
import time
import logging

from Login import Auth_con
from utili import SS_logs

logging.info("-----Tests for DROPDOWN OPTIONS (Studygen MAIN MENU)-----")


#helper functions
def filter_elements_by_attribute(elements, attribute, value):
    filtered_elements = []
    for element in elements:
        if element.get_attribute(attribute) == value:
            filtered_elements.append(element)
    return filtered_elements

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
    driver.execute_script("arguments[0].scrollIntoView(true);", element)
    return None

def get_url_and_status(driver):
    current_url = driver.current_url
    response = requests.get(current_url)
    status_code = response.status_code
    return current_url, status_code


def OpenDropdown(driver):
    # Find the menu dropdown element and click on it
    menu_dropdown = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/header/nav/div[2]/div/div")))
    menu_dropdown.click()
    # Find all the menu items
    menu_items = driver.find_elements(By.XPATH, '//*[@id="navbarCollapse"]/div/div/div')
    SS_logs.log_and_screenshot(driver, "Menu dropdown clicked", "Menu Items")

# Defined functions for each option in the menu dropdown
def Profile(driver):
    OpenDropdown(driver)
    logging.info("dropdown opened")
    profile_link = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/header/nav/div[2]/div/div/div/a[1]")))
    profile_link.click()
    time.sleep()
    SS_logs.log_and_screenshot(driver, "Profile clicked", "Menu Items")
    
    current_url, status_code = get_url_and_status(driver)
    logging.info(f"Current URL: {current_url}")
    logging.info(f"Status Code: {status_code}")

    return current_url, status_code

def DesignSchema(driver):
    OpenDropdown(driver)
    designSchema_link = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/header/nav/div[2]/div/div/div/a[2]")))
    designSchema_link.click()
    time.sleep(1)
    SS_logs.log_and_screenshot(driver,"Design Schema clicked", "Menu Items")
    
    current_url, status_code = get_url_and_status(driver)
    logging.info(f"Current URL: {current_url}")
    logging.info(f"Status Code: {status_code}")

    return current_url, status_code

def RdbSchema(driver):
    OpenDropdown(driver)  
    rdbSchema_link = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/header/nav/div[2]/div/div/div/a[3]")))
    rdbSchema_link.click()
    time.sleep(1)
    SS_logs.log_and_screenshot(driver,"RDB Schema clicked", "Menu Items")
    
    current_url, status_code = get_url_and_status(driver)
    logging.info(f"Current URL: {current_url}")
    logging.info(f"Status Code: {status_code}")

    return current_url, status_code

def EnvironmentType(driver):
    OpenDropdown(driver)
    environmentType_link = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/header/nav/div[2]/div/div/div/a[4]")))
    environmentType_link.click()
    time.sleep(1)
    SS_logs.log_and_screenshot(driver,"Environment Type clicked", "Menu Items")
    
    current_url, status_code = get_url_and_status(driver)
    logging.info(f"Current URL: {current_url}")
    logging.info(f"Status Code: {status_code}")

    return current_url, status_code

def  ShowConfiguration(driver):
    OpenDropdown(driver)
    ShowConfiguration_link = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/header/nav/div[2]/div/div/div/a[5]")))
    ShowConfiguration_link.click()
    time.sleep(1)
    SS_logs.log_and_screenshot(driver,"Show Configuration clicked", "Menu Items")
    
    current_url, status_code = get_url_and_status(driver)
    logging.info(f"Current URL: {current_url}")
    logging.info(f"Status Code: {status_code}")

    return current_url, status_code

def ShowRfsConfigs(driver):
    OpenDropdown(driver)
    ShowRfsConfigs_link = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/header/nav/div[2]/div/div/div/a[6]")))
    ShowRfsConfigs_link.click()
    time.sleep(1)
    SS_logs.log_and_screenshot(driver,"Show RFS Configs clicked", "Menu Items")
    
    current_url, status_code = get_url_and_status(driver)
    logging.info(f"Current URL: {current_url}")
    logging.info(f"Status Code: {status_code}")

    return current_url, status_code

def OktaPropeties(driver):
    OpenDropdown(driver)
    OktaPropeties_link = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/header/nav/div[2]/div/div/div/a[7]")))
    OktaPropeties_link.click()
    time.sleep(1)
    SS_logs.log_and_screenshot(driver,"OKTA Properties clicked", "Menu Items")
    
    current_url, status_code = get_url_and_status(driver)
    logging.info(f"Current URL: {current_url}")
    logging.info(f"Status Code: {status_code}")

    return current_url, status_code

def BuildAuditSchema(driver):
    OpenDropdown(driver)
    BuildAuditSchema_link = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/header/nav/div[2]/div/div/div/a[8]")))
    BuildAuditSchema_link.click()
    time.sleep(1)
    SS_logs.log_and_screenshot(driver,"Build Audit Schema clicked", "Menu Items")
    
    current_url, status_code = get_url_and_status(driver)
    logging.info(f"Current URL: {current_url}")
    logging.info(f"Status Code: {status_code}")

    return current_url, status_code

def AuditLog(driver):
    OpenDropdown(driver)
    AuditLog_link = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/header/nav/div[2]/div/div/div/a[9]")))
    AuditLog_link.click()
    time.sleep(1)
    SS_logs.log_and_screenshot(driver,"Audit Logs clicked", "Menu Items")
    
    current_url, status_code = get_url_and_status(driver)
    logging.info(f"Current URL: {current_url}")
    logging.info(f"Status Code: {status_code}")

    return current_url, status_code

def RolesSetup(driver):
    OpenDropdown(driver)
    RolesSetup_link = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/header/nav/div[2]/div/div/div/a[10]")))
    RolesSetup_link.click()
    time.sleep(1)
    SS_logs.log_and_screenshot(driver,"Roles Setup clicked", "Menu Items")
    
    current_url, status_code = get_url_and_status(driver)
    logging.info(f"Current URL: {current_url}")
    logging.info(f"Status Code: {status_code}")

    return current_url, status_code

def RolesManagement(driver):
    OpenDropdown(driver)
    RolesManagement_link = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/header/nav/div[2]/div/div/div/a[11]")))
    RolesManagement_link.click()
    time.sleep(1)
    SS_logs.log_and_screenshot(driver,"Roles Management clicked", "Menu Items")
    
    current_url, status_code = get_url_and_status(driver)
    logging.info(f"Current URL: {current_url}")
    logging.info(f"Status Code: {status_code}")

    return current_url, status_code

def UsersManagement(driver):
    OpenDropdown(driver)
    UsersManagement_link = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/header/nav/div[2]/div/div/div/a[12]")))
    UsersManagement_link.click()
    time.sleep(1)
    SS_logs.log_and_screenshot(driver,"Users Management clicked", "Menu Items")
    
    current_url, status_code = get_url_and_status(driver)
    logging.info(f"Current URL: {current_url}")
    logging.info(f"Status Code: {status_code}")

    return current_url, status_code

def WorkerConfigurations(driver):
    OpenDropdown(driver)
    WorkerConfigurations_link = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/header/nav/div[2]/div/div/div/a[13]")))
    WorkerConfigurations_link.click()
    time.sleep(1)
    SS_logs.log_and_screenshot(driver,"Worker Configurations clicked", "Menu Items")
    
    current_url, status_code = get_url_and_status(driver)
    logging.info(f"Current URL: {current_url}")
    logging.info(f"Status Code: {status_code}")

    return current_url, status_code

def StudySections(driver):
    OpenDropdown(driver)
    StudySections_link = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/header/nav/div[2]/div/div/div/a[14]")))
    StudySections_link.click()
    time.sleep(1)
    SS_logs.log_and_screenshot(driver,"Study Sections clicked", "Menu Items")
    
    current_url, status_code = get_url_and_status(driver)
    logging.info(f"Current URL: {current_url}")
    logging.info(f"Status Code: {status_code}")

    return current_url, status_code

def AddFileType(driver):
    OpenDropdown(driver)
    AddFileType_link = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/header/nav/div[2]/div/div/div/a[15]")))
    AddFileType_link.click()
    time.sleep(1)
    SS_logs.log_and_screenshot(driver,"Add File Type clicked", "Menu Items")
    
    current_url, status_code = get_url_and_status(driver)
    logging.info(f"Current URL: {current_url}")
    logging.info(f"Status Code: {status_code}")

    return current_url, status_code

def AddWorkFlowAction(driver):
    OpenDropdown(driver)
    AddWorkFlowAction_link = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/header/nav/div[2]/div/div/div/a[16]")))
    AddWorkFlowAction_link.click()
    time.sleep(1)
    SS_logs.log_and_screenshot(driver,"Add Work Flow Action clicked", "Menu Items")
    
    current_url, status_code = get_url_and_status(driver)
    logging.info(f"Current URL: {current_url}")
    logging.info(f"Status Code: {status_code}")

    return current_url, status_code

def ShowLoginLogs(driver):
    OpenDropdown(driver)
    ShowLoginLogs_link = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/header/nav/div[2]/div/div/div/a[17]")))
    ShowLoginLogs_link.click()
    time.sleep(1)
    SS_logs.log_and_screenshot(driver,"Show Login Logs clicked", "Menu Items")
    
    current_url, status_code = get_url_and_status(driver)
    logging.info(f"Current URL: {current_url}")
    logging.info(f"Status Code: {status_code}")

    return current_url, status_code

def ExportEntities(driver):
    OpenDropdown(driver)
    ExportEntities_link = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/header/nav/div[2]/div/div/div/a[18]")))
    ExportEntities_link.click()
    time.sleep(1)
    SS_logs.log_and_screenshot(driver,"Export Entities clicked", "Menu Items")
    
    current_url, status_code = get_url_and_status(driver)
    logging.info(f"Current URL: {current_url}")
    logging.info(f"Status Code: {status_code}")

    return current_url, status_code

def ImportEntities(driver):
    OpenDropdown(driver)
    ImportEntities_link = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/header/nav/div[2]/div/div/div/a[19]")))
    ImportEntities_link.click()
    time.sleep(1)
    SS_logs.log_and_screenshot(driver,"Import Entities clicked", "Menu Items")
    
    current_url, status_code = get_url_and_status(driver)
    logging.info(f"Current URL: {current_url}")
    logging.info(f"Status Code: {status_code}")

    return current_url, status_code

def OnboardingRequests(driver):
    OpenDropdown(driver)
    OnboardingRequests_link = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/header/nav/div[2]/div/div/div/a[20]")))
    OnboardingRequests_link.click()
    time.sleep(1)
    SS_logs.log_and_screenshot(driver,"Onboarding Request clicked", "Menu Items")
    
    current_url, status_code = get_url_and_status(driver)
    logging.info(f"Current URL: {current_url}")
    logging.info(f"Status Code: {status_code}")

    return current_url, status_code

def TwoFactorAuthentication(driver):
    OpenDropdown(driver)
    TwoFactorAuthentication_link = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/header/nav/div[2]/div/div/div/a[21]")))
    TwoFactorAuthentication_link.click()
    time.sleep(1)
    SS_logs.log_and_screenshot(driver,"Two Factor Authentication clicked", "Menu Items")
    
    current_url, status_code = get_url_and_status(driver)
    logging.info(f"Current URL: {current_url}")
    logging.info(f"Status Code: {status_code}")

    return current_url, status_code

def Logout(driver):
    OpenDropdown(driver)
    Logout_link = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/header/nav/div[2]/div/div/div/a[22]")))
    Logout_link.click()
    time.sleep(1)
    SS_logs.log_and_screenshot(driver,"Logout clicked", "Menu Items")
    
    current_url, status_code = get_url_and_status(driver)
    logging.info(f"Current URL: {current_url}")
    logging.info(f"Status Code: {status_code}")

    return current_url, status_code