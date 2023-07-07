
from spacy import Language
from spacy.tokens import Doc, Token

import itertools
import math
import string
from typing import Dict


class Summarizer:
    """
    Summarizer

    This class is responsible for eliminating sentences that have low co-occurrence entropy to reduce the number of
    tokens while generally preserving keywords and keyword relationships.

    """
    def __init__(self, max_token_count: int, nlp: Language):
        self.max_token_count: int = max_token_count
        self.nlp: Language = nlp

    def __call__(self, document: Doc) -> Doc:
        if len(document) < self.max_token_count:
            return document

        sentences = list(document.sents)

        # Build a co-occurrence map

        co_occurrence_map = dict()
        word_set = set()

        for sentence in sentences:
            words = sentence.as_doc()
            for word1, word2 in itertools.product(words, words):
                if word1.text not in co_occurrence_map:
                    co_occurrence_map[word1.text] = dict()
                if word2.text not in co_occurrence_map[word1.text]:
                    co_occurrence_map[word1.text][word2.text] = 0
                co_occurrence_map[word1.text][word2.text] = co_occurrence_map[word1.text][word2.text] + 1
                word_set.add(word1)

        # Calculate the entropy of each word

        word_entropies = dict()

        for word in word_set:
            if Summarizer._is_function_word(word.text):
                word_entropies[word.text] = 0.0

            co_occurrence_sum = 0.0
            for pair_word in word_set:
                if pair_word.text in co_occurrence_map[word.text]:
                    co_occurrence_sum += co_occurrence_map[word.text][pair_word.text]

            entropy = 0.0

            for pair_word in word_set:
                if pair_word.text in co_occurrence_map[word.text]:
                    probability = co_occurrence_map[word.text][pair_word.text] / co_occurrence_sum
                    entropy += - probability * math.log(probability)
            word_entropies[word.text] = entropy



            # Sort sentences by the summed entropy of their sentences

            sentences_by_entropy = sorted(sentences, key=lambda sent: Summarizer._get_sentence_entropy(sent, word_entropies), reverse=True)

            sentences_to_include = set()

            total_length = 0

            for sentence in sentences_by_entropy:
                if len(sentence) + total_length > self.max_token_count:
                    break

                total_length += len(sentence)
                sentences_to_include.add(sentence)

            return_doc = Doc(self.nlp.vocab)

            for sentence in sentences:
                if sentence in sentences_to_include:
                    return_doc = Doc.from_docs([return_doc, sentence.as_doc()])

            return return_doc

    @staticmethod
    def _is_function_word(word: str) -> bool:
        if str(word.translate(str.maketrans('', '', string.punctuation))).strip() == 0:
            return True
        return word in {"hello"}

    @staticmethod
    def _get_sentence_entropy(sentence: Doc, entropy_map: Dict[str, float]) -> float:
        entropy_sum = 0.0
        for token in sentence:
            if token.text in entropy_map:
                entropy_sum += entropy_map[token.text]
        return entropy_sum






