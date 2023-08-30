from pages.no_credential_user_page_locator import NoCredentialUserPageLocators
from resources.constants import MAX_WAIT_INTERVAL
from pages.base_page import BasePage


class NoCredentialUserPage(BasePage):
    def wait_and_type_user_name(self, username_and_pw_list):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, NoCredentialUserPageLocators.USERNAME_TEXT_BOX).send_keys(
            username_and_pw_list[0])

    def wait_and_type_password(self, username_and_pw_list):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, NoCredentialUserPageLocators.PASSWORD_TEXT_BOX).send_keys(
            username_and_pw_list[1])

    def click_login_btn(self):
        self.find_element(NoCredentialUserPageLocators.LOGIN_BTN).click()

    def get_no_credential_user_label(self):
        lbl_glitch_user_txt = self.explicitly_wait_and_find_element(
            MAX_WAIT_INTERVAL, NoCredentialUserPageLocators.NO_CREDENTIAL_USER_TEXT_LBL).text
        return lbl_glitch_user_txt

    def click_error_btn(self):
        self.find_element(NoCredentialUserPageLocators.GLITCH_USER_ERROR_BTN).click()

    def add_to_cart_btn(self):
        self.find_element(NoCredentialUserPageLocators.ADD_TO_CART_BTN).click()

    def click_cart_link(self):
        self.find_element(NoCredentialUserPageLocators.SHOPPING_CART_LINK).click()

    def clear_user_name(self):
        self.find_element(NoCredentialUserPageLocators.USERNAME_TEXT_BOX).clear()

    def clear_user_password(self):
        self.find_element(NoCredentialUserPageLocators.USERNAME_TEXT_BOX).clear()
