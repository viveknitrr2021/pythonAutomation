from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

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
    browser.get("https://www.pythonanywhere.com/")
    return browser


def main():
    driver = get_driver()
    element = driver.find_elements(By.TAG_NAME, "h1")
    for ele in element:
        print(ele.text)


main()
