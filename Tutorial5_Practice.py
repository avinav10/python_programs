class Employee:

    def __init__(self,emp_id,emp_name,sal):

        self.emp_id = emp_id
        self.emp_name = emp_name
        self.sal =sal

    def display_info(self):
        print(self.emp_id,self.emp_name,self.sal)


s1 = Employee(7896, 'avinav', 898998)
s1.display_info()
