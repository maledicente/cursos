import matplotlib.pyplot as plt
import pandas as pd
import csv

df = pd.read_csv("WORLD-2019.csv", delimiter=',')

print(df['Age'].describe())

