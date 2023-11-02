import urllib.request
import html2text
from pypdf import PdfReader
import requests
import io
import pyperclip
from tkinter import Tk


class TextImporter:
    """
    TextImporter

    This class is responsible for getting and cleaning text either through copy-paste, importing a pdf, or through a
    url.
    """

    def __init__(self):
        pass

    @staticmethod
    def get_from_url(target_url) -> str:
        """
        :return: Returns cleaned text from a target_url
        """
        raw_html = ""
        try:
            lines = urllib.request.urlopen(target_url)
            for line in lines:
                raw_html += line.decode('utf-8')

            plain_text = html2text.html2text(raw_html)
            return plain_text
        except UnicodeDecodeError:
            r = requests.get(target_url)
            f = io.BytesIO(r.content)

            reader = PdfReader(f)

            plain_text = ""
            for page in reader.pages:
                plain_text += page.extract_text()
            return plain_text

    @staticmethod
    def get_from_clipboard() -> str:
        """
        :return: The text currently in the clipboard
        """
        text = pyperclip.paste()
        return text
