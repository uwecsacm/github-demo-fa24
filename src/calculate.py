import os
import numpy as np

DATA = [1, 2, 5, 4, 10, 2]

def getData():
    return DATA

if __name__ == '__main__':
    print(f'Running module: {os.path.basename(__file__)}')    

    data_np = np.array(DATA)
    sum = data_np.sum()
    mean = data_np.mean()
    std_dev = data_np.std()

    print(f'Sum: {sum}\nAverage: {mean}\nStd Deviation: {std_dev}')

    

