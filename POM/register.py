import time

# ## STEP1
#
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
from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)
driver.implicitly_wait(10)

driver.get('https://demowebshop.tricentis.com/')
time.sleep(2)

class Register:

    def click_on_register(self):
        driver.find_element('xpath', '//a[text()="Register"]').click()

    def click_on_gender_btn(self):
        driver.find_element('id', 'gender-male').click()

    def enter_firstname(self, fname):
        driver.find_element('id', 'FirstName').send_keys(fname)

    def enter_lastname(self, lname):
        driver.find_element('id', 'LastName').send_keys(lname)

    def enter_reg_email(self, email_id):
        driver.find_element('id', 'Email').send_keys(email_id)

    def enter_reg_pwd(self, password):
        driver.find_element('id', 'Password').send_keys(password)

    def enter_confirm_pwd(self, confirm_pwd):
        driver.find_element('id', 'ConfirmPassword').send_keys(confirm_pwd)













































