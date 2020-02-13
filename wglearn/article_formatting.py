from dataclasses import dataclass, field
from typing import List, Dict
from nltk.tokenize import RegexpTokenizer

@dataclass
class ArticleFormatting:

    article_dict: Dict = field(init=False)
    corpus: Dict = field(init=False)
    topic: str = field(default='music')
    language: str = field(default="en")

    def __post_init__(self):
        self.data_init()

    def split_text_to_word(self) -> List[str]:

        tokenizer = RegexpTokenizer(r'\w+')
        path = self.article_dict[self.topic]
        file = open(path, "r", encoding='UTF8')
        file_reader = file.read()
        words = tokenizer.tokenize(file_reader)
        return words

    def data_init(self):

        self.article_dict = {'music': 'Articles/Music/music.txt', 'marketing': 'Articles/Marketing/marketing.txt'}
        self.corpus = {}
        words = self.split_text_to_word()
        nb_of_words = len(words)
        for word in words:
            if word not in self.corpus.keys():
                occurrence = words.count(word)
                frequency = occurrence / nb_of_words
                self.corpus[word] = frequency

    def get_frequency_word(self, word: str) -> float:
        return self.corpus[word]
