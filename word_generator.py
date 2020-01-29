from dataclasses import dataclass, field
from typing import Dict
import numpy as np

from article_formating import ArticleFormatting

ALPHABET = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
            "v", "w", "x", "y", "z"]


@dataclass
class WordGenerator:
    article_formatting: ArticleFormatting = field(default_factory=ArticleFormatting)
    language: str = field(default="en")
    topic: str = field(default="Music")

    def get_letter_probability(self, letter_1: str, letter_2: str) -> float:

        data = self.article_formatting.corpus
        article = " ".join(word for word in data.keys())
        occurrence_letter_1 = article.count(letter_1)
        sequential_occurrence = article.count(letter_1 + letter_2)
        probability = sequential_occurrence / occurrence_letter_1

        return probability

    def get_matrix_probability(self):

        probabilities_list = []
        for letter in ALPHABET:
            probability_list = []
            for letter_ in ALPHABET:
                prob = self.get_letter_probability(letter, letter_)
                probability_list.append(prob)
            probabilities_list.append(probability_list)

        return probabilities_list


def main():
    file = open("Articles/Music/Article_1.txt", "r", encoding='UTF8')
    file_ = file.read()
    articleformatter = ArticleFormatting(article=file_)
    word_generator = WordGenerator(article_formatting=articleformatter)
    print(word_generator.get_matrix_probability())


if __name__ == '__main__':
    main()
