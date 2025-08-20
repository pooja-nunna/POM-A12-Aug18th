# class Employee:
#
#     c_name = 'tesla'                        ## class variable
#
#     def __init__(self, name, emp_id):       ## object variable
#         self.name = name
#         self.emp_id = emp_id
#
#     def greet(self):
#         print(f"Hello {self.name}, Your emp_id is {self.emp_id}. Welcome to {self.c_name}")
#
#     def email_id(self):
#         print(f'Your email-id is = {self.name}_{self.emp_id}@{self.c_name}.com')
#         print("=====================================================================================")
#
# emp1 = Employee('Ankitha', '101')
# emp1.greet()
# emp1.email_id()
#
# emp2 = Employee('Ajay', '002')
# emp2.greet()
# emp2.email_id()
#
# emp3 = Employee('Sweeta', '003')
# emp3.greet()
# emp3.email_id()
#
# emp4 = Employee("Gayathri", '004')
# emp4.greet()
# emp4.email_id()



####################################################################################################

# class Sample:
#
#     def __init__(self, name):
#         self.name = name
#
# s_obj = Sample('Sujitha')

##########################################################################

name = 'Sujitha'

class Sample:

    def __init__(self, name):
        self.name = name        ## self.name --> name = Sujitha

    def display(self):
        print(self.name)


s_obj = Sample(name)
s_obj.display()

































