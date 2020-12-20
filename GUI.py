from tkinter import * 
from tkinter import filedialog
from tkinter.ttk import *
from Chart import Chart
from Factor import Factor


# Initializes the window with title and dimensions
root = Tk()
root.title("valueOf")
root.geometry("1200x660")

# Create New File Function
# Creates an empty chart and draws it
def newFile():
    drawChart(Chart())


# Uses file dialog and opens a file
def openFile():
    chart_file = filedialog.askopenfilename(initialdir="C:/valueOf", title="Open File", filetypes=(("Text Files", "*txt"), ("All Files", "*.")))

    # Reads file and creates a chart
    chart = Chart()
    f = open(chart_file, "r")
    line = f.readline()
    chart.setConsideration(line)
    print(chart.getConsideration())
    while True:
        line = f.readline()
        if (line == "~~~\n"):  # Make error catcher that prints "Unacceptable File" if loop doesnt break
            break
        if not line:
            break
        factorInfo = line.split("~")
        proFactor = Factor(factorInfo[1], int(factorInfo[0]))
        chart.prosAddFactor(proFactor)
    while True:
        line = f.readline()
        if not line:
            break
        factorInfo = line.split("~")
        conFactor = Factor(factorInfo[1], int(factorInfo[0]))
        chart.consAddFactor(conFactor)
    f.close()

    print(chart.getConsList()[1].getFactorName())
    print(chart.getConsList()[1].getFactorValue())

    drawChart(chart)


# Quits the program
def exitProgram():
    quit()


# Draws a given chart in the window
def drawChart(chart):
    for widget in root.winfo_children():
        widget.destroy()
    drawFrame()
    consideration_entry = Entry(root)
    consideration_entry.insert(END, chart.getConsideration())
    consideration_entry.grid(column=3, row=1)
    # Entry(root, text=chart.getConsideration()).grid(column=3, row=1)
    Label(root, text="Pros", relief="groove", borderwidth=1).grid(column=1, columnspan=2, row=2, sticky=NSEW)
    Label(root, text="Cons", relief="groove", borderwidth=1).grid(column=4, columnspan=2, row=2, sticky=NSEW)

    # root.grid_rowconfigure(0, weight=1)
    # root.grid_rowconfigure(4, weight=1)
    root.grid_columnconfigure(0, weight=1)
    root.grid_columnconfigure(6, weight=1)

    # Draws each of the pro factors as a prewritten entry with a corresponding combobox for each value
    pros = chart.getProsList()
    for i in range(len(pros)):
        factor_entry = Entry(root)
        factor_entry.insert(END, pros[i].getFactorName())
        factor_entry.grid(column=1, row=i+3, sticky=NSEW)
        
        value_widget = Combobox(root)
        value_widget["values"] = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
        value_widget.current(pros[i].getFactorValue()-1)
        value_widget.grid(column=2, row=i+3)

    # Draws each of the con factors as a label with a corresponding combobox for each value
    cons = chart.getConsList()
    for i in range(len(cons)):
        factor_entry = Entry(root, text=cons[i].getFactorName())
        factor_entry.insert(END, cons[i].getFactorName())
        factor_entry.grid(column=4, row=i+3, sticky=NSEW)
        
        value_widget = Combobox(root)
        value_widget["values"] = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
        value_widget.current(cons[i].getFactorValue()-1)
        value_widget.grid(column=5, row=i+3)


# Draws the frame (outside of the window) for the program
def drawFrame():
    my_frame = Frame(root)
    my_frame.grid(column=0, row=0)

    # Navbar Menu
    my_menu = Menu(root, tearoff=False)
    root.config(menu=my_menu)

    # Menu for File
    file_menu = Menu(my_menu, tearoff=False)
    my_menu.add_cascade(label="File", menu=file_menu)
    file_menu.add_command(label="New Chart", command=newFile) #lambda: drawChart(test_chart)
    file_menu.add_command(label="Open Chart", command=openFile)
    file_menu.add_separator()
    file_menu.add_command(label="Save As")
    file_menu.add_command(label="Save")
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


# Test chart
# test_chart = Chart()
# test_chart.setConsideration("Should I walk my dog?")
# f1 = Factor()
# f1.setFactorName("Exercise")
# f1.setFactorValue(1)
# f2 = Factor()
# f2.setFactorName("Boring")
# f2.setFactorValue(5)
# f3 = Factor()
# f3.setFactorName("Companionship")
# f3.setFactorValue(5)

# test_chart.prosAddFactor(f1)
# test_chart.prosAddFactor(f2)
# test_chart.consAddFactor(f3)


drawFrame()
root.mainloop()