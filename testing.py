import pyautogui
import os


from selenium import webdriver
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
from time import sleep

load_dotenv()

'''select browser'''
driver = webdriver.Firefox()
driver.get\
    ('https://imgflip.com/memegenerator')


def click_on(path, pause=1):
    elem = driver.find_element\
        (By.XPATH, path)
    elem.click()
    sleep(pause)

'''upload new template'''
click_on\
    ('//*[@id="mm-show-upload"]')

'''upload'''
click_on\
    ('//*[@id="mm-upload-file-btn"]')

'''locate image / select image'''
pyautogui.write\
    (os.environ.get('image_path'),
     interval=.01)
sleep(1)
pyautogui.press('enter')
sleep(1)

'''upload image'''
click_on\
    ('//*[@id="mm-upload-btn"]')

'''top text'''
click_on\
    ('/html/body/div[3]/div[2]/div[2]/div[6]/div[1]/div[1]/textarea', 3)
pyautogui.write\
    ('my face when the')
sleep(1)

'''bottom text'''
click_on\
    ('/html/body/div[3]/div[2]/div[2]/div[6]/div[2]/div[1]/textarea')
pyautogui.write\
    ('imposter is sus!!')
sleep(1)

'''generate meme'''
click_on\
    ('/html/body/div[3]/div[2]/div[2]/div[10]/div[5]/button[1]')

'''extract link uploaded image'''
elem = driver.find_element\
    (By.XPATH, '//*[@id="done-img"]')
sleep(1)
link = elem.get_attribute('src')
sleep(1)

print(link)

driver.close()

