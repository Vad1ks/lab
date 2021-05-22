from abc import ABC, abstractmethod


class AbstractClass(ABC):

    def template_method(self) -> None:

        self.base_operation1()
        self.convertToPDF()
        self.base_operation2()
        self.convertToDocx()
        self.base_operation3()

    def base_operation1(self) -> None:
        print("AbstractClass says: I am converting file")

    def base_operation2(self) -> None:
        print("AbstractClass says: But I let convert too different formats")

    def base_operation3(self) -> None:
        print("AbstractClass says: But I am converting file anyway")


    @abstractmethod
    def convertToPDF(self) -> None:
        pass

    @abstractmethod
    def convertToDocx(self) -> None:
        pass


class ConcreteClass1(AbstractClass):

    def convertToPDF(self) -> None:
        print("ConcreteClass2: starting convertation process")
        print("ConcreteClass2: Implemented PDF convertation")
        print("ConcreteClass2: convertation process finished")

    def convertToDocx(self) -> None:
        print("ConcreteClass2: starting convertation process")
        print("ConcreteClass2: Implemented DOCX convertation")
        print("ConcreteClass2: convertation process finished")


class ConcreteClass2(AbstractClass):

    def convertToPDF(self) -> None:
        print("ConcreteClass2: starting convertation process")
        print("ConcreteClass2: Implemented PDFv2.0 convertation")
        print("ConcreteClass2: convertation process finished")

    def convertToDocx(self) -> None:
        print("ConcreteClass2: starting convertation process")
        print("ConcreteClass2: Implemented DOCXv2.0 convertation")
        print("ConcreteClass2: convertation process finished")


def client_code(abstract_class: AbstractClass) -> None:
    abstract_class.template_method()


if __name__ == "__main__":
    print("Same client code can work with different subclasses:")
    client_code(ConcreteClass1())
    print("")

    print("Same client code can work with different subclasses:")
    client_code(ConcreteClass2())