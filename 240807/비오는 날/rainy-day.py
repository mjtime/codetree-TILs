class Forecast():
    def __init__(self, day, week, weather):
        self.day = day
        self.week = week
        self.weather = weather

n = int(input())

# 변수 선언 및 입력
arr = [tuple(input().split()) for _ in range(n)]
weathers = [Forecast(day, week, weather) for day, week, weather in arr]

rain_day = '9'
rain_idx = -1
for i, w in enumerate(weathers):
    if w.weather == "Rain":
        if rain_day > w.day:
            rain_day = w.day
            rain_idx = i

print(weathers[rain_idx].day, weathers[rain_idx].week, weathers[rain_idx].weather)