import time

## STEP1

# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
# driver.implicitly_wait(10)
#
# driver.get('https://demowebshop.tricentis.com/')
# time.sleep(2)
#
# driver.find_element('xpath', '//a[text()="Register"]').click()
# driver.find_element('id', 'gender-male').click()
# driver.find_element('id', 'FirstName').send_keys('Maanas')
# driver.find_element('id', 'LastName').send_keys('Jadhav')
# driver.find_element('id', 'Email').send_keys('maanas@gmail.com')
# driver.find_element('id', 'Password').send_keys('maanas@12345')
# driver.find_element('id', 'ConfirmPassword').send_keys('maanas@12345')

#####################################################################################################

'''
STEP2
In step2 we are defining the classes/attributes. 
Created the object for Register class.
Here only we are calling the attributes

'''
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
# driver.implicitly_wait(10)
#
# driver.get('https://demowebshop.tricentis.com/')
# time.sleep(2)
#
# class Register:
#
#     def click_on_register(self):
#         driver.find_element('xpath', '//a[text()="Register"]').click()
#
#     def click_on_gender_btn(self):
#         driver.find_element('id', 'gender-male').click()
#
#     def enter_firstname(self, fname):
#         driver.find_element('id', 'FirstName').send_keys(fname)
#
#     def enter_lastname(self, lname):
#         driver.find_element('id', 'LastName').send_keys(lname)
#
#     def enter_reg_email(self, email_id):
#         driver.find_element('id', 'Email').send_keys(email_id)
#
#     def enter_reg_pwd(self, password):
#         driver.find_element('id', 'Password').send_keys(password)
#
#     def enter_confirm_pwd(self, confirm_pwd):
#         driver.find_element('id', 'ConfirmPassword').send_keys(confirm_pwd)
#
# reg_obj = Register()
# reg_obj.click_on_register()
# reg_obj.click_on_gender_btn()
# reg_obj.enter_firstname('Maanas')
# reg_obj.enter_lastname('Jadhav')
# reg_obj.enter_reg_email('maanas@gmail.com')
# reg_obj.enter_reg_pwd('maanas@12345')
# reg_obj.enter_confirm_pwd('maanas@12345')


#####################################################################################################

'''
STEP3

'''
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
# driver.implicitly_wait(10)
#
# driver.get('https://demowebshop.tricentis.com/')
# time.sleep(2)
#
# class Register:
#
#     def click_on_register(self):
#         driver.find_element('xpath', '//a[text()="Register"]').click()
#
#     def click_on_gender_btn(self):
#         driver.find_element('id', 'gender-male').click()
#
#     def enter_firstname(self, fname):
#         driver.find_element('id', 'FirstName').send_keys(fname)
#
#     def enter_lastname(self, lname):
#         driver.find_element('id', 'LastName').send_keys(lname)
#
#     def enter_reg_email(self, email_id):
#         driver.find_element('id', 'Email').send_keys(email_id)
#
#     def enter_reg_pwd(self, password):
#         driver.find_element('id', 'Password').send_keys(password)
#
#     def enter_confirm_pwd(self, confirm_pwd):
#         driver.find_element('id', 'ConfirmPassword').send_keys(confirm_pwd)

#####################################################################################################

'''
STEP4   :   We removed the initialization of driver and launching of the web-application and we gave it in the test_reg.py 

'''

# class Register:
#
#     def click_on_register(self):
#         driver.find_element('xpath', '//a[text()="Register"]').click()
#
#     def click_on_gender_btn(self):
#         driver.find_element('id', 'gender-male').click()
#
#     def enter_firstname(self, fname):
#         driver.find_element('id', 'FirstName').send_keys(fname)
#
#     def enter_lastname(self, lname):
#         driver.find_element('id', 'LastName').send_keys(lname)
#
#     def enter_reg_email(self, email_id):
#         driver.find_element('id', 'Email').send_keys(email_id)
#
#     def enter_reg_pwd(self, password):
#         driver.find_element('id', 'Password').send_keys(password)
#
#     def enter_confirm_pwd(self, confirm_pwd):
#         driver.find_element('id', 'ConfirmPassword').send_keys(confirm_pwd)
#
# ## ERROR
# ## Because there is no driver in this file

#####################################################################################################

'''
STEP5

'''
# class Register:
#
#     def __init__(self, driver):
#         self.driver = driver        ## self.driver --> driver = webdriver.Chrome()
#
#     def click_on_register(self):
#         self.driver.find_element('xpath', '//a[text()="Register"]').click()
#
#     def click_on_gender_btn(self):
#         self.driver.find_element('id', 'gender-male').click()
#
#     def enter_firstname(self, fname):
#         self.driver.find_element('id', 'FirstName').send_keys(fname)
#
#     def enter_lastname(self, lname):
#         self.driver.find_element('id', 'LastName').send_keys(lname)
#
#     def enter_reg_email(self, email_id):
#         self.driver.find_element('id', 'Email').send_keys(email_id)
#
#     def enter_reg_pwd(self, password):
#         self.driver.find_element('id', 'Password').send_keys(password)
#
#     def enter_confirm_pwd(self, confirm_pwd):
#         self.driver.find_element('id', 'ConfirmPassword').send_keys(confirm_pwd)
#

#####################################################################################################

'''
STEP6

'''

# from object_repository.reg_repo import RegisterLocators
#
# reg_loc = RegisterLocators()
# # print(reg_loc.reg_link)     ## ('xpath', '//a[text()="Register"]')
# # print(reg_loc.gender_btn)   ## ('id', 'gender-male')
# # print(reg_loc.firstname)    ## ('id', 'FirstName')
# # print(reg_loc.lastname)     ## ('id', 'LastName')
# # print(reg_loc.reg_email)    ## ('id', 'Email')
# # print(reg_loc.reg_pwd)      ## ('id', 'Password')
# # print(reg_loc.confirm_pwd)  ## ('id', 'ConfirmPassword')
#
#
# class Register:
#
#     def __init__(self, driver):
#         self.driver = driver        ## self.driver --> driver = webdriver.Chrome()
#
#     def click_on_register(self):
#         # self.driver.find_element('xpath', '//a[text()="Register"]').click()
#         self.driver.find_element(*reg_loc.reg_link).click()
#
#     def click_on_gender_btn(self):
#         # self.driver.find_element('id', 'gender-male').click()
#         self.driver.find_element(*reg_loc.gender_btn).click()
#
#     def enter_firstname(self, fname):
#         # self.driver.find_element('id', 'FirstName').send_keys(fname)
#         self.driver.find_element(*reg_loc.firstname).send_keys(fname)
#
#     def enter_lastname(self, lname):
#         # self.driver.find_element('id', 'LastName').send_keys(lname)
#         self.driver.find_element(*reg_loc.lastname).send_keys(lname)
#
#     def enter_reg_email(self, email_id):
#         # self.driver.find_element('id', 'Email').send_keys(email_id)
#         self.driver.find_element(*reg_loc.reg_email).send_keys(email_id)
#
#     def enter_reg_pwd(self, password):
#         # self.driver.find_element('id', 'Password').send_keys(password)
#         self.driver.find_element(*reg_loc.reg_pwd).send_keys(password)
#
#     def enter_confirm_pwd(self, confirm_pwd):
#         # self.driver.find_element('id', 'ConfirmPassword').send_keys(confirm_pwd)
#         self.driver.find_element(*reg_loc.confirm_pwd).send_keys(confirm_pwd)


#####################################################################################################

'''
STEP6

'''

# from object_repository.reg_repo import RegisterLocators
#
# reg_loc = RegisterLocators()
#
# class Register:
#
#     def __init__(self, driver):
#         self.driver = driver        ## self.driver --> driver = webdriver.Chrome()
#
#     def click_on_register(self):
#         self.driver.find_element(*reg_loc.reg_link).click()
#
#     def click_on_gender_btn(self):
#         self.driver.find_element(*reg_loc.gender_btn).click()
#
#     def enter_firstname(self, fname):
#         self.driver.find_element(*reg_loc.firstname).send_keys(fname)
#
#     def enter_lastname(self, lname):
#         self.driver.find_element(*reg_loc.lastname).send_keys(lname)
#
#     def enter_reg_email(self, email_id):
#         self.driver.find_element(*reg_loc.reg_email).send_keys(email_id)
#
#     def enter_reg_pwd(self, password):
#         self.driver.find_element(*reg_loc.reg_pwd).send_keys(password)
#
#     def enter_confirm_pwd(self, confirm_pwd):
#         self.driver.find_element(*reg_loc.confirm_pwd).send_keys(confirm_pwd)

#####################################################################################################

'''
STEP7

'''

# from object_repository.reg_repo import RegisterLocators
#
# reg_loc = RegisterLocators()
#
# class SeleniumWrapper:
#
#     def __init__(self, driver):
#         self.driver = driver
#
#     def click_on_element(self, element):
#         self.driver.find_element(*element).click()
#
#     def enter_data(self, element, data):
#         self.driver.find_element(*element).send_keys(data)
#
#
# class Register:
#
#     def __init__(self, driver):
#         self.driver = driver        ## self.driver --> driver = webdriver.Chrome()
#         self.sel_ = SeleniumWrapper(driver)
#
#     def click_on_register(self):
#         # self.driver.find_element(*reg_loc.reg_link).click()
#         self.sel_.click_on_element(reg_loc.reg_link)
#
#     def click_on_gender_btn(self):
#         # self.driver.find_element(*reg_loc.gender_btn).click()
#         self.sel_.click_on_element(reg_loc.gender_btn)
#
#     def enter_firstname(self, fname):
#         # self.driver.find_element(*reg_loc.firstname).send_keys(fname)
#         self.sel_.enter_data(reg_loc.firstname, fname)
#
#     def enter_lastname(self, lname):
#         # self.driver.find_element(*reg_loc.lastname).send_keys(lname)
#         self.sel_.enter_data(reg_loc.lastname, lname)
#
#     def enter_reg_email(self, email_id):
#         # self.driver.find_element(*reg_loc.reg_email).send_keys(email_id)
#         self.sel_.enter_data(reg_loc.reg_email, email_id)
#
#     def enter_reg_pwd(self, password):
#         # self.driver.find_element(*reg_loc.reg_pwd).send_keys(password)
#         self.sel_.enter_data(reg_loc.reg_pwd, password)
#
#     def enter_confirm_pwd(self, confirm_pwd):
#         # self.driver.find_element(*reg_loc.confirm_pwd).send_keys(confirm_pwd)
#         self.sel_.enter_data(reg_loc.confirm_pwd, confirm_pwd)

#####################################################################################################

'''
STEP7

'''

from object_repository.reg_repo import RegisterLocators
from generic_utilities.webdriver_utility import SeleniumWrapper

reg_loc = RegisterLocators()


class Register:

    def __init__(self, driver):
        self.driver = driver        ## self.driver --> driver = webdriver.Chrome()
        self.sel_ = SeleniumWrapper(driver)

    def click_on_register(self):
        self.sel_.click_on_element(reg_loc.reg_link)

    def click_on_gender_btn(self):
        self.sel_.click_on_element(reg_loc.gender_btn)

    def enter_firstname(self, fname):
        self.sel_.enter_data(reg_loc.firstname, fname)

    def enter_lastname(self, lname):
        self.sel_.enter_data(reg_loc.lastname, lname)

    def enter_reg_email(self, email_id):
        self.sel_.enter_data(reg_loc.reg_email, email_id)

    def enter_reg_pwd(self, password):
        self.sel_.enter_data(reg_loc.reg_pwd, password)

    def enter_confirm_pwd(self, confirm_pwd):
        self.sel_.enter_data(reg_loc.confirm_pwd, confirm_pwd)

























