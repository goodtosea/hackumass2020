# Navigation Bar class, includes basic functions such as save, save as, open, options, and exit
class NavBar:
    def newFile(self):
        # Creates new blank chart

    def openFile(self):
        # Opens an existing file

    def saveFileAs(self, fileName):
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

    def saveFile(self):
        # Same as saveFileAs, but writes over existing file that is the same as the one currently being worked on.
        # If file does not exist in the folder, it will run saveFileAs

    def exitProgram(self):
        # If current file has not been saved or is different than its saved version, ask
        # "Would you like to first save your file?" with yes or no options. (in GUI. If yes, run saveFile.)

    def programOptions(self, previousOptions):
        # LAST ON PRIORITIES
        # Shows all options in a checkmark format
        # Implementations needed include: Dark Theme (Default off), Autofill Words (Default on after
        # 3 files created), Autofill Values (Default on after 3 files created), Show Trends (Default off),
        # Incorporate Tends In Suggestions (Incorporates prior Values on each word towards later ratings/suggestions)