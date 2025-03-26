import random
howManyDo = int(input("how many numbers do i generste"))
total = 0
for i in range(int(howManyDo)):
    lastRoll = random.randint(0, 100)
    print(lastRoll)
    total = total + lastRoll
total = int(total)/int(howManyDo)
print("average is", howManyDo)
