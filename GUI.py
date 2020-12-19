from tkinter import *
from Chart import Chart

root = Tk()
root.title("valueOf")
root.geometry("1200x660")

# Create New File Function
# Creates an empty chart and draws it
def newFile():
    drawChart(Chart())

# Draws a given chart in the window
def drawChart(chart):
    for widget in root.winfo_children():
        widget.destroy()
    drawFrame()
    Label(root, text=chart.getConsideration).grid(column=1, row=1)
    Label(root, text="Pros").grid(column=0, row=2)
    Label(root, text="Cons").grid(column=2, row=2)

def drawFrame():
    my_frame = Frame(root)
    my_frame.grid(column=0, row=0)

    # Navbar Menu
    my_menu = Menu(root, tearoff=False)
    root.config(menu=my_menu)

    # Menu for File
    file_menu = Menu(my_menu, tearoff=False)
    my_menu.add_cascade(label="File", menu=file_menu)
    file_menu.add_command(label="New Chart", command=newFile)
    file_menu.add_command(label="Open Chart")
    file_menu.add_separator()
    file_menu.add_command(label="Save As")
    file_menu.add_command(label="Save")
    file_menu.add_separator()
    file_menu.add_command(label="Exit")

    # Menu for Options
    options_menu = Menu(my_menu, tearoff=False)
    my_menu.add_cascade(label="Options", menu=options_menu)
    options_menu.add_command(label="Autofill Words")
    options_menu.add_command(label="Autofill Values")
    options_menu.add_command(label="Show Trends")
    options_menu.add_command(label="Incorporate Trends in Suggestions")
    options_menu.add_separator()

    # Theme Menu
    theme_menu = Menu(options_menu, tearoff=False)
    options_menu.add_cascade(label="Themes", menu=theme_menu)
    theme_menu.add_command(label="Light")
    theme_menu.add_command(label="Dark")

test_chart = Chart()
test_chart.setConsideration("Should I walk my dog?")
test_chart
drawFrame()
root.mainloop()