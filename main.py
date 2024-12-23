from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait     
import time
import logging
import datetime

from Login import TFA
from Study.Header import header_Class
from Study.CRUD import crud_class
#from AuditTrail import BuildAuditSchema
#from RolesManagement import RolesSetup
import utili
from utili import webdriverOptions
#from WorkerSetup.ConfigureWorker import ConfigureWorkersclass
#from EnvironmentType.EnvironmentTypes import Environment_Type
#from EnvironmentType.SetDefault import StudyTypeDefaults

### Main page
logging.info("-----Tests for CRUD operations(Studygen study section)-----")
crudCall= crud_class(webdriverOptions.driver)
headerCall= header_Class(webdriverOptions.driver)

headerCall.verify_dropdown_links()
ts = datetime.datetime.now().timestamp()
crudCall.create_entry(webdriverOptions.driver, "Automated Study "+str(ts), str(ts), "report", "Default", "User")
#time.sleep(1)

#CRUD.read_data(driver)
#time.sleep(1)
#ts = int(datetime.datetime.now().timestamp())

#CRUD.update_entry(driver, "9", "Updated Automated study 5.0 "+str(ts), str(ts), "automation Update", "ICHM 10", "User")
#time.sleep(1)

#CRUD.delete_entry(driver, 10, "yes")
#time.sleep(1)

### Excess menu items
#logging.info("-----Tests for Menu item access (Studygen)-----")
#menu.RolesManagement(driver)
#logging.info("-----SELECT SPECIFIC DROPDOWN OPTION (Studygen MAIN MENU)-----")
#Parent_menu_name = "Audit Trail"
#Child_menu_name = "Build Audit Schema"
#SpecificMenuItems.click_child_menu_item(driver,Parent_menu_name,Child_menu_name)
#UpdatedSpecificMenuItems.click_on_parent_and_child(driver, 'Audit Trail', 'Build Audit Schema')

#time.sleep(1)

#logging.info("-----Tests for build audit schema operations(Studygen)-----")
#BuildAuditSchema.select_audit_type(driver, 'Studies', 'Create', 'Active')
#auditSchema.select_audit_type(driver, 'Studies', 'Create', 'None')

#logging.info("-----Tests for Role setup operations(Studygen)-----")
#add permissions i.e. key pair values for module names and action names. these will be followed by state option to turn on or off(one at a time)
#permissions = [('Actions', 'Index'), ('ApiAuditTrail', 'ShowAudits'), ('ApiStudies','Create')]
#state = 'on'
#RolesSetup.selectRole(webdriverOptions.driver, "test role", permissions, state)
#time.sleep(2)

###Initialize the ConfigureWorkersclass
#logging.info("-----Tests for Worker configuration operations(Studygen)-----")

#worker_config = ConfigureWorkersclass(webdriverOptions.driver)
### Call the methods
#worker_config.CreateworkerConfig("testQ", "xyz")
#worker_config.delete_row("testQ", "xyz")
#ConfigureWorker.delete_row(webdriverOptions.driver, "testQ", "xyz")

###Initialize the EnvironmentType class
#logging.info("-----Tests for environment type operations(Studygen)-----")

#env_type = Environment_Type(webdriverOptions.driver)
### Call the methods
#env_type.AddEnvType("Automated Test Name")
#env_type.EditStudy("Test Name A","Edited Test Name A")
#env_type.DeleteStudy("Test Name A changed to Edited Test Name A")
#env_type.SetDefaults("Test Name A")

#env_type = Environment_Type(webdriverOptions.driver)
#env_type.SetDefaults("Test Name A")

#set_def=StudyTypeDefaults(webdriverOptions.driver)
#path = "W:\\StudyGen\\Test_data\\ICHM10-vxl\\Project\\5506_working_ichm10.env"
#set_def.SetStudyTypeDefaults("Automated Test Name", "RDBs", "SannovaV2", path, "BlankMatrix")


# Quit the WebDriver
logging.info("\nQuitting the WebDriver\n")
logging.info("*************************************************************************************************************************************************************************\n")
input("press enter to exit")
#webdriverOptions.driver.quit()