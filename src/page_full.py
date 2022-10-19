from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class PageFull:
    def __init__(self, driver: WebDriver):
        self.menu = driver.find_element(By.ID, "menu-main")
        self.wearefull_button = self.menu.find_element(By.LINK_TEXT, "WE ARE FULL")
        self.weareon_button = self.menu.find_element(By.LINK_TEXT, "WE ARE ON")
        self.wearenet_button = self.menu.find_element(By.LINK_TEXT, "WE ARE NET")
        self.contact_button = self.menu.find_element(By.LINK_TEXT, "CONTACTO")

        self.footer = driver.find_element(By.ID, "menu-footer-legal")
        self.legal_link = self.footer.find_element(By.PARTIAL_LINK_TEXT, "Aviso legal")
        self.cookies = self.footer.find_element(By.LINK_TEXT, "Cookies")

        self.cookies_accept = driver.find_element(By.ID, "cookie_action_close_header")

    def accept_cookies(self):
        self.cookies_accept.click()

    def open_contact_page(self):
        self.contact_button.click()

    def open_legal(self):
        self.legal_link.click()

    def open_cookies(self):
        self.cookies.click()

    def open_link(self, link_text):
        self.footer.find_element(By.PARTIAL_LINK_TEXT, link_text).click()