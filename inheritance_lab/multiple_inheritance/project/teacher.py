from project.employee import Employee
from project.person import Person


class Teacher(Person, Employee):
    def teach(self):
        return "teaching..."

# teacher = Teacher()
# print(teacher.teach())
# print(teacher.sleep())
# print(teacher.get_fired())
#
# employee = Employee()
# print(employee.get_fired())
#
# person = Person()
# print(person.sleep())