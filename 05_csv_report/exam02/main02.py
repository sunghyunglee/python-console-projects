#파일 읽기
import csv

with open("loans.csv" , "r" , encoding="utf-8") as f:
    reader = csv.DictReader(f)
    data = list(reader)


#총 대출 건수
total_count = 0
for row in data:
    total_count += 1


#평균 대출일수
total_days = 0
for row in data:
    total_days += int(row["대출일수"])

avg_days = total_days / total_count


#도서별 대출 건수
loans_by_book = {}
for row in data:
    a = row["도서명"]
    loans_by_book[a] = loans_by_book.get(a, 0) + 1


#분야별 대출 건수
loans_by_area = {}
for row in data:
    a = row["분야"]
    loans_by_area[a] = loans_by_area.get(a, 0) + 1


#대출자 유형별
loans_by_category = {}
for row in data:
    a = row["대출자유형"]
    loans_by_category[a] = loans_by_category.get(a, 0) + 1


#월별 대출 건수
loans_by_month = {}
for row in data:
    k = row["대출일"][:7]
    loans_by_month[k] = loans_by_month.get(k , 0) + 1



#분석 결과
best_book = max(loans_by_book , key=loans_by_book.get)
best_area = max(loans_by_area , key=loans_by_area.get)


#리포트 파일 저장
with open("report02.txt" , "w", encoding="utf-8") as f:
    f.write("\n=== 한빛도서관 대출 리포트 (2025.03 ~ 05) ===\n\n")

    f.write(f"[총 대출 건수]{total_count: ,}건\n")


    f.write(f"[평균 대출일수]{avg_days: .1f}일\n\n")


    f.write("[분야별 대출 건수]\n")
    for k,v in sorted (loans_by_area.items() , key=lambda x: x[1] , reverse=True):
        f.write(f"{k}: {v}건\n")


    f.write("\n[대출자 유형별]\n")
    for k,v in sorted (loans_by_category.items() , key=lambda x: x[1] , reverse=True):
        f.write(f"{k}:{v: ,}건\n")


    f.write("\n[월별 대출 건수]\n")
    for k,v in loans_by_month.items():
        f.write(f"{k}:{v: ,}건\n")


    f.write("\n[분석 결과]\n")

    f.write(f"최다 대출 도서: {best_book} ({loans_by_book[best_book]}건)\n")

    f.write(f"인기 분야 1위: {best_area} ({loans_by_area[best_area] }건)\n")

