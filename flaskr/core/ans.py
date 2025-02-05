from traceback import print_tb
import numpy as np
import pandas as pd
from itertools import chain
from probs import *

# 事前計算した確率一覧の読み込み
A = pd.read_csv("out.csv", header=None).loc[:, 0].to_numpy()
print("elms: {}\n".format(A.size))

# print(test2.shape)
# print(test3.shape)
def idx_lb(idx):
  lb = ""
  for i in range(prs3.shape[0]):
    idx, r = divmod(idx, test3.shape[1])
    lb += str(r)

  for i in range(prs2.shape[0]):
    idx, r = divmod(idx, test2.shape[1])
    lb += str(r)

    # print(idx, r)

  return lb[::-1]

base = np.array([int(i) for i in ("2"*prs2.shape[0] + "3"*prs3.shape[0])])
def lb_idx(lb):
  idx = np.array([int(i) for i in lb])
  size = np.append(1, np.cumprod(base)[:-1])
  return np.sum(idx*size)

size = 1
ans = 0
lb_ans = ""
j = 0

# 回答入力部
for i, n in enumerate(base):
  print("q{:>2d}: {}".format(i, lb_q[i]))
  if n == 2:
    curr = True if input("yY/nN: ".format(i)).lower()=="y" else False
  else:
    curr = int(input("0~{}: ".format(n-1)))
    j+=1
  lb_ans += str(int(curr))

# テスト用入力例
# lb_ans = "1"*prs2.shape[0] + "2"*prs3.shape[0]

# 回答に対する確率の表示
# "conbination : probability %"
print("{} : {:.2f} %".format(lb_ans, 100*A[ans]))

# 確率の高い上位10個の組み合わせの表示
# "rank : conbination = probability %"
idx_sort = np.argsort(A)[::-1] 
idx_sort = np.sort(idx_sort[:10])
lb_sort = [idx_lb(i) for i in idx_sort]
print("The combination of options most likely to result in a science degree is as follows")

for i in np.arange(0, 10):
  print("{} : {} = {:.2f} %".format(i+1, lb_sort[i], 100*A[idx_sort[i]]))
