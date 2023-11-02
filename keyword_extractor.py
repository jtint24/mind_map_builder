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

    @staticmethod
    def _get_keywords(text: str) -> List[str]:
        """
        Gets a list of keywords from a text using a fine-tuned descendent of ChatGPT

        :param text: The text to extract the keywords from
        :return: Keywords from the text as a list
        """
        response = openai.ChatCompletion.create(
            model="keyword-ex-davinci-ft",  # "gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content":
                    "Give the keywords in the following text in descending order of importance in a comma-separated "
                    "list: {}".format(text)},
            ]
        )
        choices = response["choices"]
        main_response = choices[0]["message"]["content"]
        print(main_response)

        lines = main_response.split(",")
        keywords = []
        for line in lines:
            keyword = line.strip()
            if keyword != "":
                keywords.append(keyword)
        return keywords
