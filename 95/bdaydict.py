from datetime import date

MSG = "Hey {}, there are more people with your birthday!"


class BirthdayDict(dict):
    """Override dict to print a message every time a new person is added that has
    the same birthday (day+month) as somebody already in the dict"""

    # def __init__(self):
    #     super(BirthdayDict, self).__init__()

    def __setitem__(self, name: str, birthday: date):
        if any(
            [birthday.day == bday.day and birthday.month == bday.month for bday in self.values()]
        ):
            print(MSG.format(name))
        super(BirthdayDict, self).__setitem__(name, birthday)
