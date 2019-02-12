N = int(input())

swifts = input().split(sep=" ")
semaphores = input().split(sep=" ")

swiftsTotal = 0
semaphoresTotal = 0

answer = 0

for index in range(len(swifts)):
    swiftsTotal += int(swifts[index])
    semaphoresTotal += int(semaphores[index])

    if swiftsTotal == semaphoresTotal:
        answer = index + 1

print(answer)
