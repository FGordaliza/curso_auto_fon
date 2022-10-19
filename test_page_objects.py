from selenium import webdriver
from selenium.webdriver.common.by import By
from src.homepage import HomePage
from src.contactpage import ContactPage
import time


def main(driver):
    driver.get("http://www.full-on-net.com")
    homepage = HomePage(driver=driver)
    homepage.accept_cookies()
    homepage.open_contact_page()

    contactpage = ContactPage(driver=driver)
    assert contactpage.print_text_we_are_here() == "We are here"

    HomePage(driver=driver).open_legal()
    HomePage(driver=driver).open_cookies()

    time.sleep(5)


if __name__ == "__main__":
    driver = webdriver.Chrome()
    driver.maximize_window()
    try:
        main(driver)
    except:
        raise Exception("Error no controlado")
    finally:
        driver.quit()
