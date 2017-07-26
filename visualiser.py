import matplotlib.pyplot as plt
import sys
import numpy as np


"""
Visualiser program for checking if mcl is working ok
To use:
Make a FIFO in this folder, call it VISUAL or something (use mkfifo in bash)

Set FIFO_PATH in this program to point to the FIFO

On the sub, set config/modeling.py's VISUALIZE to True

Run this file. 

Then cat to ttyUSB0, run.sh, and then vs.sh with the path to the FIFO and your computer deets

A window should pop up with the visualization

Happy debugging

"""

FIFO_PATH = "VISUAL"

READ_FILE = open(FIFO_PATH, 'r')

plt.ion()
fig = plt.figure()
ax = fig.add_subplot(111)
first_time = True
while True:
    if READ_FILE.readline() != "FOOFOO\n": # Beginning of data packet
        continue
    one = READ_FILE.readline()
    two = READ_FILE.readline()
    three = READ_FILE.readline()
    four = READ_FILE.readline()
    if READ_FILE.readline() != "RASPUTIN\n":
        continue  # malformed packet if RASPUTIN is not present
    particles_x = [float(x) for x in one.strip()[1:-1].split(",")]
    particles_y = [float(x) for x in two.strip()[1:-1].split(",")]
    probability = [float(x) for x in three.strip()[1:-1].split(",")]
    other_stuff = [float(x) for x in four.strip()[1:-1].split(",")]
    yaw = other_stuff[0]
    depth = other_stuff[1]
    our_x = other_stuff[2]
    our_y = other_stuff[3]
    buoy_x = other_stuff[4]
    buoy_y = other_stuff[5]
    ax.clear()
    ax.scatter(particles_x, particles_y, c=probability, alpha=.55555)
    ax.scatter(buoy_x, buoy_y, c ='red')
    ax.scatter(our_x, our_y, c='black')

    plt.show()
    plt.pause(0.1)



