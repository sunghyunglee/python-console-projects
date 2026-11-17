import json
from phone.model.phone import Phone

def print_menu() -> None:
    print("----- 메뉴 ------")
    print("1. 핸드폰 등록")
    print("2. 핸드폰 목록")
    print("3. 핸드폰 조회")
    print("4. 핸드폰 수정")
    print("5. 핸드폰 삭제")
    print("0. 프로그램 종료")
    print("-----------------")


def scan_menu_num() -> int:
    num = int(input("메뉴 번호: "))
    return num

#insert
def insert_phone():
    phone_list = select_list()
    with open("phone_data.json" , "w" , encoding="utf-8") as f:
        b = input("브랜드: ")
        m = input("모델: ")
        c = input("색상: ")
        s = scan_storage()
        y = int(input("년도: "))
        p = int(input("가격: "))
        phone = Phone(b, m, c, s, y, p)
        phone_dict = phone.to_dict()
        phone_list.append(phone_dict)
        json.dump(phone_list, f, ensure_ascii=False, indent=2)

#select
def select_list():
    with open("phone_data.json" , "r" , encoding="utf-8") as f:
        phone_list = json.load(f)
    return phone_list

#list
def select_phone_list():
    phone_list = select_list()
    print()
    print("----- 핸드폰 목록 -----")
    for idx , phone_dict in enumerate(phone_list):
        phone = Phone.from_dict(phone_dict)
        print(f"{idx}. {phone.brand} / {phone.model}")
    print("---------------------")
    print()

#search
def select_phone_search():
    phone_list = select_list()
    print()
    print("----- 핸드폰 상세 -----")
    num = int(input("등록 번호: "))
    for idx , phone_dict in enumerate(phone_list):
        phone = Phone.from_dict(phone_dict)
    phone = phone_list[num]
    print(phone)
    print("---------------------")
    print()

#edit
def edit_phone():
    phone_list = select_list()
    print()
    print("----- 핸드폰 수정 -----")
    num = int(input("등록 번호: "))

    print(Phone.from_dict(phone_list[num]))
    print()

    b = input("브랜드: ")
    m = input("모델: ")
    c = input("색상: ")
    s = scan_storage()
    y = int(input("년도: "))
    p = int(input("가격: "))

    phone = Phone(b, m, c, s, y, p)
    phone_list[num] = phone.to_dict()

    with open("phone_data.json", "w", encoding="utf-8") as f:
        json.dump(phone_list, f, ensure_ascii=False, indent=2)
    print("---------------------")
    print("<수정 완료!>")
    print()

#remove  #<작동안함 수정필요>
def remove_phone():
    phone_list = select_list()
    print()
    print("----- 핸드폰 삭제 -----")
    num = int(input("등록 번호: "))
    del phone_list[num]
    for idx , phone_dict in enumerate(phone_list):
        phone = Phone.from_dict(phone_dict)
    print("---------------------")
    print()
    print("<삭제 완료!>")
    print()

#storage limit
def scan_storage() -> int:
    valid_storage = [256, 512, 1024]  # GB 기준, 1TB = 1024GB
    while True:
        s = int(input("용량 (256/512/1024<1TB>): "))
        if s in valid_storage:
            return s
        print("용량은 256, 512, 1024<1TB> 중 하나만 입력 가능합니다.")

#process
def process(num: int) -> None:
    match num:
        case 1:
            insert_phone()
        case 2:
            select_phone_list()
        case 3:
            select_phone_search()
        case 4:
            edit_phone()
        case 5:
            remove_phone()

#start
def program_start():
    while True:
        try:
            print_menu()
            num = scan_menu_num()
            if num == 0: break
            process(num)
        except Exception as e:
            print()
            print("[에러~ 에러~ 비상!]" , e)
            print("프로그램은 정상적으로 작동됩니다")
            print()

