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
    
    app = wx.App()
    frame = MyFrame()
    app.MainLoop()
    

def sizers_example():

    class MyFrame(wx.Frame):    
        def __init__(self):
            super().__init__(parent=None, title='Fluid Program')
            panel = wx.Panel(self)        
            my_sizer = wx.BoxSizer(wx.VERTICAL)        
            self.text_ctrl = wx.TextCtrl(panel)
            my_sizer.Add(self.text_ctrl, 0, wx.ALL | wx.EXPAND, 5)        
            my_btn = wx.Button(panel, label='Press Me')
            my_sizer.Add(my_btn, 0, wx.ALL | wx.CENTER, 5)        
            panel.SetSizer(my_sizer)        
            self.Show()

    app = wx.App()
    frame = MyFrame()
    app.MainLoop()

def event_example():

    class MyFrame(wx.Frame):
        def __init__(self):
            super().__init__(parent=None, title='Hello World')
            panel = wx.Panel(self)        
            my_sizer = wx.BoxSizer(wx.VERTICAL)        
            self.text_ctrl = wx.TextCtrl(panel)
            my_sizer.Add(self.text_ctrl, 0, wx.ALL | wx.EXPAND, 5)        
            my_btn = wx.Button(panel, label='Press Me')
            my_btn.Bind(wx.EVT_BUTTON, self.on_press)
            my_sizer.Add(my_btn, 0, wx.ALL | wx.CENTER, 5)        
            panel.SetSizer(my_sizer)        
            self.Show()

        def on_press(self, event):
            value = self.text_ctrl.GetValue()
            if not value:
                print("You didn't enter anything!")
            else:
                print(f'You typed: "{value}"')

    
    app = wx.App()
    frame = MyFrame()
    app.MainLoop()


def main():
    # button_example()
    # sizers_example()
    event_example()


    


if __name__ == '__main__':
    main()