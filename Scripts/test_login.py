# ## STEP3
#
# from POM.login import Login
#
# def test_login():
#     login_obj = Login()
#     login_obj.click_on_login()
#     login_obj.enter_login_email('maanas@gmail.com')
#     login_obj.enter_login_pwd('maanas@12345')

# ####################################################################################
#
# ## STEP3 only
# ## We are reading the test data from the excel
#
# from POM.login import Login
# from generic_utilities.excel_utility import excel_data
#
# data = excel_data('login')
# print(data)     ## {'email': 'maanas@gmail.com', 'pwd': 'maanas@12345'}
#
# '''
# data['email'] = 'maanas@gmail.com'
# data['pwd'] = 'maanas@12345'
# '''
#
# def test_login():
#     login_obj = Login()
#     login_obj.click_on_login()
#     login_obj.enter_login_email(data['email'])
#     login_obj.enter_login_pwd(data['pwd'])


####################################################################################

## STEP3 only
## We are reading the test data from the excel. Same as above step. Removed commented lines


from POM.login import Login
from generic_utilities.excel_utility import excel_data

data = excel_data('login')

def test_login():
    login_obj = Login()
    login_obj.click_on_login()
    login_obj.enter_login_email(data['email'])
    login_obj.enter_login_pwd(data['pwd'])













