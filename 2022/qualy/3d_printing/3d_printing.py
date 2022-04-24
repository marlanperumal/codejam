N = int(1e6)

T = int(input())

for t in range(1, T + 1):
    cartridges = {
        "C": [],
        "M": [],
        "Y": [],
        "K": [],
    }
    for i in range(3):
        c, m, y, k = [int(i) for i in input().split()]
        cartridges["C"].append(c)
        cartridges["M"].append(m)
        cartridges["Y"].append(y)
        cartridges["K"].append(k)
    colour = {}
    for i in range(4):
        cartridge = min(cartridges, key=lambda x: min(cartridges[x]))
        colour[cartridge] = min(cartridges[cartridge])
        del cartridges[cartridge]

    if sum(colour.values()) < N:
        result = "IMPOSSIBLE"
    else:
        for c in ["C", "M", "Y", "K"]:
            colour[c] -= min(colour[c], sum(colour.values()) - N)
            if sum(colour.values()) == N:
                break
        result = f"{colour['C']} {colour['M']} {colour['Y']} {colour['K']}"

    print(f"Case #{t}: {result}")
