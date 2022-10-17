import time

from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("https://full-on-net.com/contacto/")
driver.maximize_window()
time.sleep(5)
print("===============================================================================================================")
by_id = driver.find_element(by=By.ID, value="menu-main")
print(by_id.text)

print("===============================================================================================================")
by_class_name = driver.find_element(by=By.CLASS_NAME, value="wearehere")
print(by_class_name.text)

print("===============================================================================================================")
by_css_selector = driver.find_element(by=By.CSS_SELECTOR, value="div.uncode_text_column")
print(by_css_selector.text)

print("===============================================================================================================")
by_css_selector_all = driver.find_elements(by=By.CSS_SELECTOR, value="div.uncode_text_column")
for i in by_css_selector_all:
    print(i.text)

print("===============================================================================================================")
by_name = driver.find_element(by=By.NAME, value="nombre")
print(by_name.find_element(By.XPATH, "../../label").text)

print("===============================================================================================================")
by_link_text = driver.find_element(by=By.LINK_TEXT, value="CONTACTO")
print(by_link_text.text)

print("===============================================================================================================")
by_partial_link_text = driver.find_element(by=By.PARTIAL_LINK_TEXT, value="ONTAC")
print(by_partial_link_text.text)

print("===============================================================================================================")
by_tag_all = driver.find_elements(by=By.TAG_NAME, value="a")
for i in by_tag_all:
    print(i.text)

print("===============================================================================================================")
by_xpath = driver.find_element(by=By.XPATH, value="//ul[@id='menu-main']/li[2]")
print(by_xpath.text)

driver.quit()

