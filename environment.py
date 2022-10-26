from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time


def before_all(context):
    pass


def before_scenario(context, scenario):
    context.driver = webdriver.Chrome(service=ChromeService(executable_path=ChromeDriverManager().install()))
    context.driver.maximize_window()


def after_scenario(context, scenario):
    time.sleep(5)
    context.driver.quit()
    print("reporte Jira: ", scenario.status)
    if scenario.status == "passed":
        print("test passed")
    else:
        print("test failed")


def after_all(context):
    print("after_all")

