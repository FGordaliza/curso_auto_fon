from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time


def before_scenario(context, scenario):
    context.driver = webdriver.Chrome(service=ChromeService(executable_path=ChromeDriverManager().install()))
    context.driver.maximize_window()
    print(context.config.userdata["environment"])
    print(context.config.userdata["another_param"])


def after_scenario(context, scenario):
    time.sleep(5)
    context.driver.quit()
