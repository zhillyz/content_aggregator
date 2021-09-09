class Animal():
    """Modelling an animal"""
    def __init__(self, type, name, age):
        """Initialise type of animal and name/age attributes."""
        self.type = type
        self.name = name
        self.age = age
    
    def sit(self):
        """Makes animal sit."""
        print(self.name.title() + " has sat down.")

    def roll_over(self):
        """ Makes animal roll over"""
        print(self.name.title() + " is rolling over!")
    
    def introduces(self):
        """Animal tells you its name"""
        if self.type == "dog":
            action = "barks"
        elif self.type == "cat":
            action = "meow"
        elif self.type == "horse":
            action = "neighs"
        else:
            action = "says"
        
        print(self.type.title() + " " + action + " my name is " + self.name.title())

    def how_old(self):
        """Animal tells you its age"""
        print(self.name.title() + " is " + self.age + " old.")

Larry = Animal('dog','Larry','2months')
Larry.sit()
Larry.roll_over()
Larry.introduces()
Larry.how_old()