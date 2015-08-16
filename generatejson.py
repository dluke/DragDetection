

import random
import numpy as np

top = 55.95493
bot = 55.89530
yrange = np.linspace(bot, top, 10000)

left = -3.14166
right = -3.33735
xxrange = np.linspace(right, left, 10000)


def randlatt():
    while True:
        y = random.sample(yrange, 1)[0]
        x = random.sample(xxrange, 1)[0]
        yield (x, y)

corrdgen = randlatt()

for _ in range(10):
    print corrdgen.next()

        
    
