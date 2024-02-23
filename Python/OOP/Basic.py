class main():

    attr1 = "mammal"

    def __init__ (self,name):
        self.name = name

    def speak(self):
        print("My is name {}".format(self.name))

Roger = main("Roger")
Tommy = main("Tommy")

Roger.speak()
Tommy.speak()