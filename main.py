#!/usr/bin/env python3
import wx


class MyFrame(wx.Frame):    
    def __init__(self):
        super().__init__(parent=None, title='Hello World')
        panel = wx.Panel(self)

        self.text_ctrl = wx.TextCtrl(panel, pos=(5, 5))
        my_btn = wx.Button(panel, label='Press Me', pos=(5, 55))

        self.Show()







def main():
    app = wx.App()
    frame = MyFrame()
    app.MainLoop()


if __name__ == '__main__':
    main()