from Factor import Factor
from Chart import Chart

# Navigation Bar class, includes basic functions such as save, save as, open, options, and exit

class NavBar:
    # def newFile(self):
    #     Creates new blank chart
    #     self.chart = Chart()

    def openFile(self, fileName):
        # Opens an existing file

        chart = Chart()

        # Reads file and creates a chart
        f = open(fileName, "r")
        line = f.readline()
        chart.setConsideration(line)
        while True:
            line = f.readline()
            if (line == "~~~"):    # Make error catcher that prints "Unacceptable File" if loop doesnt break
                break
            line = line.split("~")
            proFactor = Factor(line[1], line[0])
            chart.prosAddFactor(proFactor)
        while True:
            line = f.readline()
            if not line:
                break
            line = line.split("~")
            conFactor = Factor(line[1], line[0])
            chart.consAddFactor(conFactor)
        f.close()


    def saveFileAs(self, fileName, chart):

        # Creates existing file. Error message will show when trying to create fileName that already exists.
        # Save file in the following format
        #    Consideration
        #    pro_value pro_name
        #    pro_value pro_name
        #    …
        #    ~~~          (Splits pros from cons)
        #    con_value con_name
        #    con_value con_name
        #    …

        # Writes new file
        testFile = open(fileName, "x")
        f.write(chart.getConsideration() + "\n")
        prosList = chart.getProsList()
        consList = chart.getConsList()
        for x in prosList:
            f.write(prosList[x].getFactorValue + "~")
            f.write(prosList[x].getFactorName + "\n")
        f.write("~~~\n")
        for x in consList:
            f.write(consList[x].getFactorValue + "~")
            f.write(consList[x].getFactorName + "\n")
        f.close()


    def saveFile(self, fileName, chart):
        # Same as saveFileAs, but writes over existing file that is the same as the one currently being worked on.
        # If file does not exist in the folder, it will run saveFileAs

        # Overwrites existing file or writes new file
        testFile = open(fileName, "w")
        f.write(chart.getConsideration() + "\n")
        prosList = chart.getProsList()
        consList = chart.getConsList()
        for x in prosList:
            f.write(prosList[x].getFactorValue + "~")
            f.write(prosList[x].getFactorName + "\n")
        f.write("~~~\n")
        for x in consList:
            f.write(consList[x].getFactorValue + "~")
            f.write(consList[x].getFactorName + "\n")
        f.close()

    def exitProgram(self):
        # If current file has not been saved or is different than its saved version, ask
        # "Would you like to first save your file?" with yes or no options. (in GUI. If yes, run saveFile.)
        quit()

    def programOptions(self, previousOptions):
        x = 5
        # LAST ON PRIORITIES
        # Shows all options in a checkmark format
        # Implementations needed include: Dark Theme (Default off), Autofill Words (Default on after
        # 3 files created), Autofill Values (Default on after 3 files created), Show Trends (Default off),
        # Incorporate Tends In Suggestions (Incorporates prior Values on each word towards later ratings/suggestions)