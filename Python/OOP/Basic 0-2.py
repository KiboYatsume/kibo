class main(object):
    def __init__ (self,name,idnumber):
        self.name = name
        self.idnumber = idnumber
    
    def display(self):
        print(self.name)
        print(self.idnumber)

    def details(self):
        print("My name is".format(self.name))
        print("Idnumber{}".format(self.idnumber))

class employee(main):
    def __init__ (self,name,idnumber,salary,post):
        self.salary = salary
        self.post = post

        main.__init__(self,name,idnumber)

    def details(self):
        print("My Name is {}".format(self.name))
        print("Idnumber :{}".format(self.idnumber))
        print("Post:{}".format(self.post))

a = employee('Ajay',8768452,340000,'Intern')

a.display()
a.details()