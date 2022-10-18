import time

from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("https://full-on-net.com/")
driver.maximize_window()
time.sleep(5)

title = driver.title
assert title == "Full On Net"

link = driver.find_element(By.LINK_TEXT, "Aviso legal y Política de privacidad")
link_href = link.get_property("href")
print(link_href)
assert link_href == "https://full-on-net.com/aviso-legal/"

driver.quit()

