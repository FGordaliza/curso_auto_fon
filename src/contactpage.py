from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.page_full import PageFull


class ContactPage(PageFull):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.driver = driver
        self.locator_wearehere = (By.CLASS_NAME, "wearehere")

    def print_text_we_are_here(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator=self.locator_wearehere))
        wearehere = self.driver.find_element(*self.locator_wearehere)
        print(wearehere.text)
        return wearehere.text


