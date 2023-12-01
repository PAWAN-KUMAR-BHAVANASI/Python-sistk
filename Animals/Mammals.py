class Mammals:
    def __init__(self):
        '''Constructor for this class'''
        # Initialize the members attribute
        self.members = ["Tiger", "Elephant", "WildCat"]

    def printMembers(self):
        print('Printing Members of the mammals Class')
        for member in self.members:
            print("\t%s" % member)
