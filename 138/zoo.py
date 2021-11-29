class Animal:

    _zoo = {}
    _last_id = 10000

    def __init__(self, name: str):
        self.name = name.title()
        self.id = self.__class__._last_id + 1
        self.__class__._last_id = self.id
        self.__class__._zoo[self.id] = self

    def __str__(self):
        return f"{self.id}. {self.name}"

    @classmethod
    def zoo(cls):
        return "\n".join([str(animal) for animal in cls._zoo.values()])
