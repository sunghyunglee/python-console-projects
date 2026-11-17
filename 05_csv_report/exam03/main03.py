#파일 읽기
import csv

with open("weather.csv" , "r" , encoding="utf-8") as f:
    reader = csv.DictReader(f)
    data = list(reader)


#전체 관측
total_count = 0
for row in data:
    total_count += 1


#비 온 날
rainy_days = 0
for row in data:
    rainy_days += int(row["강수량"]) > 0


#도시별 최고기온 합계 & 건수
city_ht_total = {}
city_ht_count = {}
for row in data:
    x = row["도시"]
    y = row["최고기온"]
    city_ht_total[x] = city_ht_total.get(x, 0) + int(y)
    city_ht_count[x] = city_ht_count.get(x, 0) + 1


#도시별 평균 최고기온
city_ht_avg = {}
for city in city_ht_total:
    city_ht_avg[city] = city_ht_total[city] / city_ht_count[city]


#분석 결과
best_h_day = max(data, key=lambda row: int(row["최고기온"]))
best_range_day = max(data, key=lambda row: int(row["최고기온"]) - int(row["최저기온"]))



#리포트 파일 저장
with open("report03.txt" , "w", encoding="utf-8") as f:
    f.write("\n=== 여름 날씨 분석 리포트 (2025.06 ~ 08) ===\n\n")

    f.write(f"[전체 관측]{total_count: }건\n")


    f.write(f"[비 온 날]{rainy_days: }건 ({(rainy_days / total_count)*100:.1f}%)\n\n")


    f.write("[도시별 평균 최고기온]\n")
    for k,v in sorted (city_ht_avg.items() , key=lambda x: x[1] , reverse=True):
        f.write(f"{k}:{v: .1f}℃\n")


    f.write("\n[분석 결과]\n")

    f.write(f"가장 더웠던 날: {best_h_day['날짜']} {best_h_day['도시']} ({best_h_day['최고기온']}℃)\n")

    td = int(best_range_day["최고기온"]) - int(best_range_day["최저기온"])
    f.write(f"일교차가 가장 큰 날: {best_range_day['날짜']} {best_range_day['도시']} ({td}℃)\n")
