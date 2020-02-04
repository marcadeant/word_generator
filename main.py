from Instagram_request import InstagramRequest
from article_formating import ArticleFormatting
from dataclasses import dataclass, field

from word_generator import WordGenerator


@dataclass
class Process:

    article: str = field(default='')
    article_formating: ArticleFormatting = field(default_factory=ArticleFormatting)
    instagram_request: InstagramRequest = field(default_factory=InstagramRequest)
    word_generator: WordGenerator = field(default_factory=WordGenerator)

    def __post_init__(self):
        self.article_formating = ArticleFormatting(article=self.article)

    def process(self):
        # Use statistical analysies to create a word chain
        self.word_generator = WordGenerator(self.article_formating)
        for i in range(0, 100):
            print(self.word_generator.forecast_word(4, 'a'))




if __name__=='__main__':

    file = open("Articles/Music/Article_1.txt", "r", encoding='UTF8')
    file_ = file.read()
    process = Process(article=file_)
    process.process()
