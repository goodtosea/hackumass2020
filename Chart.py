from Factor import Factor

# Object representing the T-Chart that contains all the factors present in the decision

class Chart:
    def __init__(self, consideration="", prosList=[], consList=[]):
        self.consideration = consideration           # The decision being made
        self.prosList = prosList                     # The list of pro factors
        self.consList = consList                     # The list of con factors

    def getConsideration(self):                      # Returns the consideration
        return self.consideration

    def setConsideration(self, cons):                # Sets the consideration
        self.consideration = cons

    def getProsList(self):                           # Returns the pros list
        return self.prosList

    def getConsList(self):                           # Returns the cons list
        return self.consList

    def prosAddFactor(self, factor):                 # Adds a factor to the list of pros
        self.prosList.append(factor)

    def prosRemoveFactor(self, factor):              # Removes a factor from the list of pros
        self.prosList.remove(factor)

    def consAddFactor(self, factor):                 # Adds a factor to the list of cons
        self.consList.append(factor)

    def consRemoveFactor(self, factor):              # Removes a factor from the list of cons
        self.consList.remove(factor)

    def generateSuggestion(self):                    # Judges factor values and returns a suggestion
        # Establishes the sum of all the factor values for each list
        prosValue = 0
        consValue = 0
        for f in self.prosList:
            prosValue += f.getFactorValue
        for f in self.consList:
            consValue += f.getFactorValue

        # Initializes the variables for the judgement
        suggestion = "No suggestion can be made at this time"
        suggValue = prosValue / (prosValue + consValue)

        # Compares suggested values to a list of ratios, generating a suggestion
        if (suggValue < 0.33):
            suggestion = "Highly recommend you do not do this."
        elif (0.33 <= suggValue < 0.45):
            suggestion = "You probably shouldn't do this."
        elif (0.45 <= suggValue < 0.5):
            suggestion = "It's close... you may consider against this."
        elif (suggValue == 0.5):
            suggestion = "You probably won't go wrong either way... coin flip?"
        elif (0.5 < suggValue <= 0.55):
            suggestion = "It's close... you may consider doing this."
        elif (0.55 < suggValue <= 0.66):
            suggestion = "You probably should do this."
        elif (suggValue > 0.66):
            suggestion = "Highly recommend you do this."

        return suggestion