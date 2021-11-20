from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from WebScraping.instagram_auto_liking_tool import Setup

driver = Setup.driver




def like_photos():
    amount = int(input('How many photos would you like to like ?'))

    click_pic = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME,'eLAPa')))
    driver.execute_script("arguments[0].click();", click_pic)

    first_pic = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, 'fr66n'))).click()

    first_arrow = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[6]/div[1]/div/div/div/button')))
    driver.execute_script("arguments[0].click();", first_arrow)

#for some off reason instagrames first arrow is a different element then the rest

    for i in range(amount-1):
        sleep(3)
        like_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, 'fr66n'))).click()

        arrow = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[6]/div[1]/div/div/div[2]'))).click()#works


like_photos()