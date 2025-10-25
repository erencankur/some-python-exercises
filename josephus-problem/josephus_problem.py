def josephus(l):
    i = 0
    while len(l) > 1:
        i = (i + 1) % len(l) # dairesel sıra
        print(f"{l[i-1]} eleminated {l[i]}")
        l.remove(l[i])
        print(l, "\n")
    print(f"Survived: {l[0]}")

n = int(input("Enter the number of people: "))
l = [i for i in range(1, n+1)]
print(f"\nPeople: {l}\n")
josephus(l)