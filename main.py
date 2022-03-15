#!/usr/bin/env python3
import wx

def button_example():
    class MyFrame(wx.Frame):    
        def __init__(self):
            super().__init__(parent=None, title='Fluid Program')
            panel = wx.Panel(self)

            self.text_ctrl = wx.TextCtrl(panel, pos=(5, 5))
            my_btn = wx.Button(panel, label='Press Me', pos=(5, 55))

            self.Show()
    

    def example1():
        app = wx.App()
        frame = MyFrame()
        app.MainLoop()
    
    example1()


def main():
    button_example()
    


if __name__ == '__main__':
    main()