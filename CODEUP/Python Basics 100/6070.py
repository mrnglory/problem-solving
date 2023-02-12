month = int(input())

index = month // 3

if index in (0, 4):
    print("winter")
elif index == 1:
    print("spring")
elif index == 2:
    print("summer")
elif index == 3:
    print("fall")
