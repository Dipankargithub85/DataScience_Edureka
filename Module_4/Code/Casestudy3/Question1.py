import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Hurricanes.csv")

x = df["Year"]
y = df["Hurricanes"]

plt.bar(x,y)
plt.xlabel("Year")
plt.ylabel("Hurricanes")
plt.grid()
plt.title("Hurricanes vs Year")

plt.setp(plt.gca().get_xticklabels(), rotation=90, horizontalalignment='right') # Rotate Axis Labels

plt.show()