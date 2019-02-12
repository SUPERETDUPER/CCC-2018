N = int(input())

measurements = input().split(sep=" ")
measurements = map(int, measurements)

measurements = sorted(measurements)

# print(measurements)

if N % 2 == 0:
    middle = int(N / 2 - 1)
else:
    middle = int((N - 1) / 2)

print(measurements[middle], end=" ")

distance = 1

while True:
    if middle + distance >= N:
        break

    print(measurements[middle + distance], end=" ")

    if middle - distance < 0:
        break
    print(measurements[middle - distance], end=" ")
    distance += 1
