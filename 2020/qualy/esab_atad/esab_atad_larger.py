T, B = [int(i) for i in input().split()]

for t in range(T):
    X = []
    for i in range(B // 10):
        front = []
        back = []
        same = []
        different = []
        for j in range(5):
            print(j + i * 5 + 1)
            k1 = int(input())
            print(B - j - i * 5)
            k2 = int(input())
            front.append(k1)
            back.append(k2)
            if k1 == k2:
                same.append(j)
            else:
                different.append(j)
        X.append({
            "front": front,
            "back": back,
            "same": same,
            "different": different
        })
    for i in range(B // 10):
        Y = X[i]
        if Y["same"]:
            j = Y["same"][0]
            k1 = Y["front"][j]
            print(i * 5 + j + 1)
            k2 = int(input())
            if k1 != k2:
                for j in Y["same"]:
                    Y["front"][j] = 1 - Y["front"][j]
                    Y["back"][j] = 1 - Y["back"][j]
        else:
            print(1)
            _ = input()
    for i in range(B // 10):
        Y = X[i]
        if Y["different"]:
            j = Y["different"][0]
            k1 = Y["front"][j]
            print(i * 5 + j + 1)
            k2 = int(input())
            if k1 != k2:
                for j in Y["different"]:
                    Y["front"][j] = 1 - Y["front"][j]
                    Y["back"][j] = 1 - Y["back"][j]
        else:
            print(1)
            _ = input()
    for i in range(B // 10):
        Y = X[i]
        if Y["same"]:
            j = Y["same"][0]
            k1 = Y["front"][j]
            print(i * 5 + j + 1)
            k2 = int(input())
            if k1 != k2:
                for Y2 in X:
                    for j in Y2["same"]:
                        Y2["front"][j] = 1 - Y2["front"][j]
                        Y2["back"][j] = 1 - Y2["back"][j]
            break
    for i in range(B // 10):
        Y = X[i]
        if Y["different"]:
            j = Y["different"][0]
            k1 = Y["front"][j]
            print(i * 5 + j + 1)
            k2 = int(input())
            if k1 != k2:
                for Y2 in X:
                    for j in Y2["different"]:
                        Y2["front"][j] = 1 - Y2["front"][j]
                        Y2["back"][j] = 1 - Y2["back"][j]
            break
    result = []
    for Y in X:
        result.extend(Y["front"])
    for Y in reversed(X):
        result.extend(reversed(Y["back"]))
    print("".join([str(i) for i in result]))
    response = input()
    if response == "N":
        break
