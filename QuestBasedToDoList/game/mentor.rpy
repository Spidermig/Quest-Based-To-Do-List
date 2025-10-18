python:
    class mentor:

        # Initialization
        def _init_(self, name, dialog):
            self.namesList = ["boy", "girl", "nonbinary"] # List of characters

            self.name = name # Name of current character
            self.dialog = dialog # Dialogue choices

        # Choose character
        def chooseCharacter(choice):
            if choice in self.namesList:
                self.name = choice
            else:
                printf('Pick a character')
                return chooseCharacter

        # Get the characters name
        def getName():
            return self.name
        
