class food:
    def __init__(self, name, spice, country, taste):
        self.name=name
        self.spice=spice
        self.country=country
        self.taste=taste

    def revealursecrets(self):
        print("The details of the food given are as shown below:")
        print("Name:",self.name)
        print("Spice:",self.spice)
        print("Country",self.country)
        print("Taste",self.taste)


food1=food("biryani","2","India","good")
food2=food("ramen","4","Japan","tasty")

food1.revealursecrets()

food2.revealursecrets()