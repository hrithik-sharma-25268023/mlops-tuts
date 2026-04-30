"""OOPs Tut 2"""

class Employee:

    increment = 1.5   # Class Variable

    def __init__(self, fname: str, lname: str, salary: int):
        self.fname = fname       # Instance Variable
        self.lname = lname       # Instance Variable
        self.salary = salary     # Instance Variable

    def increase(self):
        self.salary = self.salary * Employee.increment

    @classmethod
    def change_increment(cls, amount):
        cls.increment = amount

    @classmethod
    def from_string(cls, emp_string):
        fname, lname, salary = emp_string.split("-")
        return cls(fname, lname, salary)
    
    
    @staticmethod
    def is_open(day):
        if day =='sunday':
            return False
        return True


class Programmer(Employee):
    
    def __init__(self, fname, lname, salary, prog_lang):
        super().__init__(fname, lname, salary)
        self.prog_lang = prog_lang
        


jacob = Programmer('Jacob', 'Marley', 75000, 'Python')
harry = Employee('Rohan', 'Das', 44000)
rohan = Employee('Harry', 'Jackson', 44000)
jane = Employee.from_string('jane-doe-74000')

print(jacob.__dict__)