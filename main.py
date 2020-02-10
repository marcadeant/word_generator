import pandas as pd
from Instagram_request import InstagramRequest
from article_formating import ArticleFormatting
from dataclasses import dataclass, field
from time import sleep

from word_generator import WordGenerator


@dataclass
class Process:

    article_formating: ArticleFormatting = field(default_factory=ArticleFormatting)
    instagram_request: InstagramRequest = field(default_factory=InstagramRequest)
    word_generator: WordGenerator = field(default_factory=WordGenerator)

    def process(self):
        # Use statistical analysies to create a word chain
        self.word_generator = WordGenerator(self.article_formating)
        list_of_word = []
        availibility = []
        for i in range(0, 100):
            list_of_word.append(self.word_generator.forecast_word(4, 'a'))
        for i, word in enumerate(list_of_word):
            print("Process word n°:"+str(i))
            instagram_request = InstagramRequest(word=word)
            available = instagram_request.isavailable()
            availibility.append(available)
            sleep(0.5)


        data_dict = {'word': list_of_word, 'availabality': availibility}
        data_pd = pd.DataFrame.from_dict(data_dict)
        pd.DataFrame.to_csv(data_pd, 'data_word.csv', sep=';')





if __name__=='__main__':

    process = Process()
    process.process()