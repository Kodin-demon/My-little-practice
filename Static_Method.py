
class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def pers_info(self):
        return f"{self.name} at a position {self.position}"

    @staticmethod
    def is_valid_position(position):
        valid_position = ["Operator", "Janitor", "Programmer", "Jester"]
        return position in valid_position

employee_001 = Employee("Stanford","Operator")
employee_002 = Employee("Zeus","Janitor")
employee_003 = Employee("Billy","Jester")

position_valid = Employee.is_valid_position("Adventurer")

if position_valid:
    print("You have a valid position")
else:
    print("You dont have a valid position")

print(employee_001.pers_info())
print(employee_002.pers_info())
print(employee_003.pers_info())
