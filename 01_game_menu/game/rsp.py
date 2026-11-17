#가위바위보 게임

import random

# 컴퓨터의 선택지 준비하기
choice = ["가위", "바위", "보"]

def judgeRSP(computer, user):
    print("\n------------------------------------------")
    print(f"\n 사용자: {user} vs 컴퓨터: {computer}\n")
    print("------------------------------------------\n")

# 판단하기 및 결과 출력
    if user == computer:
        print("(비겼습니다! 다시 시도하시오)\n")
        return False
    elif (user == "가위" and computer == "보") or \
            (user == "바위" and computer == "가위") or \
            (user == "보" and computer == "바위"):
        print("(승리했습니다!) \n[게임을 종료합니다]")
        return True
    else:
        print("(패배했습니다!) \n[게임을 종료합니다]")
        return True


#playRSP() 함수로 감싸기 <for main 게임 메뉴 프로그램>
def playRSP():

# main에서 의도치 않게 먼저 출력 에러 해결
    print("\n === 가위바위보 게임 프로그램 ===\n")

    print("[가위, 바위, 보 중 하나를 입력하세요]")

    while True:
# 매 라운드마다 컴퓨터가 새로운 선택을 함
        computer_choice = random.choice(choice)

        user_choice = input("입력: ").strip()

#강제 종료 명령어 처리
        if user_choice in ["종료"]:
            print("\n[게임을 강제 종료합니다.]")
            break

# 잘못된 입력 처리
        if user_choice not in choice:
            print("'가위', '바위', '보' 중에서만 입력해주세요.\n")
            continue

# 승패를 판단하고, 승/패가 결정되면 반복문 종료 (비기면 계속)
        if judgeRSP(computer_choice, user_choice):
            break


#여기서 게임 실행하기
if __name__ == "__main__":
    playRSP()
