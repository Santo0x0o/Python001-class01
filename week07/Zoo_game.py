from abc import ABCMeta, abstractmethod


class Zoo(object):
    def __init__(self, name):
        self.name = name
        self.animals = {}

    def add_animal(self, animal):

        if id(animal) in self.animals:
            print(
                f'Error: {type(animal).__name__} {id(animal)} already in the zoo!')

        else:
            self.animals[id(animal)] = animal
            if not hasattr(self, type(animal).__name__):
                setattr(self, type(animal).__name__, [animal])

            print(f'Added {type(animal).__name__} {id(animal)} to the zoo.')


class Animal(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self, ani_type, size, character):
        self.ani_type = ani_type
        self.size = size
        self.character = character

    @property
    def is_ferocious(self):
        if self.ani_type == '食肉' and self.character == '凶猛' and (self.size == '中' or self.size == '大'):
            return True
        else:
            return False


class Cat(Animal):
    cry = 'miaow~'

    def __init__(self, name, ani_type, size, character):
        self.name = name
        super(Cat, self).__init__(ani_type, size, character)

    @property
    def for_pet(self):
        return not self.is_ferocious


if __name__ == '__main__':
    # 实例化动物园
    z = Zoo('时间动物园')
    # 实例化一只猫，属性包括名字、类型、体型、性格
    cat1 = Cat('大花猫 1', '食肉', '小', '温顺')
    # 增加一只猫到动物园
    z.add_animal(cat1)
    # 动物园是否有猫这种动物
    have_cat = getattr(z, 'Cat')
    print(f'Q: Have Cat in the Zoo? A: {bool(have_cat)}')
    print(f'Q: What is the cry of that cat? A: {cat1.cry}')
    print(f'Q: If this cat can feed for pet? A: {cat1.for_pet}')
    print(f'Q: What is the type of this animal? A: {cat1.ani_type}')
    print(f'Q: What is the size of this cat? A: {cat1.size}')
    print(f'Q: What is the character of this cat? A: {cat1.character}')
    print(f'Q: If this is a ferocious animal? A: {cat1.is_ferocious}')
    # 尝试再增加同一只猫
    z.add_animal(cat1)
