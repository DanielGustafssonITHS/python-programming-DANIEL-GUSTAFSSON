#

# Ladda in filen

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd



k = -1
m = 0
# definera en funktion som baseras på y = kx + m


def classify_datapoints(x, y, k, m):
    line_y = k * x + m
    if y >= line_y:
        print("point is above line")
        return 1
    else:
        print("point is below line")
        return 0


def plot_classify(data, k, m):
    colors = data["label"].map({0: "red", 1:"blue"})
    plt.scatter(data["x"], data["y"], c = colors, label = "Punkter")

    x_vals = sorted(data["x"])
    y_vals = [k * x + m for x in x_vals]
    plt.plot(x_vals, y_vals, color = "black", label = f"y = {k}x + {m}")
    
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Klassifiering efter linje")
    plt.legend()
    plt.show()


if __name__=="__main__":

    filename = "LABB3/unlabelled_data.csv"

    data = pd.read_csv(filename)

    data.columns = ["x", "y"]
    data["label"] = data.apply(lambda row: classify_datapoints(row["x"], row["y"], k, m), axis=1)

    data.to_csv("labelled_data.csv",index=False)

    plot_classify(data, k = 1, m = 0)



    """
    colors = data["label"].map({0: "red", 1: "blue"})
    plt.scatter(data["x"], data["y"], c=colors, label="Punkter")


    x_vals = sorted(data["x"])
    y_vals = [k * x + m for x in x_vals]
    plt.plot(x_vals, y_vals, color="black", label=f"y = {k}x + {m}")

    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Klassificering med linje")
    plt.legend()
    plt.show()
"""