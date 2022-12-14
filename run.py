import random
from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import cv2
import numpy as np

plt.style.use('ggplot')

x_vals = []
y_vals = []

index = count()


def animate(i):
    data = pd.read_csv('data.csv')
    x = data['Date']
    y = data['Count']

    plt.cla()

    plt.plot(x, y, label='Pixel Count')

    plt.legend(loc='upper left')
    plt.xlabel('Time')
    plt.ylabel('Red frequency')
    degrees = 70
    plt.xticks(rotation=degrees)

    plt.tight_layout()


ani = FuncAnimation(plt.gcf(), animate, interval=1000)

plt.tight_layout()
plt.show()