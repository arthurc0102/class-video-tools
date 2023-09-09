import time

from selenium import webdriver

driver = webdriver.Remote(options=webdriver.ChromeOptions())

print("before get")

time.sleep(5)

driver.get("https://python.org")

print("after get")

time.sleep(5)

driver.close()
