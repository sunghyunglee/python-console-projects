'''
- 퀴즈 프로그램 만들기 (주제 : 리눅스 명령어)
- 조건문,반복문,리스트 사용할 것
- 문제는 최소 5문제 이상 준비할 것
(문제로는 명령어의 설명을 주고, 정답은 명령어를 맞히도록)
- 5문제 중 랜덤으로 3문제 뽑아서 출제할 것
- 문제 유형은 모두 주관식으로 할 것
- 정답은 대소문자 구분없이 정답처리 가능하도록 할 것
- 정답을 못 맞추면, 바로 정답을 알려줄 것
- 마지막에 총 몇문제 맞추었는지 알려줄 것
- 맞춘 문제 수에 따라 등급 출력 (A,B,C,F)
- 게임 종료 후 재시도 할 수 있게 만들어줄 것
- 유저 입력으로 게임을 그만할 수 있게 만들어줄 것 (프로세스 종료)
- 커밋은 최소 2개 이상 찍을 것
'''


import random


quiz_list = [
    {"question": "현재 디렉토리의 파일과 폴더 목록을 출력하는 명령어는?",
        "answer": "ls",},
    {"question": "현재 작업 중인 디렉토리의 경로를 출력하는 명령어는?",
        "answer": "pwd",},
    {"question": "디렉토리를 이동할 때 사용하는 명령어는?",
        "answer": "cd"},
    {"question": "새로운 디렉토리(폴더)를 생성하는 명령어는?",
        "answer": "mkdir",},
    {"question": "파일이나 디렉토리를 삭제하는 명령어는?",
        "answer": "rm",}
]


while True:
    print("\n=== 리눅스 명령어 퀴즈 프로그램 ===\n")


    selected_quizzes = random.sample(quiz_list, 3)
    score = 0

    for i in range(len(selected_quizzes)):
        quiz = selected_quizzes[i]
        print(f"[{i + 1}] {quiz['question']}")
        user_input = input("정답 입력: ").strip().lower()

        if user_input == quiz["answer"].lower():
            print("Correct")
            score += 1
        else:
            print(f"Inccorrect! 정답은 '{quiz['answer']}' 입니다.")


    print("\n------------------------------------------")
    print(f"게임 종료! 총 3문제 중 {score} 문제를 맞추셨습니다.")

    if score == 3:
        grade = 'A'
    elif score == 2:
        grade = 'B'
    elif score == 1:
        grade = 'C'
    else:
        grade = 'F'

    print(f"당신의 등급은 [{grade}] 입니다.")
    print("------------------------------------------")


    retry = input("\n게임을 종료겠습니까? (y/n): ").strip().lower()
    if retry != 'n':
        print("게임을 종료합니다.")
        break
