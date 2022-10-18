import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


driver = webdriver.Chrome()
driver.get("https://full-on-net.com/")
driver.maximize_window()
time.sleep(1)

actions = ActionChains(driver)
section_2 = driver.find_element(by=By.XPATH, value="//div[@data-section='2']")
actions.scroll_to_element(section_2).perform()

columns = section_2.find_elements(By.CSS_SELECTOR, ".wpb_column .col-lg-4")
for column in columns:
    time.sleep(2)
    actions.move_to_element(column).perform()

driver.quit()
