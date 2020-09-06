from abc import ABCMeta, abstractmethod
import random


class Animal(metaclass=ABCMeta):

    def __init__(self, genre: str, shape: str, personality: str):
        '''
        genre 类型
        shape 体型 
              1..10表示 数值越大，体型越大
              5 中等 默认
        personality 性格
        '''
        self.genre = genre
        self.personality = personality
        self.shape = shape

    @property
    def shape(self):
        if self.shape < 5:
            return '小'
        elif self.shape == 5:
            return '中'
        elif self.shape > 5:
            return '大'

    @shape.setter
    def shape(self, shape: str):
        if shape == '小':
            self.__shape = random.randint(1, 4)
        elif shape == '大':
            self.__shape = random.randint(6, 10)
        else:
            self.__shape = 5

    @property
    def ferocity(self):
        return self.genre == '食肉' and self.personality == '凶猛' and self.__shape >= 5

    @abstractmethod
    def overview(self):
        pass


class Cat(Animal):
    cry = '喵喵'

    def __init__(self, name: str, genre: str, shape: int, personality: str):
        super().__init__(genre, shape, personality)
        self.name = name
        self.pet = not self.ferocity

    def overview(self):
        if self.pet:
            return f'我是喵喵界：{self.name}，快来领养！！！'
        else:
            return f'我是故宫御猫：{self.name}，请勿投喂！！！'

    def __str__(self):
        return self.overview()


class Zoo(object):

    def __init__(self, name: str):
        self.name = name
        self.__animal = {}

    def __getattribute__(self, name):
        try:
            return super().__getattribute__(name)
        except Exception:
            if name in self.__animal:
                return self.__animal[name]
            else:
                self.__animal[name] = {}
                return self.__animal[name]

    def add_animal(self, animal: Animal):
        animalclass = type(animal).__name__
        animalname = animal.name
        if animalclass in self.__animal:
            self.__animal[animalclass][animalname] = animal
        else:
            self.__animal[animalclass] = {}
            self.__animal[animalclass][animalname] = animal


if __name__ == '__main__':
    zoo = Zoo('时间动物园')
    cat1 = Cat('鳌拜', '食肉', '大', '凶猛')
    cat2 = Cat('瘪小三', '食肉', '小', '温顺')
    zoo.add_animal(cat1)
    zoo.add_animal(cat2)
    zoo.add_animal(cat1)
    cats = getattr(zoo, 'Cat')
    for cat in cats.values():
        print(cat)