from abc import ABC, abstractmethod


class Hero:
    def __init__(self):
        self.positive_effects = []
        self.negative_effects = []
        self.stats = {
            "HP": 128,  # health points
            "MP": 42,  # magic points,
            "SP": 100,  # skill points
            "Strength": 15,  # сила
            "Perception": 4,  # восприятие
            "Endurance": 8,  # выносливость
            "Charisma": 2,  # харизма
            "Intelligence": 3,  # интеллект
            "Agility": 8,  # ловкость
            "Luck": 1  # удача
        }

    def get_positive_effects(self):
        return self.positive_effects.copy()

    def get_negative_effects(self):
        return self.negative_effects.copy()

    def get_stats(self):
        return self.stats.copy()


class AbstractEffect(Hero, ABC):
    def __init__(self, obj):
        self.base = obj

    def get_positive_effects(self):
        return self.base.get_positive_effects()

    def get_negative_effects(self):
        return self.base.get_negative_effects()

    def get_stats(self):
        return self.base.get_stats()

    def add_positive(self, effect):
        try:
            self.base.positive_effects.append(effect)
        except AttributeError:
            self.base.add_positive(effect)

    def add_negative(self, effect):
        try:
            self.base.negative_effects.append(effect)
        except AttributeError:
            self.base.add_negative(effect)


class AbstractPositive(AbstractEffect):
    def __init__(self, obj, effect):
        super().__init__(obj)
        self.add_positive(effect)


class AbstractNegative(AbstractEffect):
    def __init__(self, obj, effect):
        super().__init__(obj)
        self.add_negative(effect)


class Berserk(AbstractPositive):
    def __init__(self, obj):
        super().__init__(obj, self.__class__.__name__)


class Blessing(AbstractPositive):
    def __init__(self, obj):
        super().__init__(obj, self.__class__.__name__)


class Weakness(AbstractNegative):
    def __init__(self, obj):
        super().__init__(obj, self.__class__.__name__)


class Curse(AbstractNegative):
    def __init__(self, obj):
        super().__init__(obj, self.__class__.__name__)


class EvilEye(AbstractNegative):
    def __init__(self, obj):
        super().__init__(obj, self.__class__.__name__)


h = Hero()
m1 = Berserk(h)
m2 = Berserk(m1)
m3 = EvilEye(m2)
print(m3.get_positive_effects())
print(m3.get_negative_effects())

m3.base = m1
print(m3.get_positive_effects())
print(m3.get_negative_effects())
