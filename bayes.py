from tkinter import Y
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def bays(y_x, x):
  x_y = y_x[0]*x[0]/(y_x[0]*x[0]+y_x[1]*x[1])
  return np.array([x_y, 1-x_y])

B_A = pd.DataFrame(
    data=[[0.4, 0.6], [0.3, 0.7]],
    index=["A1", "A2"],
    columns=["B1_A", "B2_A"]
)

C_A = pd.DataFrame(
    data=[[0.75, 0.25], [0.4, 0.6]],
    index=["A1", "A2"],
    columns=["C1_A", "C2_A"]
)

A = np.array([0.5, 0.5])

res = pd.DataFrame(data=[
    bays(C_A["C1_A"].to_numpy(), bays(B_A["B1_A"].to_numpy(), A)), 
    bays(C_A["C2_A"].to_numpy(), bays(B_A["B1_A"].to_numpy(), A)), 
    bays(C_A["C1_A"].to_numpy(), bays(B_A["B2_A"].to_numpy(), A)), 
    bays(C_A["C2_A"].to_numpy(), bays(B_A["B2_A"].to_numpy(), A))], 
    index=["A_B1C1", "A_B1C2", "A_B2C1", "A_B2C2"],
    columns=["A1", "A2"]
).T

flg_B = input("do you like the japanese(subject), yY/nN : ")
flg_C = input("do you like the mathematics, yY/nN       : ")
if flg_B == "y" or flg_B == "Y":  
  if flg_C == "y" or flg_C == "Y":  
    you = res.loc["A1", "A_B1C1"]
  else:
    you = res.loc["A1", "A_B1C2"]

else:                       
  if flg_C == "y" or flg_C == "Y":  
    you = res.loc["A1", "A_B2C1"]
  else:
    you = res.loc["A1", "A_B2C2"]

print("your potential of science, {:.2f}[%]\n".format(100*you))
print("~~~ result list up ~~~")
print(res)
