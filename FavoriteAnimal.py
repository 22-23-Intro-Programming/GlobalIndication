class BaldEagle:

    def __init__(self, name, age):
        self.age = age
        self.name = name
        self.wingspan = "7 feet"
        self.height = "3 feet"

    def getAge (self):
        return self.age
    def getName(self):
        return self.name
    def getWingspan(self):
        return self.wingspan
    def getHeight(self):
        return self.height



def main():

    BE = BaldEagle("Hunter", 15)
    FE = BaldEagle("Bob", 2)

    print("Hi Bald Eagle, what is your name?")
    print(BE.getName())

    print("How old are you?")
    print(BE.getAge())

    print("How long is your wingspan?")
    print(BE.getWingspan())

    print("How tall are you?")
    print(BE.getHeight())

    print("Hi other Bald Eagle, what is your name?")
    print(FE.getName())

    print("How old are you?")
    print(FE.getAge())





if __name__ == "__main__":
    main()
