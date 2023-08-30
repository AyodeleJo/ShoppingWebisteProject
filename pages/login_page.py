from pages.base_page import BasePage
from pages.login_page_locator import LoginPageLocators
from resources.constants import MAX_WAIT_INTERVAL


class LoginPage(BasePage):

    def wait_and_type_user_name(self, username_and_pw_list):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, LoginPageLocators.USERNAME_TEXT_BOX).send_keys(
            username_and_pw_list[0])

    def wait_and_type_password(self, username_and_pw_list):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, LoginPageLocators.PASSWORD_TEXT_BOX).send_keys(
            username_and_pw_list[1])

    def click_login_btn(self):
        self.find_element(LoginPageLocators.LOGIN_BTN).click()

    # This is a test
    def driver_back(self):
        self.driver_back()
