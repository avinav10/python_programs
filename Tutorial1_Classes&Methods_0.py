#a class is a blue print of object
# an object is a unique copy of class with same or diff data associated to it

#static metod---normal function inside a class used  it makes sense for the method to be present in class

class BDemo:

    name = "Avinav"
    age  = 10

    @staticmethod
    def display_info():
        print("Name", BDemo.name)
        print("age" , BDemo.age)


BDemo.display_info()

    