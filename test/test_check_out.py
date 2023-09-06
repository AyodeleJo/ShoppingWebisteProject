from test_utils import *
from resources.constants import TEST_SITE_URL
from pages.check_out_page import CheckOutPage


class TestCheckOut:

    def test_check_out(self, driver, user_name_password):
        check_out = CheckOutPage(driver)
        check_out.navigate_to(TEST_SITE_URL)
        driver.maximize_window()
        check_out.wait_and_type_user_name(user_name_password)
        check_out.wait_and_type_pass_word(user_name_password)
        check_out.click_login_btn()
        check_out.add_to_cart_btn1()
        check_out.add_to_cart_btn2()
        check_out.add_to_cart_btn3()
        check_out.click_cart_link()
        check_out.click_check_out_btn()

        check_out_lbl = check_out.verify_check_out_lbl()
        assert check_out_lbl == "Checkout: Your Information", "failed"

    def test_personal_info_form(self, driver, personal_info, user_name_password):
        form_page = CheckOutPage(driver)
        form_page.navigate_to(TEST_SITE_URL)
        driver.maximize_window()

        form_page.wait_and_type_user_name(user_name_password)
        form_page.wait_and_type_pass_word(user_name_password)
        form_page.click_login_btn()
        # form_page.add_to_cart_btn1()
        form_page.click_cart_link()
        form_page.click_check_out_btn()
        form_page.wait_and_type_first_name(personal_info)
        form_page.wait_and_type_last_name(personal_info)
        form_page.wait_and_type_postal_code(personal_info)
        form_page.click_cont_btn()
        form_page_cont_lbl = form_page.verify_check_info_con_btn()
        assert form_page_cont_lbl == "Checkout: Overview", "failed"

    def test_no_info_form(self, driver, user_name_password, personal_info):
        form_page = CheckOutPage(driver)
        form_page.navigate_to(TEST_SITE_URL)
        driver.maximize_window()

        form_page.wait_and_type_user_name(user_name_password)
        form_page.wait_and_type_pass_word(user_name_password)
        form_page.click_login_btn()
        # form_page.add_to_cart_btn1()
        form_page.click_cart_link()
        form_page.click_check_out_btn()
        # entering the last name and postal code only
        form_page.wait_and_type_last_name(personal_info)
        form_page.wait_and_type_postal_code(personal_info)
        form_page.click_cont_btn()
        error_msg_lbl = form_page.verify_error_text_lbl()
        assert error_msg_lbl == "Error: First Name is required", "failed"

    def test_overview_info(self, driver, user_name_password, personal_info):
        overview_page = CheckOutPage(driver)
        overview_page.navigate_to(TEST_SITE_URL)
        driver.maximize_window()

        overview_page.wait_and_type_user_name(user_name_password)
        overview_page.wait_and_type_pass_word(user_name_password)
        overview_page.click_login_btn()
        # overview_page.add_to_cart_btn1()
        # overview_page.add_to_cart_btn2()
        overview_page.click_cart_link()
        overview_page.click_check_out_btn()
        overview_page.wait_and_type_first_name(personal_info)
        overview_page.wait_and_type_last_name(personal_info)
        overview_page.wait_and_type_postal_code(personal_info)
        overview_page.click_cont_btn()
        payment_info_lbl = overview_page.verify_payment_info()
        assert payment_info_lbl == "SauceCard #31337", "failed"

        shipping_info_lbl = overview_page.verify_shipping_info()
        assert shipping_info_lbl == "Free Pony Express Delivery!", "failed"

        price_info_lbl = overview_page.verify_price_info()
        assert price_info_lbl == "Item total: $47.97", "failed"

    def test_final_confirmation_page(self, driver, user_name_password, personal_info):
        confirmation_page = CheckOutPage(driver)
        confirmation_page.navigate_to(TEST_SITE_URL)
        confirmation_page.wait_and_type_user_name(user_name_password)
        confirmation_page.wait_and_type_pass_word(user_name_password)
        confirmation_page.click_login_btn()
        # confirmation_page.add_to_cart_btn1()
        # confirmation_page.add_to_cart_btn2()
        confirmation_page.click_cart_link()
        confirmation_page.click_check_out_btn()
        confirmation_page.wait_and_type_first_name(personal_info)
        confirmation_page.wait_and_type_last_name(personal_info)
        confirmation_page.wait_and_type_postal_code(personal_info)
        confirmation_page.click_cont_btn()
        confirmation_page.click_finish_btn()
        final_con_info = confirmation_page.verify_final_check_out_lbl()
        assert final_con_info == "Thank you for your order!", "failed"
