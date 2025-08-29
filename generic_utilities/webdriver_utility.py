from selenium.webdriver.common.action_chains import ActionChains

class SeleniumWrapper:

    def __init__(self, driver):
        self.driver = driver
        self.ac_obj = ActionChains(driver)

    def click_on_element(self, element):
        self.driver.find_element(*element).click()

    def enter_data(self, element, data):
        self.driver.find_element(*element).send_keys(data)

    def mouse_over(self, element):
        self.ac_obj.move_to_element(element).perform()

    def double_click(self, element):
        self.ac_obj.double_click(element).perform()

    def implicit_wait(self, seconds):
        self.driver.implicitly_wait(seconds)




















