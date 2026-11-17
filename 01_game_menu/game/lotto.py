#로또번호 게임

import random

# 정답 로또 번호 준비하기 (중복 없음)
answer_numbers = sorted(random.sample(range(1, 46), 6))

def judgeLotto(answer, user_numbers):
    matched = sorted(list(set(answer) & set(user_numbers)))

# 판단하기 및 결과 출력
    if len(matched) == 6:
        print(f"\n(정답입니다! 로또 번호 6개를 모두 맞추셨습니다)")
        print(f"최종 번호: {answer}")
        print("[게임을 종료합니다]")
        return True
    else:
        print("\n------------------------------------------")
        print(f"내가 입력한 번호: {sorted(user_numbers)}")
        print(f"(현재 맞춘 번호 {len(matched)}개: {matched})")
        print("<아직 틀렸습니다! 다시 시도해보세요>")
        print("------------------------------------------\n")
        return False


#playLotto() 함수로 감싸기 <for main 게임 메뉴 프로그램>
def playLotto():

# main에서 의도치 않게 먼저 출력 에러 해결
    print("\n === 로또 번호 맞추기 게임 프로그램 ===\n")

    print("[1부터 45 사이의 숫자 6개를 맞춰보세요]")

#quit_game 변수 초기화
    quit_game = False

    while True:
        user_numbers = []

# 6개의 숫자를 한 개씩 반복 입력 받기
        while len(user_numbers) < 6:
            try:
                num = int(input(f"{len(user_numbers) + 1}. 숫자 입력: "))

# 강제 종료 처리
                if num == 0:
                    print("\n[게임을 중단합니다! 메인 메뉴로 돌아갑니다]")
                    quit_game = True
                    break

# 범위 예외 처리
                if num < 1 or num > 45:
                    print("<1부터 45 사이의 숫자만 입력해주세요.>\n")
                    continue

# 중복 입력 예외 처리
                if num in user_numbers:
                    print("<이미 입력한 숫자입니다. 다른 숫자를 입력해주세요.>\n")
                    continue

                user_numbers.append(num)

            except ValueError:
                print("<숫자만 입력해주세요.>\n")


# 강제 종료가 눌렸다면 바깥 while문도 탈출
        if quit_game:
            break
# 6개 숫자를 모두 입력받은 후 비교 판단
        if judgeLotto(answer_numbers, user_numbers):
            break


#여기서 게임 실행하기
if __name__ == "__main__":
    playLotto()

