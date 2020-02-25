from dataclasses import dataclass, field
import requests
from selenium import webdriver
import json
from selenium.webdriver.common.by import By
from time import sleep

from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.support.wait import WebDriverWait
from wglearn.constants import EMAIL, FULLNAME, USERNAME, PASSWORD


@dataclass
class InstagramRequest:
    url: str = field(init=False)
    word: str = field(default='')
    _url: str = field(init=False)
    form: json = field(init=False)

    def __post_init__(self):
        self.url = 'https://www.instagram.com/'
        self._url = self.url + self.word

    def isavailable(self):

        response = requests.get(self._url)
        word_response = 1 if response else self.fill_forms()
        # Response = 200 means that the word isn't available for sur

        return word_response

    def fill_forms(self):

        # response = 1 means that the word is already used
        try:
            with open('/Users/amarcade/Documents/word_generator/auth.json', 'r') as json_file:
                token = json.load(self.form)

            token['username'] = self.word
            browser = webdriver.Chrome('/Users/amarcade/Documents/ADSL_connector/chromedriver')

            wait = WebDriverWait(browser, 2)
            browser.get(self.url)
            sleep(1.5)
            email = browser.find_element_by_name(EMAIL)
            email.send_keys(token[EMAIL])
            fullname = browser.find_element_by_name(FULLNAME)
            fullname.send_keys(token[FULLNAME])
            username = browser.find_element_by_name(USERNAME)
            username.send_keys(token[USERNAME])
            password = browser.find_element_by_name(PASSWORD)
            password.send_keys(token[PASSWORD])
            submit = browser.find_element_by_xpath(
                "/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[7]/div/button")
            submit.click()
            wait.until(presence_of_element_located((By.CLASS_NAME, "nZl92")))
            response = 1
        except ValueError:
            response = 0

        return response


def main():
    instagram_request = InstagramRequest(word='ahgn')
    response = instagram_request.isavailable()
    print(response)


if __name__ == '__main__':
    main()
