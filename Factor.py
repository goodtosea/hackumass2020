class Factor:
    def __init__(self, factorName="", factorValue=-1):
        self.factorName = factorName
        self.factorValue = factorValue

    def __del__(self):
        del self

    def getFactorName(self):
        return self.factorName

    def getFactorValue(self):
        return self.factorValue

    def setFactorName(self, name):
        self.factorName = name

    def setFactorValue(self, value):
        self.factorValue = value