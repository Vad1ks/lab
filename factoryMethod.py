from __future__ import annotations
from abc import ABC, abstractmethod

# абстрактний клас студентів
class Student(ABC):

    @abstractmethod
    def factory_method_make(self):
        pass

    def some_operation(self) -> str:
        product = self.factory_method_make()
        result = f"Creator: The same creator's code has just worked with {product.operation()}"

        return result


# робить курсову
class CourseProjectStudent(Student):

    def factory_method_make(self) -> Product:
        return CourseProject()


# робить розрахункову
class SettlementProjectStudent(Student):
    def factory_method_make(self) -> Product:
        return SettlementProject()

# абстрактний клас продуктів
class Product(ABC):

    @abstractmethod
    def operation(self) -> str:
        pass


class CourseProject(Product):
    def operation(self) -> str:
        return "I have done the course project"


class SettlementProject(Product):
    def operation(self) -> str:
        return "I have done the settlement!"


def client_code(creator: Student) -> None:
    print(f"Client: So, we have created an instance and it has done something.\n"
          f"{creator.some_operation()}", end="")


if __name__ == "__main__":
    print("App: Launched with the CourseProjectStudent.")
    client_code(CourseProjectStudent())
    print("\n")

    print("App: Launched with the SettlementProjectStudent.")
    client_code(SettlementProjectStudent())
