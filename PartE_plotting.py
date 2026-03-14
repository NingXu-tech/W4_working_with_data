from matplotlib import pyplot as plt
import csv
import numpy as np

# ======================================
# Part 1: Simple line plot with basic pyplot
# ======================================

years = [2020, 2021, 2022, 2023, 2024]
sales = [120, 135, 150, 160, 180]

plt.figure()  # create a new figure
plt.plot(years, sales)  # line plot
plt.xlabel("Year")
plt.ylabel("Sales")
plt.title("Annual Sales")
plt.savefig("annual_sales.png")
print("Plot saved as annual_sales.png")

# ======================================
# Part 2: Read CSV and make a bar chart
# ======================================

with open("student.csv", "r", encoding="utf-8") as f:
    csv_reader = csv.DictReader(f)
    rows = [row for row in csv_reader]

print("rows:", rows)

names = [row["name"] for row in rows]
scores = [int(row["score"]) for row in rows]

plt.figure()  # create another figure
plt.bar(names, scores)  # bar chart
plt.xlabel("Name")
plt.ylabel("Score")
plt.title("Score for students")
plt.savefig("Students_Scores.png")
print("Saved Students_Scores.png")

# ======================================
# Part 3: Object-oriented plotting with fig and ax
# ======================================

x = [0, 1, 2, 3, 4]
y = [1, 4, 9, 16, 25]

fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_title("y = x^2")
fig.savefig("quadratic.png")
print("Saved quadratic.png")

# ======================================
# Part 4: Multiple subplots
# ======================================

# np.linspace(start, stop, number_of_points)
x = np.linspace(-2, 2, 100)

# create 1 row and 3 columns of subplots
fig, axes = plt.subplots(nrows=1, ncols=3, figsize=(12, 4))

axes[0].plot(x, x)
axes[0].set_xlabel("x")
axes[0].set_ylabel("y")
axes[0].set_title("y = x")

axes[1].plot(x, x**2)
axes[1].set_xlabel("x")
axes[1].set_ylabel("y")
axes[1].set_title("y = x^2")

axes[2].plot(x, x**3)
axes[2].set_xlabel("x")
axes[2].set_ylabel("y")
axes[2].set_title("y = x^3")

fig.tight_layout()  # avoid overlap between subplots
fig.savefig("three_pictures.png")
print("Saved three_pictures.png")

# ======================================
# Part 5: Multiple lines in one plot
# ======================================

x = np.linspace(-3, 4, 100)

fig, ax = plt.subplots()
ax.plot(x, x, label="y = x")
ax.plot(x, x**2, label="y = x^2")
ax.plot(x, x**3, label="y = x^3")

ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_title("3 lines in 1 picture")
ax.legend()  # show legend for labels

fig.savefig("three_lines.png")
print("Saved three_lines.png")