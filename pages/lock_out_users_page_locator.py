from selenium.webdriver.common.by import By


class LockOutUserPageLocators:

    USERNAME_TEXT_BOX = (By.NAME, "user-name")
    PASSWORD_TEXT_BOX = (By.NAME, "password")
    LOGIN_BTN = (By.NAME, "login-button")
    LOCK_OUT_TEXT_LBL = (By.XPATH, "//h3")
    LOCK_OUT_ERROR_BTN = (By.XPATH, "//button")
