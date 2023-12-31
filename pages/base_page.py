from test_utils import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select
from PIL import Image, ImageChops


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def navigate_to(self, url):
        self.driver.get(url)

    def explicitly_wait_and_find_element(self, interval, locator_type_and_locator_tuple):
        return WebDriverWait(self.driver, interval).until(
            ec.presence_of_element_located(locator_type_and_locator_tuple))

    def find_element(self, locator_type_and_locator_tuple):
        return self.driver.find_element(*locator_type_and_locator_tuple)

    def driver_back(self):
        self.driver.back()

    def driver_take_screenshot1(self):
        self.driver.save_screenshot("image1.png")

    def driver_take_screenshot2(self):
        self.driver.save_screenshot("image2.png")

    def driver_take_screenshot4(self):
        self.driver.save_screenshot("image4.png")

    def driver_take_screenshot3(self):
        self.driver.save_screenshot('image3.png')

    def driver_take_screenshot5(self):
        self.driver.save_screenshot('image5.png')

    def driver_maximize_window(self):
        self.driver.maximize_window()

    def capture_web_element_as_an_image(self, image_file_name):
        image_element = self.driver.get("C:\\Users\\Amos\\ShopingWebisteProject\\test\\image5.png")
        image_element.screenshot(image_file_name)

    def capture_web_element_as_an_image(self, locator_type_and_locator_tuple, image_file_name):
        image_element = self.driver.find_element(*locator_type_and_locator_tuple)
        image_element.screenshot(image_file_name)

    def compare_images(self, actual_image_file_name, stored_image_file_name):
        actual_image = Image.open(actual_image_file_name)
        stored_image = Image.open(stored_image_file_name)
        diff = ImageChops.difference(actual_image, stored_image)
        if diff.getbbox():
            percentage_diff = (diff.getbbox()[2] * diff.getbbox()[3]) / (
                    actual_image.size[0] * actual_image.size[1]) * 100
        else:
            percentage_diff = 0  # Images are identical

        return percentage_diff
