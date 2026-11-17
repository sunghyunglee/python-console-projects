#포켓몬 프로그램

from abc import abstractmethod, ABC

class Pokemon(ABC):
    def __init__(self, name , max_hp , atk, ar):
        self.name = name
        self.max_hp = max_hp
        self.hp = self.max_hp
        self.atk = atk
        self.ar = ar

    def __str__(self):
        return f"{self.name} ({self.hp}/{self.max_hp}) {self.atk} {self.ar}"

    def tackle(self , enemy):
        print("<몸통 박치기!>")
        dmg = self.atk - enemy.ar
        if dmg < 1: dmg = 1
        enemy.hp -= dmg

    @abstractmethod
    def skill(self , enemy):
        pass

    def bark(self):
        print("~~~~")

    def is_dead(self):
        return self.hp <= 0



#상속
class Pikachu(Pokemon):
    def __init__(self):
        super().__init__(name="피카츄", max_hp=100, atk=10, ar=5)

    # def __init__(self, name, max_hp, atk: int=0, ar: int=0):
    #     super().__init__(name="name", max_hp=max_hp, atk=atk, ar=ar)

    def bark(self):
        print("피카피카~")

    def skill(self , enemy  ):
        print("<백만볼트!>")
        dmg = self.atk * 2 - enemy.ar
        enemy.hp -= dmg


class Charmander(Pokemon):
    def __init__(self):
        super().__init__(name="파이리", max_hp=80, atk=12, ar=5)

    def bark(self):
        print("파이리이~")

    def skill(self , enemy  ):
        print("<불꽃세례!>")
        dmg = self.atk * 3 - enemy.ar
        enemy.hp -= dmg


class Squirtle(Pokemon):
    def __init__(self):
        super().__init__(name="꼬부기", max_hp=90, atk=11, ar=6)

    def bark(self):
        print("꼬북꼬북~")

    def skill(self, enemy   ):
        print("<물대포!>")
        dmg = self.atk * 2 - enemy.ar
        enemy.hp -= dmg
        self.hp += round(dmg * 0.3 , 0)


class Bulbasaur(Pokemon):
    def bark(self):
        print("이상이상~")

    def __init__(self):
        super().__init__(name="이상해씨", max_hp=90, atk=9, ar=7)

    def bark(self):
        print("이상이상~")

    def skill(self, enemy   ):
        print("<덩출채찍!>")
        dmg = self.atk * 2 - enemy.ar
        enemy.hp -= dmg
