from selenium.webdriver.common.by import By


class LoginPageLocators:
    USERNAME_TEXT_BOX = (By.NAME, "user-name")
    PASSWORD_TEXT_BOX = (By.NAME, "password")
    LOGIN_BTN = (By.NAME, "login-button")
