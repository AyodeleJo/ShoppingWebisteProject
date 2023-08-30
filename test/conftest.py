from selenium import webdriver
import pytest as pytest


@pytest.fixture(scope="module")
def driver():
    _driver = webdriver.Chrome()
    yield _driver
    _driver.quit()


@pytest.fixture(scope="function")
def user_name_password():
    username = "standard_user"
    password = "secret_sauce"
    return [username, password]


@pytest.fixture(scope="function")
def locke_out_users():
    username = "locked_out_user"
    password = "secret_sauce"
    return [username, password]


@pytest.fixture(scope="function")
def problem_users():
    username = "problem_user"
    password = "secret_sauce"
    return [username, password]


@pytest.fixture(scope="function")
def personal_info():
    first_name = "rose"
    last_name = "Bucket"
    postal_code = "K1v123"

    return [first_name, last_name, postal_code]
