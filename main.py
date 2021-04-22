class User:
    userID = 1

    def __init__(self, name, phoneNumber, email):
        self.userID = User.userID
        self.name = name
        self.phoneNumber = phoneNumber
        self.email = email
        User.userID += 1


class Student(User):
    pass


class Professor(User):
    pass


class Chat:
    pass