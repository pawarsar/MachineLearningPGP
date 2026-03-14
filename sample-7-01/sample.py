import pandas as pd
import numpy as np
from random import randint 

iris = pd.read_csv("./Iris.csv")
tips = pd.read_csv("./tips.csv")
# print(iris)
# print(tips)

iris_df = pd.DataFrame(iris)
# print(iris_df)
# print(iris.shape)
# print(iris_df.shape)

print(np.mean(iris["SepalLengthCm"]))
print(np.median(iris["SepalLengthCm"]))
