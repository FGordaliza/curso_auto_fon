# Generated by Selenium IDE
import pytest
import time
import json
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class TestLogin():
    def setup_class(self):
        self.timestamp = datetime.timestamp(datetime.now())

    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {
            "USER": "USER" + str(self.timestamp),
            "PASS": "PASS" + str(self.timestamp)
        }
        print(self.vars)

    def teardown_method(self, method):
        self.driver.quit()

    def test_register(self):
        self.driver.get("https://www.demoblaze.com/index.html")
        self.driver.maximize_window()
        self.driver.find_element(By.ID, "signin2").click()
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.ID, "sign-username")))
        self.driver.find_element(By.ID, "sign-username").click()
        self.driver.find_element(By.ID, "sign-username").send_keys(self.vars["USER"])
        self.driver.find_element(By.ID, "sign-password").click()
        self.driver.find_element(By.ID, "sign-password").send_keys(self.vars["PASS"])
        self.driver.find_element(By.CSS_SELECTOR, "#signInModal .btn-primary").click()
        WebDriverWait(self.driver, 3).until(EC.alert_is_present(),
                                            'Timed out waiting for PA creation ' +
                                            'confirmation popup to appear.')
        assert self.driver.switch_to.alert.text == "Sign up successful."
        time.sleep(1)

    def test_login_with_error_in_user(self):
        self.driver.get("https://www.demoblaze.com/index.html")
        self.driver.maximize_window()
        self.driver.find_element(By.ID, "login2").click()
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.ID, "loginusername")))
        self.driver.find_element(By.ID, "loginusername").click()
        self.driver.find_element(By.ID, "loginusername").send_keys(self.vars["USER"]+"A")
        self.driver.find_element(By.ID, "loginpassword").click()
        self.driver.find_element(By.ID, "loginpassword").send_keys("test")
        self.driver.find_element(By.XPATH, "//div[@id=\'logInModal\']/div/div/div[3]/button[2]").click()
        WebDriverWait(self.driver, 3).until(EC.alert_is_present(),
                                            'Timed out waiting for PA creation ' +
                                            'confirmation popup to appear.')

        assert self.driver.switch_to.alert.text == "User does not exist."
        time.sleep(1)

    def test_login_with_error_in_password(self):
        self.driver.get("https://www.demoblaze.com/index.html")
        self.driver.maximize_window()
        self.driver.find_element(By.ID, "login2").click()
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.ID, "loginusername")))
        self.driver.find_element(By.ID, "loginusername").click()
        self.driver.find_element(By.ID, "loginusername").send_keys(self.vars["USER"])
        self.driver.find_element(By.ID, "loginpassword").click()
        self.driver.find_element(By.ID, "loginpassword").send_keys("test")
        self.driver.find_element(By.XPATH, "//div[@id=\'logInModal\']/div/div/div[3]/button[2]").click()
        WebDriverWait(self.driver, 3).until(EC.alert_is_present(),
                                            'Timed out waiting for PA creation ' +
                                            'confirmation popup to appear.')
        assert self.driver.switch_to.alert.text == "Wrong password."
        time.sleep(1)

    def test_login_sucessfull(self):
        self.driver.get("https://www.demoblaze.com/index.html")
        self.driver.maximize_window()
        self.driver.find_element(By.ID, "login2").click()
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.ID, "loginusername")))
        self.driver.find_element(By.ID, "loginusername").click()
        self.driver.find_element(By.ID, "loginusername").send_keys(self.vars["USER"])
        self.driver.find_element(By.ID, "loginpassword").click()
        self.driver.find_element(By.ID, "loginpassword").send_keys(self.vars["PASS"])
        self.driver.find_element(By.XPATH, "//div[@id=\'logInModal\']/div/div/div[3]/button[2]").click()
        WebDriverWait(self.driver, 30).until(EC.presence_of_all_elements_located((By.ID, "nameofuser")))

        WebDriverWait(self.driver, 30).until(
            EC.text_to_be_present_in_element((By.ID, "nameofuser"), "Welcome"))

        expected = "Welcome " + self.vars["USER"]
        really = self.driver.find_element(By.ID, "nameofuser").text

        assert(
                self.driver.find_element(By.ID, "nameofuser").text == expected,
                f'Not found {expected}, found : {really}'
        )
        time.sleep(1)


    def test_Navigate_with_user(self):
        self.test_login_sucessfull()
        self.driver.find_element(By.LINK_TEXT, "Laptops").click()
        WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.LINK_TEXT, "2017 Dell 15.6 Inch")))
        self.driver.find_element(By.LINK_TEXT, "2017 Dell 15.6 Inch").click()
        WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.LINK_TEXT, "Add to cart")))
        self.driver.find_element(By.LINK_TEXT, "Add to cart").click()
        WebDriverWait(self.driver, 3).until(EC.alert_is_present(),
                                            'Timed out waiting for PA creation ' +
                                            'confirmation popup to appear.')

        assert self.driver.switch_to.alert.text == "Product added."
        expected = "Product added."
        really = self.driver.switch_to.alert.text
        assert(
                self.driver.switch_to.alert.text == expected,
                f'Not found {expected}, found : {really}'
        )
        self.driver.switch_to.alert.accept()
        time.sleep(10)
        self.driver.close()
