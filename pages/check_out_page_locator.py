from selenium.webdriver.common.by import By


class CheckOutPageLocator:
    USERNAME_TEXT_BOX = (By.NAME, "user-name")
    PASSWORD_TEXT_BOX = (By.NAME, "password")
    LOGIN_BTN = (By.NAME, "login-button")
    SHOPPING_CART_LINK = (By.XPATH, "//a[@class='shopping_cart_link']")
    CHECK_OUT_BTN = (By.XPATH, "//button[@id='checkout']")
    ADD_TO_CART_BTN1 = (By.XPATH, "//*[@id='add-to-cart-sauce-labs-backpack']")
    ADD_TO_CART_BTN2 = (By.XPATH, "//*[@id='add-to-cart-sauce-labs-bike-light']")
    ADD_TO_CART_BTN3 = (By.XPATH, "//*[@id='add-to-cart-sauce-labs-onesie']")
    CONTINUE_BTN = (By.XPATH, "//input[@id='continue']")
    CHECK_OUT_TEXT_LBL = (By.XPATH, "//span[@class='title']")
    FIRST_NAME = (By.XPATH, "//input[@id='first-name']")
    LAST_NAME = (By.XPATH, "//input[@id='last-name']")
    POSTAL_CODE = (By.XPATH, "//input[@id='postal-code']")
    OVER_VIEW_LBL = (By.XPATH, "//span[text()='Checkout: Overview']")
    CHECK_OUT_COMPLETE_LBL = (By.XPATH, "//h2")
    PAYMENT_INFO_LBL = (By.XPATH, "//div[text()='SauceCard #31337']")
    SHIPPING_INFO_LBL = (By.XPATH, "//div[text()='Free Pony Express Delivery!']")
    ITEM_TOTAL_LBL = (By.XPATH, "//div[text()='Item total: $']")
    FINISH_BTN = (By.XPATH, "//button[@id='finish']")
    NO_INFO_ERROR_LBL = (By.XPATH, "//h3")

    ERROR_BTN_LBL = (By.XPATH, "//button[@class='error-button']")

