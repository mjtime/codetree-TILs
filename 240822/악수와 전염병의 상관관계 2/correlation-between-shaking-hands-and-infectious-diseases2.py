# N명의 개발자, 처음 전염병에 걸려 있는 개발자의 번호 P
# T번에 걸쳐 t초에 x개발자가 y개발자와 악수
# K번의 악수 동안만 전염 (전염 + 전염 = 전염)
# 최종적으로 누가 전염병에 걸리게 되었는지? 0 or 1로 전체 개발자 표현

# cnt번 입력 받은 후, t오름차순 정렬

n, k, p, cnt = map(int, input().split())
people = [0 for _ in range(n)] # 개발자
people[p-1] = 1 # 제시된 감염인
times_left = [2 for _ in range(n)] # 남은 감염 횟수
arr_hand = [list(map(int, input().split())) for _ in range(cnt)] # 악수 정보
arr_hand.sort(key = lambda x:x[0]) # 시간순 정렬

for i in range(cnt):
    x_person = arr_hand[i][1] - 1
    y_person = arr_hand[i][2] - 1

    if people[x_person] == 1 and times_left[x_person]>0:
        people[y_person] = 1
        times_left[x_person] -= 1
    if people[y_person] == 1 and times_left[y_person]>0:
        people[x_person] = 1
        times_left[y_person] -= 1

for person in people:
    print(person, end ='')