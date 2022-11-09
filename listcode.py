if __name__ == '__main__':
    x = int(input("insert a natural number"))
    y = int(input("insert a natural number"))
    z = int(input("insert a natural number"))
    n = int(input("insert a natural number"))
    tot = []
    for i in range(0, x + 1):
        for j in range(0, y + 1):
            for k in range(0, z + 1):
                if i+j+k != n:
                    perm = [i ,j,k]
                    tot.append(perm)
    print(tot)