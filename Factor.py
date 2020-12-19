# Object representing the factor for consideration and its weighting on the final decision

class Factor:
    def __init__(self, factorName="", factorValue=-1):
        self.factorName = factorName       # Name of the factor
        self.factorValue = factorValue     # Factor's significance

    def getFactorName(self):               # Returns factor name
        return self.factorName

    def getFactorValue(self):              # Returns factor value
        return self.factorValue

    def setFactorName(self, name):         # Changes factor name
        self.factorName = name

    def setFactorValue(self, value):       # Changes factor value
        self.factorValue = value