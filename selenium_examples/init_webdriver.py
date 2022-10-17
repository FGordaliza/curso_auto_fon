from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

# webdriver in path
driver = webdriver.Chrome()
driver.get("https://www.full-on-net.com")
driver.quit()

# webdriver in specific folder
service = Service(executable_path="../webdrivers/chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get("https://www.full-on-net.com")
driver.quit()

# autoinstall webdriver
driver = webdriver.Chrome(service=ChromeService(executable_path=ChromeDriverManager().install()))
driver.get("https://www.full-on-net.com")
driver.quit()
