import urllib.request
import html2text
from pypdf import PdfReader
import requests
import io
from tkinter import Tk


class TextImporter:
    """
    TextImporter

    This class is responsible for getting and cleaning text either through copy-paste, importing a pdf, or through a
    url.
    """

    def __init__(self, tk: Tk):
        self.tk: Tk = tk

    def get_from_url(self, target_url) -> str:
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

    def get_from_pdf(self, pdf_name) -> str:
        # reader = PdfReader(pdf_name)
        text = ""
        # for page in reader.pages:
        #    text += page.extract_text() + "\n"

    def get_from_clipboard(self) -> str:
        text = self.tk.clipboard_get()
        return text
