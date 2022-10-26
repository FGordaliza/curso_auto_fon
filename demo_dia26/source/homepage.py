import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.signup_link = driver.find_element(By.ID, "signin2")
        self.login_link = driver.find_element(By.ID, "login2")
        self.signup_username = driver.find_element(By.ID, "sign-username")
        self.signup_password = driver.find_element(By.ID, "sign-password")
        self.login_username = driver.find_element(By.ID, "loginusername")
        self.login_password = driver.find_element(By.ID, "loginpassword")
        self.signup_confirm_button = driver.find_element(By.CSS_SELECTOR, "#signInModal .btn-primary")
        self.login_confirm_button = driver.find_element(By.CSS_SELECTOR, "#logInModal .btn-primary")

        self.laptop_section_link = (By.LINK_TEXT, "Laptops")

    def open_signup_form(self):
        self.signup_link.click()

    def open_login_form(self):
        self.login_link.click()

    def fill_signup_form(self, user, password):
        self.signup_username.send_keys(user)
        self.signup_password.send_keys(password)
        self.signup_confirm_button.click()

        WebDriverWait(self.driver, 3).until(EC.alert_is_present(),
                                            'Timed out waiting for PA creation ' + 'confirmation popup to appear.')
        alert_text = self.driver.switch_to.alert.text
        self.driver.switch_to.alert.accept()
        return alert_text

    def fill_login_form(self, user, password):
        self.login_username.send_keys(user)
        self.login_password.send_keys(password)
        self.login_confirm_button.click()

    def open_laptop_section(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.laptop_section_link))
        time.sleep(3)
        laptop_section_link = self.driver.find_element(*self.laptop_section_link)
        laptop_section_link.click()

    def open_item(self, item):
        item = self.driver.find_element(By.LINK_TEXT, item)
        item.click()

    def add_to_cart(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "btn-success")))
        time.sleep(3)
        self.driver.find_element(By.CLASS_NAME, "btn-success").click()