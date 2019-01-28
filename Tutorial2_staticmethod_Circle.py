
class Circle:

    pi = 3.14
    r  = 5

    @staticmethod
    def Circumference_of_Circle():
        cir = 2*Circle.pi*Circle.r
        print("Circumference of Circle =", cir)

    @staticmethod
    def Area_of_Circle():
        area = Circle.pi * Circle.r * Circle.r
        print("Area of Circle =", area)

Circle.Circumference_of_Circle()
Circle.Area_of_Circle()