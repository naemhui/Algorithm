def room(data, k):
    arr = [[0]*2 for _ in range(6)]
    for student in data:
        grade = student[1]
        gender = student[0]

        arr[grade - 1][gender] += 1
    # 여기까지 이제 6*2 배열 만들어짐. 리스트 끝

    room_count = 0  # 방 개수 카운트 시작
    for r in range(6):
        for c in range(2):
            if arr[r][c] > k:
                if arr[r][c] % k == 0:
                    room_count += arr[r][c] // k
                else:
                    room_count += arr[r][c] // k + 1
            elif arr[r][c] == 0:
                pass
            else:
                room_count += 1
    
    return room_count


n, k = map(int, input().split())
data = []
for _ in range(n):
    student = list(map(int, input().split()))
    data.append(student)
    result = room(data, k)
print(result)



# dict1 = {'1':'a', '3':'b', '2':'c'}
# print(len(dict1))

