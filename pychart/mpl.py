import csv
import sys

import matplotlib.pyplot as plt
import numpy as np

sid = {"Adelie": 0, "Chinstrap": 1, "Gentoo": 2}
colors = [(1, 0.8, 0.4, 0.8), (0.8, 0.4, 1, 0.8), (0.4, 0.8, 0.7, 0.8)]


def load(file: str) -> np.ndarray:
    """returns species, bill, flipper, mass"""
    with open(file, "r") as f:
        reader = csv.reader(f)
        items = []
        for row in reader:
            if row[0] == "":
                continue
            try:
                items.append([sid[row[1]], float(row[3]), float(row[5]), float(row[6])])
            except ValueError:
                continue
        return np.array(items).transpose()

def lerp(min, max, x):
    return (max - min) * x + min

def ilerp(min, max, x):
    return (x - min) / (max - min)

def main() -> None:
    if len(sys.argv) != 2:
        print("This program needs the path to the pengligns data file.")
        sys.exit(1)
    data = load(sys.argv[1])

    minbill, maxbill = data[1].min(), data[1].max()
    v = lerp(20, 120, ilerp(minbill, maxbill, data[1]))
    scatter = plt.scatter(data[2], data[3], v, data[0], cmap="cool", alpha=0.7)

    ax = scatter.axes
    if ax:
        ax.set_xlabel("Flipper Length (mm)")
        ax.set_ylabel("Body Mass (g)")

        s, _ = scatter.legend_elements(prop="sizes")
        sv = np.arange(minbill, maxbill, (maxbill - minbill - 0.00001) / len(s))
        l1 = plt.legend(s, [f"{x:5.2f}" for x in sv])
        ax.add_artist(l1)

        c, _ = scatter.legend_elements(prop="colors")
        plt.legend(c, ["Adelie", "Chinstrap", "Gentoo"], loc="lower right")

    plt.show()


if __name__ == "__main__":
    main()
