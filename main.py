import os
import time

from selenium.common.exceptions import InvalidArgumentException
from selenium import webdriver
from selenium.webdriver.common.by import By


class Imgflip_Paths:

    def __init__(self):
        self.driver = webdriver.Firefox()
        self.driver.get(self.url)

    url = \
        'https://imgflip.com/memegenerator'
    new_template_btn = \
        '//*[@id="mm-show-upload"]'
    image_url_text_box = \
        '//*[@id="mm-upload-url"]'
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

    def input_keys(self, box_path, text, pause=1):
        try:  
            elem = \
                self.driver.find_element(By.XPATH, box_path)
        except InvalidArgumentException:
            print('Text box accessed too early.')
            return
        elem.send_keys(text)
        time.sleep(pause)

    def click_new_template(self):
        self.click(self.new_template_btn)

    def click_upload(self):
        self.click(self.upload_btn)

    def click_generate(self):
        self.click(self.generate_btn)

    def enter_image_link(self, text):
        self.input_keys(self.image_url_text_box, text)

    def enter_top_text(self, text):
        self.input_keys(self.top_text_box, text)

    def enter_bottom_text(self, text):
        self.input_keys(self.bottom_text_box, text)

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


def main():
    '''test image'''
    test_image_link = \
        'https://cdn.discordapp.com/attachments/1047375362289586279/1077857538940350464/test_image.jpg'

    '''call class'''
    flip = Imgflip_Paths()

    '''upload image'''
    flip.click_new_template()
    flip.enter_image_link(test_image_link)
    flip.click_upload()

    '''fill text'''
    flip.enter_top_text('mfw(my face when)')
    flip.enter_bottom_text('when the imposter is sus')

    '''generate meme and get link'''
    flip.click_generate()
    flip.get_result()

    'close_driver'
    flip.driver.close()


if __name__ == '__main__':
    main()





