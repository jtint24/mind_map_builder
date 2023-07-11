import openai

import os

from typing import List, Dict


class KeywordExtractor:
    """
    Uses calls to the OpenAI GPT API to extract a list of keywords from a piece of text
    """

    def __init__(self):
        self.api_key = os.getenv("GPT_API_KEY")
        openai.api_key = self.api_key
        self.keywordCache: Dict[str, List[str]] = {}

    def __call__(self, text: str) -> List[str]:
        if text not in self.keywordCache:
            self.keywordCache[text] = self._get_keywords(text)
        return self.keywordCache[text]

    def _get_keywords(self, text: str) -> List[str]:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content":
                    "Give the keywords in the following text in descending order of importance: {}".format(text)},
            ]
        )
        return response



