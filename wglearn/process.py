import pandas as pd
from wglearn.instagram_request import InstagramRequest
from wglearn.article_formatting import ArticleFormatting
from dataclasses import dataclass, field
from time import sleep

from wglearn.word_generator import WordGenerator


@dataclass
class Process:
    article_formatting: ArticleFormatting = field(default_factory=ArticleFormatting)
    instagram_request: InstagramRequest = field(default_factory=InstagramRequest)
    word_generator: WordGenerator = field(default_factory=WordGenerator)

    def process(self):
        # Use statistical analysis to create a word chain
        self.word_generator = WordGenerator(self.article_formatting)
        list_of_word = []
        list_of_prob = []
        availability = []
        for i in range(0, 100):
            word, prob = self.word_generator.forecast_word(6, 'a')
            list_of_word.append(word)
            list_of_prob.append(prob)
        for i, word in enumerate(list_of_word):
            print("Process word n°:" + str(i))
            print(word)
            # instagram_request = InstagramRequest(word=word)
            # available = instagram_request.isavailable()
            available = 'unknown'
            availability.append(available)
            # sleep(0.5)

        data_dict = {'word': list_of_word, 'availability': availability, 'prob': list_of_prob}
        data_pd = pd.DataFrame.from_dict(data_dict)
        pd.DataFrame.to_csv(data_pd, 'data_word.csv', sep=';')


if __name__ == '__main__':
    article_formatting = ArticleFormatting()
    process = Process(article_formatting=article_formatting)
    process.process()
