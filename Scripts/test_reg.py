# ## STEP3
#
# from POM.register import Register
#
# def test_reg():
#     reg_obj = Register()
#     reg_obj.click_on_register()
#     reg_obj.click_on_gender_btn()
#     reg_obj.enter_firstname('Maanas')
#     reg_obj.enter_lastname('Jadhav')
#     reg_obj.enter_reg_email('maanas@gmail.com')
#     reg_obj.enter_reg_pwd('maanas@12345')
#     reg_obj.enter_confirm_pwd('maanas@12345')
#
# #################################################################################
#
#
# ## STEP3
# ## We are reading the test data from the excel
#
#
# from POM.register import Register
# from generic_utilities.excel_utility import excel_data
#
# data = excel_data('reg')
# # print(data)
#
# ## {'fname': 'Maanas', 'lname': 'Jadhav', 'email': 'maanas@gmail.com', 'pwd': 'maanas@12345',
# ### 'pwd_confirm': 'maanas@12345'}
#
# '''
# data['fname'] = 'Maanas'
# data['lname'] = 'Jadhav'
# data['email'] = 'maanas@gmail.com'
# data['pwd'] = 'maanas@12345'
# data['pwd_confirm'] = 'maanas@12345'
# '''
#
# def test_reg():
#     reg_obj = Register()
#     reg_obj.click_on_register()
#     reg_obj.click_on_gender_btn()
#     reg_obj.enter_firstname(data['fname'])
#     reg_obj.enter_lastname(data['lname'])
#     reg_obj.enter_reg_email(data['email'])
#     reg_obj.enter_reg_pwd(data['pwd'])
#     reg_obj.enter_confirm_pwd(data['pwd_confirm'])


# #################################################################################
#
# ## STEP3
# ## We are reading the test data from the excel. Same as above step. Removed commented lines
#
#
# from POM.register import Register
# from generic_utilities.excel_utility import excel_data
#
# data = excel_data('reg')
#
# def test_reg():
#     reg_obj = Register()
#     reg_obj.click_on_register()
#     reg_obj.click_on_gender_btn()
#     reg_obj.enter_firstname(data['fname'])
#     reg_obj.enter_lastname(data['lname'])
#     reg_obj.enter_reg_email(data['email'])
#     reg_obj.enter_reg_pwd(data['pwd'])
#     reg_obj.enter_confirm_pwd(data['pwd_confirm'])

# #################################################################################
#
# ## STEP4
#
# import time
#
# from selenium import webdriver
#
# from POM.register import Register
# from generic_utilities.excel_utility import excel_data
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
# data = excel_data('reg')
#
# def test_reg():
#     reg_obj = Register()
#     reg_obj.click_on_register()
#     reg_obj.click_on_gender_btn()
#     reg_obj.enter_firstname(data['fname'])
#     reg_obj.enter_lastname(data['lname'])
#     reg_obj.enter_reg_email(data['email'])
#     reg_obj.enter_reg_pwd(data['pwd'])
#     reg_obj.enter_confirm_pwd(data['pwd_confirm'])

# #################################################################################
#
# ## STEP5
#
# import time
#
# from selenium import webdriver
#
# from POM.register import Register
# from generic_utilities.excel_utility import excel_data
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
# data = excel_data('reg')
#
# def test_reg():
#     reg_obj = Register(driver)
#     reg_obj.click_on_register()
#     reg_obj.click_on_gender_btn()
#     reg_obj.enter_firstname(data['fname'])
#     reg_obj.enter_lastname(data['lname'])
#     reg_obj.enter_reg_email(data['email'])
#     reg_obj.enter_reg_pwd(data['pwd'])
#     reg_obj.enter_confirm_pwd(data['pwd_confirm'])
#

# #################################################################################
#
# ## STEP5
#
# import time
# import pytest
#
# from selenium import webdriver
#
# from POM.register import Register
# from generic_utilities.excel_utility import excel_data
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# @pytest.fixture()
# def browser_setup():
#     driver = webdriver.Chrome(opts)
#     driver.implicitly_wait(10)
#     driver.get('https://demowebshop.tricentis.com/')
#     time.sleep(2)
#     yield driver
#
# data = excel_data('reg')
#
# ## browser_setup --> driver
#
# def test_reg(browser_setup):
#     reg_obj = Register(browser_setup)
#     reg_obj.click_on_register()
#     reg_obj.click_on_gender_btn()
#     reg_obj.enter_firstname(data['fname'])
#     reg_obj.enter_lastname(data['lname'])
#     reg_obj.enter_reg_email(data['email'])
#     reg_obj.enter_reg_pwd(data['pwd'])
#     reg_obj.enter_confirm_pwd(data['pwd_confirm'])
#

#################################################################################

## STEP5

from POM.register import Register
from generic_utilities.excel_utility import excel_data

data = excel_data('reg')

def test_reg(browser_setup):
    reg_obj = Register(browser_setup)
    reg_obj.click_on_register()
    reg_obj.click_on_gender_btn()
    reg_obj.enter_firstname(data['fname'])
    reg_obj.enter_lastname(data['lname'])
    reg_obj.enter_reg_email(data['email'])
    reg_obj.enter_reg_pwd(data['pwd'])
    reg_obj.enter_confirm_pwd(data['pwd_confirm'])





















