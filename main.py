from tkinter import *
from tkinter import filedialog
from tkinter.ttk import *
from theChart import theChart
from Chart import Chart
from Factor import Factor

root = Tk()
root.title("valueOf")
root.geometry("800x800")

# Set variable for open file name
global open_name
open_name = False

def newFile():                                  # Creates new chart
    chart.resetChart()
    global open_name
    open_name = False

def openFile():                                 # Opens existing chart
    chart_file = filedialog.askopenfilename(initialdir="C:/valueOf", title="Open File", filetypes=(("valueOf Files", "*.vof"), ("Text Files", "*.txt"), ("All Files", "*.*")))

    if chart_file:
        global open_name
        open_name = chart_file

    chart.readChart(chart_file)


def saveFileAs():                               # Saves a chart as a new file
    chart_file = filedialog.asksaveasfilename(defaultextension=".vof", initialdir="C:/valueOf", title="Save File",
                                              filetypes=(("Text Files", "*.txt"), ("All Files", "*.*")))
    if chart_file:
        chart.exportChart(chart_file)

def saveFile():                                 # Overwrites saved chart, or if not saved, saves chart as new file
    global open_name
    if open_name:
        chart.exportChart(open_name)
    else:
        saveFileAs()

def exitProgram(self):                          # Exits the program
    quit()

chart = theChart()