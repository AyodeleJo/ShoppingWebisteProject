from selenium.webdriver.common.by import By


class ProductPageLocators:
    USERNAME_TEXT_BOX = (By.NAME, "user-name")
    PASSWORD_TEXT_BOX = (By.NAME, "password")
    LOGIN_BTN = (By.ID, "login-button")
    ADD_TO_CART_BTN = (By.XPATH, "//*[@id='add-to-cart-sauce-labs-backpack']")
    SHOPPING_CART_LINK = (By.XPATH, "//a[@class='shopping_cart_link']")
    PRODUCT_TEXT_LBL = (By.XPATH, "//div[@class='inventory_item_name']")
    REMOVE_BTN = (By.XPATH, "//button[@class='btn btn_secondary btn_small cart_button']")
    EMPTY_CART_TEXT_LBL =(By.XPATH, "//div[@class='cart_quantity_label']")
    PRODUCT_IMAGE_ONE = (By.XPATH, "//img[@alt='Sauce Labs Backpack']")
    PRODUCT_IMAGE_TWO = (By.XPATH, "//img[@alt='Sauce Labs Bike Light']")
    PRODUCT_IMAGE_THREE = (By.XPATH, "//img[@alt='Sauce Labs Bolt T-Shirt']")
    PRODUCT_IMAGE_FOUR = (By.XPATH, "//img[@alt='Sauce Labs Fleece Jacket']")
    PRODUCT_IMAGE_FIVE = (By.XPATH, "//img[@alt='Sauce Labs Onesie']")
    PRODUCT_IMAGE_SIX = (By.XPATH, "//img[@alt='Test.allTheThings() T-Shirt (Red)']")
    CHECK_OUT_BTN = (By.XPATH, "//button[@id='checkout']")
    PRODUCT_ONE_TEXT_LBL = (By.XPATH, "//div[text() ='Sauce Labs Backpack']")
    PRODUCT_TWO_TEXT_LBL = (By.XPATH, "//div[text() ='Sauce Labs Bike Light']")
    PRODUCT_THREE_TEXT_LBL = (By.XPATH, "//div[text() ='Sauce Labs Bolt T-Shirt']")
    PRODUCT_FOUR_TEXT_LBL = (By.XPATH, "//div[text() ='Sauce Labs Fleece Jacket']")
    PRODUCT_FIVE_TEXT_LBL = (By.XPATH, "//div[text() ='Sauce Labs Onesie']")
    PRODUCT_SIX_TEXT_LBL = (By.XPATH, "//div[text() ='Test.allTheThings() T-Shirt (Red)']")
    CHECK_OUT_TEXT_LBL = (By.XPATH, "//h2[@class='complete-header']")
    FILTER_ICON = (By.XPATH, "//select")
    PRODUCT_PRICE_0NE_LBL = (By.XPATH, "//*[@id='inventory_container']/div/div[1]/div[2]/div[2]/div")
    PRODUCT_PRICE_TWO_LBL = (By.XPATH, "//*[@id='inventory_container']/div/div[2]/div[2]/div[2]/div")
    PRODUCT_PRICE_THREE_LBL = (By.XPATH, "//*[@id='inventory_container']/div/div[3]/div[2]/div[2]/div")
    PRODUCT_PRICE_FOUR_LBL = (By.XPATH, "//*[@id='inventory_container']/div/div[4]/div[2]/div[2]/div")
    PRODUCT_PRICE_FIVE_LBL = (By.XPATH, "//*[@id='inventory_container']/div/div[5]/div[2]/div[2]/div")
    PRODUCT_PRICE_SIX_LBL = (By.XPATH, "//*[@id='inventory_container']/div/div[6]/div[2]/div[2]/div")