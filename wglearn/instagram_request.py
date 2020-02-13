from dataclasses import dataclass, field

import requests

@dataclass
class InstagramRequest:

    url: str = field(init=False)
    word: str = field(default='')
    _url: str = field(init=False)

    def __post_init__(self):
        self.url = 'https://www.instagram.com/'
        self._url = self.url + self.word

    def isavailable(self):

       response = requests.get(self._url)
       word_response = 1 if response else 0

       return word_response

def main():

    instagram_request = InstagramRequest(word='triolet')
    print(instagram_request.isavailable())

if __name__ == '__main__':
    main()