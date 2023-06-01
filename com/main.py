import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.common.keys import Keys

service = Service('D:\chromedriver.exe')


def get_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("no-sandbox")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument("disable-blink-features=AutomationControlled")

    browser = webdriver.Chrome(service=service, options=options)
    browser.get("https://automated.pythonanywhere.com/login/")
    return browser


def main():
    driver = get_driver()
    time.sleep(1)
    driver.find_element(by="id", value="id_username").send_keys("automated")
    time.sleep(1)
    driver.find_element(by="id", value="id_password").send_keys("automatedautomated" + Keys.ENTER)
    time.sleep(1)
    print(driver.current_url)
    driver.find_element(by="xpath", value="/html/body/nav/div/a").click()
    print(driver.current_url)
    time.sleep(4)

print(main())
