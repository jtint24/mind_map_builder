import wx
import spacy

from text_importer import TextImporter
from summarizer import Summarizer
from map_displayer import MapDisplayer
from map_builder import MapBuilder
from relation_extractor import RelationExtractor
from keyword_extractor import KeywordExtractor

from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas


class MainFrame(wx.Frame):
    """
    MainFrame

    A wx frame that holds the interface to read different kinds of text
    """

    def __init__(self):
        super().__init__(parent=None, title='Mind Map Builder')
        panel = wx.Panel(self)
        self.sizer = wx.BoxSizer(wx.VERTICAL)

        my_btn = wx.Button(panel, label='Import Text from Clipboard')
        my_btn.Bind(wx.EVT_BUTTON, self.make_from_clipboard)
        self.sizer.Add(my_btn, 0, wx.ALL | wx.CENTER, 5)

        url_btn = wx.Button(panel, label='Import Text from URL')
        url_btn.Bind(wx.EVT_BUTTON, self.make_from_url)
        self.sizer.Add(url_btn, 0, wx.ALL | wx.CENTER, 5)

        self.loading_messages = wx.StaticText(panel, label="", size=wx.Size(200, 200))
        self.sizer.Add(self.loading_messages, 0, wx.ALL | wx.CENTER, 5)

        panel.SetSizer(self.sizer)
        self.Show()

    def make_from_text(self, text):
        nlp = spacy.load("en_core_web_sm")
        summarizer = Summarizer(200, nlp)
        kw_extractor = KeywordExtractor()
        relation_extractor = RelationExtractor(0.03)
        map_builder = MapBuilder()
        map_displayer = MapDisplayer()

        summarized_text = summarizer(text)
        self.loading_messages.SetLabelText("Loaded text...\n")
        # print(summarized_text)
        keywords = kw_extractor(summarized_text)
        self.loading_messages.SetLabelText("Extracted keywords...\n")

        # print(keywords)
        relations = relation_extractor(keywords)
        self.loading_messages.SetLabelText("Extracted relations...\n")

        # print(relations)
        relation_maps = map_builder.make_maps(keywords, relations)
        self.loading_messages.SetLabelText("Built map!\n")

        # for relation_map in relation_maps:
        # print(relation_map)

        figure = map_displayer(relation_maps)
        fig_canvas = FigureCanvas(self, figure)
        self.sizer.Add(fig_canvas, 1, wx.LEFT | wx.TOP | wx.GROW)
        self.Fit()

    def make_from_clipboard(self, event):
        importer = TextImporter()

        text = importer.get_from_clipboard()
        self.make_from_text(text)

    def make_from_url(self, event):
        dlg = wx.TextEntryDialog(self, "please enter the URL:")
        result = dlg.ShowModal()

        if result != wx.OK:
            importer = TextImporter()
            try:
                text = importer.get_from_url(dlg.GetValue())
                self.make_from_text(text)
            except (ValueError, Exception):
                self.loading_messages.SetLabelText("Couldn't load the requested URL\n")


class Interface:
    def __init__(self):
        pass

    def main_menu(self):
        app = wx.App()
        frame = MainFrame()

        frame.Show()
        app.MainLoop()
