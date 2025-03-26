import random
howManyDo = input("how many numbers do i generste")
total = 0
for i in range(howManyDo):
    lastRoll = random.randint(0, 100)
    print(lastRoll)
    total = total + lastRoll
total = total/howManyDo
print("average is", howManyDo)
