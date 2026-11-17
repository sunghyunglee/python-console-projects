#게임 불러오기
from game.updown import playUpDown
from game.rsp import playRSP
from game.lotto import playLotto


#게임 모음

print("\n === 게임 메뉴 프로그램 ===\n")

# 게임 메뉴
while True:

#메뉴 출력
    print("--------------------")
    print("1. 업다운 게임")
    print("2. 가위바위보 게임")
    print("3. 로또번호맞추기 게임")
    print("0. 종료")
    print("--------------------\n")


#선택 입력받기
    menu = int(input("메뉴 선택: "))

    if menu == 1:
        playUpDown()
    elif menu == 2:
        playRSP()
    elif menu == 3:
        playLotto()
    elif menu == 0:
        break
