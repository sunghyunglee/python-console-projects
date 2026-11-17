#포켓몬 프로그램

import random

from model.pokemon import Pokemon, Pikachu, Charmander, Squirtle, Bulbasaur

user = None
com = None


print("===== POKEMON GAME =====\n")


def print_pokemon_list():
    print("----- pokemon list -----")
    print("1." , Pikachu())
    print("2." , Charmander())
    print("3." , Squirtle())
    print("4." , Bulbasaur())
    print("------------------------")



def select_user_pokemon():
    global user
    while True:
        num = int(input("선택한 포켓몬 번호: "))
        print()
        match num:
            case 1:
                user = Pikachu()
            case 2:
                user = Charmander()
            case 3:
                user = Squirtle()
            case 4:
                user = Bulbasaur()
            case _:
                print("잘못 입력하셨습니다.")
                continue
        break



def select_com_pokemon():
    global com
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



def attack(attacker , defender, num):
# 동작 수행
    match num:
        case 1:
            attacker.tackle(defender)
        case 2:
            attacker.skill(defender)
#정보 출력
    print()
    print("attacker:",attacker)
    print("defender:",defender)
    print()
# 결과 판단
    result = com.is_dead()
    if result:
        print(f"[--- {user.name}의 승리! ---]")
        print("\n게임을 종료합니다.")
        return True



def battle_start():
    while True:
# 사용자 차례
        print("----- 동작 선택 -----")
        print("1. 몸통박치기")
        print("2. 스킬")
        print("--------------------")
        num = int(input("동작 번호: "))
        print()
        attack(user, com, num)
        is_finish = attack(user, com, num)
        if is_finish: break
# 컴퓨터 차례
        num = random.randint(1, 2)
        is_finish = attack(attacker=com, defender=user, num=num)
        if is_finish: break



def play_game():
    print("===== POKEMON =====")
print_pokemon_list()
select_user_pokemon()
select_com_pokemon()
battle_start()
