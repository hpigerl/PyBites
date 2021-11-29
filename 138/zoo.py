class Animal:

    zoo_dict = {}

    def __init__(self, name: str):
        self.name = name.title()

        if len(self.__class__.zoo_dict) == 0:
            self.id = 10001
        else:
            self.id = max(self.__class__.zoo_dict) + 1

        self.__class__.zoo_dict[self.id] = self

    def __str__(self):
        return f"{self.id}. {self.name}"

    @classmethod
    def zoo(cls):
        return "\n".join([animal.__str__() for animal in cls.zoo_dict.values()])
