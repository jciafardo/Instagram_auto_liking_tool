from WebScraping.instagram_auto_liking_tool import Setup
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


driver = Setup.driver



def get_like_user():
    user = input('Enter username of person you want to like photos')
    search_box = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,"//*[@id='react-root']/section/nav/div[2]/div/div/div[2]/input")))
    driver.execute_script("arguments[0].click();", search_box)
    search_box.send_keys(user)
    search_box.send_keys(Keys.ENTER)

    insta_user = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//*[@id='react-root']/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div[1]"))).click()


get_like_user()