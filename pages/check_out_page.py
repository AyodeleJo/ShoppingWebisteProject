from pages.base_page import BasePage
from pages.check_out_page_locator import CheckOutPageLocator
from resources.constants import MAX_WAIT_INTERVAL


class CheckOutPage(BasePage):
    def wait_and_type_user_name(self, username_and_pw_list):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, CheckOutPageLocator.USERNAME_TEXT_BOX).send_keys(
            username_and_pw_list[0])

    def wait_and_type_pass_word(self, username_and_pw_list):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, CheckOutPageLocator.PASSWORD_TEXT_BOX).send_keys(
            username_and_pw_list[1])

    def wait_and_type_first_name(self, personal_info_list):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, CheckOutPageLocator.FIRST_NAME).send_keys(
            personal_info_list[0])

    def wait_and_type_last_name(self, personal_info_list):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, CheckOutPageLocator.LAST_NAME).send_keys(
            personal_info_list[1])

    def wait_and_type_postal_code(self, personal_info_list):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, CheckOutPageLocator.POSTAL_CODE).send_keys(
            personal_info_list[2])

    def click_cont_btn(self):
        self.find_element(CheckOutPageLocator.CONTINUE_BTN).click()

    def click_login_btn(self):
        self.find_element(CheckOutPageLocator.LOGIN_BTN).click()

    def add_to_cart_btn1(self):
        self.find_element(CheckOutPageLocator.ADD_TO_CART_BTN1).click()

    def add_to_cart_btn2(self):
        self.find_element(CheckOutPageLocator.ADD_TO_CART_BTN2).click()

    def add_to_cart_btn3(self):
        self.find_element(CheckOutPageLocator.ADD_TO_CART_BTN3).click()

    def click_cart_link(self):
        self.find_element(CheckOutPageLocator.SHOPPING_CART_LINK).click()

    def click_check_out_btn(self):
        self.find_element(CheckOutPageLocator.CHECK_OUT_BTN).click()

    def verify_check_out_lbl(self):
        check_out_lbl_text = self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL,
                                                                   CheckOutPageLocator.CHECK_OUT_TEXT_LBL).text
        return check_out_lbl_text

    def verify_check_info_con_btn(self):
        check_out_cont_text = self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL,
                                                                    CheckOutPageLocator.OVER_VIEW_LBL).text
        return check_out_cont_text

    def verify_payment_info(self):
        payment_info_text = self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL,
                                                                  CheckOutPageLocator.PAYMENT_INFO_LBL).text
        return payment_info_text

    def verify_shipping_info(self):
        shipping_info_text = self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL,
                                                                   CheckOutPageLocator.SHIPPING_INFO_LBL).text
        return shipping_info_text

    def verify_price_info(self):
        price_info_text = self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL,
                                                                CheckOutPageLocator.ITEM_TOTAL_LBL).text
        return price_info_text

    def verify_error_text_lbl(self):
        error_lbl_text = self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL,
                                                               CheckOutPageLocator.NO_INFO_ERROR_LBL).text
        return error_lbl_text

    def click_finish_btn(self):
        self.find_element(CheckOutPageLocator.FINISH_BTN).click()

    def click_error_btn(self):
        self.find_element(CheckOutPageLocator.ERROR_BTN_LBL).click()

    def clear_firstname_(self):
        self.find_element(CheckOutPageLocator.FIRST_NAME).clear()

    def clear_lastname_(self):
        self.find_element(CheckOutPageLocator.LAST_NAME).clear()

    def clear_postalcode_(self):
        self.find_element(CheckOutPageLocator.POSTAL_CODE).clear()

    def verify_final_check_out_lbl(self):
        final_check_out_lbl_text = self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL,
                                                                         CheckOutPageLocator.CHECK_OUT_COMPLETE_LBL).text
        return final_check_out_lbl_text
