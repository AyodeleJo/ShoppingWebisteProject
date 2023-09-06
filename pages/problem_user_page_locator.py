from selenium.webdriver.common.by import By


class ProblemUserLocators:

    USERNAME_TEXT_BOX = (By.NAME, "user-name")
    PASSWORD_TEXT_BOX = (By.NAME, "password")
    LOGIN_BTN = (By.ID, "login-button")
    PROBLEM_USER_IMG = (By.XPATH, "//img")
    LOCK_OUT_TEXT_LBL = (By.XPATH, "//h3")
    LOCK_OUT_USER_ERROR_BTN = (By.XPATH, "//button")
