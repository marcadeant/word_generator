from dataclasses import dataclass, field
from typing import List
import numpy as np

from article_formating import ArticleFormatting
from constants import INDEX, ALPHABET

@dataclass
class WordGenerator:

    article_formatting: ArticleFormatting = field(default_factory=ArticleFormatting)

    def get_conditional_probability(self, letter_1: str, letter_2: str) -> float:

        data = self.article_formatting.corpus
        article = " ".join(word for word in data.keys())
        occurrence_letter_2 = article.count(letter_2)
        sequential_occurrence = article.count(letter_1 + letter_2)
        probability = sequential_occurrence / occurrence_letter_2

        return probability

    def get_matrix_probability(self) -> List[List[float]]:

        probabilities_list = []
        for letter in ALPHABET:
            probability_list = []
            for letter_ in ALPHABET:
                prob = self.get_conditional_probability(letter_, letter)
                probability_list.append(prob)
            probabilities_list.append(probability_list)

        return probabilities_list

    # Markov chains implementation
    def forecast_word(self, nb_of_letter: int, initial_state: str) -> str:

        transition_name = [[b + a for a in ALPHABET] for b in ALPHABET]
        # Choose the starting state (First letter of the word generated)
        first_letter = initial_state
        transition_matrix = self.get_matrix_probability()
        final_word_list = [initial_state]

        prob = 1
        i = 0
        while i < nb_of_letter - 1:
            p = np.array(transition_matrix[INDEX[first_letter]])
            p /= p.sum()
            change = np.random.choice(transition_name[0], replace=True, p=p)
            letter_next_state = change[-1:]

            prob = prob * transition_matrix[INDEX[first_letter]][INDEX[letter_next_state]]
            first_letter = letter_next_state
            final_word_list.append(first_letter)
            i += 1

        return ''.join(letter for letter in final_word_list)
