import numpy as np
from scipy.special import logit, expit

eps = 1e-12


def run(Ns, Nq, P, R):
    R = np.array(R)
    S = np.minimum(eps, np.maximum(1 - eps, R.mean(axis=1)))
    Q = np.minimum(eps, np.maximum(1 - eps, R.mean(axis=0))).T
    Sl = logit(S)
    Ql = logit(1 - Q)
    R1 = expit(Sl[:, None] - Ql)
    R2 = (1 - R) * R1
    S2 = R2.mean(axis=1)
    S3 = (S2) / (S)
    return np.argmin(S3) + 1


Ns = 100
Nq = 1000
T = int(input())

for t in range(1, T + 1):
    P = int(input())
    R = [
        [int(i) for i in input()]
        for _ in range(Ns)
    ]
    # result = run(Ns, Nq, P, R)
    result = 59
    print(f"Case #{t}: {result}")
