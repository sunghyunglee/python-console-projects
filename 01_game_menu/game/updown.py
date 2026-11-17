#업다운 게임

import random

#정답(랜덤)숫자 준비하기
answer = random.randint(1, 50)

def judgeUpDown(answer , num):
    if answer > num:   #판단하기 및 결과출력
        print("\n------------------------------------------")
        print("(up)")
        print("------------------------------------------\n")
        return False
    elif answer < num:
        print("\n------------------------------------------")
        print("(down)")
        print("------------------------------------------\n")
        return False
    else:
        print("\n------------------------------------------")
        print(f"(fuck)")
        print("------------------------------------------\n")
        print("[게임을 종료합니다]\n")
        return True


#playUpDown() 함수로 감싸기 <for main 게임 메뉴 프로그램>
def playUpDown():

# main에서 의도치 않게 먼저 출력 에러 해결
    print("\n === 업다운 게임 프로그램 ===\n")

    print("[1부터 50 사이의 숫자를 맞춰보세요]")

#quit_game 변수 초기화
    quit_game = False

    while True:
        user_num = int(input("숫자 입력: "))

# 강제 종료 처리
        if user_num == 0:
            print("\n[게임을 중단합니다! 메인 메뉴로 돌아갑니다]")
            quit_game = True
            break

# 범위 체크: 1 미만이거나 50 초과인 경우 경고
        if user_num < 1 or user_num > 50:
            print("\n<1부터 50 사이의 숫자만 입력해 주세요!>\n")
            continue

# 범위 내의 올바른 숫자인 경우에만 판단 진행
        if judgeUpDown(answer, user_num):
            break


# 강제 종료가 눌렸다면 바깥 while문도 탈출
        if quit_game:
            break


#여기서 게임 실행하기
if __name__ == "__main__":
    playUpDown()
