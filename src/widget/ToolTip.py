from tkinter import *
from function.search import search

class ToolTip(object):

    def __init__(self, widget):
        self.widget = widget
        self.tipwindow = None
        self.id = None
        self.x = self.y = 0

    def showtip(self, text):
        self.text = text
        if self.tipwindow or not self.text:
            return
        # Placement de l'objet
        x, y, cx, cy = self.widget.bbox("insert")
        x = x + self.widget.winfo_rootx() + 57
        y = y + cy + self.widget.winfo_rooty() +27
        self.tipwindow = tw = Toplevel(self.widget)
        tw.wm_overrideredirect(1)
        tw.wm_geometry("+%d+%d" % (x, y))
        label = Label(tw, text=self.text, justify=LEFT,
                      background="#ffffe0", relief=SOLID, borderwidth=1,
                      font=("tahoma", "8", "normal"))
        label.pack(ipadx=1)

    def hidetip(self):
        tw = self.tipwindow
        self.tipwindow = None
        if tw:
            tw.destroy()

# Fonction de création de l'objet
def CreateToolTip(widget, text):
    toolTip = ToolTip(widget)
    def enter(event):
        summary = search(text)
        summary = summary.find("div", class_='mw-parser-output')
        result = ""
        if not summary.findChildren('p', recursive=False):
            result = "Pas de résumé disponible :("
        else:
            for element in summary.findChildren('p', recursive=False):
                if element.text and element.text.strip():
                    result = element.text
                    break
            if len(result) > 150:
                result = result[0:150]+"..."
        toolTip.showtip(result)
    def leave(event):
        toolTip.hidetip()
    widget.bind('<Enter>', enter)
    widget.bind('<Leave>', leave)