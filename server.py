import numpy as np
import numpy.random as npr
import sys
import time
i = 1 

"""
Dummy server for testing the visualizer
Usage: python server.py > *pipe*
Begins sending data in agreed-on format to the pipe to be read by the visualizer
If everything is correct, you'll see randomly colored and placed dots move
around in matplotlib graph
"""




while True:
    a = str(np.array(npr.uniform(0, 100, 1000), dtype=np.float32).tolist())
    b = str(np.array(npr.uniform(0, 100, 1000), dtype=np.float32).tolist())
    c = str(np.array(npr.uniform(0, 1, 1000), dtype=np.float32).tolist())
    d = str(np.array([0, 0, 0, 0, 0, 0], dtype=np.float32).tolist())

    print >> sys.stdout, "FOOFOO"
    print >> sys.stdout, a
    print >> sys.stdout, b
    print >> sys.stdout, c
    print >> sys.stdout, d
    print >> sys.stdout, "RASPUTIN"
    sys.stdout.flush()

    i+=1

