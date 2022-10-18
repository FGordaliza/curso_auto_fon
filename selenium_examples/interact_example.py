import time

from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("https://full-on-net.com/")
driver.maximize_window()
time.sleep(5)

contact_button = driver.find_element(by=By.LINK_TEXT, value="CONTACTO")
print(contact_button.size)
print(contact_button.value_of_css_property("color"))
contact_button.click()

name_input = driver.find_element(by=By.NAME, value="nombre")
name_input.send_keys("Full On Net")
time.sleep(5)
name_input.clear()
time.sleep(5)
driver.quit()

