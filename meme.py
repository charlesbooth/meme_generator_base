import time

from selenium.common.exceptions import InvalidArgumentException as SeleniumInvalidArgument
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By


class Imgflip_Paths:

    def __init__(self):
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        self.driver = webdriver.Firefox(options=options)
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
        except SeleniumInvalidArgument:
            print('Buttons accessed in improper order.')
            return
        elem.click()
        time.sleep(pause)

    def input_keys(self, box_path, text, pause=1):
        try:  
            elem = \
                self.driver.find_element(By.XPATH, box_path)
        except SeleniumInvalidArgument:
            print('Text box accessed too early.')
            return
        time.sleep(pause)
        elem.send_keys(text)
        time.sleep(pause)

    def click_new_template(self):
        self.click\
            (self.new_template_btn, pause=0)

    def click_upload(self):
        self.click\
            (self.upload_btn, pause=0)

    def click_generate(self):
        self.click\
            (self.generate_btn, pause=2)

    def enter_image_link(self, text):
        self.input_keys\
            (self.image_url_text_box, text, pause=2)

    def enter_top_text(self, text):
        self.input_keys\
            (self.top_text_box, text, pause=0)

    def enter_bottom_text(self, text):
        self.input_keys\
            (self.bottom_text_box, text, pause=0)

    def get_result(self):
        try:  
            elem = \
                self.driver.find_element(By.XPATH, self.result_text_output)
        except SeleniumInvalidArgument:
            print('Result accessed too early.')
            return
        time.sleep(1.5)
        link = elem.get_attribute('src')
        return link


def make_meme(image_link, top_text, bottom_text=''):
    #'''call class'''
    flip = Imgflip_Paths()

    #'''upload image'''
    flip.click_new_template()
    flip.enter_image_link(image_link)
    flip.click_upload()

    #'''fill text'''
    flip.enter_top_text(top_text)
    flip.enter_bottom_text(bottom_text)

    #'''generate meme, get link, and close driver'''
    flip.click_generate()
    result = str(flip.get_result())
    flip.driver.close()
    
    #'''send link to main.py'''
    return result
 

def main():
    make_meme()


if __name__ == '__main__':
    main()
