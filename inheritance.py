# -------------------------
# Exercise on Inheritance:
# -------------------------
# 1. Create a base class named Employee as follows:
# Employee (
# -- class variables and methods
# 	organisation_name, 
# 	get_organisation_name(),
# 	set_organisation_name(org_name)

# -- instance variables and methods()
# emp_id,
# name,
# base_location,
# deployed_location,
# designation,
# salary ,
# get_employee_details() 	



# Create a subclass of Employee named Manager as follows:
# Manager(
	
# 	-- instance variables and methods()
# 	managed_employees[], # this is list of emp_references
# 	perform_appraisal_for_an_employee(emp_reference,percent_raise),
# 	get_manager_details()
# )

# Write a main method that does the following:
# create 3 objects of Employee 
# create an object of Manager_class and add the above 3 employee objects created as managed employees 
# display get_manager_details()
# for an employee do perform_appraisal_for_an_employee()


# class Employee:
#     organisation_name = "XYZ Company"

#     def __init__(self, emp_id, name, base_location, deployed_location, designation, salary):
#         self.emp_id = emp_id
#         self.name = name
#         self.base_location = base_location
#         self.deployed_location = deployed_location
#         self.designation = designation
#         self.salary = salary

#     def get_organisation_name(self):
#         return self.organisation_name

#     def set_organisation_name(self, org_name):
#         self.organisation_name = org_name

#     def get_employee_details(self):
#         return f"Employee ID: {self.emp_id}, Name: {self.name}, Designation: {self.designation}, Salary: {self.salary}"


# class Manager(Employee):
#     def __init__(self, emp_id, name, base_location, deployed_location, designation, salary):
#         super().__init__(emp_id, name, base_location, deployed_location, designation, salary)
#         self.managed_employees = []

#     def perform_appraisal_for_an_employee(self, emp_reference, percent_raise):
#         for employee in self.managed_employees:
#             if employee.emp_id == emp_reference.emp_id:
#                 employee.salary *= (1 + percent_raise / 100)
#                 return f"Appraisal successful. New salary for {employee.name}: {employee.salary}"
#         return "Employee not found."

#     def get_manager_details(self):
#         employee_details = "\n".join(emp.get_employee_details() for emp in self.managed_employees)
#         return f"Manager Details:\n{employee_details}"


# def main():
#     emp1 = Employee(1, "John", "HQ", "HQ", "Developer", 50000)
#     emp2 = Employee(2, "Alice", "HQ", "Branch", "Designer", 60000)
#     emp3 = Employee(3, "Bob", "HQ", "Remote", "Engineer", 55000)

#     manager = Manager(4, "Manager Name", "HQ", "HQ", "Manager", 80000)
#     manager.managed_employees.extend([emp1, emp2, emp3])

#     print(manager.get_manager_details())
#     print(manager.perform_appraisal_for_an_employee(emp2, 10))


# if __name__ == "__main__":
#     main()

# 2. Define  
#   Person (superclass) that has name , place_of_residence , display_attributes()
#   Sister (subclass of Person)  that has additionally exam_subjects , display_attributes()
#   Uncle (subclass of Persom)  that has additionally business , display_attributes()

# main method:
# create a sister class object and display its attributes 
# create a Uncle class object and display its attributes 

class Person:
    def __init__(self, name, place_of_residence):
        self.name = name
        self.place_of_residence = place_of_residence

    def display_attributes(self):
        return f"Name: {self.name}, Place of Residence: {self.place_of_residence}"


class Sister(Person):
    def __init__(self, name, place_of_residence, exam_subjects):
        super().__init__(name, place_of_residence)
        self.exam_subjects = exam_subjects

    def display_attributes(self):
        return f"Name: {self.name}, Place of Residence: {self.place_of_residence}, Exam Subjects: {self.exam_subjects}"


class Uncle(Person):
    def __init__(self, name, place_of_residence, business):
        super().__init__(name, place_of_residence)
        self.business = business

    def display_attributes(self):
        return f"Name: {self.name}, Place of Residence: {self.place_of_residence}, Business: {self.business}"


def main():
    sister = Sister("Emily", "New York", ["Mathematics", "Physics", "English"])
    uncle = Uncle("Michael", "Los Angeles", "Restaurant")

    print("Sister's Attributes:")
    print(sister.display_attributes())

    print("\nUncle's Attributes:")
    print(uncle.display_attributes())


if __name__ == "__main__":
    main()
