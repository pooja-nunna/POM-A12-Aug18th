from POM.register import Register
from POM.login import Login

def test_reg():
    reg_obj = Register()
    reg_obj.click_on_register()
    reg_obj.click_on_gender_btn()
    reg_obj.enter_firstname('Maanas')
    reg_obj.enter_lastname('Jadhav')
    reg_obj.enter_reg_email('maanas@gmail.com')
    reg_obj.enter_reg_pwd('maanas@12345')
    reg_obj.enter_confirm_pwd('maanas@12345')


def test_login():
    login_obj = Login()
    login_obj.click_on_login()
    login_obj.enter_login_email('maanas@gmail.com')
    login_obj.enter_login_pwd('maanas@12345')





































