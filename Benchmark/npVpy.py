from mpi4py import MPI
import numpy as np

def measure_time():
    return MPI.Wtime()

def bench_npsum(data, iters=1000):
    npdata = np.array(data)
    time = measure_time()
    for _ in range(iters):
        npdata.sum()
    time = measure_time() - time
    return (len(npdata), time / iters, iters)

def bench_npmin(data, iters=1000):
    npdata = np.array(data)
    time = measure_time()
    for _ in range(iters):
        npdata.min()
    time = measure_time() - time
    return (len(npdata), time / iters, iters)

def bench_npmax(data, iters=1000):
    npdata = np.array(data)
    time = measure_time()
    for _ in range(iters):
        npdata.sum()
    time = measure_time() - time
    return (len(npdata), time / iters, iters)

def bench_npmul(data, iters=1000):
    npdata = np.array(data)
    time = measure_time()
    for _ in range(iters):
        3 * npdata
    time = measure_time() - time
    return (len(npdata), time / iters, iters)

def bench_npdiv(data, iters=1000):
    npdata = np.array(data)
    time = measure_time()
    for _ in range(iters):
        npdata / 3
    time = measure_time() - time
    return (len(npdata), time / iters, iters)

#
# def bench_nprev(data, iters=1000):
#     npdata = np.array(data)
#     time = measure_time()
#     for _ in range(iters):
#         npdata[::-1]
#     time = measure_time() - time
#     return (len(data), time / iters, iters)
#
# def bench_npsrt(data, iters=1000):
#     npdata = np.array(data)
#     #reverse data
#     rev_npdata = np.copy(npdata[::-1])
#     time = measure_time()
#     for _ in range(iters):
#         rev_npdata.sort()
#     time = measure_time() - time
#     return (len(data), time / iters, iters)

def bench_pysum(data, iters=1000):
    time = measure_time()
    for _ in range(iters):
        sum(data)
    time = measure_time() - time
    return (len(data), time / iters, iters)

def bench_pymin(data, iters=1000):
    time = measure_time()
    for _ in range(iters):
        min(data)
    time = measure_time() - time
    return (len(data), time / iters, iters)

def bench_pymax(data, iters=1000):
    time = measure_time()
    for _ in range(iters):
        max(data)
    time = measure_time() - time
    return (len(data), time / iters, iters)

def bench_pymul(data, iters=1000):
    time = measure_time()
    for _ in range(iters):
        [3 * val for val in data]
    time = measure_time() - time
    return (len(data), time / iters, iters)

def bench_pydiv(data, iters=1000):
    time = measure_time()
    for _ in range(iters):
        [val / 3 for val in data]
    time = measure_time() - time
    return (len(data), time / iters, iters)

# def bench_pyrev(data, iters=1000):
#     time = measure_time()
#     len_data = len(data)
#     for _ in range(iters):
#         data[::-1]
#     time = measure_time() - time
#     return (len_data, time / iters, iters)
#
# def bench_pysrt(data, iters=1000):
#     #reverse data
#     rev_data = data[::-1]
#     time = measure_time()
#     for _ in range(iters):
#         sort(rev_data)
#     time = measure_time() - time
#     return (len(data), time / iters, iters)

if __name__ == '__main__':
    for power in range(0, 9):
        iters = 10000 if power < 5 else 100 if power < 6 else 10
        data = np.arange((10**power), dtype=np.float64).tolist()
        print("np,sum,%d,%.9f,%d" % bench_npsum(data, iters=iters))
        print("np,min,%d,%.9f,%d" % bench_npmin(data, iters=iters))
        print("np,max,%d,%.9f,%d" % bench_npmax(data, iters=iters))
        print("np,mul,%d,%.9f,%d" % bench_npmul(data, iters=iters))
        print("np,div,%d,%.9f,%d" % bench_npdiv(data, iters=iters))
        print("py,sum,%d,%.9f,%d" % bench_pysum(data, iters=iters))
        print("py,min,%d,%.9f,%d" % bench_pymin(data, iters=iters))
        print("py,max,%d,%.9f,%d" % bench_pymax(data, iters=iters))
        print("py,mul,%d,%.9f,%d" % bench_pymul(data, iters=iters))
        print("py,div,%d,%.9f,%d" % bench_pydiv(data, iters=iters))
