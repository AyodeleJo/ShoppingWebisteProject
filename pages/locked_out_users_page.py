from pages.lock_out_users_page_locator import LockOutUserPageLocators
from resources.constants import MAX_WAIT_INTERVAL
from pages.base_page import BasePage


class LockOutUsersPage(BasePage):
    def wait_and_type_user_name(self, username_and_pw_list):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, LockOutUserPageLocators.USERNAME_TEXT_BOX).send_keys(
            username_and_pw_list[0])

    def wait_and_type_password(self, username_and_pw_list):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, LockOutUserPageLocators.PASSWORD_TEXT_BOX).send_keys(
            username_and_pw_list[1])

    def click_login_btn(self):
        self.find_element(LockOutUserPageLocators.LOGIN_BTN).click()

    def get_lock_out_label(self):
        lbl_lock_out_txt = self.explicitly_wait_and_find_element(
            MAX_WAIT_INTERVAL, LockOutUserPageLocators.LOCK_OUT_TEXT_LBL).text
        return lbl_lock_out_txt

    def click_error_btn(self):
        self.find_element(LockOutUserPageLocators.LOCK_OUT_ERROR_BTN).click()

    def clear_user_name(self):
        self.find_element(LockOutUserPageLocators.USERNAME_TEXT_BOX).clear()

    def clear_user_password(self):
        self.find_element(LockOutUserPageLocators.USERNAME_TEXT_BOX).clear()
