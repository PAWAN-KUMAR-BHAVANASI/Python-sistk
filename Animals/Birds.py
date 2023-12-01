class Birds:
    def __init__(self):
        '''Constructor for this class'''
        # Initialize the members attribute
        self.members = ["Sparrow","Robin","Duck"]

    def printMembers(self):
        print('Printing Members of the Birds Class')
        for member in self.members:
            print("\t%s" % member)
    