from dataclasses import dataclass, field

import requests

@dataclass
class InstagramRequest:

    url: str = field(default='')
    word: str = field(default='')

    def isavailable(self):

       response = requests.get(self.url)
       word_response = 1 if response else 0

       return word_response


