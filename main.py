class User:
    userID = 1

    def __init__(self, name, phoneNumber, email):
        self.userID = User.userID
        self.name = name
        self.phoneNumber = phoneNumber
        self.email = email
        User.userID += 1


class Address:
    def __init__(self, country, city, street):
        self.country = country
        self.city = city
        self.street = street

    def __str__(self):
        return f"\n\tCountry: {self.country}\n\tCity: {self.city}\n\tStreet: {self.street}\n"


class Student(User):
    def __init__(self, name, phoneNumber, email):
        super().__init__(name, phoneNumber, email)
        self.address = Address(country="Not filled", city="Not filled", street="Not filled")
        self.marks = []

    def __str__(self):
        return f"userID = {self.userID};\nname = {self.name};\nphoneNumber: {self.phoneNumber};\nemail: {self.email};\
        \navgMark: {self.get_average_mark():.2f}\nAddress: {self.address}"

    def set_address(self, country, city, street):
        self.address.country = country
        self.address.city = city
        self.address.street = street

    def add_marks(self, *marks):
        for mark in marks:
            self.marks.append(mark)

    def get_average_mark(self):
        marksum = 0
        for mark in self.marks:
            marksum += mark
        return marksum / len(self.marks)

class StudentsGroup:
    #average mark
    def __init__(self, name):
        self.name = name
        self.studentsList = []


class Professor(User):
    def __init__(self, name, phoneNumber, email, subject):
        super().__init__(name, phoneNumber, email)
        self.subject = subject

    def __str__(self):
        return str("")


class Chat:
    pass


if __name__ == "__main__":
    s = Student("Vadym", "0508271003", "vadiksosnovenko@gmail.com")
    s.add_marks(4, 4, 5, 4)
    print(s)
