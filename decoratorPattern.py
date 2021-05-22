class Student:

    def operation(self) -> str:
        pass

    def getEstimatedTime(self) -> str:
        pass


class DiplomaProjStudent(Student):

    def operation(self) -> str:
        return "I am doing my homework(Diploma Project)"

    def getEstimatedTime(self) -> str:
        return "I need 2 months"


class CourseProjStudent(Student):

    def operation(self) -> str:
        return "I am doing my homework(Course Project)"

    def getEstimatedTime(self) -> str:
        return "I need 2 weeks"

class LabStudent(Student):

    def operation(self) -> str:
        return "I am doing my homework(lab)"

    def getEstimatedTime(self) -> str:
        return "I need 2 days"

class Decorator(Student):

    _component: Student = None

    def __init__(self, component: Student) -> None:
        self._component = component

    @property
    def component(self):

        return self._component

    def operation(self) -> str:
        return self._component.operation()

    def getTime(self) -> str:
        return self._component.getEstimatedTime()


class ConcreteDecoratorDiploma(Decorator):

    def operation(self) -> str:
        return f"{self.component.operation()}, {self.component.getEstimatedTime()}." \
               f"It is decorator for students, who are doing diploma project"


class ConcreteDecoratorCourseProj(Decorator):

    def operation(self) -> str:
        return f"{self.component.operation()}, {self.component.getEstimatedTime()}." \
               f"It is decorator for students, who are doing course project"

class ConcreteDecoratorLab(Decorator):

    def operation(self) -> str:
        return f"{self.component.operation()}, {self.component.getEstimatedTime()}." \
               f"It is decorator for students, who are doing labs"

def client_code(component: Student) -> None:

    print(f"RESULT: {component.operation()}", end="")


if __name__ == "__main__":
    stud = DiplomaProjStudent()
    print("Client: I've got a simple component:")
    client_code(stud)
    print("\n")

    decorator1 = ConcreteDecoratorDiploma(stud)
    print("Client: Now I've got a decorated component:")
    client_code(decorator1)
