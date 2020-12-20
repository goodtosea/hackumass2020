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


def newFile():  # Resets working_chart's chart to a blank chart and redraws.
    working_chart.resetChart()
    global open_name
    open_name = False
    drawChart(working_chart.getChart())


def openFile():  # Opens existing chart

    chart_file = filedialog.askopenfilename(initialdir="C:/valueOf", title="Open File", filetypes=(
    ("valueOf Files", "*.vof"), ("Text Files", "*.txt"), ("All Files", "*.*")))

    if chart_file:
        global open_name
        open_name = chart_file

    working_chart.readChart(chart_file)
    drawChart(working_chart.getChart())


def saveFileAs():  # Saves a chart as a new file
    chart_file = filedialog.asksaveasfilename(defaultextension=".vof", initialdir="C:/valueOf", title="Save File",
                                              filetypes=(("valueOf Files", "*.vof"), ("Text Files", "*.txt"),
                                                         ("All Files", "*.*")))
    if chart_file:
        drawChart(working_chart.getChart())
        saveCurrentChart()
        working_chart.exportChart(chart_file)


def saveFile():  # Overwrites saved chart, or if not saved, saves chart as new file
    global open_name
    if open_name:
        drawChart(working_chart.getChart())
        saveCurrentChart()
        working_chart.exportChart(open_name)
    else:
        saveFileAs()


def exitProgram(self):  # Exits the program
    quit()


def drawFrame():  # Draws the frame (outside of the window) for the program
    my_frame = Frame(root)
    my_frame.grid(column=0, row=0)

    # Navbar Menu
    my_menu = Menu(root, tearoff=False)
    root.config(menu=my_menu)

    # Menu for File
    file_menu = Menu(my_menu, tearoff=False)
    my_menu.add_cascade(label="File", menu=file_menu)
    file_menu.add_command(label="New Chart", command=newFile)  # lambda: drawChart(test_chart)
    file_menu.add_command(label="Open Chart", command=openFile)
    file_menu.add_separator()
    file_menu.add_command(label="Save As", command=saveFileAs)
    file_menu.add_command(label="Save", command=saveFile)
    file_menu.add_separator()
    file_menu.add_command(label="Exit", command=exitProgram)

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


# Draws a given chart in the window
def drawChart(chart):
    for widget in root.winfo_children():
        widget.destroy()
    drawFrame()
    consideration_entry = Entry(root)
    consideration_entry.insert(END, chart.getConsideration())
    consideration_entry.grid(column=3, row=1)
    consideration_entry_list.clear()
    consideration_entry_list.append(consideration_entry)
    # Entry(root, text=chart.getConsideration()).grid(column=3, row=1)
    Label(root, text="Pros", relief="groove", borderwidth=1).grid(column=1, columnspan=2, row=2, sticky=NSEW)
    Label(root, text="Cons", relief="groove", borderwidth=1).grid(column=4, columnspan=2, row=2, sticky=NSEW)

    # root.grid_rowconfigure(0, weight=1)
    # root.grid_rowconfigure(4, weight=1)
    root.grid_columnconfigure(0, weight=1)
    root.grid_columnconfigure(6, weight=1)

    # Draws each of the pro factors as a prewritten entry with a corresponding combobox for each value
    # Resets the pro entry list and refills it
    pros = chart.getProsList()
    pro_entry_list.clear()
    for i in range(len(pros)):
        factor_entry = Entry(root)
        factor_entry.insert(END, pros[i].getFactorName())
        factor_entry.grid(column=1, row=i + 3, sticky=NSEW)
        pro_entry_list.append(factor_entry)

        value_combobox = Combobox(root)
        value_combobox["values"] = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
        value_combobox.current(pros[i].getFactorValue() - 1)
        value_combobox.grid(column=2, row=i + 3)
        pro_combobox_list.append(value_combobox)

    # Pro add button
    Button(root, text="+", command=pressedNewEntry).grid(column=1, columnspan=2, row=len(pros) + 3)

    # Draws each of the con factors as a label with a corresponding combobox for each value
    # Resets the con entry list and refills it
    cons = chart.getConsList()
    for i in range(len(cons)):
        factor_entry = Entry(root, text=cons[i].getFactorName())
        factor_entry.insert(END, cons[i].getFactorName())
        factor_entry.grid(column=4, row=i + 3, sticky=NSEW)
        con_entry_list.append(factor_entry)

        value_combobox = Combobox(root)
        value_combobox["values"] = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
        value_combobox.current(cons[i].getFactorValue() - 1)
        value_combobox.grid(column=5, row=i + 3)
        con_combobox_list.append(value_combobox)

    # Con add button
    Button(root, text="+", command=pressedNewEntry).grid(column=4, columnspan=2, row=len(cons) + 3)

    print(pro_entry_list)
    print(con_entry_list)
    print(pro_combobox_list)
    print(con_combobox_list)

# Adds a new entry to the table
def pressedNewEntry():
    x = 5

def saveCurrentChart():
    chart_to_save = Chart(consideration_entry_list[0])
    for i in range(len(pro_entry_list)):
        chart_to_save.prosAddFactor(Factor(pro_entry_list[i].get(), pro_combobox_list[i].get()))

    for i in range(len(con_entry_list)):
        chart_to_save.consAddFactor(Factor(con_entry_list[i].get(), con_combobox_list[i].get()))

    working_chart.setChart(chart_to_save)


working_chart = theChart(Chart())

consideration_entry_list = []

pro_entry_list = []
con_entry_list = []
pro_combobox_list = []
con_combobox_list = []

drawFrame()
root.mainloop()