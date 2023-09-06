from test_utils import *
from resources.constants import TEST_SITE_URL
from pages.product_page import ProductPage
from resources.constants import TEST_SITE_URL, MAX_ALLOWED_DIFF_PERCENTAGE


class TestProduct:

    def test_verify_product_in_cart(self, driver, user_name_password):
        product_page = ProductPage(driver)
        product_page.navigate_to(TEST_SITE_URL)
        product_page.driver_take_screenshot5()
        product_page.wait_and_type_user_name(user_name_password)
        product_page.wait_and_type_password(user_name_password)
        product_page.click_login_btn()
        product_page.add_to_cart_btn()
        product_page.click_cart_link()

        product_text_lbl = product_page.get_product_label()
        assert product_text_lbl == "Sauce Labs Backpack", "failed"

    def test_remove_product_from_cart(self, driver, user_name_password):
        product_page = ProductPage(driver)
        product_page.navigate_to(TEST_SITE_URL)
        product_page.driver_maximize_window()
        product_page.wait_and_type_user_name(user_name_password)
        product_page.wait_and_type_password(user_name_password)
        product_page.click_login_btn()
        # product_page.add_to_cart_btn()
        product_page.click_cart_link()
        product_page.click_remove_btn()
        product_page.driver_take_screenshot5()
        empty_cart_text_lbl = product_page.get_empty_cart_text()
        assert empty_cart_text_lbl == "QTY", "failed"

    def test_for_product_image(self, driver, user_name_password):
        product_page = ProductPage(driver)
        product_page.navigate_to(TEST_SITE_URL)
        product_page.driver_maximize_window()
        product_page.wait_and_type_user_name(user_name_password)
        product_page.wait_and_type_password(user_name_password)
        product_page.click_login_btn()

        percentage_diff = product_page.verify_product_image1()
        assert percentage_diff <= MAX_ALLOWED_DIFF_PERCENTAGE, f"Images are different by {percentage_diff}%"

        percentage_diff = product_page.verify_product_image2()
        assert percentage_diff <= MAX_ALLOWED_DIFF_PERCENTAGE, f"Images are different by {percentage_diff}%"

        percentage_diff = product_page.verify_product_image3()
        assert percentage_diff <= MAX_ALLOWED_DIFF_PERCENTAGE, f"Images are different by {percentage_diff}%"

        percentage_diff = product_page.verify_product_image4()
        assert percentage_diff <= MAX_ALLOWED_DIFF_PERCENTAGE, f"Images are different by {percentage_diff}%"

        percentage_diff = product_page.verify_product_image5()
        assert percentage_diff <= MAX_ALLOWED_DIFF_PERCENTAGE, f"Images are different by {percentage_diff}%"

        percentage_diff = product_page.verify_product_image6()
        assert percentage_diff <= MAX_ALLOWED_DIFF_PERCENTAGE, f"Images are different by {percentage_diff}%"

        print("all picture assertion complete")

    def test_for_product_description(self, driver, user_name_password):
        product_page = ProductPage(driver)
        product_page.navigate_to(TEST_SITE_URL)
        product_page.driver_maximize_window()
        product_page.wait_and_type_user_name(user_name_password)
        product_page.wait_and_type_password(user_name_password)
        product_page.click_login_btn()

        first_product_lbl = product_page.verify_product_name()
        assert first_product_lbl == "Sauce Labs Backpack", "failed"

        first_product_lbl = product_page.verify_product_name2()
        assert first_product_lbl == "Sauce Labs Bike Light", "failed"
        first_product_lbl = product_page.verify_product_name3()
        assert first_product_lbl == "Sauce Labs Bolt T-Shirt", "failed"
        first_product_lbl = product_page.verify_product_name4()
        assert first_product_lbl == "Sauce Labs Fleece Jacket", "failed"
        first_product_lbl = product_page.verify_product_name5()
        assert first_product_lbl == "Sauce Labs Onesie", "failed"
        first_product_lbl = product_page.verify_product_name6()
        assert first_product_lbl == "Test.allTheThings() T-Shirt (Red)", "failed"

    def test_price(self, driver, user_name_password):
        product_page = ProductPage(driver)
        product_page.navigate_to(TEST_SITE_URL)
        product_page.driver_maximize_window()
        product_page.wait_and_type_user_name(user_name_password)
        product_page.wait_and_type_password(user_name_password)
        product_page.click_login_btn()
        first_product_price = product_page.verify_product_price1()
        assert first_product_price == "$29.99", "failed"
        second_product_price = product_page.verify_product_price2()
        assert second_product_price == "$9.99", "failed"
        third_product_price = product_page.verify_product_price3()
        assert third_product_price == "$15.99", "failed"
        fourth_product_price = product_page.verify_product_price4()
        assert fourth_product_price == "$49.99", "failed"
        fifth_product_price = product_page.verify_product_price5()
        assert fifth_product_price == "$7.99", "failed"
        sixth_product_price = product_page.verify_product_price6()
        assert sixth_product_price == "$15.99", "failed"
