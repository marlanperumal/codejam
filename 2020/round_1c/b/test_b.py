# %%[markdown]
# Testing results

# %%
from collections import defaultdict

# %%
filename = "sample.in.txt"

# %%
with open(filename, "r") as f:
    T = int(f.readline().strip())
    for t in range(1, T + 1):
        U = int(f.readline().strip())
        Q = []
        M = []
        for i in range(int(1e4)):
            q, m = f.readline().strip().split()
            Q.append(q)
            M.append(m) 

# %%
print(Q[:10])

# %%
print(M[:10])

# %%
mapping = defaultdict(int)

# %%
for m in M:
    for c in m:
        mapping[c] += 1
        
# %%
for m in M:
    mapping[m[-1]] += 1
        
# %%
sorted_mapping = sorted(mapping, key=lambda x: mapping[x])

# %%
sorted_mapping[0:1] + list(reversed(sorted_mapping[1:]))
