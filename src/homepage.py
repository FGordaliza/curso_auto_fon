from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from src.page_full import PageFull


class HomePage(PageFull):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)
