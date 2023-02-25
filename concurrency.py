import multiprocessing as mp
from datetime import datetime
import time
import random


def random_proc():
    wait_time = random.random()
    time.sleep(wait_time)
    print(datetime.now())

if __name__ == "__main__":
    for x in range(3):
        p = mp.Process(target=random_proc)
        p.start()
        

