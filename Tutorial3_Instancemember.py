class EDemo:
    a=10

    def a1(self):
        self.a=20
        print(" running a1 in Edemo class",self.a)

    def a2(self):
        print(" running a2 in Edemo class")

    @staticmethod
    def a3():
        a=20
        print("Static method call...", a)

ob = EDemo()

print("print ob", ob)

print(ob.a1())
print(ob.a2())

print("-------------------------")
ref = EDemo()

print(ref)
print(ref.a1())
print(ref.a2())
print(EDemo.a3())