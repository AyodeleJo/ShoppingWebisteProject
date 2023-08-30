from pages.login_page import LoginPage
from resources.constants import TEST_SITE_URL
from pages.login_success_page import LoginSuccessPage
from pages.locked_out_users_page import LockOutUsersPage
from pages.problem_user_page import ProblemUsersPage
from pages.no_credential_user_page import NoCredentialUserPage


class TestLogin:
    # Test case 1(loging in the users)
    def test_login_standard_user(self, driver, user_name_password):
        login_page = LoginPage(driver)
        login_page.navigate_to(TEST_SITE_URL)
        login_page.driver_maximize_window()
        login_page.wait_and_type_user_name(user_name_password)
        login_page.wait_and_type_password(user_name_password)
        login_page.click_login_btn()

        login_success_page = LoginSuccessPage(driver)
        login_success_lbl = login_success_page.get_login_success_label()
        assert login_success_lbl == "Products", "login failed"
        login_page.driver_take_screenshot1()
        driver.back()

    def test_locked_out_users(self, driver, locke_out_users):
        lock_out_users = LockOutUsersPage(driver)
        # lock_out_users.navigate_to(TEST_SITE_URL)
        lock_out_users.wait_and_type_user_name(locke_out_users)
        lock_out_users.wait_and_type_password(locke_out_users)
        lock_out_users.click_login_btn()

        lock_out_users_lbl = lock_out_users.get_lock_out_label()
        assert lock_out_users_lbl == "Epic sadface: Sorry, this user has been locked out.", "failed"
        lock_out_users.driver_take_screenshot2()

        lock_out_users.click_error_btn()
        lock_out_users.clear_user_name()
        lock_out_users.clear_user_password()

    def test_problem_users(self, driver, problem_users):
        problem_user = ProblemUsersPage(driver)
        problem_user.wait_and_type_user_name(problem_users)
        problem_user.wait_and_type_password(problem_users)
        problem_user.click_login_btn()
        problem_user.driver_take_screenshot3()

        problem_user_lbl = problem_user.get_problem_user_label()
        assert problem_user_lbl == "Epic sadface: Username and password do not match any user in this service", "failed"

        problem_user.click_error_btn()
        problem_user.clear_user_name()
        problem_user.clear_user_password()

    def test_no_credentials_users(self, driver):
        no_credential_user = NoCredentialUserPage(driver)
        no_credential_user.navigate_to(TEST_SITE_URL)
        no_credential_user.click_login_btn()
        no_credential_user.driver_take_screenshot4()

        no_credential_user_lbl = no_credential_user.get_no_credential_user_label()
        assert no_credential_user_lbl == "Epic sadface: Username is required", "failed"
