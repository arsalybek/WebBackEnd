from random import choice

#function for generating winner by user's number then return login by generated number


class User:
    def __init__(self, login, comment, number):
        self.login = login
        self.comment = comment
        self.number = number


def show_login(users, numb):
    for i in range(len(users)):
        if users[i].number == winner:
            return users[i].login


user1 = User("@aikerim", "Well Done", 123)
user2 = User("@carodaur", "Well Done", 124)
user3 = User("@maryleest", "Well Done", 125)
user4 = User("@_galieva", "Well Done", 126)
users = [user1, user2, user3, user4]
users_number = [user1.number, user2.number, user3.number, user4.number]


def choose_winner_by_number(users):
    return choice(users)


winner = choose_winner_by_number(users_number)
print(show_login(users, winner))
