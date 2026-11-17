#내가 만든 거
#포켓몬 프로그램

import random

from model.pokemon import Pokemon, Pikachu, Charmander, Squirtle, Bulbasaur

def battle(attacker , defender):
    print(f"\n<\"{attacker}\"가 \"{defender}\"를 공격!>")
    defender.hp -= attacker.atk
    print("공격자:", attacker)
    print("수비자:", defender)

print("===== POKEMON GAME =====\n")

#포켓몬 객체
p1 = Pikachu()
p2 = Charmander()
p3 = Squirtle()
p4 = Bulbasaur()

#포켓몬 목록
print("----- pokemom list -----")
print([1], p1)
print([2], p2)
print([3], p3)
print([4], p4)
print("------------------------")

#유저 포켓몬 선택
user = None
num = int(input("선택한 포켓몬 번호: "))

match num:
    case 1:
        user = Pikachu()
    case 2:
        user = Charmander()
    case 3:
        user = Squirtle()
    case 4:
        user = Bulbasaur()

com = None
num = random.randint(1,4)
match num:
    case 1:
        com = Pikachu()
    case 2:
        com = Charmander()
    case 3:
        com = Squirtle()
    case 4:
        com = Bulbasaur()


while True:
#유저가 (컴퓨터) 공격
    battle(user , com)
    if com.hp <= 0: break
#컴퓨터가 (유저) 공격
    battle(com , user)
    if user.hp <= 0: break
