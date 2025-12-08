from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver

try:
    driver = webdriver.Chrome()
    driver.get("https://www.google.com")
    driver.find_element("id", "not exist button")
except NoSuchElementException as e:
    print("Element not found!", e.msg)

