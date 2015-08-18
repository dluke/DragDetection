import random
import numpy as np

# generates random locations almost in Edinburgh

def random_lattitutde_generator():
	top = 55.95493
	bot = 55.89530
	yrange = np.linspace(bot, top, 10000)

	left = -3.14166
	right = -3.33735
	xxrange = np.linspace(right, left, 10000)

    while True:
        y = random.sample(yrange, 1)[0]
        x = random.sample(xxrange, 1)[0]
        yield (x, y)

corrdgen = random_lattitutde_generator()

return corrdgen.next()

        
    
