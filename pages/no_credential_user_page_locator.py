from selenium.webdriver.common.by import By


class NoCredentialUserPageLocators:

    USERNAME_TEXT_BOX = (By.NAME, "user-name")
    PASSWORD_TEXT_BOX = (By.NAME, "password")
    LOGIN_BTN = (By.ID, "login-button")
    NO_CREDENTIAL_USER_TEXT_LBL = (By.XPATH, "//h3")
    GLITCH_USER_ERROR_BTN = (By.XPATH, "//button")

