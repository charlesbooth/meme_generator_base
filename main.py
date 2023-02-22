import pyautogui
import os
import time

from selenium.common.exceptions import InvalidArgumentException
from selenium import webdriver
from selenium.webdriver.common.by import By
from dotenv import load_dotenv


class Imgflip_Paths:

    def __init__(self):
        self.driver = webdriver.Firefox()
        self.driver.get(self.url)

    url = \
        'https://imgflip.com/memegenerator'
    new_template_btn = \
        '//*[@id="mm-show-upload"]'
    select_file_btn = \
        '//*[@id="mm-upload-file-btn"]'
    upload_btn = \
        '//*[@id="mm-upload-btn"]'
    top_text_box = \
        '/html/body/div[3]/div[2]/div[2]/div[6]/div[1]/div[1]/textarea'
    bottom_text_box = \
        '/html/body/div[3]/div[2]/div[2]/div[6]/div[2]/div[1]/textarea'
    generate_btn = \
        '/html/body/div[3]/div[2]/div[2]/div[10]/div[5]/button[1]'
    result_text_output = \
        '//*[@id="done-img"]'

    def click(self, button_path, pause=1):
        try:  
            elem = \
                self.driver.find_element(By.XPATH, button_path)
        except InvalidArgumentException:
            print('Buttons accessed in improper order.')
            return
        elem.click()
        time.sleep(pause)

    def click_new_template(self):
        self.click(self.new_template_btn)

    def click_select_file(self):
        self.click(self.select_file_btn)

    def click_upload(self):
        self.click(self.upload_btn)

    def click_top_text(self):
        self.click(self.top_text_box)

    def click_bottom_text(self):
        self.click(self.bottom_text_box)

    def click_generate(self):
        self.click(self.generate_btn)

    def get_result(self):
        try:  
            elem = \
                self.driver.find_element(By.XPATH, self.result_text_output)
        except InvalidArgumentException:
            print('Result accessed too early.')
            return
        time.sleep(1.5)
        link = elem.get_attribute('src')
        print(link)


def type_text(text, submit=False):
    '''types text / optional: submits it with enter key'''
    pyautogui.write\
        (text, interval=.01)
    time.sleep(2)
    if submit:
        pyautogui.press('enter')
        time.sleep(1)


def main():
    '''load .env file and call class'''
    load_dotenv()
    path = os.environ.get('image_path')
    flip = Imgflip_Paths()

    '''upload image'''
    flip.click_new_template()
    flip.click_select_file()
    type_text(path, submit=True)
    flip.click_upload()

    '''fill text'''
    flip.click_top_text()
    type_text('my face when')
    flip.click_bottom_text()
    type_text('the impostor is sus!!')

    '''generate meme and get link'''
    flip.click_generate()
    flip.get_result()

    'close_driver'
    flip.driver.close()


if __name__ == '__main__':
    main()





