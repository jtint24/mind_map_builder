from tkinter import Tk, Label
import wx


class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title='Hello World')
        panel = wx.Panel(self)

        clipboard_btn = wx.Button(panel, label='Import Text from Clipboard', pos=(10+90, 55))
        url_btn = wx.Button(panel, label='Import Text from URL', pos=(25+90, 85))

        self.Show()
class Interface:
    def __init__(self):
        pass

    def main_menu(self):
        app = wx.App()
        frame = MyFrame()

        frame.Show()
        app.MainLoop()


