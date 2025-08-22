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
# driver.find_element('xpath', '//a[text()="Log in"]').click()
# driver.find_element('id', 'Email').send_keys('maanas@gmail.com')
# driver.find_element('id', 'Password').send_keys('maanas@12345')

###########################################################################################################

'''
STEP 2
In step2 we are defining the classes/attributes. 
Created the object for Login class.
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
# class Login:
#
#     def click_on_login(self):
#         driver.find_element('xpath', '//a[text()="Log in"]').click()
#
#     def enter_login_email(self, email_id):
#         driver.find_element('id', 'Email').send_keys(email_id)
#
#     def enter_login_pwd(self, password):
#         driver.find_element('id', 'Password').send_keys(password)
#
# login_obj = Login()
# login_obj.click_on_login()
# login_obj.enter_login_email('maanas@gmail.com')
# login_obj.enter_login_pwd('maanas@12345')

###########################################################################################################

'''
STEP 3
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
# class Login:
#
#     def click_on_login(self):
#         driver.find_element('xpath', '//a[text()="Log in"]').click()
#
#     def enter_login_email(self, email_id):
#         driver.find_element('id', 'Email').send_keys(email_id)
#
#     def enter_login_pwd(self, password):
#         driver.find_element('id', 'Password').send_keys(password)


###########################################################################################################

'''
STEP4   :   We removed the initialization of driver and launching of the web-application and we gave it in the test_login.py 
'''

# class Login:
#
#     def click_on_login(self):
#         driver.find_element('xpath', '//a[text()="Log in"]').click()
#
#     def enter_login_email(self, email_id):
#         driver.find_element('id', 'Email').send_keys(email_id)
#
#     def enter_login_pwd(self, password):
#         driver.find_element('id', 'Password').send_keys(password)
#
# ## ERROR
# ## Because there is no driver in this file

###########################################################################################################

'''
STEP5'''

# class Login:
#
#     def __init__(self, driver):
#         self.driver = driver        ## self.driver --> driver = webdriver.Chrome()
#
#     def click_on_login(self):
#         self.driver.find_element('xpath', '//a[text()="Log in"]').click()
#
#     def enter_login_email(self, email_id):
#         self.driver.find_element('id', 'Email').send_keys(email_id)
#
#     def enter_login_pwd(self, password):
#         self.driver.find_element('id', 'Password').send_keys(password)

###########################################################################################################

'''
STEP6

'''

# from object_repository.login_repo import LoginLocators
#
# login_loc = LoginLocators()
#
# class Login:
#
#     def __init__(self, driver):
#         self.driver = driver        ## self.driver --> driver = webdriver.Chrome()
#
#     def click_on_login(self):
#         # self.driver.find_element('xpath', '//a[text()="Log in"]').click()
#         self.driver.find_element(*login_loc.login_link).click()
#
#     def enter_login_email(self, email_id):
#         # self.driver.find_element('id', 'Email').send_keys(email_id)
#         self.driver.find_element(*login_loc.login_email).send_keys(email_id)
#
#     def enter_login_pwd(self, password):
#         # self.driver.find_element('id', 'Password').send_keys(password)
#         self.driver.find_element(*login_loc.login_pwd).send_keys(password)


###########################################################################################################

'''
STEP6

'''
#
# from object_repository.login_repo import LoginLocators
#
# login_loc = LoginLocators()
#
# class Login:
#
#     def __init__(self, driver):
#         self.driver = driver        ## self.driver --> driver = webdriver.Chrome()
#
#     def click_on_login(self):
#         self.driver.find_element(*login_loc.login_link).click()
#
#     def enter_login_email(self, email_id):
#         self.driver.find_element(*login_loc.login_email).send_keys(email_id)
#
#     def enter_login_pwd(self, password):
#         self.driver.find_element(*login_loc.login_pwd).send_keys(password)

###########################################################################################################

'''
STEP7

'''

# from object_repository.login_repo import LoginLocators
#
# login_loc = LoginLocators()
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
# class Login:
#
#     def __init__(self, driver):
#         self.driver = driver        ## self.driver --> driver = webdriver.Chrome()
#         self.sel_ = SeleniumWrapper(driver)
#
#     def click_on_login(self):
#         # self.driver.find_element(*login_loc.login_link).click()
#         self.sel_.click_on_element(login_loc.login_link)
#
#     def enter_login_email(self, email_id):
#         # self.driver.find_element(*login_loc.login_email).send_keys(email_id)
#         self.sel_.enter_data(login_loc.login_email, email_id)
#
#     def enter_login_pwd(self, password):
#         # self.driver.find_element(*login_loc.login_pwd).send_keys(password)
#         self.sel_.enter_data(login_loc.login_pwd, password)

###########################################################################################################

'''
STEP7

'''

from object_repository.login_repo import LoginLocators

login_loc = LoginLocators()

class SeleniumWrapper:

    def __init__(self, driver):
        self.driver = driver

    def click_on_element(self, element):
        self.driver.find_element(*element).click()

    def enter_data(self, element, data):
        self.driver.find_element(*element).send_keys(data)

class Login:

    def __init__(self, driver):
        self.driver = driver        ## self.driver --> driver = webdriver.Chrome()
        self.sel_ = SeleniumWrapper(driver)

    def click_on_login(self):
        self.sel_.click_on_element(login_loc.login_link)

    def enter_login_email(self, email_id):
        self.sel_.enter_data(login_loc.login_email, email_id)

    def enter_login_pwd(self, password):
        self.sel_.enter_data(login_loc.login_pwd, password)


























































