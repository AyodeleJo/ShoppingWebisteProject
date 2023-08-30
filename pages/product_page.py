from pages.base_page import BasePage
from pages.product_page_locator import ProductPageLocators
from resources.constants import MAX_WAIT_INTERVAL


class ProductPage(BasePage):
    def wait_and_type_user_name(self, username_and_pw_list):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, ProductPageLocators.USERNAME_TEXT_BOX).send_keys(
            username_and_pw_list[0])

    def wait_and_type_password(self, username_and_pw_list):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, ProductPageLocators.PASSWORD_TEXT_BOX).send_keys(
            username_and_pw_list[1])

    def click_login_btn(self):
        self.find_element(ProductPageLocators.LOGIN_BTN).click()

    def add_to_cart_btn(self):
        self.find_element(ProductPageLocators.ADD_TO_CART_BTN).click()

    def click_cart_link(self):
        self.find_element(ProductPageLocators.SHOPPING_CART_LINK).click()

    def click_remove_btn(self):
        self.find_element(ProductPageLocators.REMOVE_BTN).click()

    def get_product_label(self):
        product_lbl__txt = self.explicitly_wait_and_find_element(
            MAX_WAIT_INTERVAL, ProductPageLocators.PRODUCT_TEXT_LBL).text
        return product_lbl__txt

    def get_empty_cart_text(self):
        empty_cart_lbl__txt = self.explicitly_wait_and_find_element(
            MAX_WAIT_INTERVAL, ProductPageLocators.EMPTY_CART_TEXT_LBL).text
        return empty_cart_lbl__txt

    def verify_product_image1(self):
        self.capture_web_element_as_an_image(ProductPageLocators.PRODUCT_IMAGE_ONE, "captured_product_image1.jpg")
        percentage_dif = self.compare_images("product_image1.jpg", "captured_product_image1.jpg")
        return percentage_dif

    def verify_product_image2(self):
        self.capture_web_element_as_an_image(ProductPageLocators.PRODUCT_IMAGE_TWO, "product_image2.jpg")
        percentage_dif = self.compare_images("product_image2.jpg", "product_image2.jpg")
        return percentage_dif

    def verify_product_image3(self):
        self.capture_web_element_as_an_image(ProductPageLocators.PRODUCT_IMAGE_THREE, "product_image3.jpg")
        percentage_dif = self.compare_images("product_image3.jpg", "product_image3.jpg")
        return percentage_dif

    def verify_product_image4(self):
        self.capture_web_element_as_an_image(ProductPageLocators.PRODUCT_IMAGE_FOUR, "product_image4.jpg")
        percentage_dif = self.compare_images("product_image4.jpg", "product_image4.jpg")
        return percentage_dif

    def verify_product_image5(self):
        self.capture_web_element_as_an_image(ProductPageLocators.PRODUCT_IMAGE_FIVE, "product_image5.jpg")
        percentage_dif = self.compare_images("product_image5.jpg", "product_image5.jpg")
        return percentage_dif

    def verify_product_image6(self):
        self.capture_web_element_as_an_image(ProductPageLocators.PRODUCT_IMAGE_SIX, "product_image6.jpg")
        percentage_dif = self.compare_images("product_image6.jpg", "product_image6.jpg")
        return percentage_dif

    def verify_product_name(self):
        product_lbl_text = self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL,
                                                                 ProductPageLocators.PRODUCT_ONE_TEXT_LBL).text
        return product_lbl_text

    def verify_product_name2(self):
        product_lbl_text = self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL,
                                                                 ProductPageLocators.PRODUCT_TWO_TEXT_LBL).text
        return product_lbl_text

    def verify_product_name3(self):
        product_lbl_text = self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL,
                                                                 ProductPageLocators.PRODUCT_THREE_TEXT_LBL).text
        return product_lbl_text

    def verify_product_name4(self):
        product_lbl_text = self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL,
                                                                 ProductPageLocators.PRODUCT_FOUR_TEXT_LBL).text
        return product_lbl_text

    def verify_product_name5(self):
        product_lbl_text = self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL,
                                                                 ProductPageLocators.PRODUCT_FIVE_TEXT_LBL).text
        return product_lbl_text

    def verify_product_name6(self):
        product_lbl_text = self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL,
                                                                 ProductPageLocators.PRODUCT_SIX_TEXT_LBL).text
        return product_lbl_text

    def verify_product_price1(self):
        product_lbl_text = self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL,
                                                                 ProductPageLocators.PRODUCT_PRICE_0NE_LBL).text
        return product_lbl_text

    def verify_product_price2(self):
        product_lbl_text = self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL,
                                                                 ProductPageLocators.PRODUCT_PRICE_TWO_LBL).text
        return product_lbl_text

    def verify_product_price3(self):
        product_lbl_text = self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL,
                                                                 ProductPageLocators.PRODUCT_PRICE_THREE_LBL).text
        return product_lbl_text

    def verify_product_price4(self):
        product_lbl_text = self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL,
                                                                 ProductPageLocators.PRODUCT_PRICE_FOUR_LBL).text
        return product_lbl_text

    def verify_product_price5(self):
        product_lbl_text = self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL,
                                                                 ProductPageLocators.PRODUCT_PRICE_FIVE_LBL).text
        return product_lbl_text

    def verify_product_price6(self):
        product_lbl_text = self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL,
                                                                 ProductPageLocators.PRODUCT_PRICE_SIX_LBL).text
        return product_lbl_text

