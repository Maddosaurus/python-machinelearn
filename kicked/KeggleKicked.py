import matplotlib.pyplot as plt
import seaborn as sb
import pandas as pd


car_data = pd.read_csv('training.csv', na_values=['NA'], nrows=100)
car_data.head()

sb.pairplot(car_data.dropna(), hue='IsBadBuy')