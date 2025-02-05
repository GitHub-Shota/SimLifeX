import numpy as np
import pandas as pd
from itertools import chain
from probs import *

def bayes(A, pr):
  return A*pr[0]/(A*pr[0]+(1-A)*pr[1])

# print("elms: {}".format(
#   (test2.shape[0]**test2.shape[1])
#   *(test3.shape[0]**test3.shape[1])
#   *(test5.shape[0]**test5.shape[1])
# ))

# ver1 : 23億通り
# ver2 : 14万通り
print("elms: {}".format(
  (prs2.shape[1]**prs2.shape[0])
  *(prs3.shape[1]**prs3.shape[0])
  # *(prs5.shape[1]**prs5.shape[0])
))

A = 0.5
for pr in chain(prs2, prs3):
# for pr in chain(test2, test3):
  A = np.array([bayes(A, pr) for pr in pr])
  A = np.squeeze(A.reshape(1, -1))
  print(A.shape)

exp = pd.DataFrame(data=A)
exp.to_csv("out.csv", index=False, header=False, lineterminator='\r\n')
