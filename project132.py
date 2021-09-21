import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("final.csv")

mass = df["Mass"].to_list()
radius = df["Radius"].to_list()
dist = df["Distance"].to_list()
gravity = df["Gravity"].to_list()

mass.sort()
radius.sort()
gravity.sort()

plt.plot(radius,mass)
plt.scatter(radius,mass)
plt.xlabel("Radius")
plt.ylabel("Mass")
plt.show()


plt.plot(mass,gravity)
plt.scatter(mass,gravity)
plt.xlabel("Mass")
plt.ylabel("Gravity")
plt.show()