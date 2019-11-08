import wx

#declare classes that will hold static values
class variables_5v5_NoShips:
    gpValues = ['0 - 599.9k', '600k - 799.9k', '800k - 999.9k', '1M - 1.29M', '1.3M - 1.59M', '1.6M - 1.99M', '2M - 2.49M', '2.5M - 3.09M', '3.1M - 3.79M', '3.8M - 4.49M', '4.5M+']
    gpDivisions = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    gacDefences = [4, 4, 4, 4, 4, 5, 5, 6, 6, 8, 8]

class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title='GAC Calculator')

        #declare panel
        panel = wx.Panel(self)
        #declare Box Sizer
        my_sizer = wx.BoxSizer(wx.VERTICAL)
        #declare calculate button widget
        calculateBtn = wx.Button(panel, label='Calculate', pos=(5, 55))
        #declare GP choice widget
        self.gpChoice = wx.Choice(panel, choices = variables_5v5_NoShips.gpValues)

        #add widgets to Sizer
        my_sizer.Add(self.gpChoice, 0, wx.ALL | wx.EXPAND, 5)
        my_sizer.Add(calculateBtn, 0, wx.ALL | wx.CENTER, 5)

        calculateBtn.Bind(wx.EVT_BUTTON, self.calcBtnPress)

        self.gpChoice.Bind(wx.EVT_CHOICE, self.gpOnChoice)

        panel.SetSizer(my_sizer)
        self.Show()

    def calcBtnPress(self, event):
        print("In Development")

    def gpOnChoice(self,event):
        selectedString = self.gpChoice.GetString(self.gpChoice.GetSelection())
        selectedIndex = self.gpChoice.GetSelection()
        print("selected " + selectedString + ".")
        print(selectedIndex)

if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame()
    app.MainLoop()
