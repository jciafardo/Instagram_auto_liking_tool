from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from WebScraping.instagram_auto_liking_tool import Setup

driver = Setup.driver


def login():
    user = input('Enter Username')
    user_box = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')))
    user_box.click()
    user_box.send_keys(user)

    password = input('Enter Password')
    pass_box = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')))
    pass_box.click()
    pass_box.send_keys(password)
    pass_box.send_keys(Keys.ENTER)

login()