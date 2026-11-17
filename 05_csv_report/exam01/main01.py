#파일 읽기
import csv

with open("sales.csv" , "r" , encoding="utf-8") as f:
    reader = csv.DictReader(f)
    data = list(reader)


#전체 매출
total = 0
for row in data:
    total += int(row["단가"]) * int(row["수량"])


#메뉴별 판매량
qty_by_menu = {}
for row in data:
    x = row["메뉴"]
    y = row["수량"]
    qty_by_menu[x] = qty_by_menu.get(x, 0) + int(y)


#카테고리별 매출
sales_by_category = {}
for row in data:
    a = row["카테고리"]
    b = row["수량"]
    c = row["단가"]
    sales_by_category[a] = sales_by_category.get(a, 0) + int(b) * int(c)


#월별 매출
sales_by_month = {}
for row in data:
    k = row["날짜"][:7]
    result = int(row["수량"]) * int(row["단가"])
    sales_by_month[k] = sales_by_month.get(k , 0) + result


#분석결과
best_menu = max(qty_by_menu , key=qty_by_menu.get)
best_category = max(sales_by_category , key=sales_by_category.get)



#리포트 파일 저장
with open("report01.txt" , "w", encoding="utf-8") as f:
    f.write("\n=== 파이빈 카페 매출 리포트 (2025.01 ~ 03) ===\n\n")

    f.write(f"[전체 매출]{total: ,}원\n\n")


    f.write("[메뉴별 판매량]\n")
    for k,v in sorted (qty_by_menu.items() , key=lambda x: x[1] , reverse=True):
        f.write(f"{k}: {v}잔\n")


    f.write("\n[카테고리별 매출]\n")
    for k,v in sorted (sales_by_category.items() , key=lambda x: x[1] , reverse=True):
        f.write(f"{k}:{v: ,}원\n")


    f.write("\n[월별 매출]\n")
    for k,v in sales_by_month.items():
        f.write(f"{k}:{v: ,}원\n")


    f.write("\n[분석 결과]\n")

    f.write(f"가장 많이 팔린 메뉴: {best_menu} ({qty_by_menu[best_menu]}잔)\n")

    f.write(f"매출 1위 카테고리: {best_category} ({sales_by_category[best_category]:,}원)\n")
