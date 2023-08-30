from pages.base_page import BasePage
from pages.problem_user_page_locator import ProblemUserLocators
from resources.constants import MAX_WAIT_INTERVAL


class ProblemUsersPage(BasePage):
    def wait_and_type_user_name(self, username_and_pw_list):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, ProblemUserLocators.USERNAME_TEXT_BOX).send_keys(
            username_and_pw_list[0])

    def wait_and_type_password(self, username_and_pw_list):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, ProblemUserLocators.PASSWORD_TEXT_BOX).send_keys(
            username_and_pw_list[1])

    def click_login_btn(self):
        self.find_element(ProblemUserLocators.LOGIN_BTN).click()

    def verify_image(self):
        verify_image = self.explicitly_wait_and_find_element(
            MAX_WAIT_INTERVAL, ProblemUserLocators.PROBLEM_USER_IMG)
        return verify_image

    def get_problem_user_label(self):
        lbl_lock_out_txt = self.explicitly_wait_and_find_element(
            MAX_WAIT_INTERVAL, ProblemUserLocators.LOCK_OUT_TEXT_LBL).text
        return lbl_lock_out_txt

    def click_error_btn(self):
        self.find_element(ProblemUserLocators.LOCK_OUT_USER_ERROR_BTN).click()

    def clear_user_name(self):
        self.find_element(ProblemUserLocators.USERNAME_TEXT_BOX).clear()

    def clear_user_password(self):
        self.find_element(ProblemUserLocators.USERNAME_TEXT_BOX).clear()
