amt = int(input())
d = int(input())

notes = [100, 50, 20, 10, 5, 2, 1]
start = 0
match d:
    case 100:
        start = 0
    case 50:
        start = 1
    case 20:
        start = 2
    case 10:
        start = 3
    case 5:
        start = 4
    case 2:
        start = 5
    case 1:
        start = 6
    case _:
        print("Invalid denomination")
        exit()


for i in range(start, len(notes)):
    cnt = amt // notes[i]
    amt %= notes[i]
    print(f"{notes[i]} rupees note: {cnt}")
