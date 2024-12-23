from selenium.common.exceptions import TimeoutException
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import logging
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Login import Auth_con
from utili import secretCode
from utili import SS_logs



# Log TOTP login
logging.info("Generating TOTP")
user_otp=Auth_con.TOTP()

def do_tfa(TFAdriver, user_otp):

    # Capture a screenshot at this point
    SS_logs.log_and_screenshot(TFAdriver , "Capturing a screenshot after opening login page", "TFA")
    logging.info("Clicking on the Microsoft login field")
    
    microsoft_login = TFAdriver.find_element(By.XPATH, '//*[@id="loginWithSocial"]/form/div[2]').click()

    select_account_element = WebDriverWait(TFAdriver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="tilesHolder"]/div[1]/div/div/div/div[2]'))
    )

    logging.info("Account options found.")
    SS_logs.log_and_screenshot(TFAdriver, "Capturing a screenshot after accounts found", "TFA")

    # Select an account and wait explicitly until the element is clickable.
    logging.info("Selecting the desired account")
    select_account = TFAdriver.find_element(By.XPATH, '//*[@id="tilesHolder"]/div[1]/div/div/div/div[2]').click()

    # Wait for the 2FA input field to be clickable
    logging.info("Waiting for the 2FA input field to be clickable")
    auth_2fa_element = WebDriverWait(TFAdriver, 20).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="Input_TwoFactorCode"]'))
    )

    # Capture a screenshot at this point
    SS_logs.log_and_screenshot(TFAdriver, "Capturing a screenshot after 2FA page opens up", "TFA")


    # Input the generated random OTP into the field
    if auth_2fa_element:
        logging.info("Entering the OTP into the 2FA input field")
        auth_2fa_element.send_keys(user_otp)
        
        # Capture a screenshot at this point
        SS_logs.log_and_screenshot(TFAdriver, "Capturing a screenshot after entering OTP in the field", "TFA")
        
        auth_2fa_element.send_keys(Keys.RETURN)
    else:
        # Capture a screenshot at this point
        SS_logs.log_and_screenshot(TFAdriver, "Capturing a screenshot after failing to enter OTP in the missing 2FA field", "TFA")
        

    currentUrl= TFAdriver.current_url
    expectedUrl= "https://c003.dev.uptodata.studygen.cloud/"
    if currentUrl == expectedUrl:
        # Capture a screenshot at this point
        SS_logs.log_and_screenshot(TFAdriver, "operations completed", "TFA")
    else:
        SS_logs.log_and_screenshot(TFAdriver, "Authentication failed", "TFA")
        # Raise an exception if the URL doesn't match
        raise AssertionError(f"Expected URL: {expectedUrl}, Actual URL: {currentUrl}")

    TFAdriver.implicitly_wait(5)

def filter_elements_by_attribute(elements, attribute, value):
    filtered_elements = []
    for element in elements:
        if element.get_attribute(attribute) == value:
            filtered_elements.append(element)
    return filtered_elements

def filter_elements_by_text(elements, text):
    filtered_elements = []
    for element in elements:
        if element.text == text:
            filtered_elements.append(element)
    return filtered_elements


def elogin(TFAdriver):


    filter_elements_by_text(TFAdriver.find_elements(By.CLASS_NAME, 'social_label'),'Sign in using email')[0].click()
    
    #email_login= TFAdriver.find_element(By.XPATH, '//*[@id="loginWithSocial"]/form/div[5]').click()
    
    email = TFAdriver.find_element(By.ID, 'emailaddress')
    email.send_keys(secretCode.email)
    password = TFAdriver.find_element(By.ID, 'password')
    password.send_keys(secretCode.password)
    login = TFAdriver.find_element(By.XPATH, '//*[@id="loginWithEmail"]/form/div[3]/button')
    SS_logs.log_and_screenshot(TFAdriver, "Capturing a screenshot after entering email and password", "TFA")
    login.click()
    tfa_otp= TFAdriver.find_element(By.XPATH, '//*[@id="Input_TwoFactorCode"]')
    otp_timeout = 60
    start_time = time.time()
    user_otp = Auth_con.TOTP()


    # Keep trying to find the OTP element within the timeout
    while time.time() - start_time < otp_timeout:
        try:
            tfa_otp = TFAdriver.find_element(By.XPATH, '//*[@id="Input_TwoFactorCode"]')
            logging.info("OTP element found")
            break  # Exit the loop if the OTP element is found
        except Exception as NoSuchElementException:
            logging.warning("OTP element not found. Waiting...")
            time.sleep(1)  # Wait for 1 second before retrying

    if time.time() - start_time >= otp_timeout:
        # If the timeout is reached, generate a new OTP
        logging.warning("OTP retrieval timeout. Generating a new OTP.")
        user_otp = Auth_con.TOTP()
    if tfa_otp:
        try:
            logging.info("Entering the OTP into the 2FA input field")
            tfa_otp.send_keys(user_otp)
            SS_logs.log_and_screenshot(TFAdriver, "Capturing a screenshot after entering OTP in the field", "TFA")
        except TimeoutException:
            logging.error("Timeout waiting for the login button to be clickable.")
    else:
        SS_logs.log_and_screenshot(TFAdriver, "failing to enter OTP in the missing 2FA field", "TFA")
        
