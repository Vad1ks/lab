class User:
    users = []
    userID = 1

    def __init__(self, name="Not filled", phoneNumber="Not filled", email="Not filled"):
        self.userID = User.userID
        self.name = name
        self.phoneNumber = phoneNumber
        self.email = email
        User.users.append(self)
        User.userID += 1

    def __str__(self):
        return f"userID = {self.userID};\nname = {self.name};\nphoneNumber: {self.phoneNumber};\nemail: {self.email};"

    def write_message(self, chatname, message):
        for chat in Chat.chatList:
            if chat.name == chatname:
                chat.messages.append(f"sent by: {self.userID}, message: {message}")

    @classmethod
    def get_all_users_count(cls):
        return len(cls.users)


class Address:
    def __init__(self, country="Not filled", city="Not filled", street="Not filled"):
        self.country = country
        self.city = city
        self.street = street

    def __str__(self):
        return f"\n\tCountry: {self.country}\n\tCity: {self.city}\n\tStreet: {self.street}\n"


class Student(User):
    students = []

    def __init__(self, name="Not filled", phoneNumber="Not filled", email="Not filled"):
        super().__init__(name, phoneNumber, email)
        self.address = Address()
        self.marks = []
        Student.students.append(self)

    def __str__(self):
        return f"{super().__str__()} \navgMark: {self.get_average_mark():.2f}\nAddress: {self.address}"

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

    def get_student_info(self):
        return self.__str__()


class Group:
    groups = []

    def __init__(self, name):
        self.name = name
        self.studentsList = []
        Group.groups.append(self)

    def get_average_mark(self):
        marksum = 0
        for student in self.studentsList:
            marksum += student.get_average_mark()
        return marksum / len(self.studentsList)

    def get_students_count(self):
        return len(self.studentsList)

    def add_student(self, *students):
        for student in students:
            self.studentsList.append(student)

    def show_studentsList(self):
        for student in self.studentsList:
            print("\tID | Name")
            print(f"\t{student.userID}  | {student.name}")


class Professor(User):
    professors = []

    def __init__(self, name="Not filled", phoneNumber="Not filled", email="Not filled", subject="Not filled"):
        super().__init__(name, phoneNumber, email)
        self.subject = subject
        self.address = Address()
        Professor.professors.append(self)

    def __str__(self):
        return f"{super().__str__()} \navgMark: {self.subject}\nAddress: {self.address}"

    def create_chat(self, chatname):
        tempchat = Chat(chatname)
        tempchat.add_user(self)
        Chat.chatList.append(tempchat)


class Chat:
    chatID = 1
    chatList = []

    def __init__(self, name):
        self.chatID = Chat.chatID
        self.name = name
        self.users = []
        self.messages = []
        Chat.chatList.append(self)

    def add_user(self, *users):
        for user in users:
            self.users.append(user)

    def show_all_messages(self):
        print(self.messages)


if __name__ == "__main__":
    s = Student("Vadym", "0508271003", "vadiksosnovenko@gmail.com")
    s.add_marks(4, 4, 5, 4)
    print(s)

    g = Group("NEWGROUP")
    g.add_student(s)
    print(f"There are {g.get_students_count()} student(s) in group {g.name}:")
    g.show_studentsList()
    print(f"The average mark of students is {g.get_average_mark()}")

    u = User()
    c = Chat("test")
    u.write_message("test", "Hello")
    c.show_all_messages()
