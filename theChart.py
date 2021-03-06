from Chart import Chart
from Factor import Factor

# The chart that the program will be changing and manipulating

class theChart:
    def __init__(self, chart):
        self.chart = chart

    def resetChart(self):  # Used in New File function
        self.chart = Chart()

    def getChart(self):
        return self.chart

    def setChart(self, chart):
        self.chart = chart

    def readChart(self, file):
        # Reads file and creates a chart
        f = open(file, "r")
        line = f.readline().rstrip("\n")
        self.chart.setConsideration(line)
        while True:
            line = f.readline().rstrip("\n")
            if (line == "~~~"):  # Make error catcher that prints "Unacceptable File" if loop doesnt break
                break
            if not line:
                break
            factorInfo = line.split("~")
            proFactor = Factor(factorInfo[1], int(factorInfo[0]))
            self.chart.prosAddFactor(proFactor)
        while True:
            line = f.readline().rstrip("\n")
            if not line:
                break
            factorInfo = line.split("~")
            conFactor = Factor(factorInfo[1], int(factorInfo[0]))
            self.chart.consAddFactor(conFactor)
        f.close()

    def exportChart(self, file):  # Used in Save File function
        f = open(file, "w")
        f.write(self.chart.getConsideration() + "\n")
        prosList = self.chart.getProsList()
        consList = self.chart.getConsList()
        for x in range(len(prosList)):
            f.write(str(prosList[x].getFactorValue()))
            f.write("~" + prosList[x].getFactorName() + "\n")
        f.write("~~~\n")
        for x in range(len(consList)):
            f.write(str(consList[x].getFactorValue()))
            f.write("~" + consList[x].getFactorName() + "\n")
        f.close()