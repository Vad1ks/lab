class User:
    userID = 1

    def __init__(self, name, phoneNumber, email):
        self.userID = User.userID
        self.name = name
        self.phoneNumber = phoneNumber
        self.email = email
        User.userID += 1


class Student(User):
    def __init__(self, name, phoneNumber, email, *marks):
        super().__init__(name, phoneNumber, email)
        marksum = 0
        for mark in marks:
            marksum += mark
        self.averageMark = marksum / len(marks)

    def __str__(self):
        return str("userID = %i;\nname = %s;\nphoneNumber: %s;\nemail: %s;\navgMark: %.2f" % (
        self.userID, self.name, self.phoneNumber, self.email, self.averageMark))


class Professor(User):
    pass


class Chat:
    pass


if __name__ == "__main__":
    s = Student("Vadym", "0508271003", "vadiksosnovenko@gmail.com", 5, 4, 5, 5, 4)
    print(s)
