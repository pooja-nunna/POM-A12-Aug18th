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

class Login:

    def __init__(self, driver):
        self.driver = driver        ## self.driver --> driver = webdriver.Chrome()

    def click_on_login(self):
        self.driver.find_element('xpath', '//a[text()="Log in"]').click()

    def enter_login_email(self, email_id):
        self.driver.find_element('id', 'Email').send_keys(email_id)

    def enter_login_pwd(self, password):
        self.driver.find_element('id', 'Password').send_keys(password)






























































