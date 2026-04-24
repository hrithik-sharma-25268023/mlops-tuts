"""Employee Class Example"""

class Employee:
    """class Employee"""

    def __init__(self):
        self.id = 123
        self.salary = 50000 
        self.designation = "SDE"

    def travel(self, place):
        return f"Employee is now travelling to {place}."

if __name__ == "__main__":
    
    sam = Employee()
    print(f"ID:- {sam.id}, Salary:- {sam.salary}, Designation:- {sam.designation}")
    print(sam.travel("Dublin"))