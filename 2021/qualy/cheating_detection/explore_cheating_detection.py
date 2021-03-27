# %% [markdown]
# # Explore question mechanism
# %% [markdown]
# ## Initial imports
# %%
from random import uniform
import pandas as pd
import numpy as np
from math import exp, log
# %%
def sigmoid(x):
    "Numerically-stable sigmoid function."
    if x >= 0:
        z = exp(-x)
        return 1 / (1 + z)
    else:
        z = exp(x)
        return z / (1 + z)
# %%
def logit(x):
    return log(x / (1 - x))
# %%
Ns = 1000
Nq = 10000
S = [uniform(-3, 3) for _ in range(Ns)]
Q = [uniform(-3, 3) for _ in range(Nq)]
# %%
R = [
    [sigmoid(s - q) for q in Q]
    for s in S
]
# %%
Rr = [
    [uniform(0, 1) < r for r in row]
    for row in R
]
# %%
Rs = [sum(row)/len(row) for row in Rr]
Rq = [sum([row[i] for row in Rr])/len(S) for i in range(len(Q))]
# %%
Ss = [sigmoid(s) for s in S]
# %%
Qq = [1 - sigmoid(q) for q in Q]
# %%
Ss[:5]
# %%
Rs[:5]
# %%
Qq[:5]
# %%
Rq[:5]
# %%
logit(sigmoid(0.5))
# %%
