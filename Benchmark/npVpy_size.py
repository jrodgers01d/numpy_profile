import numpy as np
import sys

if __name__ == '__main__':
    for power in range(0, 9):
        npdata = np.arange((10**power), dtype=np.float64)
        list_data = npdata.tolist()
        print(f"np,{10**power},{sys.getsizeof(npdata)}")
        print(f"py,{10**power},{sys.getsizeof(list_data)}")
